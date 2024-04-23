document.addEventListener("DOMContentLoaded", function() {
    const loginForm = document.getElementById("login-form");
    const agreeCheckbox = document.getElementById("agree-check-box");
  
    loginForm.addEventListener("submit", function(event) {
      if (!agreeCheckbox.checked) {
        alert("請先勾選同意條款");
        event.preventDefault();
      }
    });
  });