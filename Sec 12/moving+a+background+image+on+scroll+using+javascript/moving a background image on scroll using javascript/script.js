let pattern = document.querySelector('.bg');

window.addEventListener('scroll', () => {
    pattern.style.backgroundPosition = window.scrollY + 'px';
});


