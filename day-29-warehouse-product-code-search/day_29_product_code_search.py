def word_exists(board, word):
    if word == "":
        return True

    if not board or not board[0]:
        return False

    rows = len(board)
    columns = len(board[0])

    def search(row, column, word_index):
        # Every character has been matched
        if word_index == len(word):
            return True

        # Invalid position or wrong/visited cell
        if (
            row < 0
            or row >= rows
            or column < 0
            or column >= columns
            or board[row][column] != word[word_index]
        ):
            return False

        original = board[row][column]

        # Choose: mark this cell as visited
        board[row][column] = "#"

        # Explore four directions
        found = (
            search(row - 1, column, word_index + 1)
            or search(row + 1, column, word_index + 1)
            or search(row, column - 1, word_index + 1)
            or search(row, column + 1, word_index + 1)
        )

        # Undo: restore the original character
        board[row][column] = original

        return found

    for row in range(rows):
        for column in range(columns):
            if search(row, column, 0):
                return True

    return False

board = [
    ["A", "B", "C", "E"],
    ["S", "F", "C", "S"],
    ["A", "D", "E", "E"],
]

print(word_exists(board, "ABCCED"))
print(word_exists(board, "SEE"))
print(word_exists(board, "ABCB"))