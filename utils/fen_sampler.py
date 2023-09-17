import os
import random
import chess.pgn

class RandomFENSelector:
    def __init__(self, directory):
        self._directory = directory
        self._files = [f for f in os.listdir(self.directory) if f.endswith('.pgn')]

        self.pgn = random.choice(self.files)
        self.pgn_path = os.path.join(self.directory, self.pgn)

        self._games = self.get_games_from_pgn(self.pgn_path)
        self._game = random.choice(self._games)
        self._positions = self.get_positions_from_game(self._game)
        self._position = random.choice(self._positions)
    
    def get_random_position(self):
        return self._position
    
    def get_games_from_pgn(self, pgn_path):
        """Extract all games from a given PGN file."""
        games = []
        with open(pgn_path, 'r') as pgn_file:
            while True:
                game = chess.pgn.read_game(pgn_file)
                if game is None:
                    break
                games.append(game)

        if not games:
            raise ValueError(f"No games found in PGN file: {pgn_path}")

        return games

    def get_positions_from_game(self, game):
        """Extract all positions from a given game."""
        positions = []
        game_node = game
        while game_node:
            positions.append(game_node.board().fen())
            game_node = game_node.variations[0] if game_node.variations else None

        if not positions:
            raise ValueError("No positions found in the game")

        return positions
    
    @property
    def directory(self):
        # check if the directory exists
        if not os.path.exists(self._directory):
            raise ValueError(f"Directory does not exist: {self._directory}")
        return self._directory

    @property
    def files(self):
        if not self._files:
            raise ValueError(f"No PGN files found in the directory: {self.directory}")
        return self._files

    @property
    def games(self):
        if not self._games:
            raise ValueError("Games not initialized properly")
        return self._games

    @property
    def game(self):
        if not self._game:
            raise ValueError("Game not selected properly")
        return self._game

    @property
    def positions(self):
        if not self._positions:
            raise ValueError("Positions not extracted properly")
        return self._positions

    @property
    def position(self):
        if not self._position:
            raise ValueError("Position not selected properly")
        return self._position

if __name__ == "__main__":
    selector = RandomFENSelector("/home/nirmal/Research/others/blindfold_chess/data/pgns")
    random_position = selector.get_random_position()
    print(random_position)
