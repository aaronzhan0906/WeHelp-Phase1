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