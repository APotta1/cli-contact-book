import json
import os
from contact import Contact

class ContactBook:
    def __init__(self, filename = "contacts.json"):
        self.filename = filename
        self.contacts = [] #to hold Contact objects
        self.load_from_file() #to populate 

    def add_contact(self, name, phone, email): #adds new contact
        contact = Contact(name, phone, email) #
        self.contacts.append(contact)
        self.save_to_file()
        print(f"Contact '{name}' added successfully")

    def delete_contact(self, name): #self - contact book, #name is piece of information passed
        for contact in self.contacts: #loop through the contacts
            if contact.name.lower() == name.lower(): #checks a condition condition is true
                self.contacts.remove(contact) #names matched removes the contact
                self.save_to_file()
                print(f"Contact '{name}' deleted successfully!")
                return
        print(f"Contact '{name}' not found.")

    def search_contact(self, name): #defined method called as self
        results = [c for c in self.contacts if name.lower() in c.name.lower()]
        if results:
            for contact in results:
                print(contact)
        else:
            print(f"No contacts to be found for '{name}")

    def list_all(self, name):
        with open(self.filename, "w") as f:
            json.dump([c.to_dict() for c in self.contacts]f, indent = 2)

    def load_from_file(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                data = json.load(f)
                self.contacts = [Contact.from_dict(c) for c in data]