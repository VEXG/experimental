function telephoneCheck(str) {
    let get_check =
        /^(1\s?)?(\d{3}|\(\d{3}\))(([\-\s])|(\d{3}))?(\d{3}[\-\s])\d{4}|(^\d{10}$)$/g.test(str);
    return get_check;
}

// US phone number format
console.log(telephoneCheck('555-555-5555'));
