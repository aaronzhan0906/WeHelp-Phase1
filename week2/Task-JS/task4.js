function getNumber(index){
    const term = -5 * Math.floor(index / 3);
    const number = index * 4 + term

    return console.log(number)
    }

getNumber(1); // print 4
getNumber(5); // print 15
getNumber(10); // print 25
getNumber(30); // print 70