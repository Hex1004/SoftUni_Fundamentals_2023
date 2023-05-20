year = int(input())

while True:
    year += 1
    year_str = str(year)
    set_value = set(year_str)
    set_len = len(set(year_str))
    if len(set(year_str)) == len(year_str):
        break
print(year)