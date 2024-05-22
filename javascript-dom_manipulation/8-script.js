window.addEventListener('load', function() {
  const helloDiv = document.querySelector('#hello');

  fetch('https://hellosalut.stefanbohacek.dev/?lang=fr')
    .then(response => response.json())
    .then(data => {
      helloDiv.textContent = data.hello;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
