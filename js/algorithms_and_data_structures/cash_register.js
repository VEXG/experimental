function checkCashRegister(price, cash, cid) {
    let get_change = cash - price;
    let get_template = {
        status: String,
        change: [],
    };

    let sum_cid = 0;
    cid.forEach((a) => (sum_cid += a[1]));

    if (get_change === sum_cid) {
        get_template.status = 'CLOSED';
        get_template.change = cid;
        return get_template;
    } else if (get_change > sum_cid) {
        get_template.status = 'INSUFFICIENT_FUNDS';
        return get_template;
    }

    let get_denom = [
        ['ONE HUNDRED', 100.0],
        ['TWENTY', 20.0],
        ['TEN', 10.0],
        ['FIVE', 5.0],
        ['ONE', 1.0],
        ['QUARTER', 0.25],
        ['DIME', 0.1],
        ['NICKEL', 0.05],
        ['PENNY', 0.01],
    ];
    let get_update = [];
    cid = cid.reverse();

    cid.forEach((a, b) => {
        let get_val = 0;
        let denum = get_denom[b][1];

        while (get_change >= denum && a[1] > 0) {
            a[1] -= denum;
            get_change = get_change.toFixed(2);
            get_change -= denum;
            get_val += denum;
        }

        if (get_val > 0) get_update.push([a[0], get_val]);
    });

    if (get_change > 0) {
        get_template.status = 'INSUFFICIENT_FUNDS';
        return get_template;
    } else {
        get_template.status = 'OPEN';
        get_template.change = get_update;
        return get_template;
    }
}

console.log(
    checkCashRegister(3.26, 100, [
        ['PENNY', 1.01],
        ['NICKEL', 2.05],
        ['DIME', 3.1],
        ['QUARTER', 4.25],
        ['ONE', 90],
        ['FIVE', 55],
        ['TEN', 20],
        ['TWENTY', 60],
        ['ONE HUNDRED', 100],
    ]),
);
