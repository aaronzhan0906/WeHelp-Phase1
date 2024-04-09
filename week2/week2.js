// Task 1
console.log("=== Task 1 ===");
function findAndPrint(messages, currentStation) {
    const stationAndDistance = {
        "Songshan": 1,
        "Nanging Sanmin": 2,
        "Taipei Arena": 3,
        "Namjing Fuxing": 4,
        "Songjiang Nanjing": 5,
        "Zhongshan": 6,
        "Beiman": 7,
        "Ximen": 8,
        "Xiaonanmen": 9,
        "Chiang Kai-Shek Memorial Hall": 10,
        "Guting": 11,
        "Taipower Building": 12,
        "Gongguan": 13,
        "Wanlong": 14,
        "Jingmei": 15,
        "Dapinglin": 16,
        "Qizhang": 17,
        "Xiaobitan": 18,
        "Xindian City Hall": 18,
        "Xindian": 19
    };

    // dealing with issues related to metro branch lines.
    if (currentStation === "Xindian City Hall" || currentStation === "Xindian") {
        stationAndDistance["Xiaobitan"] = 16;
    } else if (currentStation === "Xiaobitan") { 
        stationAndDistance["Xindian City Hall"] = 16;
        stationAndDistance["Xindian"] = 17;
    } else {
        stationAndDistance["Xiaobitan"] = 18;
        stationAndDistance["Xindian City Hall"] = 18;
        stationAndDistance["Xindian"] = 19;
    }

    // create a regex to match the station name from the message
    const stationRegex = new RegExp(`(${Object.keys(stationAndDistance).join('|')})`, 'i'); 
    let closestPerson = "";
    let minDistance = Infinity; 

    // iterate over the messages and find the closest person
    for (const [person, message] of Object.entries(messages)) {
        const match = message.match(stationRegex);
        if (match) {
          const station = match[0]; 
          const distance = Math.abs(stationAndDistance[currentStation] - stationAndDistance[station]);
          if (distance < minDistance) {
              minDistance = distance;
              closestPerson = person;
            }
        } 
    }
    if (closestPerson) console.log(closestPerson);
}

const messages={
    "Bob":"I'm at Ximen MRT station.",
    "Mary":"I have a drink near Jingmei MRT station.",
    "Copper":"I just saw a concert at Taipei Arena.",
    "Leslie":"I'm at home near Xiaobitan station.",
    "Vivian":"I'm at Xindian station waiting for you."
};

findAndPrint(messages, "Wanlong"); // print Mary
findAndPrint(messages, "Songshan"); // print Copper
findAndPrint(messages, "Qizhang"); // print Leslie
findAndPrint(messages, "Ximen"); // print Bob
findAndPrint(messages, "Xindian City Hall"); // print Vivian





// Task 2
console.log("=== Task 2 ===");
function book(consultants, hour, duration, criteria) {
    // sort the consultants by the criteria
    if (criteria === "price") {
            consultants.sort((a, b) => a.price - b.price);
        } else if (criteria === "rate") {
            consultants.sort((a, b) => b.rate - a.rate);
        } 
        
    let availableConsultant = null;
    
    // check if the consultant has any appointment that overlaps with the given hour and duration
    for (const consultant of consultants) {
        const endHour = hour + duration;
        let isAvailable = true;
        
        for (const appointment of consultant.appointments || []) {
            if ((hour >= appointment.start && hour < appointment.end) ||
                (endHour > appointment.start && endHour <= appointment.end)||
                (hour <= appointment.start && endHour >= appointment.end)) {
                isAvailable = false;
                break;
            }
        }
        
        // create the appointments array and add the new appointment
        if (isAvailable) {
            availableConsultant = consultant;
            if (!consultant.appointments) {
                consultant.appointments = [];
            }
            consultant.appointments.push({ start: hour, end: endHour });
            break;
        }
    }
    
    if (availableConsultant !== null) {
        console.log(availableConsultant.name);
    } else {
        console.log("No Service");
    }
}
    

const consultants=[
    {"name":"John", "rate":4.5, "price":1000},
    {"name":"Bob", "rate":3, "price":1200},
    {"name":"Jenny", "rate":3.8, "price":800}
];
    
book(consultants, 15, 1, "price"); // Jenny
book(consultants, 11, 2, "price"); // Jenny
book(consultants, 10, 2, "price"); // John
book(consultants, 20, 2, "rate"); // John
book(consultants, 11, 1, "rate"); // Bob
book(consultants, 11, 2, "rate"); // No Service
book(consultants, 14, 3, "price"); // John





// Task 3
console.log("=== Task 3 ===");
function func(...data) {
    const names = {};

    // make key-value pair
    for (const name of data) {
        const fullNameSpilt = name.split("");
        let result = [];

        // get middleName
        if (fullNameSpilt.length % 2 === 1) {

            // retain the middle character
            result = fullNameSpilt.filter((_, index) => index === Math.floor(fullNameSpilt.length / 2));
            } else if (fullNameSpilt.length === 2) {
            result = fullNameSpilt.filter((_, index) => index === 1);
            } else if (fullNameSpilt.length % 2 === 0) {
            result = fullNameSpilt.filter((_, index) => index === 2);
            }       

            names[name] = result.join("");
        }

    // get the unique array
    const uniqueArray = Object.values(names);

    // get the unique index
    const unique = []
    for (const element of uniqueArray) {
        if (uniqueArray.filter(item => item === element).length === 1) {
            unique.push(element);
        } 
    }

    if (unique.length === 0) {
        console.log("沒有");
        return;
    }  

    // get the key of the unique index
    for (const key in names) {
        if (names[key] === unique[0]) {
            console.log(key);
        }
    }
}


func("彭大牆", "陳王明雅", "吳明"); // print 彭大牆
func("郭靜雅", "王立強", "郭林靜宜", "郭立恆", "林花花"); // print 林花花
func("郭宣雅", "林靜宜", "郭宣恆", "林靜花"); // print 沒有
func("郭宣雅", "夏曼藍波安", "郭宣恆"); // print 夏曼藍波安





// Task 4
console.log("=== Task 4 ===");
function getNumber(index){
    const term = -5 * Math.floor(index / 3);
    const number = index * 4 + term

    return console.log(number)
    }

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70





// Task 5
console.log("=== Task 5 ===");
function find(spaces, stat, n) {
    for (let i = 0; i < spaces.length; i++) {
        if (stat[i] === 0) {
            spaces[i] = 0; 
        }
    }
    
    let minSpaceIndex = -1;
    let minDifference = Infinity;

    for (let i = 0; i < spaces.length; i++) {
        let difference = spaces[i] - n;

        if (difference >= 0 && difference < minDifference) { 
            minDifference = difference;
            minSpaceIndex = i;
        }
    }
    console.log(minSpaceIndex);
}

find([3, 1, 5, 4, 3, 2], [0, 1, 0, 1, 1, 1], 2); // print 5
find([1, 0, 5, 1, 3], [0, 1, 0, 1, 1], 4); // print -1
find([4, 6, 5, 8], [0, 1, 1, 1], 4); // print 2