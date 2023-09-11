const head = document.querySelector('header');
const updater = document.getElementById('update_header');

updater.addEventListener('click', function onClick () {
  head.textContent = 'New Header!!!';
});
