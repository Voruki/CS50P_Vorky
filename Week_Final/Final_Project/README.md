# Simple Table Tennis Game 🏓

### Video Demo: [CS50P Final Project - Simple Table Tennis Game 🏓[4K/60FPS]](https://www.youtube.com/watch?v=7wL_XpK6ztc)

### Descriptions:

The Simple Table Tennis Game is a basic implementation of the classic game of table tennis (ping pong) built using Python and the Turtle graphics library. The game allows two players to compete against each other on a virtual ping pong table. Players control paddles using keyboard inputs to hit a ball back and forth across the table, scoring points when the opponent fails to return the ball. The player who get 3 points first wins the game!

## Files:

### project.py

This file contains the main implementation of the game. It includes the `main()` function, which serves as the entry point of the program. The `PingPongGame` class encapsulates the game logic, including setting up the GUI, controlling the characteristics of both paddles as well as the ping pong ball and its movements, handling the mathematical logics behind the collision physics, and updating the scoreboard. Additionally, this file defines the custom functions `paddle1_go_up`, `paddle1_go_down`, `paddle2_go_up`, and `paddle2_go_down`, which control the movements of the paddles.

### test_project.py

This file contains test functions for the custom functions defined in `project.py`. The test functions use the `pytest` framework to verify the behavior of each function. Tests cover the movement of both paddles, ensuring they move correctly when the corresponding keys are pressed.

### requirements.txt

This file lists the pip-installable libraries required for the project. Currently, the project requires the `turtle` and `pygame` libraries for graphics, sound effects and background music. `pytest` is required for the validation of the movements of the paddles. This is to ensure that the paddles are moved correctly when the corresponding keys are inputted.

## Design Choices:

- **Turtle Graphics**: The `Turtle` graphics library was chosen for its simplicity and suitability for beginner-level game development in Python.

- **Separation of Concerns**: The game logic is encapsulated within the `PingPongGame` class, promoting modularity and maintainability. Separate functions handle specific aspects of the game, such as paddle movements and collision detection.

- **Sound Effects**: Sound effects are used to enhance the gaming experience. `Winsound` library is utilized for playing audio cues for collisions, border hits, and score updates. Meanwhile, the `mixer` from `pygame` library is implemented for playing the background music continuously. Please take in mind that `Winsound` only works in Window System only.

- **Scalability**: While this implementation is a basic fundamental program, it provides a foundation that can be expanded upon to add features such as different game modes, AI opponents, or customizable game settings.


***This README.md aims to provide a comprehensive overview of the project, explaining its functionality, file structure, and design choices. Feel free to explore the code further and customize it to your preferences as I will share this project to the world!***
