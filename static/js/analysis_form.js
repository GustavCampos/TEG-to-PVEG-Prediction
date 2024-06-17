document.addEventListener('DOMContentLoaded', function() {
    const analysisForm = document.getElementById('analysis-form');
    const formFields = analysisForm.querySelectorAll('div.field');

    analysisForm.addEventListener('submit', function(event) {
        event.preventDefault();

        let submit = true;
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

        if (submit) {this.submit();}
    });
});