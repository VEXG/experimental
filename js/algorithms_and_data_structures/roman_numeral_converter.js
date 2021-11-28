function convertToRoman(num) {
    let get_lookUp = [
        ['M', 1000],
        ['CM', 900],
        ['D', 500],
        ['CD', 400],
        ['C', 100],
        ['XC', 90],
        ['L', 50],
        ['XL', 40],
        ['X', 10],
        ['IX', 9],
        ['V', 5],
        ['IV', 4],
        ['I', 1],
    ];

    let get_roman = [];
    for (var i = 0; get_lookUp[i]; i++) {
        while (get_lookUp[i][1] <= num) {
            get_roman.push(get_lookUp[i][0]);
            num -= get_lookUp[i][1];
        }
    }
    return get_roman.join('');
}

console.log(convertToRoman(36));
