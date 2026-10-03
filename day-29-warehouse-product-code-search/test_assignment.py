"""Tests for warehouse product-code search."""

import pytest

from assignment import (
    GridValidationError,
    ProductCodeValidationError,
    product_code_exists,
)


def test_product_code_exists_horizontally():
    """Product code can be found horizontally."""
    grid = [
        ["C", "A", "T"],
        ["X", "Y", "Z"],
    ]

    assert product_code_exists(grid, "CAT") is True


def test_product_code_exists_vertically():
    """Product code can be found vertically."""
    grid = [
        ["C", "X"],
        ["A", "Y"],
        ["T", "Z"],
    ]

    assert product_code_exists(grid, "CAT") is True


def test_product_code_exists_with_turn():
    """Product code can change direction."""
    grid = [
        ["C", "A"],
        ["X", "T"],
    ]

    assert product_code_exists(grid, "CAT") is True


def test_product_code_does_not_exist():
    """Return False when product code is absent."""
    grid = [
        ["C", "A"],
        ["X", "T"],
    ]

    assert product_code_exists(grid, "DOG") is False


def test_single_character_code():
    """A single matching cell is valid."""
    grid = [
        ["A", "B"],
        ["C", "D"],
    ]

    assert product_code_exists(grid, "A") is True


def test_single_character_code_missing():
    """A missing single character returns False."""
    grid = [
        ["A", "B"],
        ["C", "D"],
    ]

    assert product_code_exists(grid, "X") is False


def test_cell_cannot_be_reused():
    """The same cell cannot be reused in one path."""
    grid = [
        ["A"],
    ]

    assert product_code_exists(grid, "AA") is False


def test_no_diagonal_movement():
    """Diagonal movement is not allowed."""
    grid = [
        ["A", "X"],
        ["X", "B"],
    ]

    assert product_code_exists(grid, "AB") is False


def test_empty_grid_rejected():
    """An empty grid must be rejected."""
    with pytest.raises(GridValidationError):
        product_code_exists([], "ABC")


def test_empty_row_rejected():
    """Empty rows must be rejected."""
    with pytest.raises(GridValidationError):
        product_code_exists([[]], "ABC")


def test_non_rectangular_grid_rejected():
    """All rows must have equal lengths."""
    grid = [
        ["A", "B"],
        ["C"],
    ]

    with pytest.raises(GridValidationError):
        product_code_exists(grid, "ABC")


def test_grid_row_must_be_list():
    """Every grid row must be a list."""
    grid = [
        ["A", "B"],
        "CD",
    ]

    with pytest.raises(TypeError):
        product_code_exists(grid, "ABC")


def test_grid_cell_must_be_single_character():
    """Each grid cell must contain one character."""
    grid = [
        ["ABC", "D"],
    ]

    with pytest.raises(GridValidationError):
        product_code_exists(grid, "ABC")


def test_grid_cell_must_be_string():
    """Grid cells must contain strings."""
    grid = [
        ["A", 1],
    ]

    with pytest.raises(TypeError):
        product_code_exists(grid, "A")


def test_product_code_must_be_string():
    """Product code must be a string."""
    grid = [
        ["A", "B"],
    ]

    with pytest.raises(TypeError):
        product_code_exists(
            grid,
            123,  # type: ignore[arg-type]
        )


def test_empty_product_code_rejected():
    """An empty product code must be rejected."""
    grid = [
        ["A", "B"],
    ]

    with pytest.raises(ProductCodeValidationError):
        product_code_exists(grid, "")


def test_product_code_length_limit():
    """Product code length limit is enforced."""
    grid = [
        ["A"],
    ]

    with pytest.raises(ProductCodeValidationError):
        product_code_exists(
            grid,
            "ABC",
            max_word_length=2,
        )


def test_grid_row_limit():
    """Maximum row limit is enforced."""
    grid = [
        ["A"],
        ["B"],
        ["C"],
    ]

    with pytest.raises(GridValidationError):
        product_code_exists(
            grid,
            "A",
            max_rows=2,
        )


def test_grid_column_limit():
    """Maximum column limit is enforced."""
    grid = [
        ["A", "B", "C"],
    ]

    with pytest.raises(GridValidationError):
        product_code_exists(
            grid,
            "A",
            max_columns=2,
        )


def test_timeout_must_be_positive():
    """Timeout must be positive."""
    grid = [
        ["A"],
    ]

    with pytest.raises(ValueError):
        product_code_exists(
            grid,
            "A",
            timeout_seconds=0,
        )


def test_original_grid_is_not_modified():
    """The caller's grid must remain unchanged."""
    grid = [
        ["C", "A"],
        ["X", "T"],
    ]

    original = [row.copy() for row in grid]

    product_code_exists(grid, "CAT")

    assert grid == original


def test_reuse_is_not_allowed():
    """A cell cannot be used twice in a path."""
    grid = [
        ["A", "B"],
        ["C", "D"],
    ]

    assert product_code_exists(grid, "ABCA") is False


def test_longer_path():
    """Test a longer valid path."""
    grid = [
        ["C", "A", "T", "X"],
        ["X", "R", "E", "X"],
        ["X", "E", "D", "X"],
    ]

    assert product_code_exists(grid, "CATED") is True


def test_boolean_is_not_accepted_as_timeout():
    """Boolean timeout values should not be accepted."""
    grid = [
        ["A"],
    ]

    with pytest.raises(TypeError):
        product_code_exists(
            grid,
            "A",
            timeout_seconds=True,  # type: ignore[arg-type]
        )