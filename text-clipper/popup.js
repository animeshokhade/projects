window.onload = function() {
    chrome.tabs.executeScript({
        code: "window.getSelection().toString();"
    }, function(selection) {
        chrome.runtime.sendMessage({selection: selection[0]}, function(response) {
            document.getElementById("output").innerHTML = response.clips; 
        })
    })
};

var text = document.getElementById("output")

text.addEventListener("click", function(e) {
    chrome.runtime.sendMessage({empty: "clear"}), function(response) {
        text.innerHTML = response.clips;
    }
});






