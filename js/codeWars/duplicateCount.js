function duplicateCount(text) {
	if (!text) return 0;
	text = text.toLowerCase();
	const stat = {};
	for (let a = 0; text.length > a; a++) {
		const char = text.charAt(a);
		if (stat[char]) stat[char]++;
		else stat[char] = 1;
	}
	return Object.entries(stat).filter((a) => a[1] > 1)?.length ?? 0;
}
console.log(duplicateCount('indivisibility'));
