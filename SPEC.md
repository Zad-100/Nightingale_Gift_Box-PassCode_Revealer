# Spec of the Project
---
## 1. Introduction
This is a Django Web App that is meant to help _Nightingale_ (my female bestie) to hunt the passcode 
of a certain combination lock with 3 digits put on the box that contains her birthday gift. (Her 
birthday is on September 13th! I have only about 15 days to complete this project (deadline would 
be August 30th, then) so that I can wrap up the gift and send it to her in time! We live in different 
states - I would have to speedpost it to her.)

The link to this web app (most probably, hosted on Azure) would be converted into a QR code for her 
to scan, pasted on the gift box, I would be sending her. She would then be able to access this web 
app on her phone or PC, and start hunting for the passcode. It would have 3 interactive puzzles for 
her to solve, and solving each puzzle successfully would reveal to her one digit of the three. Of 
course, with some fun messages from my side.

## 2. Puzzles
#### 2.1. __Puzzle 1: The Slider Picture Puzzle__
This is a picture puzzle, where the picture is sliced into 9 pieces, and the pieces are shuffled. 
She would have to slide the pieces around to put the picture back together. The picture would be 
a picture of her in red saree (the very first saree pic she had shared with me and I had completely 
gone _"Flipped and Fallen"_ which also happens to be the title of the poem I wrote on seeing that 
picture of her).

#### 2.2. __Puzzle 2: Crossword with Riddle Clues__
This is a crossword puzzle, where the clues are riddles. She would have to solve the riddles to 
get the words that would fit into the crossword. The riddles would be related and based on some 
significant events in our friendship.

#### 2.3. __Puzzle 3: <TBD>__
This is a puzzle that I have not yet decided on. I would be adding it later. For now, I have 
thought about a Hangman Game where she would have to guess the letters of a word, related to her 
in some way or to our friendship. If that doesn't work, I have decided to simply make a form for 
her to fill up about herself and her interests (also telling her that would be a test of how well 
she knows herself and that I have the answers so, she should answer honestly). This would be a 
dummy puzzle that would reveal the third digit of the passcode and tell her that this data was being 
taken so I could know her better for a gifting next year. ;)

## 3. Web Pages
#### 3.1. __Home Page__
The home page of the Web App would simply wish her happy birthday and welcome her to the app. It would 
also contain introduction about what the web app is and starting instructions.

#### 3.2. __Puzzle 1 Page__
This page would contain the slider picture puzzle. It would have the picture sliced into 9 pieces, 
shuffled. It would also have a timer that would start as soon as she opens the page. The timer would 
be stopped as soon as she solves the puzzle. It would also have a button to reveal the first digit 
of the passcode, once she solves the puzzle. It would also have a button to go to the next puzzle 
as well as a back button to go to the previous page. However, this previous button would be disabled 
as it is the first puzzle she's solving. This page would also contain specific instructions for 
her to solve the puzzle.

#### 3.3. __Puzzle 2 Page__
This page would contain the crossword puzzle. It would have the crossword and the clues along with the 
instructions for the puzzle. It would also have a timer that would start as soon as she opens the page. 
The timer would be stopped as soon as she solves the puzzle. It would also have a button to reveal the 
second digit of the passcode, once she solves the puzzle. It would also have a button to go to the 
next puzzle as well as a back button to go to the previous page.

#### 3.4. __Puzzle 3 Page__
This page would contain the third puzzle. It would have the puzzle and the instructions for the puzzle.
Here, next button would be disabled.


> The said timer in each puzzle is only for fun and doesn't have any significance yet. I might add some significance to it later.


#### 3.5. __Passcode Page__
This page would solely be for her to enter the passcode in the same order she found them and verify 
the passcode. After verification, she would be led to the next letter page. If the passcode is wrong, 
she would be given two more chances to enter the correct passcode. If she fails to enter the correct passcode in the third
attempt, she would be shown a message telling her that the passcode is wrong and the right passcode would be 
shown to her.

#### 3.6. __A letter From My Side Page__
This page would contain a letter from my side, wishing her happy birthday and telling her how much she 
means to me. It would be the same letter I would have handwritten and kept along with the earrings 
and anklet, all of which would be kept inside the locker box.

#### 3.7. __A Thank You Page__
A simple thank you page.


## Additional Features
We need to make sure the the app is mobile-responsive since there's a good chance she might access 
it via a smartphone after scanning the QR code.