// The function below checks if the data is -1. If it isn't, then the modal is
// shown. The modal is a popup window that is displayed on top of the current
// page.
$(document).ready(function() {
    var isSolved = $("#is-solved-data").data("is-solved");
    if (isSolved !== -1) {
        $("#check-modal").modal("show");
    }
});

// *****************************************************************************
// This is jQuery code for the crossword puzzle check modal.
// jQuery is a fast, small, and feature-rich JavaScript library. It makes
// tasks like HTML document traversal and manipulation, event handling, and
// animation much simpler with an easy-to-use API that works across various
// browsers. Introduced in 2006, it became one of the most used JavaScript
// libraries, although its usage has declined somewhat in recent years due to
// the rise of modern frameworks like Angular, React, and Vue.js. jQuery is
// still widely used for tasks like AJAX calls, DOM manipulation, and animations.

// AJAX is a technique for creating fast and dynamic web pages. It allows web
// pages to be updated asynchronously by exchanging data with a web server
// behind the scenes. This means that it is possible to update parts of a web
// page, without reloading the whole page. Classic web pages, (which do not
// use AJAX) must reload the entire page if the content should change.
// AJAX is based on internet standards, and uses a combination of:
// - XMLHttpRequest object (to exchange data asynchronously with a server)
// - JavaScript/DOM (to display/interact with the information)
// - CSS (to style the data)
// - XML (often used as the format for transferring data)
// Since AJAX uses JavaScript, it can send and receive data in various formats,
// including JSON, XML, HTML, and text files. AJAX is a misleading name.
// AJAX applications might use XML to transport data, but it is equally common
// to transport data as plain text or JSON text.

// Below is a jQuery function that is called when the document is ready.
// The document ready event occurs when the HTML document has been loaded and
// the DOM is ready, even if all the graphics haven’t loaded yet. If you want
// to manipulate the DOM or CSS before the page has loaded (for example, if you
// want to hide a section of the page until it has loaded), this is called
// DOMContentLoaded event in JavaScript. The ready() method specifies what
// happens when a ready event occurs. The ready event occurs when the DOM
// (document object model) has been loaded. Because this event occurs after the
// document is ready, it is a good place to have all other jQuery events and
// functions. Like all jQuery methods, ready() should only be attached to the
// document object.

// The function below gets the data from the data attribute in the HTML
// template. The data() method attaches data to, or gets data from, selected
// elements. When used to return data: This method returns the value of the
// data attribute of the FIRST matched element. When used to set data: This
// method sets the data attribute for ALL matched elements. Tip: Use the
// removeData() method to remove the data attribute from the selected elements.
// *****************************************************************************