from typing import List

# Solução inicial
def find_average(numbers: List[int]) -> float:
    sumNumbers = 0 
    for number in numbers: sumNumbers += number
    return int(sumNumbers / len(numbers))

# Solução refatorada
def find_average_2(numbers: List[int]) -> float:
    return sum(numbers) / len(numbers)


print(find_average([5,5,5,5,5]))
