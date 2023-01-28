## Introduction

Hi there! This is my project for Pronto Software's Woven Monopoly project.

I decided to write my report in the README instead of the PDF for easier access. The README includes my thought process, design architecture, testing/running details, and so on. Here's the contents list:
Running Instructions

I wanted this application to be as extensible as possible, hence I applied as many OOP practices as I could to make it easier for customization.

### Side Note

I really wanted to challenge myself and learn Ruby on Rails, but I don't own a Mac plusthe process of installation on Windows was too difficult and time-consuming. So I opted to challenge myself by using Python instead. It was a fun learning process and I learned a lot of new techniques, including the `unittest` suite as well as Python folder structuring. I also learned how to document methods in Python using the Sphinx structure.

## 🍀 Table of Contents

* [Running Instructions](#running-instructions)
  * [Simulation Variables](#simulation-variables)
  * [Console commands](#console-commands)
* [Assumptions](#assumptions)
  * [Reasons for Assumptions](#reasons-for-assumptions)
* [Approach](#approach)
  * [Architectural Diagrams](#architectural-diagrams)
  * [Class Documentation](#class-documentation)
* [Extensibility](#extensibility)
  * [Simulation Environment](#simulation-environment)
  * [Extra Square types and Properties](#extra-square-types-and-properties)
* [Results](#results)
  * [Roll 1](#roll-1)
  * Roll 2

## Running Instructions

### Simulation Variables

These variables can by simply changed in `classes/constants.py`

| Variable              | Type     | Default   | Description                                                                                    |
| --------------------- | -------- | --------- | ---------------------------------------------------------------------------------------------- |
| `STARTING_POSITION` | `int`  | 0         | The position where the players start.                                                          |
| `STARTING_AMOUNT`   | `int`  | 16        | The amount that players start with.                                                            |
| `GO_AMOUNT`         | `int`  | 1         | The amount that players get when passing through Go.                                           |
| `PRINT_TURNS`       | `bool` | `False` | The information of each player and their turn will be output onto the console                  |
| `PRINT_RESULTS`     | `bool` | `True`  | The final statistics of the game will be printed. That is, the answers to the questions given. |

### Console Commands

You can run the given program using these commands:

**Main:**

```
python -m __init__
```

**Unit Tests:**

```
python test_unit.py
```

**Integration Tests:**

```
python test_integrated.py
```

## Assumptions

There were few considerations that I asked to clarify in my email. Since these factors were left to personal intepretation, I decided to list my assumptions here.

1. **Bankruptcy** entails that the player has **0 dollars or less**.
2. The player will **empty their wallets** to the property owner if they cannot afford the full rent. That is, the player will give whatever amount they have on hand to the owner.
3. If the player lands on a property they cannot afford to buy, they will go into debt. That is, they will have negative dollars.
4. The price of a player's owned properties do not add to the player's final amount
5. There can be **multiple winners** if players have the same maximum amount at the end of the game

#### Reasons for Assumptions

**Assumption 3**

The game rules demand that *'If you land on a property, you must buy it' .* I viewed it in a real-life scope and thought it would be better if the player went into debt.

**Assumption 4**

In the original Monopoly, the value of each player's properties is not accounted for if a player goes bankrupt. (Though, usually they would sell their properties to get money from the bank)

**Other**

The other rules are assumed to solidify my approach to this project.

## Approach

The first step was to plan the architecture of the program.

### Architectural Diagrams

### Class Documentation

I wrote docstrings for each class and method, and for the test files for the program. The documentation PDF is provided under `woven_monopoly.pdf`

## Extensibility

Since the program is based on a lot Object Oriented Practices, I believe it is easy to integrate new Squares, Board methods, and such, to accommodate new requirements in the future. Some considerations are detailed below:

### Simulation Environment

The environmental variables can by simply changed in `classes/constants.py`

| Variable              | Type     | Description                                                                                    |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| `STARTING_POSITION` | `int`  | The position where the players start.                                                          |
| `STARTING_AMOUNT`   | `int`  | The amount that players start with.                                                            |
| `GO_AMOUNT`         | `int`  | The amount that players get when passing through Go.                                           |
| `BANKRUPTCY_AMOUNT` | `int`  | The amount where players are considered bankrupt.                                              |
| `PRINT_TURNS`       | `bool` | The information of each player and their turn will be output onto the console                  |
| `PRINT_RESULTS`     | `bool` | The final statistics of the game will be printed. That is, the answers to the questions given. |

### Extra Square types and Properties

The Square class can be further extended. Some instructions to make a new `Jail` Square are provided below :

1. Ensure a `Jail` `JSON `object is in the `board.json ` `JSON` file provided for the board
2. The new class can implemented with ease in the `square.py` file:
   ```
   class Jail(Square):
       """Jail is a subclass of Square. It inherits state and behavior from
       the Square class. It is initialised the same way as a Square, with
       __square_type as "to_" for this simulation

       :param Square: Parent class
       :type Square: Square
       """
       def action(self, player):
           """The action the player performs when it lands on the Square.

           :param player: The current performing player
           :type player: Player
           """
           # Code the player actions
   ```
3. Together with some modifications with Board parse_squares_list() method:

```
        # ..Code shortened for demonstration purposes..
            if data["type"] == "go":
                # GO square
                squares[i] = Go(data["name"], data["type"])
            if data["type"] == "jail":
                # GO square
                squares[i] = Jail(data["name"], data["type"])
        return squares
```

## Results

The results can be seen if you set `PRINT_RESULTS` to `True` in the `classes/constants.py` file, and run the main program using

```
python -m __init__
```

### Roll 1

```
--------------RESULTS:--------------
Who would win each game?
Player 0, Peter, is a winner with $39

How much money does everybody end up with?
Player 0, Peter, has $39
Player 1, Billy, has $14
Player 2, Charlotte, has $0
Player 3, Sweedal, has $1

What spaces does everybody finish on?
Player 0, Peter, is at position 8
Player 1, Billy, is at position 0
Player 2, Charlotte, is at position 7
Player 3, Sweedal, is at position 7
```

### Roll 2

```
--------------RESULTS:--------------
Who would win each game?
Player 2, Charlotte, is a winner with $29

How much money does everybody end up with?
Player 0, Peter, has $5
Player 1, Billy, has $20
Player 2, Charlotte, has $29
Player 3, Sweedal, has $0

What spaces does everybody finish on?
Player 0, Peter, is at position 4
Player 1, Billy, is at position 2
Player 2, Charlotte, is at position 0
Player 3, Sweedal, is at position 8
```

## Woven coding test

Your task is to write an application to play the game of Woven Monopoly.

In Woven Monopoly, when the dice rolls are set ahead of time, the game is deterministic.

### Game rules

* There are four players who take turns in the following order:
  * Peter
  * Billy
  * Charlotte
  * Sweedal
* Each player starts with $16
* Everybody starts on GO
* You get $1 when you pass GO (this excludes your starting move)
* If you land on a property, you must buy it
* If you land on an owned property, you must pay rent to the owner
* If the same owner owns all property of the same colour, the rent is doubled
* Once someone is bankrupt, whoever has the most money remaining is the winner
* There are no chance cards, jail or stations
* The board wraps around (i.e. you get to the last space, the next space is the first space)

### Your task

* Load in the board from board.json
* Implement game logic as per the rules
* Load in the given dice rolls files and simulate the game
  * Who would win each game?
  * How much money does everybody end up with?
  * What spaces does everybody finish on?

The specifics and implementation of this code is completely up to you!

### What we are looking for:

* We are a Ruby house, however feel free to pick the language you feel you are strongest in.
* Code that is well thought out and tested
* Clean and readable code
* Extensibility should be considered
* A git commit-history would be preferred, with small changes committed often so we can see your approach

Please include a readme with any additional information you would like to include, including instructions on how to test and execute your code.  You may wish to use it to explain any design decisions.

Despite this being a small command line app, please approach this as you would a production problem using whatever approach to coding and testing you feel appropriate.
