function spinWords(string) {
    return string.split(' ').map(a => a.length > 4 ? a.split('').reverse().join('') : a).join(' ');
}

console.log(spinWords("Hey fellow warriors"));