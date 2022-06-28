# CLI-random-maze

prints random mazes, using special chars like ┴ and┌ to the console.

usage: ``` python3 maze.py <num_rows> <num_columns> ```
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
