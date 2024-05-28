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
        const resultContainer = document.getElementById('analisys-result');

        resultContainer.innerHTML = `
            <h2 class="title">Resultado da Análise</h2>

            <p>Para gerar ${response["wanted-energy"]} kWh de energia:</p>
            
            <div class="columns">
                <div class="column">
                    <h3>Quantidade de Madeira Necessária</h3>
                    <p>${response["wood-needed"]} kg</p>
                </div>
    
                <div class="column">
                    <h3>Quantidade de CO2 Emitido</h3>
                    <p>${response["teg-polution"]} kg</p>
                </div>

                <div class="column">
                    <h3>Área Preenchida por Painéis Solares</h3>
                    <p>${response["solar-panel-area"]} m2</p>
                </div>
            </div>
        `; 
    })
})