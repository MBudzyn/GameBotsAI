import chess
import chess.svg
import webbrowser
import random


class ChessBoard:
    def __init__(self):
        self.board = chess.Board()

    def __str__(self):
        return str(self.board)

    def __copy__(self):
        new_board = ChessBoard()
        new_board.board = self.board.copy()
        return new_board

    def is_white_turn(self):
        return self.board.turn == chess.WHITE

    def is_black_turn(self):
        return self.board.turn == chess.BLACK

    def get_legal_moves(self):
        return self.board.legal_moves

    def make_move(self, m):
        self.board.push(m)

    def undo_last_move(self):
        self.board.pop()
    def visualize(self):
        svg_board = chess.svg.board(self.board, size=700, coordinates=True)
        with open("chess_board.html", "w") as html_file:
            html_file.write('<html><body>\n')
            html_file.write(svg_board)
            html_file.write('\n</body></html>')
        webbrowser.open("chess_board.html")

    def get_random_move(self):
        return random.choice([move for move in self.get_legal_moves()])




    def play_game_wrandom(self):
        while not self.board.is_game_over():
            self.visualize()
            if self.is_white_turn():
                move = input("Enter move: ")
                move = chess.Move.from_uci(move)
                if move in self.get_legal_moves():
                    self.make_move(move)
                else:
                    print("Invalid move")
            else:
                print("Thinking...")
                move = self.get_random_move()
                self.make_move(move)
        self.visualize()
        print("Game over")



def main():
    board = ChessBoard()
    board.play_game_wrandom()




if __name__ == "__main__":
    main()
