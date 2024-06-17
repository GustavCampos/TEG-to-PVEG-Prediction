document.addEventListener('DOMContentLoaded', function() {
    const startDateSpan = document.getElementById('start-date');
    const endDateSpan = document.getElementById('end-date');

    const doc_lang = document.querySelector("html").lang;
    

    // Convert date items to local tz__________________________________
    const startDate = new Date(startDateSpan.innerText);
    startDateSpan.innerText = startDate.toLocaleDateString(doc_lang);

    const endDate = new Date(endDateSpan.innerText);
    endDateSpan.innerText = endDate.toLocaleDateString(doc_lang);


    // Formatting number values
    const hourValues = document.getElementsByClassName('format-value-num');

    for (let i = 0; i < hourValues.length; i++) {
        const curElement = hourValues.item(i); 

        const value = parseFloat(curElement.innerText);

        curElement.innerText = value.toLocaleString(doc_lang, { 
            minimumFractionDigits: 2, 
            maximumFractionDigits: 2 
        });
    }

    // Calculate panel-number
    const panelNumberP = document.getElementById('panel-number');

    const totalPanelValue = parseFloat(panelNumberP.children.item(0).innerText);
    const singlePanelValue = parseFloat(panelNumberP.children.item(1).innerText);

    panelNumberP.innerHTML = Math.ceil(totalPanelValue / singlePanelValue)
        .toLocaleString(doc_lang, { 
            minimumFractionDigits: 0, 
            maximumFractionDigits: 0 
        }
    );
});