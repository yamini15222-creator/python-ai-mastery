"""Unit tests for the budget package builder."""

import pytest

from assignment import build_packages


def test_expected_packages() -> None:
    """The example input should return the expected packages."""
    prices = [200, 300, 600, 700]
    budget = 700

    result = build_packages(prices, budget)

    assert result == [
        [200, 200, 300],
        [700],
    ]


def test_no_solution() -> None:
    """Return an empty list when no package reaches the budget."""
    result = build_packages([200], 600)

    assert result == []


def test_no_solution_with_smaller_prices() -> None:
    """Return an empty list when no combination exists."""
    result = build_packages([400, 600], 500)

    assert result == []


def test_empty_prices() -> None:
    """An empty price list should return no packages."""
    result = build_packages([], 700)

    assert result == []


def test_zero_price_rejected() -> None:
    """Zero prices must be rejected."""
    with pytest.raises(ValueError):
        build_packages([200, 0], 700)


def test_negative_price_rejected() -> None:
    """Negative prices must be rejected."""
    with pytest.raises(ValueError):
        build_packages([200, -100], 700)


def test_duplicate_prices_rejected() -> None:
    """Duplicate price values must be rejected."""
    with pytest.raises(ValueError):
        build_packages([200, 200], 700)


def test_zero_budget() -> None:
    """Zero budget should return one empty package."""
    result = build_packages([200, 300], 0)

    assert result == [[]]


def test_every_result_has_correct_sum() -> None:
    """Every returned package must equal the budget."""
    prices = [200, 300, 600, 700]
    budget = 700

    result = build_packages(prices, budget)

    for package in result:
        assert sum(package) == budget


def test_no_duplicate_combinations() -> None:
    """No reordered or duplicate packages should be returned."""
    result = build_packages([2, 3, 5], 8)

    normalized = {
        tuple(package)
        for package in result
    }

    assert len(normalized) == len(result)


def test_original_list_is_not_modified() -> None:
    """The caller's prices list must remain unchanged."""
    prices = [700, 200, 600, 300]
    original = prices.copy()

    build_packages(prices, 700)

    assert prices == original


def test_result_packages_are_sorted() -> None:
    """Each package should be generated in sorted order."""
    result = build_packages([2, 3, 5], 8)

    for package in result:
        assert package == sorted(package)


def test_prices_must_be_a_list() -> None:
    """prices must be a list."""
    with pytest.raises(TypeError):
        build_packages((200, 300), 500)  # type: ignore[arg-type]


def test_budget_must_be_an_integer() -> None:
    """budget must be an integer."""
    with pytest.raises(TypeError):
        build_packages([200, 300], "500")  # type: ignore[arg-type]


def test_budget_cannot_be_negative() -> None:
    """Negative budgets must be rejected."""
    with pytest.raises(ValueError):
        build_packages([200, 300], -100)


def test_price_must_be_integer() -> None:
    """Every price must be an integer."""
    with pytest.raises(TypeError):
        build_packages([200, 300.5], 500)  # type: ignore[list-item]


def test_max_results_must_be_positive() -> None:
    """max_results must be greater than zero."""
    with pytest.raises(ValueError):
        build_packages([200, 300], 500, max_results=0)


def test_max_results_limit() -> None:
    """The number of returned packages must respect max_results."""
    result = build_packages(
        [2, 3, 5],
        10,
        max_results=2,
    )

    assert len(result) <= 2


def test_boolean_budget_rejected() -> None:
    """Boolean budget values must be rejected."""
    with pytest.raises(TypeError):
        build_packages([200, 300], True)  # type: ignore[arg-type]


def test_boolean_price_rejected() -> None:
    """Boolean prices must be rejected."""
    with pytest.raises(TypeError):
        build_packages([True, 300], 500)  # type: ignore[list-item]


def test_boolean_max_results_rejected() -> None:
    """Boolean max_results must be rejected."""
    with pytest.raises(TypeError):
        build_packages(
            [200, 300],
            500,
            max_results=True,  # type: ignore[arg-type]
        )