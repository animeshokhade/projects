document.getElementById('heading').innerHTML = localStorage['title'] || 'Scribble';
document.getElementById('content').innerHTML = localStorage['text'] || 'This text is automatically saved every second';

setInterval(function() {
    // function that is saving the innerHTML of the div 
    localStorage['title'] = document.getElementById('heading').innerHTML; // default text 
    localStorage['text'] = document.getElementById('content').innerHTML; 
}, 1000); 