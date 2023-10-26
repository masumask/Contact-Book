class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def search_contact(self, keyword):
        results = []
        for contact in self.contacts:
            if keyword.lower() in contact.name.lower() or keyword in contact.phone:
                results.append(contact)
        return results

    def update_contact(self, old_contact, new_contact):
        index = self.contacts.index(old_contact)
        self.contacts[index] = new_contact

    def delete_contact(self, contact):
        self.contacts.remove(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("Contact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)
            print("Contact added successfully!")

        elif choice == "2":
            print("Contact List:")
            for contact in contact_book.contacts:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

        elif choice == "3":
            keyword = input("Enter name or phone number to search: ")
            results = contact_book.search_contact(keyword)
            print("Search Results:")
            for contact in results:
                print(f"Name: {contact.name}, Phone: {contact.phone}")

        elif choice == "4":
            name = input("Enter name of the contact to update: ")
            results = contact_book.search_contact(name)
            if results:
                contact_to_update = results[0]
                new_name = input("Enter new name (press Enter to keep it unchanged): ")
                new_phone = input("Enter new phone number (press Enter to keep it unchanged): ")
                new_email = input("Enter new email (press Enter to keep it unchanged): ")
                new_address = input("Enter new address (press Enter to keep it unchanged): ")
                updated_contact = Contact(new_name or contact_to_update.name,
                                          new_phone or contact_to_update.phone,
                                          new_email or contact_to_update.email,
                                          new_address or contact_to_update.address)
                contact_book.update_contact(contact_to_update, updated_contact)
                print("Contact updated successfully!")
            else:
                print("Contact not found.")

        elif choice == "5":
            name = input("Enter name of the contact to delete: ")
            results = contact_book.search_contact(name)
            if results:
                contact_to_delete = results[0]
                contact_book.delete_contact(contact_to_delete)
                print("Contact deleted successfully!")
            else:
                print("Contact not found.")

        elif choice == "6":
            print("Exiting... Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
