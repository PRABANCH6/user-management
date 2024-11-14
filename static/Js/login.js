var csrftoken = getCookie('csrftoken');

fetch('/login/', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrftoken,
    },
    body: JSON.stringify({
        username: document.getElementById('username').value,
        password: document.getElementById('password').value,
    }),
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        window.location.href = '/profile_home/';
    } else {
        alert('Error during login: ' + data.message);
    }
})
.catch(error => console.error('Error:', error));