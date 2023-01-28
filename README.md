## Introduction

Hi there! This is my project for Pronto Software's Woven Monopoly project.

I decided to write my report in the README instead of the PDF for easier access. The README includes my thought process, design architecture, testing/running details, and so on. Here's the contents list:
Running Instructions

I wanted this application to be as extensible as possible, hence I applied as many OOP practices as I could to make it easier for customization.

### Side Note

I really wanted to challenge myself and learn Ruby on Rails, but I don't own a Mac plusthe process of installation on Windows was too difficult and time-consuming. So I opted to challenge myself by using Python instead. It was a fun learning process and I learned a lot of new techniques, including the `unittest` suite as well as Python folder structuring.

## 🍀 Table of Contents

* [Running Instructions](#running-instructions)
  * Simulation Variables
  * Console commands
* [Assumptions](#assumptions)
* [Approach](#approach)
* [Extensibility](#extensibility)

## Running Instructions

### Simulation Variables

These variables can by simply changed in `classes/constants.py`

| Variable              | Type     | Description                                                                                    |
| --------------------- | -------- | ---------------------------------------------------------------------------------------------- |
| `STARTING_POSITION` | `int`  | The position where the players start.                                                          |
| `STARTING_AMOUNT`   | `int`  | The amount that players start with.                                                            |
| `GO_AMOUNT`         | `int`  | The amount that players get when passing through Go.                                           |
| `PRINT_TURNS`       | `bool` | The information of each player and their turn will be output onto the console                  |
| `PRINT_RESULTS`     | `bool` | The final statistics of the game will be printed. That is, the answers to the questions given. |

### Console Commands

I ran the simulation with Windows Powershell using these commands:

**Main:**
``python -m __init__``
**Unit Tests:**
``python test_unit.py``
**Integration Tests:**
``python test_integrated.py``

## Assumptions

There were few considerations that I asked to clarify in my email, but the such was left to personal intepretation. Hence, I decided to list these assumptions here.

1. **Bankruptcy** entails that the player has **0 dollars or less**.
2. The player will **empty their wallets** to the property owner if they cannot afford the full rent. That is, the player will give whatever amount they have on hand to the owner.
3. If the player lands on a property they cannot afford to buy, they will go into debt. That is, they will have negative dollars

#### Reasons for Assumptions

3. Rules demand that *'If you land on a property, you must buy it'*

## Approach

## Extensibility

## Conclusion

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
