"""
Contact manager with JSON persistence
"""
import json
import os
from typing import List, Optional
from .models import Contact, ContactError

# === CONTACT MANAGER ===
class ContactManager:
    """Manages a list of contacts with JSON backup"""
    
    def __init__(self, file="contacts.json"):
        self.file = file
        self.contacts = []
        self.load()
    
    def add(self, name: str, email: str, telephone: str) -> str:
        """Adds a new contact"""
        try:
            # Check if contact already exists
            if any(c.email == email for c in self.contacts):
                raise ContactError(f"A contact with email {email} already exists")
            
            contact = Contact(name, email, telephone)
            self.contacts.append(contact)
            self.save()
            return f"Contact {name} added successfully!"
        except ContactError as e:
            return f"❌ Error: {e}"
    
    def display_all(self):
        """Displays all contacts"""
        if not self.contacts:
            return "📭 No contacts saved"
        
        result = f"\n📋 CONTACT LIST ({len(self.contacts)})\n"
        result += "=" * 60 + "\n"
        for i, contact in enumerate(self.contacts, 1):
            result += f"{i}. {contact}\n"
        return result
    
    def search(self, term):
        """Searches for a contact by name or email"""
        term_lower = term.lower()
        results = [c for c in self.contacts
                    if term_lower in c.name.lower()
                    or term_lower in c.email.lower()]
        
        if not results:
            return f"❌ No contact found for '{term}'"
        
        return "\n".join(str(c) for c in results)
    
    def delete(self, email):
        """Deletes a contact by email"""
        for contact in self.contacts:
            if contact.email == email:
                self.contacts.remove(contact)
                self.save()
                return f"✅ Contact {contact.name} deleted"
        return f"❌ No contact with email {email}"
        
    def save(self):
        """Saves contacts to a JSON file"""
        try:
            data = [c.to_dict() for c in self.contacts]
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"⚠️ Saving error: {e}")
    
    def load(self):
        """Loads contacts from JSON file"""
        try:
            if not os.path.exists(self.file):
                return
            
            with open(self.file, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(d) for d in data]
        except json.JSONDecodeError:
            print(f"⚠️ File {self.file} corrupted, creating a new database")
            self.contacts = []
        except Exception as e:
            print(f"⚠️ Loading error: {e}")
            self.contacts = []
        
    def __len__(self):
        """Returns the number of contacts"""
        return len(self.contacts)
    
    def __str__(self):
        return f"Manager with {len(self)} contacts"
    
    def export_csv(self, filename: str = "contacts.csv") -> str:
        """Exports contacts to a CSV file"""
        import csv
        
        if not self.contacts:
            return "❌ No contacts to export"
        
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Email', 'Phone', 'Date Added'])
                for c in self.contacts:
                    writer.writerow([c.name, c.email, c.telephone, c.date_added])
            
            return f"✅ Exported {len(self.contacts)} contacts to {filename}"
        except Exception as e:
            return f"❌ Export error: {e}"
    
    def import_csv(self, filename: str = "contacts.csv") -> str:
        """Imports contacts from a CSV file"""
        import csv
        
        if not os.path.exists(filename):
            return f"❌ File {filename} not found"
        
        try:
            imported = 0
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    result = self.add(row['Name'], row['Email'], row['Phone'])
                    if "successfully" in result:
                        imported += 1
            
            return f"✅ Imported {imported} contacts from {filename}"
        except Exception as e:
            return f"❌ Import error: {e}"