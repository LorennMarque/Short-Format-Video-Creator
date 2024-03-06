import math

def area_difference(num, is_odd):
    circles_area = {}
    for i in range(num):
        circles_area[f'Ring {i}'] = round(((i+1) ** 2 - i ** 2) * math.pi, 2)

    total_area = 0
    for key, value in circles_area.items():
        if not is_odd and int(key.split()[1]) % 2 != 0:
            total_area += value
        elif is_odd and int(key.split()[1]) % 2 == 0:
            total_area += value
    return round(total_area, 2)

# Example usage:
print(area_difference(5819, False))