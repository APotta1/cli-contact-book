from contact_book import ContactBook
def main():
    book = ContactBook()

    while True:
        print("\n=== Contact Book ===")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. List All Contacts")
        print("5. Quit")

        choice = input("\nChoose option: ")
        if choice == "1":
            name = input("Name: ")
            phone = input("Phone: ")
            email = input("Email: ")
            book.add_contact(name, phone, email)

        elif choice == "2":
            name = input("Name to delete: ")
            book.delete_contact(name)

        elif choice == "3":
            name = input("Name to search: ")
            book.search_contact(name)
        
        elif choice == "4":
            book.list_all()
        
        elif choice == "5":
            print("Goodbye")
            break

        else:
            print("Invalid option. Please choose from 1 - 5")

if __name__ == "__main__":
    main()



