import chess.pgn
import chess
import cairosvg
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import random
import os

def main():
    # get random position from the pgn file
    root = tk.Tk()

    board_display = BoardDisplay(root)
    control_panel = ControlPanel(root, board_display)

    # show a text box to enter the FEN
    root

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



class BoardDisplay:
    def __init__(self, root, fen_str=None):
        self.root = root
        self.fen_str = fen_str or chess.STARTING_FEN
        self.board_image = None
        self.board = chess.Board(self.fen_str)
        self.update_display()

    def svg_to_image_data(self, svg_string):
        with BytesIO() as png_io:
            cairosvg.svg2png(bytestring=svg_string.encode('utf-8'), write_to=png_io)
            return png_io.getvalue()

    def update_display(self, fen_str=None):
        if fen_str:
            self.fen_str = fen_str
            self.board = chess.Board(self.fen_str)
        
        if self.board_image:
            self.board_image.pack_forget()
        
        svg_string = chess.svg.board(board=self.board, size=800)
        image_data = self.svg_to_image_data(svg_string)
        image = Image.open(BytesIO(image_data))

        self.photo = ImageTk.PhotoImage(image)
        self.board_image = tk.Label(self.root, image=self.photo)
        self.board_image.pack(pady=10)

class ControlPanel:
    def __init__(self, root, board_display):
        self.root = root
        self.board_display = board_display

        self.refresh_button = tk.Button(root, text="Refresh Position", command=self.refresh_position)
        self.refresh_button.pack(pady=10)

        self.show_position = True

    def get_random_position(self):
        directory = "/home/nirmal/Research/others/blindfold_chess/data/pgns/"
        random_pgn_file = get_random_pgn_file(directory)
        fen_string = get_random_fen_from_pgn(os.path.join(directory, random_pgn_file))
        return fen_string

    def refresh_position(self):
        new_fen = self.get_random_position()
        self.board_display.update_display(new_fen)


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



