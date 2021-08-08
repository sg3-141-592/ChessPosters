import cairosvg
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
    numberMoves = getNumberMoves(game)
    xTiles, yTiles = getTilesGroups(numberMoves)
    #
    moveStr = ""
    for counter, move in enumerate(game.mainline_moves()):
        moveStr += board.san(move) + " "
        board.push(move)
        # TODO: Work out handling for last move when not %2
        if (counter+1)%2 == 0:
            moveNum = int((counter+1)/2)
            figures.append(generateFigure(board, moveNum, moveStr, int(1200/xTiles)))
            moveStr = ""
    # Build main figure
    masterFigure = sg.compose.Figure(xTiles*400,yTiles*400, *figures).tile(xTiles, yTiles)
    # Convert main figure to a png
    filename = str(uuid.uuid4())
    masterFigure.save("tmp/{}.svg".format(filename))
    file = open("tmp/{}.svg".format(filename), "r")
    cairosvg.svg2png(file_obj=file,
        write_to="static/rendered/preview/{}.png".format(filename))
    file.close()
    return filename

def generateFigure(board, moveNum, moveStr, figureSize):
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

# TODO: See if there's a more elegant way to get the number of moves
def getNumberMoves(game):
    counter = 0
    for move in game.mainline_moves():
        counter += 1
    return counter

def getTilesGroups(numberMoves):
    if numberMoves <= 24:
        return (3,4)
    elif numberMoves > 24 <= 40:
        return (4,5)
    else:
        return (5,7)

if __name__ == "__main__":
    file = open("example.pgn", "r")
    generatePreview(io.StringIO(file.read()))
    file.close()