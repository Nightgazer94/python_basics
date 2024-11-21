simply_list = ["something", "something2", "something3"]

def save_get(checked_list, index):
    try:
        return checked_list[index]
    except IndexError:
        return None

print(save_get(simply_list, 3))