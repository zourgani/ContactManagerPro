#!/usr/bin/env python3
"""
Main entry point for the Contact Manager application
"""
import sys
import os

# Add parent directory to path for direct execution
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from contact_manager.cli import ApplicationCLI

def main():
    """Launches the Contact Manager application"""
    app = ApplicationCLI()
    app.run()

if __name__ == "__main__":
    main()