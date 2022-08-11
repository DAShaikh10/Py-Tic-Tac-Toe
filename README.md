<!-- PROJECT SHIELDS -->
[![Made with python][made-with-python-shield]][python-url]
[![Python][python-shield]][python-url]
[![Linting][pylint-shield]][pylint-url]
[![License][license-shield]][license-url]
[![Last commit][last-commit-shield]][last-commit-url]
[![Code size][code-size-shield]][code-url]
![Awesome badges][awesome-badges-shield]

# **Tic Tac Toe - Minimax + α-β optimization (Alpha-beta pruning)**

Tic Tac Toe game.  
This game has three game modes:
- Human vs. Human.
- Human vs. AI
- AI vs. AI

This is the terminal version of the game. In each game mode the player who starts the game is selected at random.

<p align="center">
  <img src="images\tic_tac_toe - preview.gif" alt="Tic Tac Toe console version" width="650" height="400">
  <div align="center"><em>Tic Tac Toe console version</em></div>
</p>

# Usage
```bash
python tic_tac_toe.py
```

# AI
The **AI** for *Tic Tac Toe* has been developed using **minimax algorithm** + **α-β optimization** *(Alpha-beta pruning)*.  
Click [here](AI.md) to read more.

# Project structure
```bash
├── LICENSE.md
├── README.md
├── AI.md # Article about Minimax and Alpha-beta pruning.
├── tic_tac_toe.py # Main python file.
├── players.py # Contains the Human and AI class.
└── utils.py # Helper functions and global variables.
```

# TODO
- [ ] Add Tic Tac Toe GUI version.  
- [ ] Add Reinforcement learning AI.

<div align="center">
   
   <a href="https://GitHub.com/DAShaikh10">![Built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)</a>

</div>

<!-- MARKDOWN LINKS & IMAGES -->
[made-with-python-shield]: https://img.shields.io/badge/Made%20with-Python-darkblue
[python-url]: https://www.python.org
[python-shield]: https://img.shields.io/badge/Python->=3.6-informational?style=flat&logo=python&logoColor=ffdc51&color=1e415e
[pylint-shield]: https://img.shields.io/badge/linting-pylint-yellowgreen
[pylint-url]: https://pylint.pycqa.org
[license-shield]: https://img.shields.io/github/license/DAShaikh10/Tic-Tac-Toe
[license-url]: https://github.com/DAShaikh10/Tic-Tac-Toe/blob/main/LICENSE
[last-commit-shield]: https://img.shields.io/github/last-commit/DAShaikh10/Tic-Tac-Toe
[last-commit-url]: https://github.com/DAShaikh10/Tic-Tac-Toe
[code-size-shield]: https://img.shields.io/github/languages/code-size/DAShaikh10/Tic-Tac-Toe
[code-url]: https://github.com/DAShaikh10/Tic-Tac-Toe
[awesome-badges-shield]: https://img.shields.io/badge/badges-awesome-green.svg
