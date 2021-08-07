import chess.pgn, chess.svg
import cairosvg

pgn = open("example.pgn")

game = chess.pgn.read_game(pgn)

boardColors = {
    'square light': '#ffffff',
    'square dark': '#a1a1a1'
}

board = game.board()
counter = 1
for move in game.mainline_moves():
    board.push(move)
    if counter%2 == 0:
        outFile = open("static/rendered/1/output{}.svg".format(int(counter/2)), "w")
        outFile.write(chess.svg.board(board, size=600,
            colors=boardColors, coordinates=False))
        outFile.close()
    counter += 1

# cairosvg.svg2png(bytestring=chess.svg.board(board, size=600),
#     write_to="image.png")

# outFile = open("output.svg", "w")
# outFile.write(chess.svg.board(board, size=350))
# outFile.close()
