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

module.exports = (robot) ->
  robot.hear /ladder/i, (res) ->
    orgLogin = "pulseenergy"  # TODO: also get this from an env var
    access_token = process.env.HUBOT_ORG_ACCESS_TOKEN
    unless access_token?
      console.log("Missing ORG_ACCESS_TOKEN in environment: please set and try again")
      return
    console.log("Found the access token in the environment! #{access_token}")

    options = {
      uri: "https://api.github.com/orgs/#{orgLogin}/members",
      json: "true",
      headers: {
        "accept": "application/json",
        "Authorization": "token #{access_token}",
        'User-Agent': 'request'
      }
    }
    request(options).spread((response, body) ->
      console.log(response)
      console.log('\n\n@@@\n')
      console.log(body)
      return body
    ).then((body) ->
      # Use a map here to create an array of promises, then promise.all the promises
      # and iterate through results to get contribs for each user.
      return getContributions(body[0].login)
    ).then((user) ->
      console.log('\n\nUSERLOGIN')
      console.log(user)
    )

getContributions = (userLogin) ->
  request({uri: "https://github.com/users/#{userLogin}/contributions"}).spread((response, body) ->
    return body
  )
