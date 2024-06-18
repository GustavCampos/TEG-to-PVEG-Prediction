document.addEventListener('DOMContentLoaded', function() {
    const startDateSpan = document.getElementById('start-date');
    const endDateSpan = document.getElementById('end-date');
    const docLang = document.querySelector("html").lang;
    

    // Calculate panel-number
    const panelNumberP = document.getElementById('panel-number');

    const totalPanelValue = parseFloat(panelNumberP.children.item(0).innerText);
    const singlePanelValue = parseFloat(panelNumberP.children.item(1).innerText);
    const panelNumber = Math.ceil(totalPanelValue / singlePanelValue);

    panelNumberP.innerHTML = panelNumber.toLocaleString(docLang, { 
        minimumFractionDigits: 0, 
        maximumFractionDigits: 0 
    });

    // Calculate total energy with all panels
    const totalEnergyP = document.getElementById('panel-number-x-pout');
    const totalEnergy = parseFloat(totalEnergyP.innerText);

    totalEnergyP.innerText = (totalEnergy * panelNumber);

    // Convert date items to local tz__________________________________
    const startDate = new Date(startDateSpan.innerText);
    startDateSpan.innerText = startDate.toLocaleDateString(docLang);

    const endDate = new Date(endDateSpan.innerText);
    endDateSpan.innerText = endDate.toLocaleDateString(docLang);


    // Formatting number values
    const hourValues = document.getElementsByClassName('format-value-num');

    for (let i = 0; i < hourValues.length; i++) {
        const curElement = hourValues.item(i); 

        const value = parseFloat(curElement.innerText);

        curElement.innerText = value.toLocaleString(docLang, { 
            minimumFractionDigits: 2, 
            maximumFractionDigits: 2 
        });
    }
});