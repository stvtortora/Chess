# Chess

This terminal-based chess game allows humans to play against a computer player.

## Feature Highlight

### Computer Player

The computer player uses a min-max based algorithm with alpha-beta pruning to arrive at a move. It is programmed to search three moves ahead, but can easily be adjusted to search deeper into the game tree.  



## Instructions

To play, begin by cloning this repo and navigating into it via terminal.

Next, install the following dependencies:

```
$ brew install python3
$ pip3 install getch
$ pip3 instal colored
```

If you don't have homebrew, you can download python at https://www.python.org/downloads/.
If you're on pc, install `msvcrt` instead of `getch`.

Finally, run `python3 Game.py`.
