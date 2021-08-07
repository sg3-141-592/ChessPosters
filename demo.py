import chess.pgn, chess.svg
import cairosvg

pgn = open("example.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()
for move in game.mainline_moves():
    board.push(move)

cairosvg.svg2png(bytestring=chess.svg.board(board, size=600),
    write_to="image.png")

# outFile = open("output.svg", "w")
# outFile.write(chess.svg.board(board, size=350))
# outFile.close()
