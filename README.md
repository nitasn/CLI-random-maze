# CLI-random-maze

Generate beautiful mazes in you terminal.

## Usage
Run ``` python3 maze.py fill ``` to fill up the entire terminal window:
![screenshot maze fill](https://github.com/nitasn/CLI-random-maze/blob/main/ScreenShotFill.png?raw=true)

Or ``` python3 maze.py <num_rows> <num_columns> ``` for custom dimensions:

```bash
$ python3 maze.py 3 10
╷ ↓ ╶───────┬───────────────────┬───────┐
│           │                   │       │
│   ╷   ┌───┘   ╷   ╶───┬───╴   └───╴   │
│   │   │       │       │               │
│   └───┘   ╶───┴───┐   └───────────┐   │
│                   │               │   │
└───────────────────┴───────────────┘ ↓ ╵

$ python3 maze.py 6 4
╷ ↓ ╶───────┬───┐
│           │   │
├───╴   ╷   ╵   │
│       │       │
│   ┌───┴───╴   │
│   │           │
├───┘   ┌───────┤
│       │       │
│   ╶───┤   ╷   │
│       │   │   │
├───╴   └───┘   │
│               │
└───────────╴ ↓ ╵
```

