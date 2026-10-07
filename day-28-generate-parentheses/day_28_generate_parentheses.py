def generate_parentheses(n):
    result = []
    path = []

    def backtrack(open_count, close_count):
        # A complete valid sequence
        if len(path) == 2 * n:
            result.append("".join(path))
            return

        # Choice 1: add an opening parenthesis
        if open_count < n:
            path.append("(")
            backtrack(open_count + 1, close_count)
            path.pop()

        # Choice 2: close an existing open parenthesis
        if close_count < open_count:
            path.append(")")
            backtrack(open_count, close_count + 1)
            path.pop()

    backtrack(0, 0)
    return result


print(generate_parentheses(3))