document.addEventListener('DOMContentLoaded', () => {
    const tabLinks = document.querySelectorAll('a.tabLink');

    tabLinks.forEach(tabLink => {
        tabLink.addEventListener('click', function(event) {
            event.preventDefault();

            tabLinks.forEach(tabLink => {
                tabLink.parentElement.classList.remove('is-active');
                document.getElementById(`${tabLink.id}Content`).style.display = 'none';
            })

            this.parentElement.classList.add('is-active');
            document.getElementById(`${this.id}Content`).style.display = 'block';
        });
    });
});