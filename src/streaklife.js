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
	robot.hear(/#streaklife|commit streak|test/i, function(res) {
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
			console.log("contributions: ", contributions.length);
			_.each(contributions, function (contribution) {
				calculateStreak(contribution);
			});
		});
	});
}

function gettingMembers(orgLogin, accessToken) {
	var opts = {
		uri: "https://api.github.com/orgs/" + orgLogin + "/members",
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
		return body;
	});
}

function calculateStreak(contribution) {
	$ = cheerio.load(contribution);
	var days = $('rect[class=day]');
	var streak = _.takeRightWhile(days, function (day) {
		var commits = cheerio(day).attr('data-count');
		return parseInt(commits);
	});
	console.log(streak.length);
}
