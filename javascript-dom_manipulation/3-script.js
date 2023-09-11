const head = document.querySelector('header');
const toggle = document.getElementById('toggle_header');

toggle.addEventListener('click', function onClick () {
  head.classList.toggle('green');
  head.classList.toggle('red');
});
