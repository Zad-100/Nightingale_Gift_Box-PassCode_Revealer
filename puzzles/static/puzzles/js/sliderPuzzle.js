// Start the script when the content of the document is fully loaded
document.addEventListener("DOMContentLoaded", function() {
    // Get the board element where all the tiles are contained
    const board = document.querySelector(".board");

    // Convert the NodeList of tiles to an array for easier manipulation
    let tiles = Array.from(board.children);

    // Get the blank tile element
    const blankTile = document.querySelector(".blank");

    // Initialise the "show numbers" boolean as false
    let showNumbers = false; 


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
            // Hide the show-numbers button
            document.querySelector("#show-numbers-button").style.display = "none";
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

    shuffleTiles() // initialise board by shuffling tiles


    // Add an event listener to the show numbers button to listen for clicks
    document.getElementById("show-numbers-button").addEventListener("click",
                                                    function() {
        // Toggle the showNumbers boolean
        showNumbers = !showNumbers;
        // Call the function to show/hide the numbers
        updateNumberOverlay();
    }); // end EventListener

    function updateNumberOverlay() {
        const numberElements = document.querySelectorAll('.tile-number');
        numberElements.forEach(element => {
            if (showNumbers) {
                element.style.display = "flex";
            } else {
                element.style.display = "none";
            }
        }); // end forEach
    } // end function updateNumberOverlay()
});