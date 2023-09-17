import chess.pgn
import chess
import cairosvg
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import random
import os
from panels import BoardDisplay

import sys
sys.path.append('../utils/')
from fen_sampler import RandomFENSelector

import argparse

def replay(num_pieces=32, time=5):
    global last_shown_fen

    # First, we set the last_shown_fen to a random position
    last_shown_fen = display_random_position(num_pieces=num_pieces)
    print(last_shown_fen)
    print(num_pieces, time)


    # After 1 seconds, display the empty board.
    root.after(time * 1000, lambda: fen_display(board_display, '8/8/8/8/8/8/8/8 w - - 0 1'))

    # Clear and enable the FEN entry
    fen_entry.delete(0, tk.END)
    fen_entry.config(state=tk.NORMAL)

def display_random_position(num_pieces=32):
    # selector = RandomFENSelector("/home/nirmal/Research/others/blindfold_chess/data/pgns")
    # random_position = selector.get_random_position()

    path = '/home/nirmal/Research/others/blindfold_chess/data/sorted_by_positions/'
    with open (path + f'{num_pieces}.txt', 'r') as f:
        positions = f.readlines()
    random_position = random.choice(positions).strip()

    fen_display(board_display, random_position)
    return random_position  # return the random_position so we can update the last_shown_fen


def main(**kwargs):
    global selector, root, board_display, panels, fen_entry, result_label
    
    num_pieces = kwargs.get('num_pieces', 32)
    if num_pieces > 32 or num_pieces < 3:
        raise ValueError("Number of pieces must be between 3 and 32")
    time = kwargs.get('time', None)
    if time is None:
        time = 1 * num_pieces

    root = tk.Tk()
    board_display = BoardDisplay(root)
    
    # Reset button
    reset_button = tk.Button(root, text="replay", command=lambda: replay(num_pieces=num_pieces, time=time))
    reset_button.pack()
    
    # FEN Entry widget
    fen_entry = tk.Entry(root)
    fen_entry.pack()
    fen_entry.config(state=tk.DISABLED)  # Disabled until the board is cleared

    # Button to validate entered FEN
    check_button = tk.Button(root, text="Check FEN", command=validate_fen)
    check_button.pack()

    # Label to display result of FEN validation
    result_label = tk.Label(root, text="")
    result_label.pack()

    # Initially start the process once
    replay(num_pieces=num_pieces, time=time)

    root.mainloop()


def fen_display(board_display, fen_string='8/8/8/8/8/8/8/8 w - - 0 1'):
    board_display.update_display(fen_string)

def validate_fen():
    entered_fen = fen_entry.get().strip()  # Removing any extra spaces
    piece_placement_from_last_shown_fen = last_shown_fen.split(' ')[0]  # Take only the piece placement part

    if entered_fen == last_shown_fen or entered_fen == piece_placement_from_last_shown_fen:
        result_label.config(text="Correct!")
    else:
        result_label.config(text="Incorrect! Try again.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--num_pieces', type=int, default=32, help='Number of pieces to place on the board')
    parser.add_argument('--time', type=int, default=None, help='time in seconds to memorize the board')

    args_namespace = parser.parse_args()
    kwargs = vars(args_namespace)
    print(kwargs)
    # pass the arguments to the main function
    main(**kwargs)


