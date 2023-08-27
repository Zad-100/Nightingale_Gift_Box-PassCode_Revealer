/*
A* Algorithm code to be used to make the "Next Move Hint" button
A* Algo is used to find the shortest path from current state to goal state
Here's a basic outline of what the A* function will do:

1. Maintain a "priority queue" of possible board states, sorted by their
   estimated "cost" to reach the solved state.
2. Start with the initial board state and calculate its cost.
3. Take the board state with the lowest estimated cost and generate its
   neighbors (i.e., board states that can be reached in one move).
4. Update their estimated costs and add them to the queue.
5. Repeat steps 3-4 until the queue contains the solved state.
*/
function findPathWithAStar(initialBoard) {
    const goal = "123456789"; // Solved state
    let visited = new Set(); // Set to keep track of visited states
    let priorityQueue = [{ board: initialBoard, cost: 0, moves: "" }]; // Priority queue
  
    while (priorityQueue.length > 0) {
      // Sort the priority queue by estimated cost to goal
      priorityQueue.sort((a, b) => a.cost - b.cost);
      
      // Take the board state with the lowest estimated cost
      const current = priorityQueue.shift();
      visited.add(current.board);
  
      // Check if the current board state is the goal
      if (current.board === goal) {
        return current.moves;
      }
  
      // Generate neighbors
      let neighbors = generateNeighbors(current.board);
  
      // Calculate costs for neighbors and add them to priority queue
      for (let neighbor of neighbors) {
        const newBoard = neighbor.board;
        if (!visited.has(newBoard)) {
          priorityQueue.push({
            board: newBoard,
            cost: current.cost + 1 + heuristic(newBoard, goal),
            moves: current.moves + neighbor.move
          });
        }
      }
    }
  
    return "No solution";
}
  
// Function to generate neighbors for a given board state
function generateNeighbors(boardStr) {
    // Implement the logic to generate neighbors (1-step reachable states)
    // Return them as an array of { board: newBoard, move: moveType }
    const neighbors = [];
    const boardArray = boardStr.split('').map(Number);
    const blankIndex = boardArray.indexOf(9);

    // Neighbors can be up, down, left, or right
    const dx = [-1, 1, 0, 0];
    const dy = [0, 0, -1, 1];

    const rows = 3;
    const cols = 3;
    // Add a label for each move direction
    const moveLabels = ['U', 'D', 'L', 'R'];

    for (let i = 0; i < 4; i++) {
        const newRow = Math.floor(blankIndex / rows) + dx[i];
        const newCol = (blankIndex % cols) + dy[i];

        if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
            const newIndex = newRow * rows + newCol;
            
            // Swap and generate a new board state string
            [boardArray[blankIndex], boardArray[newIndex]] = [boardArray[newIndex], boardArray[blankIndex]];
            neighbors.push({ board: boardArray.join(''), move: moveLabels[i] }); // Add move label here
            
            // Swap back to original for the next iteration
            [boardArray[blankIndex], boardArray[newIndex]] = [boardArray[newIndex], boardArray[blankIndex]];
        }
    }
    
    return neighbors;
    // for (let i = 0; i < 4; i++) {
    //     const newRow = Math.floor(blankIndex / rows) + dx[i];
    //     const newCol = (blankIndex % cols) + dy[i];
        
    //     if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
    //     const newIndex = newRow * rows + newCol;
        
    //     // Swap and generate a new board state string
    //     [boardArray[blankIndex], boardArray[newIndex]] = [boardArray[newIndex], boardArray[blankIndex]];
    //     neighbors.push(boardArray.join(''));
        
    //     // Swap back to original for the next iteration
    //     [boardArray[blankIndex], boardArray[newIndex]] = [boardArray[newIndex], boardArray[blankIndex]];
    // }
}

// Heuristic function to estimate cost from current state to goal
function heuristic(boardStr) {
    // Implement heuristic (can start with number of misplaced tiles)
    let distance = 0;
    for (let i = 0; i < boardStr.length; i++) {
        const tile = Number(boardStr[i]);
        if (tile !== 9 && tile !== i + 1) {
        distance += 1;
        }
    }
    return distance;
}



// Start the script when the content of the document is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Get the board element where all the tiles are contained
    const board = document.querySelector(".board");

    // Convert the NodeList of tiles to an array for easier manipulation
    let tiles = Array.from(board.children);

    // Get the blank tile element
    const blankTile = document.querySelector(".blank");

    // Initialise the futureMoves variable
    let futureMoves = "";


    // The board should be solvable. So check for solvability and
    // shuffle the board til it's solvable

    // Function to count inversions in the tiles array passed in
    // An inversion is when a tile precedes another tile with a lower number
    function countInversions(tilesArray) {
        // Initialise inversion count to 0
        let inversions = 0;

        // Loop through the tiles array
        for (let i = 0; i < tilesArray.length; i++) {
            // Loop through the tiles array again starting from the next tile
            // after the current tile
            for (let j = i + 1; j < tilesArray.length; j++) {
                // If the current tile has a higher order than the next tile
                // but a lower number, increment inversions
                if (tilesArray[i] > tilesArray[j]) {
                        inversions++;
                } // end if
            } // end for
        } // end for

        return inversions;
    } // end function countInversions()

    // Function to shuffle the tiles in random order
    function shuffleTiles() {

        // Loop until the board is solvable
        let invCount;
        do {
            // Randomly sort the tiles array
            tiles.sort(() => 0.5 - Math.random());

            // Get the order of each tile in a 1D array
            const tilesOrder = tiles.map(tile => parseInt(tile.dataset.order));
            // Count the number of inversions in the tiles array
            invCount = countInversions(tilesOrder);
        } while (invCount % 2 !== 0); // end do-while
        // // Randomly sort the tiles array
        // tiles.sort(() => 0.5 - Math.random());
        
        // Append each tile to the board
        tiles.forEach(tile => board.appendChild(tile));
        // alert(invCount)
    } // end function shuffleTiles()

    /*
    * Convert the board state to a unique string representation
    * @param {Array} tilesArray - Array of tile elements in their current order
    * @return {String} - String representation of the board state
    */
    function boardToString(tilesArray) {
        // Get the order of each tile in a 1D array
        const tilesOrder = tilesArray.map(tile => (tile.dataset.order));

        // Convert the array to a string
        return tilesOrder.join("");
    } // end function boardToString()
    console.log(boardToString(tiles));

    // Function to swap the position of the two tiles
    function swapTiles(tile1, tile2) {
        // Create a temp element for swapping
        const hold = document.createElement("div");
        
        // Insert temp element before tile1
        board.insertBefore(hold, tile1);

        // Swap tile1 with tile2
        board.insertBefore(tile1, tile2);

        // Swap tile2 with temp element
        board.insertBefore(tile2, hold);

        // Remove temp element
        board.removeChild(hold);
    } // end function swapTiles()

    // Function to check if a tile is adjacent to the blank tile
    function isAdjacent(tile) {
        const blankIndex = [...tiles].indexOf(blankTile);
        const tileIndex = [...tiles].indexOf(tile);
        
        // Calculate the # of tiles in one row (3 for 3x3 slider puzzle)
        const rowSize = Math.sqrt(tiles.length);

        // Check if tiles are horizontally adjacent on the same row or
        // vertically adjacent
        return (((Math.abs(blankIndex - tileIndex) === 1) && 
         (Math.floor(blankIndex / rowSize) === Math.floor(tileIndex / rowSize))) ||
         (Math.abs(blankIndex - tileIndex) === rowSize));
    } // end function isAdjacent()

    // Function to check if puzzle is solved
    function isPuzzleSolved() {
        if (tiles.every(
            (tile, index) => 
            tile.dataset.order == index + 1 || tile.classList.contains("blank")
        )) {
            // Add elements to the HTML to display the full picture
            // Hide the board
            document.querySelector(".board").style.display = "none";
            // Hide the solve button
            document.querySelector("#solve-button").style.display = "none";
            // Create a div for the full picture element
            const completeImage = document.createElement('div');
            // Add class to style the image
            completeImage.className = "complete-image";
            // Append to the body
            document.body.appendChild(completeImage);

            // Add elements to the HTML to display a congratulatory message
            const congrats = document.createElement('div');
            congrats.innerHTML = "<h3>Are badhaaiiiii, you solved it!!! 🎉</h3>"
            document.body.appendChild(congrats);


            // Redirect to the message_1 page after 4 seconds
            setTimeout(() => {
                window.location.href = message_1_URL;
            }, 4000);
        }
    } // end function isPuzzleSolved()

    // Add an event listener to board to listen for tile clicks
    board.addEventListener("click", function(event) {
        const tile = event.target; // tile that was clicked

        // If clicked tile is not the blank tile and it's
        // adjacent to the blank tile
        if (tile !== blankTile && isAdjacent(tile)) {
            // Swap clicked tile with blank one
            swapTiles(tile, blankTile);

            // Update the tiles list after swap
            tiles = Array.from(board.children);

            // After every move, check if the puzzle is solved
            isPuzzleSolved()
        } // end if
    }); // end EventListener

    // Add an event listener to the solve button to listen for clicks
    document.querySelector("#solve-button").addEventListener("click",
                                                              solvePuzzle);

    // Function to solve the puzzle
    function solvePuzzle() {
        tiles.sort((a, b) => {
            return a.dataset.order - b.dataset.order;
        });

        tiles.forEach(tile => board.appendChild(tile));

        // Update the tiles list after sorting
        tiles = Array.from(board.children);
    } // end function solvePuzzle()


    // Function to update the board with a new state
    function updateBoardWithNewState(newBoardState) {
        const newBoardArray = newBoardState.split("").map(Number);
        const blankIndexNew = newBoardArray.indexOf(9);
    
        const blankTile = tiles.find(tile => tile.dataset.order == "9");
        const tileToSwap = tiles.find(tile => tile.dataset.order == newBoardArray[blankIndexNew].toString());
    
        swapTiles(blankTile, tileToSwap);
    
        // Update the tiles list after swap
        tiles = Array.from(board.children);
    }
    
    // Function to apply the next move
    function applyMove(move) {
        const boardArray = boardToString(tiles).split("").map(Number);
        const blankIndex = boardArray.indexOf(9);
        const rows = 3;
        const cols = 3;
        let dx = 0, dy = 0;
    
        // Determine the direction to move the blank tile
        switch (move) {
            case 'U':
                dx = -1;
                dy = 0;
                break;
            case 'D':
                dx = 1;
                dy = 0;
                break;
            case 'L':
                dx = 0;
                dy = -1;
                break;
            case 'R':
                dx = 0;
                dy = 1;
                break;
            default:
                return;
        }
    
        const newRow = Math.floor(blankIndex / rows) + dx;
        const newCol = (blankIndex % cols) + dy;
    
        if (newRow >= 0 && newRow < rows && newCol >= 0 && newCol < cols) {
            const newIndex = newRow * rows + newCol;
    
            // Swap tiles
            [boardArray[blankIndex], boardArray[newIndex]] = [boardArray[newIndex], boardArray[blankIndex]];
            
            // Update the board state
            updateBoardWithNewState(boardArray.join("")); // You'll need to write this function
        }
    }
    

    // Add an event listener for next-move-hint button
    document.getElementById("next-move-hint").addEventListener("click", function() {
        if (futureMoves === "") {
            const currentBoardState = boardToString(tiles);
            futureMoves = findPathWithAStar(currentBoardState);
            console.log(futureMoves);
        }
        
        if (futureMoves !== "No solution" && futureMoves.length > 0) {
            const nextMove = futureMoves[0];
            futureMoves = futureMoves.slice(1);
            
            applyMove(nextMove);
        } else {
            alert("No more moves or puzzle is unsolvable.");
        }
    });
    

    shuffleTiles() // initialise board by shuffling tiles
});