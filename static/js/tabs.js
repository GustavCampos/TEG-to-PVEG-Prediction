document.addEventListener('DOMContentLoaded', () => {
    const tabLinks = document.querySelectorAll('a.tabLink');

    tabLinks.forEach(tabLink => {
        tabLink.addEventListener('click', function(event) {
            event.preventDefault();

            tabLinks.forEach(tabLink => {
                tabLink.parentElement.classList.remove('is-active');
                document.getElementById(`${tabLink.id}Content`).classList.add("is-hidden");
            })

            this.parentElement.classList.add('is-active');
            document.getElementById(`${this.id}Content`).classList.remove("is-hidden");
        });
    });
});