# Turtle Race Game

The Turtle Race Game is a simple Python program that simulates a race between six turtles. The user can place a bet on which turtle they think will win the race. The program uses the Turtle graphics module to create a graphical interface and animate the race.

## How to Play

1. Import the required modules: `turtle`, `random`, and `Screen` from `turtle`.
2. Create a `Screen` object and set up the screen dimensions.
3. Prompt the user to enter their bet by calling `textinput` method on the `Screen` object.
4. Create a list of colors and a list of y-positions for the turtles.
5. Create six turtle objects, setting their shape, color, and initial positions.
6. Store the turtle objects in a list called `all_turtles`.
7. If the user has placed a bet, set the `is_race_on` flag to `True`.
8. Start a while loop that continues until the race is over.
9. Iterate over each turtle in the `all_turtles` list.
    - Check if the turtle has crossed the finish line (x-coordinate greater than 230).
        - If so, set `is_race_on` to `False`.
        - Determine the winning color by calling `pencolor` method on the turtle object.
        - Compare the winning color with the user's bet and display the result.
    - Generate a random distance for the turtle to move forward.
10. Exit the program when the user clicks on the screen.

## Dependencies

The program relies on the `turtle` module, which is a standard Python library used for creating graphics and animations. It also uses the `random` module to generate random distances for the turtles.

## Installation

To run the Turtle Race Game, you need to have Python installed on your machine. The program does not require any external libraries beyond the standard Python library.

1. Copy the code into a Python file (e.g., `turtle_race.py`).
2. Save the file and navigate to its location in the terminal or command prompt.
3. Run the program using the command: `python turtle_race.py`.

## Gameplay

1. Upon running the program, a window will open displaying the race track and a prompt asking for your bet.
2. Enter the color of the turtle you think will win the race and press "OK."
3. The turtles will start moving forward randomly, simulating the race.
4. Once a turtle crosses the finish line, the program will display whether you won or lost the bet.
5. Click anywhere on the screen to exit the program.

## Customization

You can customize the program according to your preferences:

- Adjust the screen dimensions by modifying the `width` and `height` arguments in the `screen.setup` function call.
- Modify the colors in the `colors` list to change the available turtle colors.
- Change the y-positions in the `y_positions` list to adjust the starting positions of the turtles.
- Customize the random distance range by modifying the arguments of the `random.randint` function call (currently set to 0-10).

Have fun playing the Turtle Race Game!
