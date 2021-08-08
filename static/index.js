// On startup hide all of the sections
$('#LichessSelectionPage').hide();
$('#PGNPage').hide();
$('#ChessSelectionPage').hide();

function showLichess() {
    $('#LichessSelectionPage').show();
    $('#PGNPage').hide();
    $('#ChessSelectionPage').hide();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').addClass('is-active');
    $('#chessTab').removeClass('is-active');
    $('#pgnTab').removeClass('is-active');
}

function showChess() {
    $('#LichessSelectionPage').hide();
    $('#PGNPage').hide();
    $('#ChessSelectionPage').show();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').removeClass('is-active');
    $('#chessTab').addClass('is-active');
    $('#pgnTab').removeClass('is-active');
}

function showPGN() {
    $('#LichessSelectionPage').hide();
    $('#PGNPage').show();
    $('#ChessSelectionPage').hide();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').removeClass('is-active');
    $('#chessTab').removeClass('is-active');
    $('#pgnTab').addClass('is-active');
}

// Get list of games for a Lichess user name
async function getLichessPlayerGames() {
    var playerName = $('#playerName').val();
    var url = new URL(`https://lichess.org/api/games/user/${playerName}`);
    url.search = new URLSearchParams({max: 10});
    const response = await fetch(url);
    if (response.status != 200) {
        console.log(response.text);
    }
    else
    {
        const reader = response.body
            .pipeThrough(new TextDecoderStream())
            .getReader();
        while (true) {
            const { value, done } = await reader.read();
            if (done) {
                break;
            }
            extractGameData(value);
        }
    }
}

var gameData = [];

function renderPreviewLichess(gameId) {
    renderPreview(gameData[gameId]);
}

function renderPreviewPGN() {
    renderPreview($('#pgnText').val());
}

// Send the PGN of a game to be rendered
function renderPreview(pgn) {
    var renderRequest = $.ajax({
        type: "POST",
        url: "./api/render",
        data: JSON.stringify({
            gameData: pgn
        }),
        contentType: "application/json",
        dataType: "json"
    }).done(function(data) {
        $('#previewWindow').attr('src', `rendered/preview/${data.id}.png`);
    }).fail(function(err) {
        console.log(err);
    });
}

// TODO: Refactor this in future to use a generic method instead of having
// a seperate regex for each value extracted.
const whiteNameRegEx = /\[White \"(.+)\"\]/;
const blackNameRegEx = /\[Black \"(.+)\"\]/;
const whiteEloRegEx = /\[WhiteElo \"(.+)\"\]/;
const blackEloRegEx = /\[BlackElo \"(.+)\"\]/;

function extractGameData(data) {
    gameData.push(data)
    var whiteName = whiteNameRegEx.exec(data)[1];
    var blackName = blackNameRegEx.exec(data)[1];
    var whiteElo = whiteEloRegEx.exec(data)[1];
    var blackElo = blackEloRegEx.exec(data)[1];
    $('#playerGames').append(
        $('<div>')
            .attr('onclick', `renderPreviewLichess(${gameData.length-1})`)
            .text(
                `${whiteName} ${whiteElo} - ${blackName} ${blackElo}`
            )
    );
}