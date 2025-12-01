"""
Contact manager package
"""
from .manager import ContactManager
from .models import Contact, ContactError
from .cli import ApplicationCLI

__all__ = [
    "ContactManager",
    "Contact",
    "ContactError",
    "ApplicationCLI",
]