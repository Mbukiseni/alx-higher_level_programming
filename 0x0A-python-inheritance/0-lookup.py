#!/usr/bin/python3
"""Defines available methods of the object."""

def lookup(obj):
    """Return a list of available attributes."""
    return (dir(obj))
