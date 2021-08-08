import chess.pgn, chess.svg
import io
import svgutils as sg
import uuid

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
    moveStr = ""
    for counter, move in enumerate(game.mainline_moves()):
        moveStr += board.san(move) + " "
        board.push(move)
        # TODO: Work out handling for last move when not %2
        if (counter+1)%2 == 0:
            moveNum = int((counter+1)/2)
            figures.append(generateFigure(board, moveNum, moveStr))
            moveStr = ""
        if int((counter+1)%2) == 9:
            break
    # Build main figure
    masterFigure = sg.compose.Figure("1200","1200", *figures).tile(3,3)
    masterFigure.save("static/rendered/1/figure.svg")
    return None

def generateFigure(board, moveNum, moveStr):
    tmpFilename = str(uuid.uuid4())
    # TODO: Work out if there's a way to remove the extra file i/o        
    outFile = open("./tmp/{}.svg".format(tmpFilename), "w")
    outFile.write(chess.svg.board(board, size=350,
        colors=boardColors, coordinates=False))
    outFile.close()
    return sg.compose.Panel(
        sg.compose.SVG("./tmp/{}.svg".format(tmpFilename)),
        sg.compose.Text("{}. {}".format(moveNum, moveStr), 10, 385, size=12)
    )

if __name__ == "__main__":
    file = open("example.pgn", "r")
    generatePreview(io.StringIO(file.read()))
    file.close()