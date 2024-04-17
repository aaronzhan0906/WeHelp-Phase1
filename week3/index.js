let bigTitles = [];
let smallTitles = [];

async function getData() {
    try {
        const response = await fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1");
        const data = await response.json();
        const results = data.data.results;
        getTitles(results);
        smallTitles = [titles[0], titles[1], titles[2]];
        bigTitles = [titles[3], titles[4], titles[5], titles[6], titles[7], titles[8], titles[9], titles[10]];
        renderSmallBox(bigTitles, smallTitles);
    } catch (error) {
        console.error("Error fetching data:", error);
    }
}

getData();

const titles = [];
function getTitles(results){
    for (let i = 0; i < results.length; i++){
        titles.push(results[i].stitle);
    }
}

function renderSmallBox(bigTitles, smallTitles) {
    // 找到每個具有 ".small-box" 類別的元素
    const smallBoxContainers = document.querySelectorAll(".small-box");
    const bigBoxContainers = document.querySelectorAll(".big-box");
    
    // 對每個 small-box 元素執行操作
    smallBoxContainers.forEach((smallBoxContainer, index) => {
        const imgDiv = document.createElement("div");
        imgDiv.className = "small-box-img";
        imgDiv.style.backgroundImage = "url('your-image-url.jpg')";
    
        const textDiv = document.createElement("div");
        textDiv.className = "small-box-text";
        textDiv.textContent = smallTitles[index]; // 使用索引值設置內容
    
        // 將創建的元素添加到每個容器中
        smallBoxContainer.appendChild(imgDiv);
        smallBoxContainer.appendChild(textDiv);
    });

    // 對每個 big-box 元素執行操作
    bigBoxContainers.forEach((bigBoxContainer, index) => {
        bigBoxContainer.style.backgroundImage = "url('your-image-url.jpg')";

        const textDiv = document.createElement("div");
        textDiv.className = "big-box-text";
        textDiv.textContent = bigTitles[index];

        const starDiv = document.createElement("div");
        starDiv.className = "star";  

        // 將創建的元素添加到每個容器中
        bigBoxContainer.appendChild(textDiv);
        bigBoxContainer.appendChild(starDiv);
    });
}






// document.addEventListener("DOMContentLoaded", () => {
//     const hamburgerMenu = document.getElementById("hamburger-menu");
//     const menuContent = document.getElementById("menu-content");
//     const closeBtn = document.getElementById("close");

//     hamburgerMenu.addEventListener("click", () => {
//         menuContent.style.display = "block";
//     });

//     closeBtn.addEventListener("click", () => {
//         menuContent.style.display = "none";
//     });
// });