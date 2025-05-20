let sun = document.querySelector('.sun');
let scene = document.querySelector('.scene');

sun.addEventListener('click', () => {
  scene.classList.toggle('night');
});