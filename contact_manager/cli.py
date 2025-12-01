"""
Command line interface for the Contact Manager
"""
from .manager import ContactManager

# === CLI APPLICATION ===
class ApplicationCLI:
    """Command line interface for the manager"""
    
    def __init__(self):
        self.manager = ContactManager()
        self.in_progress = True
    
    def display_menu(self):
        """Displays the main menu"""
        print("\n" + "="*60)
        print("📱 CONTACT MANAGER v1.0")
        print("="*60)
        print("1. 📝 Add a contact")
        print("2. 👀 Show all contacts")
        print("3. 🔍 Search for a contact")
        print("4. 🗑️  Delete a contact")
        print("5. 📊 Statistics")
        print("6. 🚪 Quit")
        print("="*60)
    
    def add_contact(self):
        """Interface to add a contact"""
        print("\n➕ NEW CONTACT")
        name = input("Name: ").strip()
        email = input("Email: ").strip()
        telephone = input("Phone: ").strip()
        
        if name and email and telephone:
            result = self.manager.add(name, email, telephone)
            print(result)
        else:
            print("❌ All fields are required")
    
    def search_contact(self):
        """Interface to search for a contact"""
        term = input("\n🔍 Search (name or email): ").strip()
        if term:
            print(self.manager.search(term))
    
    def delete_contact(self):
        """Interface to delete a contact"""
        email = input("\n🗑️ Email of contact to delete: ").strip()
        if email:
            confirmation = input(f"Confirm deletion of {email}? (y/n): ")
            if confirmation.lower() == 'y':
                print(self.manager.delete(email))
    
    def display_stats(self):
        """Displays statistics"""
        print(f"\n📊 STATISTICS")
        print(f"Total contacts: {len(self.manager)}")
        if self.manager.contacts:
            last = self.manager.contacts[-1]
            print(f"Last added: {last.name} ({last.date_added})")
    
    def execute(self):
        """Main application loop"""
        print("\n🎉 Welcome to the Contact Manager!")
        print(f"📁 Data file: {self.manager.file}")
    
        while self.in_progress:
        
            try:
                self.display_menu()
                choice = input("\n👉 Your choice: ").strip()
                
                if choice == "1":
                    self.add_contact()
                elif choice == "2":
                    print(self.manager.display_all())
                elif choice == "3":
                    self.search_contact()
                elif choice == "4":
                    self.delete_contact()
                elif choice == "5":
                    self.display_stats()
                elif choice == "6":
                    self.in_progress = False
                    print("\n👋 Goodbye! Your contacts have been saved.")
                else:
                    print("❌ Invalid choice")
                    
                if self.in_progress:
                    input("\n⏎ Press Enter to continue...")
                    
            except KeyboardInterrupt:
                print("\n\n⚠️ Interruption detected")
                self.in_progress = False
            except Exception as e:
                print(f"❌ Unexpected error: {e}")