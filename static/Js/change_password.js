
function validateChangePassword() {
    var currentPassword = document.getElementById('currentPassword').value;
    var newPassword = document.getElementById('newPassword').value;
    var confirmNewPassword = document.getElementById('confirmNewPassword').value;

    // Basic client-side validation
    if (currentPassword.trim() === '') {
        alert('Current password is required');
        return false;
    }

    if (newPassword.trim() === '') {
        alert('New password is required');
        return false;
    }

    if (confirmNewPassword.trim() === '') {
        alert('Please confirm your new password');
        return false;
    }

    if (newPassword !== confirmNewPassword) {
        alert('New password and confirm password do not match');
        return false;
    }

    // If all validations pass, allow form submission
    return true;
}