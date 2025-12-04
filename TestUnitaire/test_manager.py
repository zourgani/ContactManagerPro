"""
Unit tests for the contact manager
"""
import pytest
import os
import json
from contact_manager.manager import ContactManager
from contact_manager.models import Contact

class TestContactManager:
    """Tests for ContactManager"""
    
    @pytest.fixture
    def manager(self, tmp_path):
        """Creates a temporary manager for tests"""
        test_file = tmp_path / "test_contacts.json"
        return ContactManager(str(test_file))
    
    def test_add_contact(self, manager):
        """Test adding a contact"""
        result = manager.add("Test User", "test@email.com", "0123456789")
        assert "successfully" in result
        assert len(manager) == 1
    
    def test_duplicate_email(self, manager):
        """Test duplicate email rejection"""
        manager.add("User 1", "test@email.com", "0123456789")
        result = manager.add("User 2", "test@email.com", "9876543210")
        assert "Error" in result
        assert len(manager) == 1
    
    def test_search(self, manager):
        """Test search"""
        manager.add("Alice Dupont", "alice@email.com", "0123456789")
        manager.add("Bob Martin", "bob@email.com", "9876543210")
        
        # Search by name
        result = manager.search("alice")
        assert "Alice Dupont" in result
        
        # Search by email
        result = manager.search("bob@")
        assert "Bob Martin" in result
    
    def test_delete(self, manager):
        """Test deletion"""
        manager.add("Test User", "test@email.com", "0123456789")
        assert len(manager) == 1
        
        result = manager.delete("test@email.com")
        assert "✅" in result
        assert len(manager) == 0
        
        # Deletion of non-existent contact
        result = manager.delete("nonexistent@email.com")
        assert "❌" in result
    
    def test_persistence(self, tmp_path):
        """Test save and load"""
        test_file = tmp_path / "test_contacts.json"
        
        # Create and save
        manager1 = ContactManager(str(test_file))
        manager1.add("Test User", "test@email.com", "0123456789")
        
        # Load into a new manager
        manager2 = ContactManager(str(test_file))
        assert len(manager2) == 1
        assert manager2.contacts[0].name == "Test User"

class TestContact:
    """Tests for the Contact class"""
    
    def test_creation(self):
        """Test contact creation"""
        contact = Contact("John Doe", "john@email.com", "0123456789")
        assert contact.name == "John Doe"
        assert contact.email == "john@email.com"
        assert contact.telephone == "0123456789"
        assert contact.date_added  # Verify that a date is set
    
    def test_to_dict(self):
        """Test conversion to dictionary"""
        contact = Contact("Jane Doe", "jane@email.com", "9876543210")
        data = contact.to_dict()
        
        assert data["name"] == "Jane Doe"
        assert data["email"] == "jane@email.com"
        assert data["telephone"] == "9876543210"
        assert "date_added" in data
    
    def test_str_representation(self):
        """Test string representation"""
        contact = Contact("Test", "test@email.com", "0000000000")
        string = str(contact)
        
        assert "Test" in string
        assert "test@email.com" in string
        assert "0000000000" in string