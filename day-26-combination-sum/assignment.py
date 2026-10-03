"""Budget package builder using backtracking."""

from __future__ import annotations

import logging
from time import perf_counter

DEFAULT_MAX_RESULTS = 1000

logger = logging.getLogger(__name__)


def _validate_inputs(
    prices: list[int],
    budget: int,
    max_results: int,
) -> None:
    """Validate build_packages inputs.

    Args:
        prices: List of unique positive integer prices.
        budget: Target budget.
        max_results: Maximum number of packages allowed.

    Raises:
        TypeError: If an argument has an invalid type.
        ValueError: If an argument has an invalid value.
    """
    if type(prices) is not list:
        raise TypeError("prices must be a list")

    if type(budget) is not int:
        raise TypeError("budget must be an integer")

    if type(max_results) is not int:
        raise TypeError("max_results must be an integer")

    if budget < 0:
        raise ValueError("budget must be non-negative")

    if max_results <= 0:
        raise ValueError("max_results must be positive")

    for price in prices:
        if type(price) is not int:
            raise TypeError("every price must be an integer")

        if price <= 0:
            raise ValueError("every price must be positive")

    if len(prices) != len(set(prices)):
        raise ValueError("prices must contain unique values")


def build_packages(
    prices: list[int],
    budget: int,
    max_results: int = DEFAULT_MAX_RESULTS,
) -> list[list[int]]:
    """Return packages whose prices total exactly to budget.

    The same price can be selected multiple times.

    Args:
        prices: Unique positive integer prices.
        budget: Target budget.
        max_results: Maximum number of packages to return.

    Returns:
        A list of packages. Each package contains prices whose
        sum is exactly equal to budget.

    Raises:
        TypeError: If the input types are invalid.
        ValueError: If prices are invalid, budget is negative,
            or max_results is not positive.
    """
    _validate_inputs(prices, budget, max_results)

    # Copy and sort so the caller's list is never modified.
    sorted_prices = sorted(prices)

    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        """Explore valid package combinations recursively."""

        # Stop if maximum result protection is reached.
        if len(results) >= max_results:
            return

        # Exact budget reached.
        if remaining == 0:
            results.append(path.copy())
            return

        for index in range(start, len(sorted_prices)):
            price = sorted_prices[index]

            # Since prices are sorted and all prices are positive,
            # all later prices will also be too large.
            if price > remaining:
                break

            path.append(price)

            # Pass the same index because the current service
            # may be selected again.
            backtrack(
                index,
                remaining - price,
            )

            # Backtrack.
            path.pop()

            if len(results) >= max_results:
                return

    start_time = perf_counter()

    # Logging is performed only at the service boundary.
    logger.info(
        "Building budget packages: price_count=%d budget=%d max_results=%d",
        len(prices),
        budget,
        max_results,
    )

    backtrack(0, budget)

    duration = perf_counter() - start_time

    logger.info(
        "Budget package search completed: result_count=%d duration=%.6fs",
        len(results),
        duration,
    )

    return results