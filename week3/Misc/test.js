function getData(){
    fetch("https://padax.github.io/taipei-day-trip-resources/taipei-attractions-assignment-1")
    .then(function(response){
        return response.json(); 
    })
    .then(function(data){
        const results = data.data.results;
        getTitles(results);
        console.log(titles[1]);

        
    })
}

getData();
// 我現在有 results 物件，我要把裡面的資料取出來
// 並且把 title 存進 titles 陣列裡面
const titles = [];
function getTitles(results){
    for (let i = 0; i < results.length; i++){
        titles.push(results[i].stitle);
    }
    console.log(titles);
    
}

