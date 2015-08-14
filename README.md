# hubot-streak-podium

A hubot script that shows who has the longest github streak in your org

See [`src/streak-podium.coffee`](src/streak-podium.coffee) for full documentation.

## Installation

In hubot project repo, run:

`npm install hubot-streak-podium --save`

Then add **hubot-streak-podium** to your `external-scripts.json`:

```json
[
  "hubot-streak-podium"
]
```

## Sample Interaction

```
user1>> hubot github streak leaders hubot>> redleader: 12
        redthree: 10
        redsix: 3
```

# Python streak-podium

Python version lives in `streak-podium` dir.

Queries Github, retrieves streaks and renders chart using Matplotlib.

![](https://github.com/supermitch/streak-podium/blob/master/sample/top_best.png)

