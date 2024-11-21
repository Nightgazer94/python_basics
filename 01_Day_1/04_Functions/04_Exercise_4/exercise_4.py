def convert_to_usd(euros):
    return round(euros / 0.82, 2)

print("385 EUR = ", convert_to_usd(385), "USD")
print("100 EUR = ", convert_to_usd(100), "USD")