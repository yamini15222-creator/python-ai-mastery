"""Warehouse product-code search using backtracking."""

from __future__ import annotations

from time import perf_counter

DEFAULT_MAX_ROWS = 100
DEFAULT_MAX_COLUMNS = 100
DEFAULT_MAX_WORD_LENGTH = 100
DEFAULT_TIMEOUT_SECONDS = 5.0


class GridValidationError(ValueError):
    """Raised when the warehouse grid is invalid."""


class ProductCodeValidationError(ValueError):
    """Raised when the product code is invalid."""


class SearchTimeoutError(TimeoutError):
    """Raised when the search exceeds the configured time limit."""


def _validate_grid(
    shelf_grid: list[list[str]],
    max_rows: int,
    max_columns: int,
) -> None:
    """Validate the warehouse grid."""

    if type(shelf_grid) is not list:
        raise TypeError("shelf_grid must be a list")

    if not shelf_grid:
        raise GridValidationError("shelf_grid must not be empty")

    if type(max_rows) is not int or max_rows <= 0:
        raise ValueError("max_rows must be a positive integer")

    if type(max_columns) is not int or max_columns <= 0:
        raise ValueError("max_columns must be a positive integer")

    if len(shelf_grid) > max_rows:
        raise GridValidationError(
            f"grid rows must not exceed {max_rows}"
        )

    column_count = None

    for row in shelf_grid:
        if type(row) is not list:
            raise TypeError("every grid row must be a list")

        if not row:
            raise GridValidationError(
                "grid rows must not be empty"
            )

        if column_count is None:
            column_count = len(row)
        elif len(row) != column_count:
            raise GridValidationError(
                "shelf_grid must be rectangular"
            )

        if len(row) > max_columns:
            raise GridValidationError(
                f"grid columns must not exceed {max_columns}"
            )

        for character in row:
            if type(character) is not str:
                raise TypeError(
                    "every grid cell must contain a string"
                )

            if len(character) != 1:
                raise GridValidationError(
                    "each grid cell must contain exactly one character"
                )


def _validate_product_code(
    product_code: str,
    max_word_length: int,
) -> None:
    """Validate the product code."""

    if type(product_code) is not str:
        raise TypeError("product_code must be a string")

    if not product_code:
        raise ProductCodeValidationError(
            "product_code must not be empty"
        )

    if len(product_code) > max_word_length:
        raise ProductCodeValidationError(
            f"product_code length must not exceed "
            f"{max_word_length}"
        )


def product_code_exists(
    shelf_grid: list[list[str]],
    product_code: str,
    max_rows: int = DEFAULT_MAX_ROWS,
    max_columns: int = DEFAULT_MAX_COLUMNS,
    max_word_length: int = DEFAULT_MAX_WORD_LENGTH,
    timeout_seconds: float = DEFAULT_TIMEOUT_SECONDS,
) -> bool:
    """Return whether a product code exists in the shelf grid.

    The search moves horizontally or vertically through adjacent
    cells. A grid cell cannot be reused within the same path.

    Args:
        shelf_grid: Rectangular warehouse grid.
        product_code: Product code to search for.
        max_rows: Maximum allowed number of rows.
        max_columns: Maximum allowed number of columns.
        max_word_length: Maximum allowed product-code length.
        timeout_seconds: Maximum search duration.

    Returns:
        True when the product code can be found, otherwise False.

    Raises:
        TypeError: If an input has an invalid type.
        ValueError: If an input has an invalid value.
        GridValidationError: If the grid is invalid.
        ProductCodeValidationError: If the product code is invalid.
        SearchTimeoutError: If the search exceeds the time limit.
    """

    _validate_grid(
        shelf_grid,
        max_rows,
        max_columns,
    )

    _validate_product_code(
        product_code,
        max_word_length,
    )

    if type(timeout_seconds) not in (int, float):
        raise TypeError(
            "timeout_seconds must be a number"
        )

    if timeout_seconds <= 0:
        raise ValueError(
            "timeout_seconds must be positive"
        )

    # Copy the grid so the caller's data cannot be changed.
    grid = [row.copy() for row in shelf_grid]

    rows = len(grid)
    columns = len(grid[0])

    visited: set[tuple[int, int]] = set()

    metrics = {
        "cells_checked": 0,
        "paths_explored": 0,
    }

    start_time = perf_counter()

    def check_timeout() -> None:
        """Raise an exception if the search timed out."""

        elapsed = perf_counter() - start_time

        if elapsed > timeout_seconds:
            raise SearchTimeoutError(
                "product-code search exceeded timeout"
            )

    def backtrack(
        row: int,
        column: int,
        code_index: int,
    ) -> bool:
        """Search recursively from one grid position."""

        check_timeout()

        metrics["paths_explored"] += 1

        if grid[row][column] != product_code[code_index]:
            return False

        metrics["cells_checked"] += 1

        if code_index == len(product_code) - 1:
            return True

        visited.add((row, column))

        directions = (
            (-1, 0),  # up
            (1, 0),   # down
            (0, -1),  # left
            (0, 1),   # right
        )

        for row_change, column_change in directions:
            next_row = row + row_change
            next_column = column + column_change

            if not (
                0 <= next_row < rows
                and 0 <= next_column < columns
            ):
                continue

            if (next_row, next_column) in visited:
                continue

            if backtrack(
                next_row,
                next_column,
                code_index + 1,
            ):
                visited.remove((row, column))
                return True

        visited.remove((row, column))
        return False

    for row in range(rows):
        for column in range(columns):
            check_timeout()

            if grid[row][column] != product_code[0]:
                continue

            if backtrack(row, column, 0):
                return True

    return False