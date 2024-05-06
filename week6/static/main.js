document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const agreeCheckbox = document.getElementById("agree-check-box");
    const signupForm = document.getElementById("signup-form");

    signupForm.addEventListener("submit", function(event) {
        const inputs = signupForm.querySelectorAll("input[name='signup-user'], input[name='signup-password'], input[name='signup-password-confirm']");
        let isEmpty = false;
        inputs.forEach(function(input) {
            if (input.value.trim() === "") {
                isEmpty = true;
            }
        });
        if (isEmpty) {
            alert("Please fill in all fields.");
            event.preventDefault();
        }
    });

    loginForm.addEventListener("submit", function(event) {
        if (!agreeCheckbox.checked) {
            alert("Please check the checkbox first.");
            event.preventDefault(); // Prevent form submission
        }
    });
});
