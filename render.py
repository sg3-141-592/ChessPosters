import chess.pgn, chess.svg
import io
import svgutils.transform as sg

boardColors = {
    'square light': '#ffffff',
    'square dark': '#a1a1a1'
}

def generatePreview(pgn):
    # Load the game
    # TODO: Integrate loaded game with API
    game = chess.pgn.read_game(pgn)
    # Build the different states of the board
    board = game.board()
    figures = []
    # 
    for counter, move in enumerate(game.mainline_moves()):
        board.push(move)
        print(move)
        # TODO: Work out handling for last move when not %2
        if counter%2 == 0:
            outFile = open("static/rendered/1/output{}.svg".format(int(counter/2)), "w")
            figures.append(generateFigure(board))
            outFile.write(chess.svg.board(board, size=600,
                colors=boardColors, coordinates=False))
            outFile.close()
    # Build main figure
    print(figures)
    masterFigure = sg.SVGFigure("210cm", "297cm")
    masterFigure.append([figures[0], figures[1]])
    masterFigure.save("static/rendered/1/composite.svg")
    return None

def generateFigure(board):
    fig = sg.SVGFigure("400", "400")
    fig1 = sg.fromstring(chess.svg.board(board, size=350))
    plot1 = fig1.getroot()
    plot1.moveto(25, 25)
    txt1 = sg.TextElement(25,425, "1. Kxh2 Qh4+", size=18, weight="normal", font="DejaVuSansMono")
    fig.append([plot1, txt1])
    return fig

if __name__ == "__main__":
    file = open("example.pgn", "r")
    generatePreview(io.StringIO(file.read()))
    file.close()