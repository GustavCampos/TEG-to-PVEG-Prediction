const analisysForm = document.getElementById('analisys-form');

analisysForm.addEventListener('submit', function(event) {
    event.preventDefault();

    const formData = new FormData(analisysForm);

    const requestHeader = {
        method: 'POST',
        body: formData,
        mode: "cors"
    } 

    fetch("/api/calculate_analisis", requestHeader).then(response => {
        if (response.status >= 200 && response.status < 300) {return response.json();}
        throw new Error(response.statusText);
    }).then(response => {
        const modalButton = document.getElementById('analysis-result-button');
        const resultDiv = document.getElementById('analysis-result-content');

        preTag = document.createElement('pre');
        preTag.innerText = JSON.stringify(response, null, 4);

        resultDiv.innerHTML = "";
        resultDiv.appendChild(preTag); 
        modalButton.click();
    })
})