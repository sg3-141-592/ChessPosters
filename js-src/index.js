import { getPlayerGames } from './lichess.js'

// Assign click events to the tabs at the top of the page
$('#lichessTab').click(function () {
    $('#LichessSelectionPage').show();
    $('#PGNPage').hide();
    $('#ChessSelectionPage').hide();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').addClass('is-active');
    $('#chessTab').removeClass('is-active');
    $('#pgnTab').removeClass('is-active');
});

// On startup hide all of the sections
$('#LichessSelectionPage').hide();
$('#PGNPage').hide();
$('#ChessSelectionPage').hide();

export function showLichess() {
    $('#LichessSelectionPage').show();
    $('#PGNPage').hide();
    $('#ChessSelectionPage').hide();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').addClass('is-active');
    $('#chessTab').removeClass('is-active');
    $('#pgnTab').removeClass('is-active');
}

export function showChess() {
    $('#LichessSelectionPage').hide();
    $('#PGNPage').hide();
    $('#ChessSelectionPage').show();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').removeClass('is-active');
    $('#chessTab').addClass('is-active');
    $('#pgnTab').removeClass('is-active');
}

export function showPGN() {
    $('#LichessSelectionPage').hide();
    $('#PGNPage').show();
    $('#ChessSelectionPage').hide();
    $('#exampleTab').removeClass('is-active');
    $('#lichessTab').removeClass('is-active');
    $('#chessTab').removeClass('is-active');
    $('#pgnTab').addClass('is-active');
}

// Get list of games for a Chess.com user name
function getChessPlayerGames() {
    // https://api.chess.com/pub/player/rmchess1954/games/archives
    var monthsRequest = $.ajax({
        type: "GET",
        url: `https://api.chess.com/pub/player/${$('#playerNameChess').val()}/games/archives`,
        dataType: "json"
    }).done(function(data) {
        // Get the games from the latest month for the player
        var lastestMonthURL = data.archives[data.archives.length - 1];
        var recentGamesList = $.ajax({
            type: "GET",
            url: lastestMonthURL,
            dataType: "json"
        }).done(function(data) {
            data.games.forEach(element => {
                $('#playerGamesChess').append(
                    $('<div>')
                        .attr('onclick', `renderPreviewLichess(${gameData.length-1})`)
                        .text(
                            `${element.white.username} ${element.white.rating} - ${element.black.username} ${element.black.rating}`
                        )
                );
            });
        }).fail(function(err) {
            console.log(err);
        });
        console.log(data);
    }).fail(function(err) {
        console.log(err);
    });
    
}

// Get list of games for a Lichess user name
export async function getLichessPlayerGames() {
    getPlayerGames($('#playerNameLichess').val());
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
