const URL = "https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1"
const titles = [];
const bigTitles = [];
const smallTitles = [];
const imageURLs = [];
document.addEventListener("DOMContentLoaded", loadHamburgerMenu);

async function getData() {   
    const response = await fetch(URL);
    const data = await response.json();
    const results = data.data.results;

    // get titles and titles
    getTitles(results);
    getImageURL(results);
               
    // render boxes
    renderBoxes(bigTitles, smallTitles);
}

function getTitles(results){
    titles.length = 0;
    for (let i = 0; i < results.length; i++){
        titles.push(results[i].stitle);
    }
}

function getImageURL(results) {
    for (let i = 0; i < results.length; i++) {
        const fileList = results[i].filelist;
        const fileListArray = fileList.split("https://");
        const imageURL = "https://" + fileListArray[1];
        imageURLs.push(imageURL);
    }
    return imageURLs;
}

function renderBoxes(bigTitles, smallTitles) {
    // querySelectorAll() 
    const smallBoxContainers = document.querySelectorAll(".small-box");
    const bigBoxContainers = document.querySelectorAll(".big-box");
    
    // append small box
    smallBoxContainers.forEach((smallBoxContainer, index) => {
        // create elements, className, textContent, backgroundImage
        const imgDiv = document.createElement("div");
        imgDiv.className = "small-box-img";
        imgDiv.style.backgroundImage = `url('${imageURLs[index]}')`;
        
        const textDiv = document.createElement("div");
        textDiv.className = "small-box-text";
        textDiv.textContent = titles[index];
    
        // appendChild() 
        smallBoxContainer.appendChild(imgDiv);
        smallBoxContainer.appendChild(textDiv);
    });

    // create elements, className, textContent, backgroundImage
    bigBoxContainers.forEach((bigBoxContainer, index) => {
        // background image for big box container (index+3)
        bigBoxContainer.style.backgroundImage = `url('${imageURLs[index+3]}')`;

        const textDiv = document.createElement("div");
        textDiv.className = "big-box-text";
        textDiv.textContent = titles[index+3];

        const starDiv = document.createElement("div");
        starDiv.className = "star";  

        // appendChild()
        bigBoxContainer.appendChild(textDiv);
        bigBoxContainer.appendChild(starDiv);
    });
}

getData();

function loadHamburgerMenu() {
    const hamburgerMenu = document.getElementById("hamburger-menu");
    const menuContent = document.getElementById("menu-content");
    const closeBtn = document.getElementById("close");

    hamburgerMenu.addEventListener("click", () => {
        menuContent.style.display = "block";
    });

    closeBtn.addEventListener("click", () => {
        menuContent.style.display = "none";
    });
}