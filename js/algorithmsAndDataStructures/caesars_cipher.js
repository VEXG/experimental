function rot13(str) {
    let input = str.toUpperCase();
    let get_normal = [
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
    ];
    let get_convert = [
        'N',
        'O',
        'P',
        'Q',
        'R',
        'S',
        'T',
        'U',
        'V',
        'W',
        'X',
        'Y',
        'Z',
        'A',
        'B',
        'C',
        'D',
        'E',
        'F',
        'G',
        'H',
        'I',
        'J',
        'K',
        'L',
        'M',
    ];
    let finalize = [];

    for (let a of input.split('')) {
        let get_normalIdx = get_normal.indexOf(a);
        if (get_normalIdx == -1) {
            finalize.push(a);
        } else {
            finalize.push(get_convert[get_normalIdx]);
        }
    }
    return finalize.join('');
}

console.log(rot13('SERR PBQR PNZC!'));
