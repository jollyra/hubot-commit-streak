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
  robot.hear /org test1/i, (res) ->
    orgLogin = "pulseenergy"  # TODO: also get this from an env var
    access_token = process.env.HUBOT_ORG_ACCESS_TOKEN
    unless access_token?
      console.log("Missing ORG_ACCESS_TOKEN in environment: please set and try again")
      return
    console.log("Found the access token in the environment! #{access_token}")
    ladder = buildLadder(orgLogin, access_token, robot, res)


buildLadder = (orgLogin, access_token, robot, res) ->
  robot.http("https://api.github.com/orgs/#{orgLogin}/members")
    .header("accept", "application/json", "Authorization", "token #{access_token}")
    .get() (err, response, body) ->
      if err
        console.log("NUTS! #{err} statusCode: #{response.statusCode}")
      else
        result = JSON.parse(body)
        users = (((json) -> return json) json for json in result)
        getContributions(robot, res, users[0].login)

getContributions = (robot, res, userLogin) ->
   robot.http("https://github.com/users/#{userLogin}/contributions")
    .get() (err, response, body) ->
      if err
        console.log("#{response.statusCode} getting  contributions for user #{userLogin}")
      else
        res.send body
