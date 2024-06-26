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
