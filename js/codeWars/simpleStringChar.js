function solve(s) {
	s = s.split('');
	const upperCase = s.filter((a) => /[A-Z]/g.test(a)).length;
	const lowerCase = s.filter((a) => /[a-z]/g.test(a)).length;
	const number = s.filter((a) => !isNaN(a)).length;
	const symbol = s.filter((a) => /\W/.test(a)).length;
	return [upperCase, lowerCase, number, symbol];
}

console.log(solve('Codewars@codewars123.com'));
