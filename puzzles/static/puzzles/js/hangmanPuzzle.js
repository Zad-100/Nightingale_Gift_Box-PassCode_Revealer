const wordDisplay = document.querySelector(".word-display");
const guessesText = document.querySelector(".guesses-text b");
const keyboardDiv = document.querySelector(".keyboard");
const hangmanImage = document.querySelector(".hangman-box img");
const gameModal = document.querySelector(".game-modal");
const playAgainBtn = gameModal.querySelector("button");

// Initializing game variables
let currentWord, correctLetters, wrongGuessCount;
const maxGuesses = 6;

const resetGame = () => {
    // Ressetting game variables and UI elements
    correctLetters = [];
    wrongGuessCount = 0;
    hangmanImage.src = `${staticImagePath}hangman-0.svg`;
    guessesText.innerText = `${wrongGuessCount} / ${maxGuesses}`;
    wordDisplay.innerHTML = currentWord.split("").map(() => `<li class="letter"></li>`).join("");
    keyboardDiv.querySelectorAll("button").forEach(btn => btn.disabled = false);
    gameModal.classList.remove("show");
}

const getRandomWord = () => {
    // Selecting a random word and hint from the wordList
    const { word, hint } = wordList[Math.floor(Math.random() * wordList.length)];
    currentWord = word; // Making currentWord as random word
    document.querySelector(".hint-text b").innerText = hint;
    resetGame();
}

const gameOver = (isVictory) => {
    // After game complete.. showing modal with relevant details
    const modalText = isVictory ? `You found the word:` : 'The correct word was:';
    // gameModal.querySelector("img").src = `${staticImagePath}${isVictory ? 'victory' : 'lost'}.gif`;
    if (isVictory) {
        gameImage.src = `${staticImagePath}victory.gif`;
        gameImage.classList.add("victory-image");
        gameImage.classList.remove("lost-image");  // Remove lost-image class if it exists
    } else {
        gameImage.src = `${staticImagePath}lost.gif`;
        gameImage.classList.add("lost-image");
        gameImage.classList.remove("victory-image");  // Remove victory-image class if it exists
    }
    
    gameModal.querySelector("h4").innerText = isVictory ? 'Congrats!' : 'Game Over!';
    gameModal.querySelector("p").innerHTML = `${modalText} <b>${currentWord}</b>`;
    gameModal.classList.add("show");
}

const initGame = (button, clickedLetter) => {
    // Checking if clickedLetter is exist on the currentWord
    if(currentWord.includes(clickedLetter)) {
        // Showing all correct letters on the word display
        [...currentWord].forEach((letter, index) => {
            if(letter === clickedLetter) {
                correctLetters.push(letter);
                wordDisplay.querySelectorAll("li")[index].innerText = letter;
                wordDisplay.querySelectorAll("li")[index].classList.add("guessed");
            }
        });
    } else {
        // If clicked letter doesn't exist then update the wrongGuessCount and hangman image
        wrongGuessCount++;
        hangmanImage.src = `${staticImagePath}hangman-${wrongGuessCount}.svg`;
    }
    button.disabled = true; // Disabling the clicked button so user can't click again
    guessesText.innerText = `${wrongGuessCount} / ${maxGuesses}`;

    // Calling gameOver function if any of these condition meets
    if(wrongGuessCount === maxGuesses) return gameOver(false);
    if(correctLetters.length === currentWord.length) return gameOver(true);
}

// Creating keyboard buttons and adding event listeners
for (let i = 97; i <= 122; i++) {
    const button = document.createElement("button");
    button.innerText = String.fromCharCode(i);
    keyboardDiv.appendChild(button);
    button.addEventListener("click", (e) => initGame(e.target, String.fromCharCode(i)));
}

getRandomWord();
playAgainBtn.addEventListener("click", getRandomWord);




































































// // The list of words for the Hangman game
// const words = ['NIGHTINGALE', 'BIRTHDAY', 'CELEBRATION', 'SURPRISE', 'PRESENT', 'CAKE', 'PARTY', 'FRIENDS'];

// // Select a word randomly from the list
// let word = words[Math.floor(Math.random() * words.length)];

// // Represents the word as underscores, hiding the actual characters
// let answerArray = [];
// for (let i = 0; i < word.length; i++) {
//     answerArray[i] = '_';
// }

// let remainingLetters = word.length;

// let messageElement = document.getElementById("message");
// let wordDisplayElement = document.getElementById("wordDisplay");

// // Main game loop
// while (remainingLetters > 0) {
//     wordDisplayElement.innerText = answerArray.join(' '); // Show the player their progress

//     let guess = prompt('Guess a letter, or click Cancel to stop playing.').toUpperCase();

//     if (guess === null) {
//         // Exit the game loop if the player wants to quit
//         messageElement.innerText = "You've chosen to exit the game!";
//         break;
//     } else if (guess.length !== 1) {
//         messageElement.innerText = "Please enter a single letter.";
//     } else {
//         // Update the game state with the guess
//         for (let j = 0; j < word.length; j++) {
//             if (word[j] === guess && answerArray[j] === '_') {
//                 answerArray[j] = guess;
//                 remainingLetters--;
//             }
//         }
//     }
// }

// // Display the answer and congratulate the player
// messageElement.innerText = "Good job! The answer was " + word;