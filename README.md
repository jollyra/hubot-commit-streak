# hubot-streak-podium

A hubot script that shows who has the longest commit streak in your org

See [`src/streaklife.js`](src/streaklife) for full documentation.

## Installation

In hubot project repo, run:

`npm install hubot-commit-streak --save`

Then add **hubot-commit-streak** to your `external-scripts.json`:

```json
[
  "hubot-commit-streak"
]
```

### Environment Variables

Hubot-commit-streak requires:

HUBOT_ORG_ACCESS_TOKEN (an access token created by an org member)

HUBOT_ORG_LOGIN (the name of your org as seen on github)

## Sample Interaction

```
hubot>> #streaklife, baby
        redleader: 12
        redthree: 10
        redsix: 3

## Local Testing

1 mkdir streakbot
2 cd streakbot
3 yo hubot
4 follow the yo instructions
5 run streakbot with >bin/hubot
6 try a command like >commit streak
