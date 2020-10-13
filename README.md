# CLI-random-maze

print a random mazes of requested dimensions, using special chars like ┴ and┌

usage: ``` python3 maze.py <int num_rows> <int num_columns> ```
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
or ``` python3 maze.py fill ``` to fill up the entire terminal window:
![screenshot maze fill](https://github.com/nitasn/CLI-random-maze/blob/main/ScreenShotFill.png?raw=true)
