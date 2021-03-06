// Description
//   A hubot script that shows who has the longest public github commit streak in your org
//
// Configuration:
//   HUBOT_ORG_ACCESS_TOKEN
//   HUBOT_ORG_LOGIN
//
// Commands:
//   #streaklife - <Gets a list of the longest github commit streaks in your org>
//   commit streak - <Gets a list of the longest github commit streaks in your org>
//
// Notes:
//   An access token is required by the github api to access a private org's members
//   so an account that is a member of the private org is required.
//
// Author:
//   Nigel Rahkola <me@nigelrahkola.com>

var Promise = require("bluebird"),
	requesting = Promise.promisify(require("request")),
	cheerio = require("cheerio"),
	_ = require("lodash");

module.exports = function(robot) {
	robot.hear(/#streaklife|commit streak/i, function(res) {
		var orgLogin = process.env.HUBOT_ORG_LOGIN;
		var accessToken = process.env.HUBOT_ORG_ACCESS_TOKEN;
		if (!orgLogin || !accessToken) {
			res.send(":( I require HUBOT_ORG_ACCESS_TOKEN and HUBOT_ORG_LOGIN");
			return;
		}
		gettingMembers(orgLogin, accessToken).then(function (users) {
			if (_.isEmpty(users)) { res.send(":( I couldn't find any users"); }
			return users;
		}).then(function (users) {
			var userPromises = _.map(users, function (userJson) {
				return gettingContributions(userJson.login);
			});
			return Promise.all(userPromises);
		}).then(function (contributions) {
			var streaks = _.map(contributions, function (contribution) {
				return {
					user: contribution.user,
					currentStreak: calcCurrentStreak(contribution.contribs)
				};
			});
			report(res, streaks);
		});
	});
}

function gettingMembers(orgLogin, accessToken) {
	var opts = {
		uri: "https://api.github.com/orgs/" + orgLogin + "/members?per_page=100",
		json: "true",
		headers: {
			"accept": "application/json",
			"Authorization": "token " + accessToken,
			'User-Agent': 'request'
		}
	};
	return requesting(opts).spread(function (response, body) {
		return body;
	});
}

function gettingContributions(userLogin) {
	var opts = { uri: "https://github.com/users/" + userLogin + "/contributions" };
	return requesting(opts).spread(function (response, body) {
		return { user: userLogin, contribs: body };
	});
}

function calcCurrentStreak(contribution) {
	$ = cheerio.load(contribution);
	var days = $('rect[class=day]');
	countCommits(_.last(days)) > 0
		? streak = _.takeRightWhile(days, function (day) { return countCommits(day); })
		: streak = _.takeRightWhile(_.dropRight(days), function (day) { return countCommits(day); });
	return streak.length;
}

function countCommits(xml) {
	var commits = cheerio(xml).attr('data-count');
	return parseInt(commits);
}

function report(res, streaks) {
	streaks = _.filter(streaks, function (streak) { streak.currentStreak !== 0; });
	streaks = _.take(_.sortByOrder(streaks, function (streak) { return streak.currentStreak; }, ['desc']), 7);
	var out = _.foldl(streaks, function (str, streak) { return str + streak.user + " " + streak.currentStreak + "\n"; }, "");
	var title = "\nTop live public commit streaks:\n";
	res.send(title + out);
}
