document.querySelectorAll('.show-more').forEach(button => {
    button.addEventListener('click', () => {
        const text = button.previousElementSibling;
        if (text.style.display === 'none' || text.style.display === '') {
            text.style.display = 'block';
            button.textContent = 'Показати менше';
        } else {
            text.style.display = 'none';
            button.textContent = 'Показати ще';
        }
    });
});