# Description
#   A hubot script that shows who has the longest github streak in your org
#
# Configuration:
#   LIST_OF_ENV_VARS_TO_SET
#   HUBOT_ORG_ACCESS_TOKEN
#
# Commands:
#   streak ladder - <Gets a list of the longest github commit streaks in your org>
#
# Notes:
#   An access token is required by the github api to access a private org's members
#   so an account that is a member of the private org is required.
#
# Author:
#   Nigel Rahkola <me@nigelrahkola.com>
#   Mitch Leblanc <>

Promise = require("bluebird")
request = Promise.promisify(require("request"))
_ = require("underscore")
cheerio = require("cheerio")

module.exports = (robot) ->
  robot.hear /#streaklife|commit streak/i, (res) ->
    orgLogin = process.env.HUBOT_ORG_LOGIN
    access_token = process.env.HUBOT_ORG_ACCESS_TOKEN
    unless access_token && orgLogin?
      res.send ":( you need to supply HUBOT_ORG_ACCESS_TOKEN and HUBOT_ORG_LOGIN"
      return

    options = {
      uri: "https://api.github.com/orgs/#{orgLogin}/members",
      json: "true",
      headers: {
        "accept": "application/json",
        "Authorization": "token #{access_token}",
        'User-Agent': 'request'
      }
    }

    # Store the contribution svgs in this list
    contributions = []

    request(options).spread((response, body) ->
      # console.log(response)
      return body
    ).then((body) ->
      promises = _.map(body, (userJson) ->
        return getContributions(userJson.login, contributions)
      )

      Promise.all(promises).then(() ->
        console.log("what should we have here?")
        console.log("contributions: ", contributions.length)
        parseContributionSvg(contributions[0])
      )
    )

getContributions = (userLogin, contributions) ->
  console.log(userLogin)
  return request({uri: "https://github.com/users/#{userLogin}/contributions"}).spread((response, body) ->
    contributions.push(body)
  )

parseContributionSvg = (svg) ->
	$ = cheerio.load(svg)
	console.log($.html())
	return {shit: "goddamn"}
