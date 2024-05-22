document.addEventListener('DOMContentLoaded', function() {
  const characterDiv = document.querySelector('#character');

  fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
      characterDiv.textContent = data.name;
    })
    .catch(error => {
      console.error('Error:', error);
    });
});
