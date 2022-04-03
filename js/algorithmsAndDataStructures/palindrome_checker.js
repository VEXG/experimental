function palindrome(input) {
    let str = input.toLowerCase();
    let get_check = str.replace(/[^A-Za-z0-9]/g, '');
    let get_reverse = get_check.split('').reverse().join('');
    if (get_check == get_reverse) {
        return true;
    } else {
        return false;
    }
}

console.log(palindrome('A man, a plan, a canal. Panama'));
