def is_valid(number):
    if number == 100:
        return "100% Complete!\n[%%%%%%%%%%]"
    loaded_percent = number // 10
    return  f"{number}% [{'%' * loaded_percent}{'.' * (10 - loaded_percent)}]\nStill loading..."


number = int(input())
print(is_valid(number))