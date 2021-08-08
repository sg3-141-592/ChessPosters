# ToDo
## Backend
- Add a title to the image
- Turn SVG chess board to an image
   - Make the stroke an argument that can be called from the chess.svg method
- Make the chess board more beautiful
- Add ability to tile based on the number of moves
    - 3x4 = 24 moves (1200/3=400)
    - 4x5 = 40 moves (1200/4=300)
    - 5x7 = 70 moves (1200/5=240)
- Get games from Chess.com
- Allow users to enter a PGN

## Frontend
- User game list
 - Make the list scrollable
 - Make the list searchable
- Add a style for the games
- Add a wait until the users preview has rendered

# Done
- Connect to the Lichess API
    - Get a list of games for a particular user
- Use PGN data to render an image
- Find a way to add borders to the chessboard
- Create a tiled page of game pictures
- Delete tmp files on startup

----------
# Setup Instructions
`export PIP_USER=false`