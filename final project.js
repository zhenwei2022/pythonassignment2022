const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);





document.querySelector('#player-form').addEventListener('submit', function (evt) {
  evt.preventDefault();
  playerName = document.querySelector('#player-input').value;
  document.getElementById('replace-name').innerHTML = `<b>${playerName}</b>`;
  document.querySelector('#player-modal').classList.add('hide');
  rule();
  gameSetup(`${apiUrl}new_game?player=${playerName}&loc=EFHK`);
});


async function gameSetup(url) {
  try {
    const response = await fetch(url);
    console.log(response);
    const data = await response.json();
    console.log(data);
    // extracting the json data and putting into <p></p> element:
  document.querySelector('p').innerHTML = `${data[0].name}, you are now in ${data[0].location}. It is the starting point of your journey.<br> <br>
    The distance between Helsinki-Vantaa Airport and ${data[0].destination}, Hamad International Airport is ${data[0].distance}kilometers. Enjoy the journey!!`;
      } catch (error) {             //
    console.log('Error1');
  }
  }

gameSetup('http://127.0.0.1:5000/game_setup?player=ABC&loc=EFHK&city=Helsinki-Vantaa Airport&destination=Doha&distance=4396.12')