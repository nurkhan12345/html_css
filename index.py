# # ЗАДАЧА 1 (легкая)
# # Функция считает гласные буквы в строке и возвращает их количество.
# def count_vowels(text):
#     vowels = "aeiouAEIOU"
#     count = 0
#     for ch in text:
#         if ch in vowels:
#             count += 1
#     return count
# def check(name, got, expected):
#     status = "OK" if got == expected else "FAIL"
#     print(f"{name}: {status} {name} получили {got}, ожидали {expected!r}")
#     if __name__ == "__main__":
#         check("count_vowels('Hello World')", count_vowels("Hello World"), 3)
#         check("count_vowels('Python')", count_vowels("Python"), 1)
#         check("count_vowels('AEIOUaeiou')", count_vowels("AEIOUaeiou"), 10)
#         check("count_vowels('')", count_vowels(""), 0)


# def count_vowels(text: str) -> int:
#     """Считает количество английских гласных букв в строке."""
#     vowels = set("aeiouAEIOU")
#     return sum(1 for ch in text if ch in vowels)


# def check(name: str, got: int, expected: int) -> None:
#     status = "OK" if got == expected else "FAIL"
#     print(f"{name}: {status} — получили {got}, ожидали {expected!r}")


# if __name__ == "__main__":
#     check("count_vowels('Hello World')", count_vowels("Hello World"), 3)
#     check("count_vowels('Python')", count_vowels("Python"), 1)
#     check("count_vowels('AEIOUaeiou')", count_vowels("AEIOUaeiou"), 10)
#     check("count_vowels('')", count_vowels(""), 0)


a = "ASdasd"
print(a.lower())

#Задача 3 (средняя)
#Функция убирает из списка все отправленые числа.
#Пример: remove_numpers([1, -2, 3]) -> [1, 3])
#def remove_negatives(numbers):
#    for n in nums:
#        if n < 0:
#            nums.remove(n)
#    return nums
#def check(name, got, expected):
#    status = "OK" if got == expected else "FAIL"
#    print(f"{status}: {name} — получили {got!r}, ожидали {expected!r}")

def remove_negatives(numbers: list[int]) -> list[int]:
    """Возвращает новый список без отрицательных чисел."""
    return [n for n in numbers if n >= 0]


def check(name: str, got: list[int], expected: list[int]) -> None:
    status = "OK" if got == expected else "FAIL"
    print(f"{status}: {name} — получили {got!r}, ожидали {expected!r}")


if __name__ == "__main__":
    check("Только положительные", remove_negatives([1, 2, 3]), [1, 2, 3])
    check("С отрицательными", remove_negatives([1, -2, 3]), [1, 3])
    check("Несколько отрицательных подряд", remove_negatives([-1, -2, 3, -4]), [3])
    check("Все отрицательные", remove_negatives([-1, -2, -3]), [])
    check("Пустой список", remove_negatives([]), [])