// // Detecting the appearence of the star which indicates that the puzzle has
// // been solved
// // Start the script when the content of the document is fully loaded
// document.addEventListener("DOMContentLoaded", function() {
//     console.log("DOM fully loaded and parsed");
//     // function checkPuzzleSolved() {
//     //     var starImg = document.querySelector("img");
//     //     if (starImg) {
//     //         // puzzle has been solved, proceed to next step
//     //         console.log("Puzzle solved!!!");
//     //     }
//     // }
    
//     // // Call the function every 1 second
//     // setInterval(checkPuzzleSolved, 1000);

//     function setUpObserver() {
//         var observer = new MutationObserver(function(mutations) {
//             mutations.forEach(function(mutation) {
//                 if (mutation.type) {
//                     var imgElement = document.body.querySelector('img[src*="/static/1691835468/img/star.svg"]');
//                     if (imgElement) {
//                         // Puzzle is solved, navigate to the next page
//                         // window.location.href = "/message-2";
//                         console.log("Puzzle solved!!!");  // <-------
//                     }
//                 }
//             });
//         });
        
//         var config = { attributes: true, childList: false, characterData: false, subtree: true };
//         observer.observe(document.body, config);
//     }

//     setInterval(setUpObserver, 500);
// });