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
  robot.hear /longest github streaks/i, (res) ->
    res.send "supermitch: 72"
    res.send "Jollyra: 22"
    res.send "joshlemer: 9"
    res.send "ananthakumaran: 6"
    res.send "mattbrehmer: 6"
    res.send "jennih: 6"
    res.send "tylerfawcett: 5"
    res.send "Abarrowman: 5"
    res.send "nicwaller: 3"
    res.send "trevortuepah: 3"
