import tkinter as tk
from PIL import Image, ImageTk
import chess.pgn
import chess, cairosvg
from io import BytesIO

class ChessDisplay:
    def __init__(self, root, fen_str):
        self.root = root
        self.fen_str = fen_str
        self.board_image = None
        self.empty_board = chess.Board(None)
        self.position_board = chess.Board(self.fen_str)
        self.show_position = True

        self.button = tk.Button(root, text="Toggle Board", command=self.toggle_display)
        self.button.pack(pady=10)
        
        self.update_display()

    def svg_to_image_data(self, svg_string):
        with BytesIO() as png_io:
            cairosvg.svg2png(bytestring=svg_string.encode('utf-8'), write_to=png_io)
            return png_io.getvalue()

    def update_display(self):
        if self.board_image:
            self.board_image.pack_forget()

        current_board = self.position_board if self.show_position else self.empty_board
        svg_string = chess.svg.board(board=current_board, size=800)
        image_data = self.svg_to_image_data(svg_string)
        image = Image.open(BytesIO(image_data))

        self.photo = ImageTk.PhotoImage(image)
        self.board_image = tk.Label(self.root, image=self.photo)
        self.board_image.pack(pady=10)

    def toggle_display(self):
        self.show_position = not self.show_position
        self.update_display()

if __name__ == "__main__":
    fen_str = "r3kr2/pppqb1pp/2np1n2/4p3/P3P3/2N1Bb1P/1PP1BPP1/R2Q1RK1 w q - 0 13"
    root = tk.Tk()
    root.title("Chess Board Toggle")
    display = ChessDisplay(root, fen_str)
    root.mainloop()
