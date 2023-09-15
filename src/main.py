import chess.pgn
import chess
import cairosvg
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import random
import os
from panels import *

def main():
    root = tk.Tk()

    board_display = BoardDisplay(root)
    control_panel = ControlPanel(root, board_display)

    # Adding specific controls to the control panel
    fen_entry = FENEntry(root, board_display)
    control_panel.add_control(fen_entry)

    refresh_button = RefreshButton(root, lambda: random_display(board_display))
    control_panel.add_control(refresh_button)

    root.mainloop()


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

    pass


def random_display(board_display):
    """Display a random position on the board."""
    directory = "/home/nirmal/Research/others/blindfold_chess/data/pgns/"
    random_pgn_file = get_random_pgn_file(directory)
    fen_string = get_random_fen_from_pgn(os.path.join(directory, random_pgn_file))
    print(fen_string)
    board_display.update_display(fen_string)


def get_random_pgn_file(directory):
    """Get a random PGN file from the directory."""
    pgn_files = [f for f in os.listdir(directory) if f.endswith('.pgn')]
    return random.choice(pgn_files)

def get_random_fen_from_pgn(pgn_path):
    """Get a random FEN string from a PGN file."""
    games = []

    with open(pgn_path, 'r') as pgn_file:
        while True:
            game = chess.pgn.read_game(pgn_file)
            if game is None:
                break
            games.append(game)

    # If no games found, return None
    if not games:
        return None

    random_game = random.choice(games)

    # Choose a random position from the game
    game_node = random_game
    moves = list(random_game.mainline_moves())
    random_move_number = random.randint(0, len(moves))
    for i in range(random_move_number):
        game_node = game_node.variation(0)

    return game_node.board().fen()



if __name__ == "__main__":
    main()



