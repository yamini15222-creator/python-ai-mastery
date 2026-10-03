"""Unit tests for the one-time coupon bundle builder."""

import pytest

from assignment import coupon_bundles


def test_expected_coupon_bundles() -> None:
    """Test the main assignment example."""
    coupons = [
        1000,
        100,
        200,
        700,
        600,
        100,
        500,
    ]

    target = 800

    result = coupon_bundles(
        coupons,
        target,
    )

    expected = {
        (100, 100, 600),
        (100, 200, 500),
        (100, 700),
        (200, 600),
    }

    assert {tuple(bundle) for bundle in result} == expected


def test_empty_coupons() -> None:
    """Empty input should return no bundles."""
    assert coupon_bundles([], 800) == []


def test_single_coupon_exact_match() -> None:
    """A single coupon matching the target is valid."""
    assert coupon_bundles([100], 100) == [[100]]


def test_single_coupon_too_small() -> None:
    """A coupon below the target alone is not enough."""
    assert coupon_bundles([100], 200) == []


def test_two_equal_coupons_can_be_used() -> None:
    """Two physical equal coupons can form one bundle."""
    assert coupon_bundles([100, 100], 200) == [[100, 100]]


def test_three_equal_coupons_do_not_create_duplicates() -> None:
    """Three equal coupons should not create duplicate bundles."""
    result = coupon_bundles(
        [100, 100, 100],
        200,
    )

    assert result == [[100, 100]]


def test_basic_multiple_solutions() -> None:
    """Test multiple valid combinations."""
    result = coupon_bundles(
        [100, 200, 500, 700],
        800,
    )

    expected = {
        (100, 200, 500),
        (100, 700),
    }

    assert {tuple(bundle) for bundle in result} == expected


def test_main_example_again() -> None:
    """Verify the complete acceptance example."""
    coupons = [
        100,
        100,
        200,
        500,
        600,
        700,
        1000,
    ]

    result = coupon_bundles(
        coupons,
        800,
    )

    expected = {
        (100, 100, 600),
        (100, 200, 500),
        (100, 700),
        (200, 600),
    }

    assert {tuple(bundle) for bundle in result} == expected


def test_zero_coupon_rejected() -> None:
    """Zero-valued coupons must be rejected."""
    with pytest.raises(ValueError):
        coupon_bundles([0, 100], 100)


def test_negative_coupon_rejected() -> None:
    """Negative coupons must be rejected."""
    with pytest.raises(ValueError):
        coupon_bundles([-100, 200], 100)


def test_target_must_be_non_negative() -> None:
    """Negative targets must be rejected."""
    with pytest.raises(ValueError):
        coupon_bundles([100, 200], -100)


def test_coupons_must_be_list() -> None:
    """Coupons must be provided as a list."""
    with pytest.raises(TypeError):
        coupon_bundles(
            (100, 200),  # type: ignore[arg-type]
            300,
        )


def test_coupon_values_must_be_integers() -> None:
    """Coupon values must be integers."""
    with pytest.raises(TypeError):
        coupon_bundles(
            [100, 200.5],  # type: ignore[list-item]
            300,
        )


def test_target_must_be_integer() -> None:
    """Target must be an integer."""
    with pytest.raises(TypeError):
        coupon_bundles(
            [100, 200],
            "300",  # type: ignore[arg-type]
        )


def test_boolean_coupon_rejected() -> None:
    """Boolean coupon values must not be accepted."""
    with pytest.raises(TypeError):
        coupon_bundles(
            [True, 100],  # type: ignore[list-item]
            100,
        )


def test_boolean_target_rejected() -> None:
    """Boolean target must not be accepted."""
    with pytest.raises(TypeError):
        coupon_bundles(
            [100, 200],
            True,  # type: ignore[arg-type]
        )


def test_max_results_must_be_positive() -> None:
    """max_results must be greater than zero."""
    with pytest.raises(ValueError):
        coupon_bundles(
            [100, 200],
            300,
            max_results=0,
        )


def test_max_coupons_limit() -> None:
    """Input size must respect max_coupons."""
    with pytest.raises(ValueError):
        coupon_bundles(
            [100, 200, 300],
            600,
            max_coupons=2,
        )


def test_max_results_limit() -> None:
    """Result count must respect max_results."""
    result = coupon_bundles(
        [100, 200, 300, 400],
        500,
        max_results=1,
    )

    assert len(result) <= 1


def test_every_bundle_has_correct_sum() -> None:
    """Every returned bundle must equal the target."""
    coupons = [
        100,
        100,
        200,
        500,
        600,
        700,
    ]

    target = 800

    result = coupon_bundles(
        coupons,
        target,
    )

    for bundle in result:
        assert sum(bundle) == target


def test_no_duplicate_bundles() -> None:
    """No duplicate bundles should be returned."""
    result = coupon_bundles(
        [100, 100, 200, 500, 600, 700],
        800,
    )

    normalized = {
        tuple(bundle)
        for bundle in result
    }

    assert len(normalized) == len(result)


def test_original_input_is_not_modified() -> None:
    """The original coupon list must remain unchanged."""
    coupons = [
        1000,
        100,
        200,
        700,
        600,
        100,
        500,
    ]

    original = coupons.copy()

    coupon_bundles(
        coupons,
        800,
    )

    assert coupons == original


def test_each_bundle_is_sorted() -> None:
    """Each generated bundle should be in sorted order."""
    result = coupon_bundles(
        [700, 100, 500, 200, 600],
        800,
    )

    for bundle in result:
        assert bundle == sorted(bundle)


def test_no_solution() -> None:
    """Return an empty list when no solution exists."""
    assert coupon_bundles([100, 200], 700) == []