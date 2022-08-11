<!-- BACK TO TOP -->
<a name="readme-top"></a>

<!-- ARTICLE SHIELD -->
<div align="center">

  <a>![Read time][read-time-shield]</a>

</div>

# **Tic Tac Toe - Artificial Intelligence**

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li><a href="#introduction">Introduction</a></li>
    <li><a href="#minimax-algorithm">Minimax Algorithm</a></li>
    <li><a href="#modified-heuristic-function---evaluate_board">Modified heuristic function - evaluate_board()</a></li>
	<li><a href="#%CE%B1-%CE%B2-optimization-alpha-beta-pruning">α-β-optimization (Alpha-beta pruning)</a></li>
	<li><a href="#reference-and-further-reading">Reference and further reading</a></li>
  </ol>
</details>

## Introduction
To develop *Artificial Intelligence* for a game like Tic Tac Toe, we need an algorithm which is able to take the best possible move in order to defeat the opponent. Since the complexity of this game in terms of the possible moves is some what simple (like the fact that it is possible in many cases for a human to judge the possible moves of the opponent and their outcomes) if we develop an AI which can look ahead and judge the best next move, we might have a good AI. Now, carrying forward this idea of judging the next best move, if we are able to get all the possible moves it becomes quite easy to select the best out of the several possible moves (Since the game involves a 3x3 board, computing all the possible moves is conceivable). So, we need an algorithm which can do this. This is where **Minimax Algorithm** from the *Artificial Intelligence* domain comes into the picture.

## Minimax Algorithm
The Minimax algorithm is a decision-making algorithm used in *artificial intelligence* essentially in *game theory*. The Minimax-based AI can be seen in two-player games like chess, tic tac toe, checkers etc. These games are known as zero-sum games since it is mathematically very simple to represent the winning state and current state of the game.

> ### Example:
> If we take Tic Tac Toe as the example.
> We can represent player **"X"** winning the game as '+1', Player **"O"** winning the game as '-1' and '0' for no winner.

The Minimax AI is developed using a *game tree*. Each *state* of the game is represented as a **node** in this game tree. The **terminal state** is always one of the following:
* Player 'X' wins
* Player 'O' wins
* Draw

<p align="center">
  <img src="images\tic_tac_toe - game_tree.png" alt="Tic Tac Toe Game tree">
  <div align="center"><em>Tic Tac Toe Game tree</em></div>
</p>

The above image depicts what a *game tree* looks like with a few states shown. Here, we can observe that the *terminal states* or *nodes* are all either win condition (for one of the players) or draw (not shown in the above image) based on the *starting state* or *node* of the tree. The **root node** is the starting phase of the game which can be either a blank board or a partially filled board.

In the minimax algorithm, we assign two players namely the **maximizer** and **minimizer**, their role is the same as their name suggests. The AI is the maximizer as it wants to win the game and the other dummy player (represents the opponent) is the minimizer. we represent each level of the tree as a maximizing or a minimizing phase\turn as shown below.

<p align="center">
  <img src="images\tic_tac_toe - game_tree_minmax.png" alt="Tic Tac Toe Game tree" width="750" height="500">
  <div align="center"><em>Tic Tac Toe Game tree</em></div>
</p>

The minimax algorithm recursively searches for the best move that leads the *maximizer* player to win the game (best case) or at least draw the game (worst case). It considers the current state of the game and the available moves at that state, then for each valid move it plays (alternating moves *minimizer* and *maximizer*) until it finds a terminal state (win, draw or lose).

**Pseudocode:**  
```
minimax(board, player)
 	if player == maximizer and maximizer is winner
 		return positive score
 	else if player == minimizer and minimizer is winner
 		return negative score
 	else if game == draw
 		return 0
 
 	if player == maximizer
 		best_move_value = -infinity
 		best_move = NULL
 		for each position in the board
 			if position is available
 				maximizer marks that position
 				move_value, move =  minimax(modified_board, minimizer)
				undo move
 
 			if move_value > best_score_value:
 				best_score = move_value			
 				best_move = move
 
 		return best_move
 	else if player == minimizer
 		best_move_value = infinity
 		best_move = NULL
 		for each position in the board
 			if position is available
 				maximizer marks that position
 				move_value, move =  minimax(modified_board, maximizer)
 				undo move
 
 			if move_value < best_score_value:
 				best_score = move_value			
 				best_move = move
 
 		return best_move
```

Now, let us implement this algorithm in python. Let us first define the tic tac toe board:

```python
board = ["1", "2", "3", "4", "5", "6", "7", "8"]
```
The indices 0, 1 and 2 represent the first row, the indices 3, 4 and 5 represent the second row and lastly, the indices 6, 7 and 8 represent the third row.

For this example consider the maximizer player as **"X"** and the minimizer player as **"O"**. Although, the implementation in this repository allows randomly either player 1 or 2 to choose the symbol.

```python
def minimax(board: list, depth: int, is_maximizing: bool) -> int:
```
* **board**: Current board. (node)
* **depth**: Index of a game tree node.
* **is_maximizing**: `Bool` value indicating if the current player is the maximizer or the minimizer.

```python
score = evaluate_board(board, depth)
if score is not None:
	return score
elif not moves_left(board):
	return 0
```

The above code computes the score by calling `evaluate_board()` function which is the **heuristic function** in terms of artificial intelligence and it returns:
* Maximizer won: +1
* Minimizer won: -1
* Otherwise: 0 (No winner yet) 

Also, we check if there are any moves left by calling the `moves_left()` function which returns `True` if there are moves left else `False`.

When we first time call the `minimax` function we start at `depth = 0`
Both players start with the worst score. If player is maximizer, score is `-infinity` and for the minimizer the score is `+infinity`. Since a sufficiently large and small value respectively will do the job, in this implementation we do not use `infinity` rather we use `+50` and `-50`. 

Now, the recursive part,
```python
if is_maximizing:
	best_score = -50
	for position, item in enumerate(board):
		if item.strip().isdigit():
			board[position] = "X"
			best_score = max(best_score, minimax(board, depth + 1, not is_maximizing))
			board[position] = str(position + 1) + " "

	return best_score
else:
	best_score = 50
	for position, item in enumerate(board):
		if item.strip().isdigit():
			board[position] = "O"
			best_score = min(best_score, minimax(board, depth + 1, not is_maximizing))
			board[position] = str(position + 1) + " "

	return best_score
```

The code inside the `if` statement and the `else` statement are identical with the subtle difference that for the maximizer we initialize: 
```python
best_score = -50
```  

and 

```python
best_score = 50
``` 

for the minimizer,  
Also, we select the `max` score in the case of the maximizer.

```python
best_score = max(best_score, minimax(board, depth + 1, False))
```

and select the `min` score in the case of the minimizer.

```python
best_score = min(best_score, minimax(board, depth + 1, True))
```

So, for each available position we play that position and then based on the current score we decide the `best_score` followed by undoing the move to that position so that we retrace to the original state of the board. The `best_score` is returned.

The final algorithm:

```python
def minimax(board, depth, is_maximizing):
	score = evaluate_board(board, depth)
	if score is not None:
		return score
	elif not moves_left(board):
		return 0

	if is_maximizing:
		best_score = -50
		for position, item in enumerate(board):
			if item.strip().isdigit():
				board[position] = "X"
				best_score = max(best_score, minimax(board, depth + 1, not is_maximizing))
				board[position] = str(position + 1) + " "

		return best_score
	else:
		best_score = 50
		for position, item in enumerate(board):
			if item.strip().isdigit():
				board[position] = "O"
				best_score = min(best_score, minimax(board, depth + 1, not is_maximizing))
				board[position] = str(position + 1) + " "

		return best_score
```

Based on the `best_score` the AI play's it's move.

```python
board[best_move] = "X"
```

*Did you notice that the `depth` variable was never used in the above code, so why is it there, let us find out.*

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Modified heuristic function - evaluate_board()
Let us observe this particular scenario where the current state of the board is shown below:
<p align="center">
  <img src="images\tic_tac_toe - anomalous_move_1.png" alt="Anomalous move" width="750" height="400">
  <div align="center"><em>Anomalous move</em></div>
</p>

Since player **"X"** is playing the move at `3`, the AI can mark `6` and win the game.
<p align="center">
  <img src="images\tic_tac_toe - anomalous_move_2.png" alt="Anomalous move" width="750" height="400">
  <div align="center"><em>Anomalous move</em></div>
</p>

Observe how the AI marked `2` instead of `6` hence **delaying** the win for itself. 
This behaviour needs to be addressed and to do so we observe the *heuristic function* i.e. `evaluate_board()`.

```python
def evaluate_board(board: list, depth: int) -> int:
	if (board[0] == board[1] == board[2]) or board[0] == board[3] == board[6]:
		return 1 if board[0] == self.symbol else -1
	elif (board[3] == board[4] == board[5]) or (board[0] == board[4] == board[8]) or \
			(board[2] == board[4] == board[6]) or (board[1] == board[4] == board[7]):
		return 1 if board[4] == self.symbol else -1
	elif (board[6] == board[7] == board[8]) or (board[2] == board[5] == board[8]):
		return 1 if board[8] == self.symbol else -1
```

Note how the function returns simply `+1`, `-1` or `0`, we modify this logic to the following.

```python
def evaluate_board(board: list, depth: int) -> int:
	if (board[0] == board[1] == board[2]) or board[0] == board[3] == board[6]:
	    return (50 - depth) if board[0] == self.symbol else (-50 + depth)
	elif (board[3] == board[4] == board[5]) or (board[0] == board[4] == board[8]) or \
	     (board[2] == board[4] == board[6]) or (board[1] == board[4] == board[7]):
	    return (50 - depth) if board[4] == self.symbol else (-50 + depth)
	elif (board[6] == board[7] == board[8]) or (board[2] == board[5] == board[8]):
	    return (50 - depth) if board[8] == self.symbol else (-50 + depth)
```

We now return `50 - depth` for the maximizer player and `-50 + depth` for the minimizer player. This forces the AI to select the move which results in quicker victory. Thus, we now utilize the depth variable to help the AI opt for a shallow solution.

> Example:  
> Assume that it's the maximizer's turn and there are two solutions available to the AI one at `depth = 2` *(Optimal)* and the other at `depth = 3` *(Not optimal)*  
> Thus,  
> `solution_1 = 50 - 2 = 48` *(depth = 2)*   
> `solution_2 = 50 - 3 = 47` *(depth = 3)*  
> Since the maximizer picks the maximum value, the AI selects `solution_1` over `solution_2` which in turn helps it to make the optimal move.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## α-β optimization (Alpha-beta pruning)
Now, we have seen the minimax algorithm and know how it works using the game tree and the generated states. But, state generation is a time expensive process and we do not want to generate the nodes where the AI loses or ends up in a draw, to avoid such nodes we introduce the Alpha-beta pruning technique. This is an optimization technique for the minimax algorithm and not an entirely new algorithm. 

Let us take an example: (Example from [GeeksForGeeks][geeksforgeeks-url]
<p align="center">
  <img src="images\alpha-beta pruning 1.png" alt="Alpha-beta pruning">
  <div align="center"><em>Alpha-beta pruning</em></div>
</p>

* The initial call starts from node `A`. The value of `alpha` here is `-infinity` and the value of `beta` is `+infinity`. These values are passed down to subsequent nodes in the tree. At `A` the maximizer must choose `max` of `B` and `C`, so `A` calls `B` first.
* At `B` the minimizer must choose `min` of `D` and `E` and hence calls `D` first.
* At `D`, it looks at its left child which is a leaf node. This node returns a value of `3`. Now the value of `alpha` at `D` is `max(-infinity, 3)` which is `3`.
* To decide whether it's worth looking at its right node or not, it checks the condition `beta <= alpha`. This is `False` since `beta = +infinity` and `alpha = 3`. So it continues the search.
* `D` now looks at its right child which returns a value of `5`. At `D`, `alpha = max(3, 5)` which is `5`. Now the value of node `D` is `5`.
`D` returns a value of `5` to `B`. At `B`, `beta = min(+infinity, 5)` which is `5`. The minimizer is now guaranteed a value of `5` or lesser. `B` now calls `E` to see if it can get a lower value than `5`.
* At `E` the values of `alpha` and `beta` are not `-infinity` and `+infinity` but instead `-infinity` and `5` respectively, because the value of `beta` was changed at `B` and that is what `B` passed down to `E`.
* Now `E` looks at its left child which is `6`. At `E`, `alpha = max(-infinity, 6)` which is `6`. Here the condition becomes `True`. `beta` is `5` and `alpha` is `6`. So `beta <= alpha` is `True`. Hence it breaks and `E` returns `6` to `B`.
* Note how it did not matter what the value of `E`'s right child is. It could have been `+infinity` or `-infinity`, it still wouldn't matter, We never even had to look at it because the minimizer was guaranteed a value of `5` or lesser. So as soon as the maximizer saw the `6` it knew the minimizer would never come this way because it can get a `5` on the left side of `B`. This way we didn't have to look at that `9` and hence saved computation time.
* `E` returns a value of `6` to `B`. At `B`, `beta = min(5, 6)` which is `5`.The value of node `B` is also `5`.

So far this is how our game tree looks. The `9` is crossed out because it was never computed. 
 
<p align="center">
  <img src="images\alpha-beta pruning 2.png" alt="Alpha-beta pruning">
  <div align="center"><em>Alpha-beta pruning</em></div>
</p>

* `B` returns `5` to `A`. At `A`, `alpha = max(-infinity, 5)` which is `5`. Now the maximizer is guaranteed a value of `5` or greater. A now calls `C` to see if it can get a higher value than `5`.
* At `C`, `alpha = 5` and `beta = +infinity`. `C` calls `F`.
* At `F`, `alpha = 5` and `beta = +infinity`. `F` looks at its left child which is `1`. `alpha = max(5, 1)` which is still `5`.
* `F` looks at its right child which is `2`. Hence the best value of this node is `2`. `Alpha` still remains `5`.
* `F` returns a value of `2` to `C`. At `C`, `beta = min(+inifinity, 2)`. The condition `beta <= alpha` becomes `True` as `beta = 2` and `alpha = 5`. So it breaks and it does not even have to compute the entire sub-tree of `G`.
* The intuition behind this break-off is that at `C` the minimizer was guaranteed a value of `2` or lesser. But the maximizer was already guaranteed a value of `5` if he choose `B`. So why would the maximizer ever choose `C` and get a value less than `2`? Again we can see that it did not matter what those last `2` values were. We also saved a lot of computation by skipping a whole sub-tree.
* `C` now returns a value of `2` to `A`. Therefore the best value at `A` is `max(5, 2)` which is `5`.
* Hence the optimal value that the maximizer can get is `5`

This is what our final game tree looks like. As you can see `G` has been crossed out as it was never computed. 

<p align="center">
  <img src="images\alpha-beta pruning 3.png" alt="Alpha-beta pruning">
  <div align="center"><em>Alpha-beta pruning</em></div>
</p>

Let us have a quick look at the code for alpha-beta pruning. The base `minimax` algorithm code remains the same with the addition of the following lines:

For maximizer,
```python
if best_score >= beta: return best_score
alpha = max(best_score, alpha)
```

For minimizer,
```python
if best_score <= alpha: return best_score
beta = min(best_score, beta)
```

Final code:
```python
def minimax(board, is_maximizing, alpha, beta, depth):
	score = evaluate_board(board, depth)
	if score is not None:
		return score
	elif not moves_left(board):
		return 0

	if is_maximizing:
		best_score = -50
		for position, item in enumerate(board):
			if item.strip().isdigit():
				board[position] = self.symbol
				best_score = max(best_score, self._minimax(board, not is_maximizing, alpha, beta, depth + 1))
				board[position] = str(position + 1) + " "

			# Alpha-beta pruning.
			if best_score >= beta: return best_score
			alpha = max(best_score, alpha)

		return best_score
	else:
		best_score = 50
		for position, item in enumerate(board):
			if item.strip().isdigit():
				board[position] = self.opponent
				best_score = min(best_score, self._minimax(board, not is_maximizing, alpha, beta, depth + 1))
				board[position] = str(position + 1) + " "

			# Alpha-beta pruning.
			if best_score <= alpha: return best_score
			beta = min(best_score, beta)

		return best_score
```

The Minimax algorithm computes approximately **55,505** states when the opponent starts first (and marks the middle of the board) to determine its next move whereas with the use of alpha-beta pruning the minimax algorithm only computes about **8,465** states to determine it's next move. 

We can test it by putting a `global` variable in the program and incrementing it for each minimax function call per turn.

The difference is more significant in the case of more complex games such as chess in which computing all the possible states is not feasible.

***This brings us to the end of our discussion. Thank you for reading!***

<p align="right">(<a href="#readme-top">back to top</a>)</p>

## Reference and further reading
1. Minimax algorithm - [Wikipedia][wiki-minimax-url]
2. Alpha-beta pruning - [Wikipedia][wiki-alpha-beta-pruning-url]
3. Alpha-beta pruning example - [GeeksForGeeks][gfg-alpha-beta-pruning-url]

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- MARKDOWN LINKS & IMAGES -->
[read-time-shield]: https://img.shields.io/badge/Read%20Time-14%20mins%20read-brightgreen
[geeksforgeeks-url]: https://www.geeksforgeeks.org
[wiki-minimax-url]: https://en.wikipedia.org/wiki/Minimax
[wiki-alpha-beta-pruning-url]: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning
[gfg-alpha-beta-pruning-url]: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/?ref=rp