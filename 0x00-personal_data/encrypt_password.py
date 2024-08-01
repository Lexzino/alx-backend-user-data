#!/usr/bin/env python3
"""Module for password hashing and validation using bcrypt"""
import bcrypt


def hash_password(password: str) -> bytes:
    """Generates a bcrypt hash for the given password."""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """Verifies a password against a given bcrypt hash."""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)
