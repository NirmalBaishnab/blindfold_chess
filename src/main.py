import chess.pgn
import chess
import cairosvg
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import random
import os
from panels import *

import sys
sys.path.append('../utils/')
from fen_sampler import RandomFENSelector

def replay():
    display_random_position()
    # After 10 seconds, display the empty board.
    root.after(1000, lambda: fen_display(board_display, '8/8/8/8/8/8/8/8 w - - 0 1'))

def display_random_position():
    selector = RandomFENSelector("/home/nirmal/Research/others/blindfold_chess/data/pgns")
    random_position = selector.get_random_position()
    fen_display(board_display, random_position)

def main():
    global selector, root, board_display  # Declare these as globals so that they can be accessed within the reset_display function

    root = tk.Tk()
    board_display = BoardDisplay(root)
    
    # Reset button
    reset_button = tk.Button(root, text="replay", command=replay)
    reset_button.pack()  # Adjust this to place the button wherever you want

    # Initially start the process once
    replay()
    
    root.mainloop()





    # refresh_callback = lambda: fen_display(board_display)
    # refresh_button = RefreshButton(root, refresh_callback)
    # control_panel.add_control(refresh_button)

    n_seconds = 5  # for example, to refresh every 5 seconds
    #auto_refresh(root, refresh_callback, n_seconds * 1000)  # Convert to milliseconds



    # directory = "/home/nirmal/Research/others/blindfold_chess/data/pgns/"
    # random_pgn_file = get_random_pgn_file(directory)
    # fen_string = get_random_fen_from_pgn(os.path.join(directory, random_pgn_file))

    # root = tk.Tk()
    # root.title("Chess Board Toggle")
    # display = ChessDisplay(root, fen_string, wait_time=2)
    # root.mainloop()

    
    # display the position on the board for 10 seconds

    # display the empty board

    # ask the user to enter the position as FEN string

    # check if the entered FEN string is correct

    # if correct say correct or else say incorrect

    # get ready to repeat the process if the replay button is pressed


def fen_display(board_display, fen_string='8/8/8/8/8/8/8/8 w - - 0 1'):
    board_display.update_display(fen_string)


if __name__ == "__main__":
    main()


