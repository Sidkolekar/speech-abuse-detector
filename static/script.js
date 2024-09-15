
function startRecognition() {
    fetch('/process', {
        method: 'POST'
    })
    .then(response => response.json())
    .then(data => {
        document.getElementById('resultText').innerText = "Recognized Text: " + data.text;
        document.getElementById('resultClassification').innerText = "Classification: " + data.classification;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('resultText').innerText = "Error occurred!";
    });
}
