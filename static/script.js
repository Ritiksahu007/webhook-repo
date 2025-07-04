function fetchEvents() {
    fetch('/events')
        .then(res => res.json())
        .then(data => {
            const list = document.getElementById('event-feed');
            list.innerHTML = '';
            data.forEach(event => {
                const li = document.createElement('li');
                li.textContent = event;
                list.appendChild(li);
            });
        });
}
setInterval(fetchEvents, 15000);
window.onload = fetchEvents;