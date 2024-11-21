def calculate_net(gross, vat):
    return gross - (gross * (vat * 0.01))

print(calculate_net(10, 21))