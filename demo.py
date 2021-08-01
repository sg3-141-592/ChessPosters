import chess.pgn, chess.svg

pgn = open("example.pgn")

game = chess.pgn.read_game(pgn)

board = game.board()
for move in game.mainline_moves():
    board.push(move)

outFile = open("output.svg", "w")
outFile.write(chess.svg.board(board, size=350))
outFile.close()
