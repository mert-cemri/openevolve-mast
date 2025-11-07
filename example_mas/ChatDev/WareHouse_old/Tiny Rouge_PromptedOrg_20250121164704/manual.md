# Roguelike Game: Tower of the Sorcerer

Welcome to the user manual for the Roguelike Game: Tower of the Sorcerer. This document will guide you through the installation process, introduce the main functions of the game, and provide instructions on how to play.

## Table of Contents

1. [Introduction](#introduction)
2. [Installation](#installation)
3. [Game Overview](#game-overview)
4. [How to Play](#how-to-play)
5. [Game Components](#game-components)

## Introduction

The Roguelike Game: Tower of the Sorcerer is a Python-based game inspired by classic roguelike games. The game features a grid-based map where players navigate through levels, encounter monsters, collect treasures, and aim to reach the door to advance to the next level.

## Installation

To play the game, you need to have Python installed on your system. Follow these steps to set up the game environment:

1. **Install Python**: Ensure that Python 3.x is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the game repository to your local machine using the following command:
   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Game Directory**: Change to the directory where the game files are located:
   ```bash
   cd <repository-directory>
   ```

4. **Install Dependencies**: Install any required dependencies using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the Game**: Start the game by executing the main script:
   ```bash
   python main.py
   ```

## Game Overview

The game is set on an 80x80 grid map. The player controls a character that can move in four directions using the keyboard keys W (up), S (down), A (left), and D (right). The objective is to navigate through the map, avoid or defeat monsters, collect treasures, and reach the door to proceed to the next level.

## How to Play

- **Movement**: Use the keyboard keys W, S, A, and D to move the player character up, down, left, and right, respectively.

- **Objective**: Reach the door to advance to the next level. The door is marked on the map, and there is always at least one path leading to it.

- **Monsters**: Encountering a monster will initiate a battle. The player's HP is reduced by the monster's HP. If the player's HP remains above zero, the monster is defeated.

- **Treasure Chests**: Collect treasure chests to restore the player's HP by a random amount between 20 and 30.

- **Walls**: The player cannot pass through walls, which are randomly placed on the map but not on the path to the door.

## Game Components

- **Player**: The main character controlled by the player. The player starts with 100 HP.

- **Map**: An 80x80 grid representing the game environment. It includes floors, walls, monsters, treasure chests, and a door.

- **Monsters**: Creatures that the player can encounter. Each monster has a specific HP value.

- **Treasure Chests**: Objects that restore the player's HP when collected.

- **Door**: The exit point to the next level.

Enjoy your adventure in the Tower of the Sorcerer! If you have any questions or encounter issues, please refer to the documentation or contact support.