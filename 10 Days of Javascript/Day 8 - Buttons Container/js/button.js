window.onload = () => {
  const button = document.getElementById('btn');
  button.addEventListener('click', e => {
    e.currentTarget.innerText ++
  });
};
