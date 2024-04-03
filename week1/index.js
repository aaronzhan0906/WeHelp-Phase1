document.addEventListener("DOMContentLoaded", () => {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const menuContent = document.getElementById("menu-content");
    const closeBtn = document.getElementById("close");

    hamburgerMenu.addEventListener("click", () => {
        menuContent.style.display = "block";
    });

    closeBtn.addEventListener("click", () => {
        menuContent.style.display = "none";
    });
});