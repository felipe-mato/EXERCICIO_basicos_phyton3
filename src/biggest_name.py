from typing import List

# Solução inicial
def find_biggest_name(names: List[str]) -> str:
    biggest_name = ''
    for name in names:
        if len(name) > len(biggest_name): biggest_name = name
    return print(biggest_name)

# Solução refatorada
def find_biggest_name_2(names: List[str]) -> str:
    return print(max(names, key=len))

(find_biggest_name(['João','Pedro','Maria', 'Joaquim', 'Rafael', 'Felipe']))