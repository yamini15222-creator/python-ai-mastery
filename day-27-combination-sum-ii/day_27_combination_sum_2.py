def combination_sum_once(candidates, target):
    numbers = sorted(candidates)
    result = []
    path = []

    def backtrack(start, remaining):
        if remaining == 0:
            result.append(path.copy())
            return

        for index in range(start, len(numbers)):
            number = numbers[index]

            # Skip duplicate choices at this recursion level
            if index > start and number == numbers[index - 1]:
                continue

            # Current and later numbers are too large
            if number > remaining:
                break

            # Choose
            path.append(number)

            # Explore: move forward because this position is used
            backtrack(index + 1, remaining - number)

            # Undo
            path.pop()

    backtrack(0, target)
    return result


print(
    combination_sum_once(
        [10, 1, 2, 7, 6, 1, 5],
        8,
    )
)