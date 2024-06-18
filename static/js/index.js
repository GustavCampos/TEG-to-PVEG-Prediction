document.addEventListener('DOMContentLoaded', function() {
    const analysisForm = document.getElementById('analysis-form');
    const formFields = analysisForm.querySelectorAll('div.field');
    const startDateInput = document.getElementById('start-date');
    const endDateInput = document.getElementById('end-date');


    analysisForm.addEventListener('submit', function(event) {
        event.preventDefault();

        // Reset Dates Danger
        startDateInput.classList.remove('is-danger');
        const startHelp = startDateInput.parentElement.querySelector('p.help');
        startHelp.classList.remove('is-danger');
        startHelp.innerText = "";

        endDateInput.classList.remove('is-danger');
        const endHelp = endDateInput.parentElement.querySelector('p.help');
        endHelp.classList.remove('is-danger');
        endHelp.innerText = "";


        let submit = true;
        //Check all inputs are filled
        formFields.forEach(field => {
            const input = field.querySelector("input");
            if (!input) {return;}

            const help = field.querySelector("p.help")
            const dangerClass = "is-danger";
            const helpMessage = "Este campo não pode estar vazio"

            if (input.value === "") {
                input.classList.add(dangerClass);
                help.classList.add(dangerClass);
                help.innerText = helpMessage;
                submit = false;
            } else {
                input.classList.remove(dangerClass);
                help.classList.remove(dangerClass);

                if (help.innerText === helpMessage) {
                    help.innerText = "";
                }
            }
        });

        // Check dates
        const startDate = new Date(startDateInput.value);
        const endDate = new Date(endDateInput.value);

        const dateDiff = Math.round((endDate - startDate) / (1000*60*60*24));

        if (dateDiff < 1) {
            endDateInput.classList.add('is-danger');
            endHelp.classList.add('is-danger');
            endHelp.innerText = "A data final não pode ser igual à data inicial";
            submit = false;
        } 

        if (endDate < startDate) {
            endDateInput.classList.add('is-danger');
            endHelp.classList.add('is-danger');
            endHelp.innerText = "A data final não pode ser anterior à data inicial";
            submit = false;
        } 
        
        if (dateDiff > 365) {
            endDateInput.classList.add('is-danger');
            endHelp.classList.add('is-danger');
            endHelp.innerText = "O intervalo de datas não pode ser superior a um ano";
            submit = false;
        }

        //console.log(submit)
        if (submit) {this.submit();}
    });
});