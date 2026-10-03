import pytest

from assignment import generate_test_patterns


def test_zero_pairs():
    assert generate_test_patterns(0) == [""]


def test_one_pair():
    assert generate_test_patterns(1) == ["()"]


def test_two_pairs():
    result = generate_test_patterns(2)

    assert set(result) == {
        "(())",
        "()()",
    }


def test_three_pairs():
    result = generate_test_patterns(3)

    expected = {
        "((()))",
        "(()())",
        "(())()",
        "()(())",
        "()()()",
    }

    assert set(result) == expected


def test_unique_patterns():
    result = generate_test_patterns(4)

    assert len(result) == len(set(result))


def test_correct_length():
    for pair_count in range(5):
        result = generate_test_patterns(pair_count)

        for pattern in result:
            assert len(pattern) == 2 * pair_count


def is_valid(pattern):
    balance = 0

    for character in pattern:
        if character == "(":
            balance += 1
        else:
            balance -= 1

        if balance < 0:
            return False

    return balance == 0


def test_every_pattern_is_valid():
    result = generate_test_patterns(4)

    for pattern in result:
        assert is_valid(pattern)


def test_negative_input():
    with pytest.raises(ValueError):
        generate_test_patterns(-1)


def test_string_input():
    with pytest.raises(TypeError):
        generate_test_patterns("3")


def test_boolean_input():
    with pytest.raises(TypeError):
        generate_test_patterns(True)