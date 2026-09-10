"""Validation and calculation for the Cyber quiz.

These functions take values in and return values out."""

import hashlib


def validate_name(name):
    """Check that a name can be used.

    Args:
        name: the text the user put in.

    Returns:
        A tuple of (True, "") if valid, or (False, reason) if not.
    """
    if name is None:
        return False, "Please enter your name"

    cleaned = name.strip()

    if cleaned == "":
        return False, "Please enter your name"

    if len(cleaned) < 2:
        return False, "Y0ur Name must be at least 2 characters"

    if any(character.isdigit() for character in cleaned):
        return False, "Please don't include numbers in your name"

    return True, ""


def calculate_percentage(score, total):
    """Working out a percentage from the score.

    Args:
        score: number of correct answers.
        total: number of questions.

    Returns:
        The percentage as a whole number. Returns 0 if total is 0.
    """
    if total == 0:
        return 0

    return round((score / total) * 100)


def hash_password(password):
    """Turns the  password into a hash so that it does not get saved as plain text

    Args:
        password: the text to hash.

    Returns:
        The hash as a string of characters.
    """
    return hashlib.sha256(password.encode()).hexdigest()


def check_password(entered_password, stored_hash):
    """Check a typed password against a stored hash.

    Args:
        entered_password: what the admin typed.
        stored_hash: the hash saved in the secrets file.

    Returns:
        True if they match, otherwise False.
    """
    return hash_password(entered_password) == stored_hash