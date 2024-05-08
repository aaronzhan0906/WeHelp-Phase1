document.addEventListener("DOMContentLoaded", function() {
    const signinForm = document.getElementById("signin-form");
    const signupForm = document.getElementById("signup-form");
    
    signupForm.addEventListener("submit", function(event) {
        const inputs = signupForm.querySelectorAll("input[name='signup-name'], input[name='signup-username'], input[name='signup-password']");
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
  
    signinForm.addEventListener("submit", function(event) {
        const inputs = signinForm.querySelectorAll("input[name='signin-username'], input[name='signin-password']");
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

    
});