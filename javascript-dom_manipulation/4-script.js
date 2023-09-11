const add = document.getElementById('add_item');
const ul = document.querySelector('.my_list');

add.addEventListener('click', function onClick () {
  const li = document.createElement('li');
  li.textContent = 'Item';
  ul.appendChild(li);
});
