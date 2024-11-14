document.getElementById('RegisterForm').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent the default form submission

    var formData = new FormData(this);

    fetch('/register/', { // Replace '/register/' with your actual registration URL
        method: 'POST',
        body: formData,
    })
   .then(response => response.json())
   .then(data => {
        if (data.success) {
            alert('Registration successful Please log in.');
            window.location.href = '/login/'; // Redirect to login page
        } else {
            alert('Error during registration: ' + data.message);
        }
    })
   .catch(error => console.error('Error:', error));
});