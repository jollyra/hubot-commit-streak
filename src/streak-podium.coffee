# Description
#   A hubot script that shows who has the longest github streak in your org
#
# Configuration:
#   LIST_OF_ENV_VARS_TO_SET
#
# Commands:
#   hubot hello - <what the respond trigger does>
#   orly - <what the hear trigger does>
#
# Notes:
#   <optional notes required for the script>
#
# Author:
#   Nigel Rahkola <me@nigelrahkola.com>

module.exports = (robot) ->
  robot.hear /github streak leaders/i, (res) ->
    res.send "supermitch: 72\nJollyra: 22\njoshlemer: 9\nananthakumaran: 6\nmattbrehmer: 6\njennih: 6\ntylerfawcett: 5\nAbarrowman: 5\nnicwaller: 3\ntrevortuepah: 3"
