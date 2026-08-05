"""Read, clean, and validate contact information from a text file."""
def cleaned_contacts(filepath:str) -> list[tuple[str,str]]:
    """Read a contact file and return a list of valid contacts
    

    The function opens a text file containing contact information,
    removes blank lines and separator lines, ignores invalid records,
    and returns only contacts with a valid email address.

    Args:
        filepath: The path to the contact text file.

    Returns:
        A list of tuples, where each tuple contains a contact's
        name and email address."""

    contacts = []

    try:
        with open(filepath,"r",encoding="utf-8") as contacts_file:
            all_lines  = contacts_file.readlines()
    except FileNotFoundError:
        print(f"No file found named {filepath} -- returning an empty list.") 
        return [] 

    for line in all_lines: 
        cleaned_line = line.strip() 
        if not cleaned_line: 
            continue 
        if cleaned_line.startswith("---"): 
            continue 
        if "," not in cleaned_line: 
            continue 

        name_part,email_part = cleaned_line.split(",",1)
        name = name_part.strip()
        email = email_part.strip() 

        if "@" not in email: 
            continue  

        email = email.split()[0] 
        contacts.append((name,email))
    return contacts 

if __name__ == "__main__": 
    contacts = cleaned_contacts("contacts.txt") 
    print(f"Found {len(contacts)} contacts:") 
    for name,email in contacts: 
        print(f"    {name:<10} {email}")