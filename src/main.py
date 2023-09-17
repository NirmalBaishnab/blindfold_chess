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

def replay():
    global last_shown_fen

    # First, we set the last_shown_fen to a random position
    last_shown_fen = display_random_position()
    print(last_shown_fen)

    # After 1 seconds, display the empty board.
    root.after(1000, lambda: fen_display(board_display, '8/8/8/8/8/8/8/8 w - - 0 1'))

    # Clear and enable the FEN entry
    fen_entry.delete(0, tk.END)
    fen_entry.config(state=tk.NORMAL)

def display_random_position():
    selector = RandomFENSelector("/home/nirmal/Research/others/blindfold_chess/data/pgns")
    random_position = selector.get_random_position()
    fen_display(board_display, random_position)
    return random_position  # return the random_position so we can update the last_shown_fen

def main():
    global selector, root, board_display, panels, fen_entry, result_label
    
    root = tk.Tk()
    board_display = BoardDisplay(root)
    
    # Reset button
    reset_button = tk.Button(root, text="replay", command=replay)
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
    replay()

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
    main()


