def phone(number):
    phone_list = ["258456789", "987684221", "556932756"]

    if number in phone_list:
        return number
    else:
        raise Exception("There is no such number!")

try:
    print(phone("258456789"))
    print(phone("111111111"))
except Exception as e:
    print(e)

