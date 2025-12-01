"""
Contact manager templates and models
"""
import json
import re
from datetime import datetime

# === CUSTOM EXCEPTION ===
class ContactError(Exception):
    """Exception for contact-related errors"""
    def __init__(self, message, field=None, value=None):
        super().__init__(message)
        self.field = field
        self.value = value

class Contact:
    """Represents a contact with name, email and phone"""
    
    def __init__(self, name, email, telephone):
        self.name = name
        self.email = self._validate_email(email)
        self.telephone = self._validate_phone(telephone)
        self.date_added = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    def _validate_email(self, email):
        """Validates email format using regex"""
        # RFC 5322 simplified pattern for email validation
        email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        
        if not re.match(email_pattern, email):
            raise ContactError(f"Invalid email format: {email}")
        
        return email
    
    def _validate_phone(self, telephone):
        """Validates phone format"""
        # Keep only digits
        tel_clean = ''.join(c for c in telephone if c.isdigit())
        
        if len(tel_clean) < 10:
            raise ContactError(f"Invalid phone number (minimum 10 digits): {telephone}")
        
        return telephone
        
    def to_dict(self):
        """Converts contact to dictionary"""
        return {
            "name" : self.name,
            "email" : self.email,
            "telephone" : self.telephone,
            "date_added" : self.date_added   
        }
        
    @classmethod
    def from_dict(cls, data):
        """Creates a contact from a dictionary"""
        contact = cls(data["name"], data["email"], data["telephone"])
        contact.date_added = data.get("date_added", contact.date_added)
        return contact
        
    def __str__(self):
        return f"📇 {self.name} | 📧 {self.email} | 📱 {self.telephone}"
        
    def __repr__(self):
        return f"Contact('{self.name}', '{self.email}', '{self.telephone}')"