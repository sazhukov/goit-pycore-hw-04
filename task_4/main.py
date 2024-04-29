def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."

def change_contact(args, contacts):
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return "Contact changed."
    else:
        return "Contact not found."

def print_contact(args, contacts):
    if args == []:
        for key, value in contacts.items():
            print(f'{key}: {value}')
        return "All contacts printed."
    else:
        name = args[0]
        if name in contacts:
            phone_number = contacts[name]
            print(f'{name}:{phone_number}')
            return "Contact printed."
        else:
            return "Contact not found."

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input("Enter a command: ")
        command, *args = parse_input(user_input)

        if command in ["close", "exit"]:
            print("Good bye!")
            break
        elif command == "hello":
            print("How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(print_contact(args, contacts))  
        elif command == "all":
            print(print_contact(args, contacts))                       
        else:
            print("Invalid command.")

if __name__ == "__main__":
    main()
