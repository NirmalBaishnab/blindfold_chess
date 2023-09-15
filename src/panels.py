import chess.pgn
import chess
import cairosvg
import tkinter as tk
from io import BytesIO
from PIL import Image, ImageTk
import random
import os


class ControlPanel:
    def __init__(self, root, board_display):
        self.root = root
        self.board_display = board_display
        self.controls = []

    def add_control(self, control):
        self.controls.append(control)
        control.display()

    def remove_control(self, control):
        if control in self.controls:
            control.hide()
            self.controls.remove(control)



class BaseControl:
    def __init__(self, root):
        self.root = root

    def display(self):
        pass

    def hide(self):
        pass

    def update(self):
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


class FENEntry(BaseControl):
    def __init__(self, root, board_display):
        super().__init__(root)
        self.board_display = board_display
        self.fen_entry = tk.Entry(self.root, width=60)
        self.set_button = tk.Button(self.root, text="Set Board", command=self.set_board_from_entry)

    def set_board_from_entry(self):
        fen_str = self.fen_entry.get()
        self.board_display.update_display(fen_str)

    def display(self):
        self.fen_entry.pack(pady=10)
        self.set_button.pack(pady=10)

    def hide(self):
        self.fen_entry.pack_forget()
        self.set_button.pack_forget()


class RefreshButton(BaseControl):
    def __init__(self, root, callback):
        super().__init__(root)
        self.button = tk.Button(self.root, text="Refresh Position", command=callback)

    def display(self):
        self.button.pack(pady=10)

    def hide(self):
        self.button.pack_forget()

    
