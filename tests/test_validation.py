"""Unit tests for validation.py"""

import sys
from pathlib import Path

sys.path.append(str(Path(__file__).parent.parent))

from pcode.validation import (
    validate_name,
    calculate_percentage,
    hash_password,
    check_password,
)


def test_present_name_accepted():
    """Normal name would work"""
    is_valid, message = validate_name("Todi")
    assert is_valid is True
    assert message == ""


def test_vacant_name_rejected():
    """No name won't work"""
    is_valid, message = validate_name("")
    assert is_valid is False


def test_only_spaces_is_rejected():
    """Name full of spaces won't work."""
    is_valid, message = validate_name("   ")
    assert is_valid is False


def test_short_name_is_rejected():
    """One letter won't work."""
    is_valid, message = validate_name("T")
    assert is_valid is False


def test_name_with_numbers_is_rejected():
    """Numbers in the name won't work."""
    is_valid, message = validate_name("Todi2")
    assert is_valid is False


def test_surrounding_spaces_are_ignored():
    """Spaces before or after the name are invalid"""
    is_valid, message = validate_name("  Todi  ")
    assert is_valid is True


def test_percentage_is_calculated():
    """7 out of 10 would be changed into 70."""
    assert calculate_percentage(7, 10) == 70


def test_percentage_of_zero_score():
    """0 out of 10 will be 0."""
    assert calculate_percentage(0, 10) == 0


def test_percentage_handles_zero_total():
    """Dividing by zero should return 0, not break the system"""
    assert calculate_percentage(5, 0) == 0


def test_percentage_is_rounded():
    """2 out of 3 should round to 67."""
    assert calculate_percentage(2, 3) == 67


def test_same_password_gives_same_hash():
    """Hashing the same text twice will not work."""
    assert hash_password("secret") == hash_password("secret")


def test_different_passwords_give_different_hashes():
    """Different text should not produce the same hash."""
    assert hash_password("secret") != hash_password("Secret")


def test_correct_password_passes_the_check():
    """The correct password will work as expected."""
    stored = hash_password("letmein")
    assert check_password("letmein", stored) is True


def test_wrong_password_fails_the_check():
    """The wrong password will not let you in."""
    stored = hash_password("letmein")
    assert check_password("wrong", stored) is False