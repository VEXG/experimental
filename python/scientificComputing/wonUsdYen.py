def won_to_usd(price):
    output = []
    for i in price:
        output.append(i/1000)
    return output


def usd_to_yen(price):
    output = []
    for i in price:
        output.append(i*125)
    return output


# Mata uang Korea
price = [34000, 13000, 5000, 21000, 1000, 2000, 8000, 3000]
print('Mata uang korea: ' + str(price))

# Mata uang AS
USD = won_to_usd(price)
print('Mata uang AS: ' + str(USD))

# Mata uang Jepang
YEN = usd_to_yen(USD)
print('Mata uang Jepang: ' + str(YEN))
