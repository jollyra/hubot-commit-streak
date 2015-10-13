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

module.exports = (robot) ->

  robot.hear /streak ladder/i, (res) ->
    access_token = process.env.HUBOT_ORG_ACCESS_TOKEN
    unless access_token?
      res.send "Missing ORG_ACCESS_TOKEN in environment: please set and try again"
      return
    res.send "Found the access token in the environment! #{access_token}"

  robot.hear /http test/i, (res) ->
    access_token = process.env.HUBOT_ORG_ACCESS_TOKEN
    robot.http("https://api.github.com/user?access_token=#{access_token}")
      .get() (err, response, body) ->
        res.send "Got a response! #{body}"

