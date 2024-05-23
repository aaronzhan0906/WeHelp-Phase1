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

fetch('https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment.json')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('There was a problem with the fetch operation:', error));