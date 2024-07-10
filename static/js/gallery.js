function openModal(src) {
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById("modalImage");
    modalImg.src = src;
    modal.style.display = 'flex';
    document.body.classList.add('modal-open'); // Блокування прокрутки

    requestAnimationFrame(() => {
        modal.classList.remove('hide');
        modal.classList.add('show');
    });
}

function closeModal(event) {
    var modal = document.getElementById("modal");
    var modalImg = document.getElementById("modalImage");

    if (event.target === modal || event.target.className === "close") {
        modal.classList.remove('show');
        modal.classList.add('hide');
        document.body.classList.remove('modal-open'); // Відновлення прокрутки

        setTimeout(function() {
            modal.style.display = 'none';
            modal.classList.remove('hide');
        }, 500); // Затримка в 0.5 секунд
    }
}

// Додаємо обробник подій на весь модальний контейнер
document.getElementById("modal").addEventListener("click", function(event) {
    if (event.target === this) {
        closeModal(event);
    }
});
