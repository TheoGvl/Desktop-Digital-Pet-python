# Desktop Digital Pet

A Tamagotchi-style desktop virtual pet built with Python and the Flet framework. This project focuses on interactive UI design and asynchronous game loops.

## Academic Context
While a fun and simple game, this application demonstrates key software development practices:
* **Game Loops:** Utilizing a continuous background process (`asyncio`) that updates game states over time without blocking user input.
* **State Management:** Tracking variables (Hunger, Happiness, Alive/Dead) and dynamically updating the user interface to reflect those internal states.
* **Constraint Logic:** Using math constraints (`min()` and `max()`) to ensure visual progress bars remain within their valid 0.0 to 1.0 boundaries.

## Features
* **Live Metabolism:** The pet's hunger and happiness naturally deplete every few seconds.
* **Dynamic Expressions:** The ASCII pet face changes its expression `( ^_^ ) -> ( O_O ) -> ( x_x )` based on its current needs.
* **Interactive Care:** Use the Feed and Play buttons to replenish the progress bars and keep your pet alive.
* **Failure State:** If both bars hit zero, the game ends and the UI locks out further interactions.

## Tech Stack
* **Language:** Python 3.8+
* **Framework:** Flet

## How to Run Locally

1. Install the Flet dependency:
   ```bash
   pip install flet
