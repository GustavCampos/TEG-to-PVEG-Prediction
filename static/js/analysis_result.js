document.addEventListener('DOMContentLoaded', function() {
    const startDateSpan = document.getElementById('start-date');
    const endDateSpan = document.getElementById('end-date');

    // Convert date items to local tz__________________________________
    doc_lang = document.querySelector("html").lang;

    const startDate = new Date(startDateSpan.innerText);
    startDateSpan.innerText = startDate.toLocaleDateString(doc_lang);

    const endDate = new Date(endDateSpan.innerText);
    endDateSpan.innerText = endDate.toLocaleDateString(doc_lang);
});