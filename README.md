# 🐍 Snake Game

A nostalgic, arcade-style Snake game built from scratch in Python using the standard `turtle` graphics module — no external libraries required.

> ⚠️ **Work in Progress** — This project is actively being developed. Features like High score tracking are coming soon.

---

## About

This project is a classic Snake game recreation built as a Python learning exercise. The snake is controlled using the arrow keys and moves continuously across a black 600×600 game window. The codebase follows an object-oriented approach, separating game logic into distinct modules.

---

## Project Structure

```
Snake_game/
├── main.py       # Entry point — sets up the screen, handles input, and runs the game loop
└── snake.py      # Snake class — handles creation, movement, and direction logic
```

---

## How It Works

**`snake.py`** defines the `Snake` class, which:
- Spawns the snake as 3 white square segments at starting positions
- Moves each segment into the position of the one ahead of it every frame
- Prevents the snake from reversing directly into itself (e.g. can't go Down while moving Up)

**`main.py`** sets up:
- A 600×600 black window using `turtle.Screen`
- Keyboard listeners for `Up`, `Down`, `Left`, `Right` arrow keys
- A game loop that updates the screen and moves the snake every 0.1 seconds

---

## Getting Started

**Requirements:** Python 3.x (no additional packages needed — `turtle` is part of the standard library)

```bash
# Clone the repository
git clone https://github.com/Prithviraj-chw/Snake_game.git
cd Snake_game

# Run the game
python main.py
```

---

## Controls

| Key        | Action      |
|------------|-------------|
| `↑` Up     | Move up     |
| `↓` Down   | Move down   |
| `←` Left   | Move left   |
| `→` Right  | Move right  |

---

## Planned Features

- [ ] Food spawning and snake growth
- [ ] Collision detection (walls & self)
- [ ] Score display
- [ ] Game over screen and restart option
- [ ] High score tracking

---

## License

This project is open source and available under the [MIT License](LICENSE).
