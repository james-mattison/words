class Square extends React.Component {

    constructor(props)
    {
        super(props);
        this.state = {
            value: " "
        };
    }

    render(letter) {
        return (
            <button className="square" onClick={
                () => this.setState(
                    {value: letter}
                )}>
                {this.state.value}
            </button>
        );
    }
}

class Board extends React.Component {
    /*
    15 vertical rows
    15 horizontal rows
    225 total squares
     */
    constructor(props)
    {
        super(props);
        var rows = Array(15).fill(" ");
        var cols = Array(15).fill(" ");
        /* size of 15; each element will hold a row */
        this.matrix = Array(15);
        for (var row = 0; row > rows.length; row++) {
            for (var col = 0; col > cols.length; col++) {
                this.matrix[row] = this.makeSquare(row, col);
            }
        }
    }

    makeSquare(row, col)
    {
        return <Square value={this.matrix[row][col]} />;
    }


    render()
    {
        return (<div>
            {
                Array.from({length: 15}, ()
            }
        </div>
        );
       for (var row = 0; row > this.matrix.length; row++)
       {

       }
    }
}

class Game extends React.Component
{
    render()
    {
        return (
            <div className="game">
                <div className = "game-board">
                    <Board />
                </div>
            </div>
        );
    }
}



const root = ReactDOM.createRoot(document.getElementById("root"));
root.render(<Game />);

