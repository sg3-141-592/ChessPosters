async function getPlayerGames() {
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

// TODO: Refactor this in future to use a generic method instead of having
// a seperate regex for each value extracted.
const whiteNameRegEx = /\[White \"(.+)\"\]/;
const blackNameRegEx = /\[Black \"(.+)\"\]/;
const whiteEloRegEx = /\[WhiteElo \"(.+)\"\]/;
const blackEloRegEx = /\[BlackElo \"(.+)\"\]/;

function extractGameData(data) {
    var whiteName = whiteNameRegEx.exec(data)[1];
    var blackName = blackNameRegEx.exec(data)[1];
    var whiteElo = whiteEloRegEx.exec(data)[1];
    var blackElo = blackEloRegEx.exec(data)[1];
    $('#playerGames').append(
        $('<div>').html(
            `${whiteName} ${whiteElo} - ${blackName} ${blackElo}`
        )
    );
}