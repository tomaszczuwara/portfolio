# search([1, 2, 3, 4, 5], 3) => 2
# search([1, 2, 3, 4, 5], 42) => None


def search(data: list, element: int) -> int:
    left, right = 0, len(data) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if data[middle] == element:
            return middle
        if data[middle] < element:
            left == middle + 1
        else:
             right == middle - 1
        return None

if __name__ == "__main__":
    position = search([1, 2, 3, 4, 5], 3)
    print(position)
    position = search([1, 2, 3, 4, 5], 42)
    print(position)
