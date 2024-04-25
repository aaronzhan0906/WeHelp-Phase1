document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const agreeCheckbox = document.getElementById("agree-check-box");
    const squareForm = document.getElementById("square-form");
    const square = document.getElementById("square");

    loginForm.addEventListener("submit", function(event) {
        if (!agreeCheckbox.checked) {
            alert("Please check the checkbox first.");
            event.preventDefault(); // Prevent form submission
        }
    });

    squareForm.addEventListener("submit", function(event) {
        const number = parseInt(square.value);
        const regex = /^[0-9]+$/;
        if (!regex.test(square.value) || parseInt(square.value) <= 0) {
            alert("Please enter a positive number.");
            event.preventDefault(); // Prevent form submission
        } else {
            window.location.href = `/square/${number}`;
            event.preventDefault();
        }
    });
});