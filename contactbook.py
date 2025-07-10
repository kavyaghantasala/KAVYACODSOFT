def validate_phone(phone):
    """Validate phone number (10 digits, numeric)."""
    return phone.isdigit() and len(phone) == 10

def validate_email(email):
    """Basic email validation (contains @ and .)."""
    return '@' in email and '.' in email if email else True

def get_contact_details():
    """Prompt for contact details with validation."""
    while True:
        name = input("Enter name: ").strip()
        if name:
            break
        print("Error: Name cannot be empty.")

    while True:
        phone = input("Enter phone number (10 digits): ").strip()
        if validate_phone(phone):
            break
        print("Error: Phone number must be 10 digits.")

    email = input("Enter email (optional): ").strip()
    if email and not validate_email(email):
        print("Warning: Email format looks invalid, but saved anyway.")

    address = input("Enter address (optional): ").strip()
    return {"name": name, "phone": phone, "email": email, "address": address}

def add_contact(contacts):
    """Add a new contact."""
    contact = get_contact_details()
    contacts.append(contact)
    print(f"\nContact '{contact['name']}' added successfully!\n")

def view_contacts(contacts):
    """Display all contacts."""
    if not contacts:
        print("\nNo contacts found.\n")
        return
    
    print("\nContact List:")
    print("-" * 50)
    print(f"{'Name':<20} {'Phone':<15}")
    print("-" * 50)
    for contact in contacts:
        print(f"{contact['name']:<20} {contact['phone']:<15}")
    print("-" * 50 + "\n")

def search_contacts(contacts):
    """Search contacts by name or phone."""
    query = input("Enter name or phone number to search: ").strip().lower()
    matches = [
        c for c in contacts
        if query in c['name'].lower() or query in c['phone']
    ]
    
    if not matches:
        print("\nNo contacts found.\n")
        return
    
    print("\nSearch Results:")
    print("-" * 50)
    print(f"{'Name':<20} {'Phone':<15} {'Email':<20} {'Address':<20}")
    print("-" * 50)
    for contact in matches:
        print(f"{contact['name']:<20} {contact['phone']:<15} {contact['email']:<20} {contact['address']:<20}")
    print("-" * 50 + "\n")

def update_contact(contacts):
    """Update a contact's details."""
    if not contacts:
        print("\nNo contacts to update.\n")
        return
    
    view_contacts(contacts)
    name = input("Enter the name of the contact to update: ").strip().lower()
    for contact in contacts:
        if contact['name'].lower() == name:
            print(f"\nUpdating contact: {contact['name']}")
            new_contact = get_contact_details()
            contact.update(new_contact)
            print(f"\nContact '{contact['name']}' updated successfully!\n")
            return
    print("\nContact not found.\n")

def delete_contact(contacts):
    """Delete a contact."""
    if not contacts:
        print("\nNo contacts to delete.\n")
        return
    
    view_contacts(contacts)
    name = input("Enter the name of the contact to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == name:
            confirm = input(f"Are you sure you want to delete '{contact['name']}'? (yes/no): ").lower().strip()
            if confirm in ['yes', 'y']:
                deleted = contacts.pop(i)
                print(f"\nContact '{deleted['name']}' deleted successfully!\n")
            else:
                print("\nDeletion cancelled.\n")
            return
    print("\nContact not found.\n")

def display_menu():
    """Display the main menu."""
    print("Contact Book Menu")
    print("----------------")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def main():
    """Main function to run the Contact Book."""
    contacts = []
    print("Welcome to the Contact Book!")
    
    while True:
        display_menu()
        choice = input("Enter your choice (1-6): ").strip()
        
        try:
            choice = int(choice)
            if choice == 1:
                add_contact(contacts)
            elif choice == 2:
                view_contacts(contacts)
            elif choice == 3:
                search_contacts(contacts)
            elif choice == 4:
                update_contact(contacts)
            elif choice == 5:
                delete_contact(contacts)
            elif choice == 6:
                print("\nThank you for using the Contact Book. Goodbye!\n")
                break
            else:
                print("\nError: Please enter a number between 1 and 6.\n")
        except ValueError:
            print("\nError: Please enter a valid number.\n")

if __name__ == "__main__":
    main()
    