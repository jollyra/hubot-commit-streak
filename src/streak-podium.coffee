# Description
#   A hubot script that shows who has the longest github streak in your org
#
# Configuration:
#   LIST_OF_ENV_VARS_TO_SET
#   ORG_ACCESS_TOKEN
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
  robot.hear /github streak leaders/i, (res) ->
    res.send "supermitch: 72\nJollyra: 22\njoshlemer: 9\nananthakumaran: 6\nmattbrehmer: 6\njennih: 6\ntylerfawcett: 5\nAbarrowman: 5\nnicwaller: 3\ntrevortuepah: 3"
