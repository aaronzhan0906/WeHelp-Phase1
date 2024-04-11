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

