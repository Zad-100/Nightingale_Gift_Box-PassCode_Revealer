// Logic to toggle visibility of a message inside the messaage_1 template

document.getElementById("showMessageButton").addEventListener("click", function() {
    var hiddenMessageDiv = document.getElementById("hiddenMessage");
    if(hiddenMessageDiv.style.display === "none") {
      hiddenMessageDiv.style.display = "block";
    }
    else {
      hiddenMessageDiv.style.display = "none";
    } // end if-else
});