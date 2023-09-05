// The function below checks the value of passcode_verified passed from the HTML
// If passcode_verified is not None, then show modals; if passcode_verified is
// 0 or 1, then run the automatic redirection stuff
$(document).ready(function() {
  var isPasscodeVerified = $("#is-passcode-verified").data("is-passcode-verified");

  if (isPasscodeVerified === -1) {
    $("#verification-modal").modal("show");
  }
  else if (isPasscodeVerified === 0 || isPasscodeVerified === 1) {
    $("#verification-modal").modal("show");
    // Wait for 30 seconds (30000 milliseconds)
    setTimeout(function() {
      // Redirect to the final message page
      window.location.href = finalMessageURL;
    }, 30000);
  }
});
