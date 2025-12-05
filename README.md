# 📇 ContactManagerPro

[![Python](https://img.shields.io/badge/Python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Rich](https://img.shields.io/badge/CLI-Rich-purple.svg)](https://github.com/Textualize/rich)

A professional contact management application built with Python OOP and a beautiful Rich CLI interface.

![Contact Manager Demo](https://img.shields.io/badge/Status-Active-success)

---

## ✨ Features

- 📝 **Add contacts** with validation (email, phone)
- 👀 **List all contacts** in a beautiful table
- 🔍 **Search contacts** by name or email
- 🗑️ **Delete contacts** with confirmation
- 📤 **Export to CSV** - Export all contacts to a CSV file
- 📥 **Import from CSV** - Import contacts from a CSV file
- 💾 **Automatic JSON persistence**
- 🎨 **Modern CLI** with Rich library
- ✅ **Data validation** (email format, phone number)

---

## 🚀 Quick Start

### Prerequisites

- Python 3.7 or higher
- pip (Python package manager)

### Installation

```bash
# Clone the repository
git clone https://github.com/zourgani/ContactManagerPro.git
cd ContactManagerPro

# Create virtual environment (recommended)
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# or
.venv\Scripts\activate     # Windows

# Install the package
pip install -e .
```

### Usage

```bash
# Run the application
contacts

# Or run directly with Python
python -m contact_manager.main
```

---

## 📖 How to Use

### Main Menu

```text
╭───────── Main Menu ─────────╮
│ CONTACT MANAGER v1.1        │
│                             │
│ [1] ➕ Add a new contact    │
│ [2] 👀 Show all contacts    │
│ [3] 🔍 Search for a contact │
│ [4] 🗑️  Delete a contact    │
│ [5] 📤 Export to CSV        │
│ [6] 📥 Import from CSV      │
│ [7] 🚪 Quit                 │
╰─────────────────────────────╯
```

### Examples

#### Adding a Contact

```text
Name: Jean Dupont
Email: jean.dupont@gmail.com
Phone: 0612345678
✅ Contact Jean Dupont added successfully!
```

#### Viewing Contacts

```text
┏━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━┳━━━━━━━━━━━━━━━━━━┓
┃ Name         ┃ Email                    ┃ Phone        ┃ Added on         ┃
┡━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━╇━━━━━━━━━━━━━━━━━━┩
│ Jean Dupont  │ jean.dupont@gmail.com    │ 0612345678   │ 2025-12-02 10:30 │
│ Marie Martin │ marie.martin@outlook.fr  │ 0698765432   │ 2025-12-02 10:31 │
└──────────────┴──────────────────────────┴──────────────┴──────────────────┘
```

---

## 🏗️ Project Structure

```text
ContactManagerPro/
├── 📄 .gitignore             # Git ignore rules
├── 📄 LICENSE                # MIT License
├── 📄 Makefile               # Automation commands
├── 📄 README.md              # Documentation
├── 📄 requirements.txt       # Python dependencies
├── 📄 setup.py               # Package configuration
├── 📄 contacts.json          # Data storage (auto-generated)
├── 📁 TestUnitaire/          # Unit tests
│   ├── __init__.py
│   └── test_manager.py       # Tests for manager & models
└── 📁 contact_manager/       # Main package
    ├── __init__.py           # Package exports
    ├── models.py             # Contact & ContactError classes
    ├── manager.py            # ContactManager (CRUD + CSV)
    ├── cli.py                # Rich CLI interface
    └── main.py               # Entry point
```

---

## 🛠️ Technical Details

### Architecture

| Module       | Responsibility                    |
|--------------|-----------------------------------|
| `models.py`  | Data models with validation       |
| `manager.py` | Business logic & JSON persistence |
| `cli.py`     | User interface with Rich          |
| `main.py`    | Application entry point           |

### Dependencies

| Package                                     | Purpose                       |
|---------------------------------------------|-------------------------------|
| [Rich](https://github.com/Textualize/rich)  | Beautiful terminal formatting |
| [Click](https://click.palletsprojects.com/) | CLI framework (future use)    |

### Data Validation

- **Email**: RFC 5322 regex pattern
- **Phone**: Minimum 10 digits required

---

## 🧪 Development

### Running Tests

```bash
# Install test dependencies
pip install pytest pytest-cov

# Run tests
pytest TestUnitaire/ -v

# With coverage
pytest --cov=contact_manager --cov-report=html
```

### Code Quality

```bash
# Format code
pip install black
black contact_manager/

# Lint code
pip install flake8
flake8 contact_manager/
```

---

## 📝 API Reference

### Contact Class

```python
from contact_manager import Contact

# Create a contact
contact = Contact("Jean", "jean@email.com", "0612345678")

# Convert to dictionary
data = contact.to_dict()

# Create from dictionary
contact = Contact.from_dict(data)
```

### ContactManager Class

```python
from contact_manager import ContactManager

manager = ContactManager()

# Add contact
manager.add("Jean", "jean@email.com", "0612345678")

# Search
results = manager.search("jean")

# Delete
manager.delete("jean@email.com")

# Get all contacts
contacts = manager.contacts

# Export to CSV
manager.export_csv("contacts.csv")

# Import from CSV
manager.import_csv("contacts.csv")
```

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 👤 Author

### ZOURGANI

- GitHub: [@zourgani](https://github.com/zourgani)
- Email: [zourgani.achraf@gmail.com](mailto:zourgani.achraf@gmail.com)

---

## 🙏 Acknowledgments

- [Rich](https://github.com/Textualize/rich) - Beautiful terminal formatting
- [Python](https://www.python.org/) - Programming language

## 🆕 Nouveautés - Version 1.0.1
