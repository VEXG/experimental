function zeroAndOne(s) {
	return s.replace(/(10|01)/g, '').split('').length;
}

console.log(zeroAndOne('110100'));
