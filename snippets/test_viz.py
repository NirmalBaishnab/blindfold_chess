import chess.pgn
import chess
import cairosvg
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk

def svg_to_image_data(svg_string):
    """Convert SVG string to image data."""
    with BytesIO() as png_io:
        cairosvg.svg2png(bytestring=svg_string.encode('utf-8'), write_to=png_io)
        return png_io.getvalue()


def display_chessboard(fen_str, timeout=2):
    # Convert FEN to chess board
    board = chess.Board(fen_str)
    svg_string = chess.svg.board(board=board, size=400)
    
    # Convert SVG to image data
    image_data = svg_to_image_data(svg_string)
    
    # Convert image data to PIL Image
    image = Image.open(BytesIO(image_data))
    
    # Create tkinter window
    root = tk.Tk()
    root.title("Chess Board")

    # Display the image
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(root, image=photo)
    label.pack()

    root.after(timeout * 1000, lambda: root.destroy())
    root.mainloop()
    # Wait for timeout seconds


fen_empty = "8/8/8/8/8/8/8/8 w - - 0 1"
fen_str = "r3kr2/pppqb1pp/2np1n2/4p3/P3P3/2N1Bb1P/1PP1BPP1/R2Q1RK1 w q - 0 13"
# display the chessboard for 2 seconds

display_chessboard(fen_str)
display_chessboard(fen_empty)
