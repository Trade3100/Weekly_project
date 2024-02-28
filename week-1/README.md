# Word Guessing Game

A simple word guessing game where the player tries to guess a 5-letter word.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [How to Play](#how-to-play)
- [Usage](#usage)
- [Dependencies](#dependencies)
- [License](#license)

## Introduction

This Python project implements a word guessing game where the player attempts to guess a randomly selected 5-letter word. The game provides feedback on each guess, indicating correct letters in the right position (green), correct letters in the wrong position (orange), and incorrect letters (gray). The player has four chances to guess the word correctly.

## Features

- Randomly selects a 5-letter word for the player to guess.
- Provides feedback on each guess, highlighting correct letters in the right position (green), correct letters in the wrong position (orange), and incorrect letters (gray).
- Allows the player five chances to guess the word correctly.

## How to Play

1. Run the script.
2. Enter a 5-letter guess when prompted.
3. Receive feedback on the guess.
4. Continue guessing until the word is correctly identified or the maximum attempts are reached.

## Usage

Clone the repository and run the Python script:

```bash
python wordl.py
```

Follow the on-screen instructions to play the game.

## Dependencies

The project relies on the following external libraries:

- [wonderwords](https://pypi.org/project/wonderwords/): For generating random words.
- [rich](https://pypi.org/project/rich/): For colorful and styled terminal output.

Install dependencies using:

```bash
pip install wonderwords rich
```

## License

This project is licensed under the [GNU General Public License (GPG)](LICENSE) - see the [LICENSE](LICENSE) file for details.
