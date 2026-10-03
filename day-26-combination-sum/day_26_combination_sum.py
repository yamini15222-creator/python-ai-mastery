def combination_sum(candidates, target):
    numbers = sorted(candidates)
    result = []
    path = []

    def backtrack(start, remaining):
        # A valid combination is complete
        if remaining == 0:
            result.append(path.copy())
            return

        for index in range(start, len(numbers)):
            number = numbers[index]

            # This and every later number are too large
            if number > remaining:
                break

            # Choose
            path.append(number)

            # Explore: same index allows reuse
            backtrack(index, remaining - number)

            # Undo
            path.pop()

    backtrack(0, target)
    return result


print(combination_sum([2, 3, 6, 7], 7))