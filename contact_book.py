import json
import os
from contact import Contact

class ContactBook:
    def __init__(self, filename: str = "contacts.json") -> None:
        self.filename = filename
        self.contacts: list[Contact] = [] #to hold Contact objects
        self.load_from_file() #to populate 

    def add_contact(self, name: str, phone: str, email: str) -> None: #adds new contact
        contact = Contact(name, phone, email) #instance method
        self.contacts.append(contact)
        self.save_to_file()
        print(f"Contact '{name}' added successfully")

    def delete_contact(self, name: str) -> None: #self - contact book, #name is piece of information passed
        for contact in self.contacts: #loop through the contacts
            if contact.name.lower() == name.lower(): #checks a condition condition is true
                self.contacts.remove(contact) #names matched removes the contact
                self.save_to_file()
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name: str) -> None: #defined method called as self
        results = [c for c in self.contacts if name.lower() in c.name.lower()]
        if results:
            for contact in results:
                print(contact)
        else:
            print(f"No contacts to be found for '{name}'.")

    def list_all(self) -> None:
        if not self.contacts:
            print("No contacts saved yet.")
        else:
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact}")

    def save_to_file(self) -> None:
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts], f, indent=2)

    def load_from_file(self) -> None:
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(c) for c in data]