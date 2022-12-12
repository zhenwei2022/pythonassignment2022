const map = L.map('map', {tap: false});
L.tileLayer('https://{s}.google.com/vt/lyrs=s&x={x}&y={y}&z={z}', {
  maxZoom: 20,
  subdomains: ['mt0', 'mt1', 'mt2', 'mt3'],
}).addTo(map);
map.setView([60, 24], 7);



const apiUrl = 'http://127.0.0.1:5000/';
const startLoc = 'EFHK';
const globalGoals = [];

const buleIcon = L.divIcon({className: 'blue-icon'});
const greenIcon = L.divIcon({className: 'green-icon'});

document.querySelector('#player-form').addEventListener('submit', function (evt) {
  evt.preventDefault();
  playerName = document.querySelector('#player-input').value;
  document.getElementById('replace-name').innerHTML = `<b>${playerName}</b>`;
  document.querySelector('#player-modal').classList.add('hide');
  rule();
  gameSetup(`${apiUrl}new_game?loc=EFHK`);
});


async function gameSetup(url) {
  try {
    const response = await fetch(url);
    const data = await response.json();
    updateWeather(data[0]);
    updateLocation(data[0]);
    await addDestination(data);
      } catch (error) {
    console.log('Error1');
  }
  }

function updateStatus(status){
  document.querySelector('#player-name').innerHTML = 'Player: ${status.name}';
  document.querySelector('#consumed').innerHTML = status.co2.consumed;
  document.querySelector('#budget').innerHTML =  status.co2.budget;
}

function checkGoals(meets_goals) {
  if (meets_goals.length >0 ) {
    for (let goal of meets_goals) {
      if(!globalGoals.includes(goal)) {
        document.querySelector('.goal').classList.remove('hide');
        location.href = '#goals';
      }
    }
  }
}

function showWeather(airport) {
  document.querySelector('#airport-name').innerHTML = 'Weather at ${airport.name}';
  document.querySelector('#airport-tem').innerHTML = '${airport.weather.tem}°C';
  document.querySelector('#weather-icon').src = airport.weather.icon;
  document.querySelector('#airport-conditions').innerHTML = airport.weather.description;
  document.querySelector('#airport-wind').innerHTML = '${airport.weather.wind.speed} m/s';

}

function updateGoals(goals) {
  document.querySelector('#goals').innerHTML = '';
  for(let goal of goals) {
    const li =  document.createElement('li');
    const figure = document.createElement('figure');
    const img = document.createElement('img');
    const figcaption = document.createElement('figcaption');
    img.src = goal.icon;
    img.alt = 'goal name: ${goal.name}';
    figcaption.innerHTML = goal.description;
    figure.append(img);
    figure.append(figcaption);
    li.append(figure);
    if(goal.reached) {
      li.classList.add('done');
    }
    document.querySelector('#goals').append(li);
  }
}
function checkGameOver (budget) {
  if (buget <= 0) {
    alert('Game Over.');
    return false;
  }
  return true;
}

async function gameSetup(url) {
  try {
    const gameData = await getData(url);
    console.log(gameData);
    updateStatus(gameData.status);
    updateGoal(gameData.goals);
    if(!checkGameOver(gameData.status.co2.budget)) return;
    for (let airport of gameData.location) {
      const marker = L.marker([airport.latitude, airport.longitude]).addTo(map);
      if(airport.active){
        showWeather(airport);
        checkGoals(airport.weather.meets_goals);
        marker.bindPopup('You are here: <b>${airport.name}</b>');
        marker.openPopup();
        marker.setIcon(greenIcon);
      } else {
          marker.setIcon(blueIcon);
          const popupContent = document.createElement('div');
          const h4 = document.createElement('h4');
          h4.innerHTML = airport.name;
          popupContent.append(h4);
          const goButton = document.createElement('button');
          goButton.classList.add('button');
          goButton.innerHTML = 'Fly here';
          popupContent.append(goButton);
          const p = document.createElement('p');
          p.innerHTML = 'Distance ${airport.distance} km';
          popupContent.append(p);
          marker.bindPopup(popupContent);
          goButton.addEventListener('click', function() {
            gameSetup();
        })
      }
    }

  } catch (error) {
    console.log('Error1');
  }
}

gameSetup('http://127.0.0.1:5000/game_setup?player=ABC&loc=EFHK&city=Helsinki-Vantaa Airport&destination=Doha&distance=4396.12')

document.querySelector('.goal').addEventListener('click', function(evt) {
 evt.currentTarget.classList.add('hide');
})