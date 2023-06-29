stuff = {'matches': 1, 'cup': 2, 'tent': 10, 'ration': 5, 'spare shoes': 3}

def backpack_capacity(capacity: int, stuff: dict) -> list[str]:
    packaging_option = []
    summary = []
    for key, value in stuff.items():
        if value <= capacity:
            capacity -= value
            packaging_option.append(key)
    return packaging_option


print(backpack_capacity(15, stuff))