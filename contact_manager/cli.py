"""
Enhanced CLI with Rich for professional display
"""
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt, Confirm
from rich.panel import Panel
from rich import print as rprint
from .manager import ContactManager

console = Console()

# === CLI APPLICATION ===
class ApplicationCLI:
    """Command line interface for the manager with Rich"""
    
    def __init__(self):
        self.manager = ContactManager()
    
    def display_menu(self):
        """Displays the main menu"""
        console.print(Panel.fit(
            "[bold cyan]CONTACT MANAGER v1.1[/bold cyan]\n\n"
            "[1] ➕ Add a new contact\n"
            "[2] 👀 Show all contacts\n"
            "[3] 🔍 Search for a contact\n"
            "[4] 🗑️  Delete a contact\n"
            "[5] 📤 Export to CSV\n"
            "[6] 📥 Import from CSV\n"
            "[7] 🚪 Quit",
            title="Main Menu", border_style="bright_blue"
        ))
    
    def list_contacts(self):
        """Displays contacts in a table"""
        contacts = self.manager.contacts
        if not contacts:
            console.print("[yellow]No contacts[/yellow]")
            return
        
        table = Table(title=f"{len(contacts)} Contact(s)")
        table.add_column("Name", style="cyan")
        table.add_column("Email", style="magenta")
        table.add_column("Phone", style="green")
        table.add_column("Added on", style="yellow")
        
        for c in contacts:
            table.add_row(c.name, c.email, c.telephone, c.date_added)
        
        console.print(table)
    
    def run(self):
        """Main loop with Rich"""
        console.print("[bold green]🎉 Welcome![/bold green]")
        
        while True:
            self.display_menu()
            choice = Prompt.ask("\n[bold]Your choice[/bold]", 
                               choices=["1","2","3","4","5","6","7"])
            
            if choice == "1":
                name = Prompt.ask("Name")
                email = Prompt.ask("Email")
                phone = Prompt.ask("Phone")
                result = self.manager.add(name, email, phone)
                rprint(f"[green]{result}[/green]" if "successfully" in result 
                      else f"[red]{result}[/red]")
            
            elif choice == "2":
                self.list_contacts()
            
            elif choice == "3":
                term = Prompt.ask("Search")
                result = self.manager.search(term)
                rprint(f"[cyan]{result}[/cyan]")
            
            elif choice == "4":
                email = Prompt.ask("Email to delete")
                if Confirm.ask(f"Confirm deletion of {email}?"):
                    result = self.manager.delete(email)
                    rprint(f"[green]{result}[/green]" if "✅" in result 
                          else f"[red]{result}[/red]")
            
            elif choice == "5":
                filename = Prompt.ask("CSV filename", default="contacts.csv")
                result = self.manager.export_csv(filename)
                rprint(f"[green]{result}[/green]" if "✅" in result 
                      else f"[red]{result}[/red]")
            
            elif choice == "6":
                filename = Prompt.ask("CSV filename to import", default="contacts.csv")
                result = self.manager.import_csv(filename)
                rprint(f"[green]{result}[/green]" if "✅" in result 
                      else f"[red]{result}[/red]")
            
            elif choice == "7":
                if Confirm.ask("Do you really want to quit?"):
                    rprint("[bold red]👋 Goodbye![/bold red]")
                    break
            
            input("\n⏎ Press Enter to continue...")