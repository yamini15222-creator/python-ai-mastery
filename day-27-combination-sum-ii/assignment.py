"""One-time coupon bundle builder using backtracking."""

from __future__ import annotations

import logging
from time import perf_counter

DEFAULT_MAX_RESULTS = 1000
DEFAULT_MAX_COUPONS = 100

logger = logging.getLogger(__name__)


def _validate_inputs(
    coupons: list[int],
    target_discount: int,
    max_results: int,
    max_coupons: int,
) -> None:
    """Validate coupon bundle inputs.

    Args:
        coupons: List of positive integer coupon values.
        target_discount: Required total discount.
        max_results: Maximum number of bundles to return.
        max_coupons: Maximum number of input coupons allowed.

    Raises:
        TypeError: If an argument has an invalid type.
        ValueError: If an argument has an invalid value.
    """
    if type(coupons) is not list:
        raise TypeError("coupons must be a list")

    if type(target_discount) is not int:
        raise TypeError("target_discount must be an integer")

    if type(max_results) is not int:
        raise TypeError("max_results must be an integer")

    if type(max_coupons) is not int:
        raise TypeError("max_coupons must be an integer")

    if target_discount < 0:
        raise ValueError("target_discount must be non-negative")

    if max_results <= 0:
        raise ValueError("max_results must be positive")

    if max_coupons <= 0:
        raise ValueError("max_coupons must be positive")

    if len(coupons) > max_coupons:
        raise ValueError(
            f"number of coupons must not exceed {max_coupons}"
        )

    for coupon in coupons:
        if type(coupon) is not int:
            raise TypeError(
                "every coupon must be an integer"
            )

        if coupon <= 0:
            raise ValueError(
                "every coupon must be positive"
            )


def coupon_bundles(
    coupons: list[int],
    target_discount: int,
    max_results: int = DEFAULT_MAX_RESULTS,
    max_coupons: int = DEFAULT_MAX_COUPONS,
) -> list[list[int]]:
    """Return unique one-time coupon bundles matching the target.

    Each physical coupon can be selected at most once.
    Duplicate coupon values are allowed.

    Args:
        coupons: List of positive integer coupon values.
        target_discount: Required total discount.
        max_results: Maximum number of bundles to return.
        max_coupons: Maximum number of input coupons allowed.

    Returns:
        A list of unique coupon bundles whose values sum to
        target_discount.

    Raises:
        TypeError: If an input has an invalid type.
        ValueError: If an input has an invalid value.
    """
    _validate_inputs(
        coupons,
        target_discount,
        max_results,
        max_coupons,
    )

    # Sort a copy so the caller's list is never modified.
    sorted_coupons = sorted(coupons)

    results: list[list[int]] = []
    path: list[int] = []

    def backtrack(start: int, remaining: int) -> None:
        """Explore valid coupon combinations recursively."""

        if len(results) >= max_results:
            return

        # Exact target reached.
        if remaining == 0:
            results.append(path.copy())
            return

        for index in range(
            start,
            len(sorted_coupons),
        ):
            coupon = sorted_coupons[index]

            # Skip duplicate values at the same recursion level.
            if (
                index > start
                and coupon == sorted_coupons[index - 1]
            ):
                continue

            # Because coupons are positive and sorted,
            # later values will also be too large.
            if coupon > remaining:
                break

            path.append(coupon)

            # index + 1 means each physical coupon
            # can be used only once.
            backtrack(
                index + 1,
                remaining - coupon,
            )

            # Backtrack.
            path.pop()

            if len(results) >= max_results:
                return

    start_time = perf_counter()

    # Logging only at the service boundary.
    logger.info(
        "Starting coupon bundle search: "
        "coupon_count=%d target=%d max_results=%d",
        len(coupons),
        target_discount,
        max_results,
    )

    backtrack(0, target_discount)

    duration = perf_counter() - start_time

    logger.info(
        "Coupon bundle search completed: "
        "result_count=%d duration=%.6fs",
        len(results),
        duration,
    )

    return results