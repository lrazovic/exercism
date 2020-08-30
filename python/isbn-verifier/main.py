from typing import List


def evaluate_isbn(isbn: List[int]) -> bool:
    isbn_formula = sum([x * n for x, n in zip(isbn, range(10, 0, -1))]) % 11
    print("In")
    return isbn_formula == 0

isbn = "3-598-2X507-9"
isbn_list = [elem for elem in isbn if elem.isdigit() or elem == "X"]
isbn_list = [10 if x == "X" else int(x) for x in isbn_list]
print(len(isbn_list) == 10 and 10 not in isbn_list[:-1] and evaluate_isbn(isbn_list))