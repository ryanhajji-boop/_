import os
import subprocess


def create_file():
    """
    Create a new text file and allow the user to add lines.
    Typing 'STOP' ends input.
    """
    filename = input("Enter a filename (without extension): ").strip() + ".txt"

    print("Enter your text line by line. Type 'STOP' to finish.")
    line_number = 1
    with open(filename, "a") as file:
        while True:
            line = input(f"Line {line_number}: ")
            if line.strip().upper() == "STOP":
                break
            file.write(line + "\n")
            line_number += 1

    print(f"✅ File '{filename}' saved.")


def view_file():
    """
    Prompt the user for a filename and display its contents in the console.
    """
    filename = input("Enter the filename to view (without extension): ").strip() + ".txt"

    if not os.path.exists(filename):
        print("❌ File does not exist.")
        return

    subprocess.run(['open', filename])
    print("\n------ File Content ------")
    with open(filename, "r") as file:
        content = file.read()
        print(content if content else "(empty file)")
    print("--------------------------\n")
    


def edit_file():
    """
    Allow the user to edit a specific line in an existing file.
    Displays file content with line numbers, then lets the user choose a line to replace.
    """
    filename = input("Enter the filename to edit (without extension): ").strip() + ".txt"

    if not os.path.exists(filename):
        print("❌ File does not exist.")
        return

    with open(filename, "r") as file:
        lines = file.readlines()

    if not lines:
        print("⚠️ The file is empty. Nothing to edit.")
        return

    print("\n------ Current File ------")
    for i, line in enumerate(lines):
        print(f"{i}: {line.strip()}")
    print("--------------------------\n")

    try:
        line_number = int(input("Enter the line number you want to edit: "))
        if not (0 <= line_number < len(lines)):
            print("❌ Invalid line number.")
            return
    except ValueError:
        print("❌ Please enter a valid number.")
        return

    new_text = input("Enter the new text: ")
    lines[line_number] = new_text + "\n"

    with open(filename, "w") as file:
        file.writelines(lines)

    print(f"✅ Line {line_number} updated successfully.")

    print("\n------ Updated File ------")
    for i, line in enumerate(lines):
        print(f"{i}: {line.strip()}")
    print("--------------------------\n")

def delete():
    choice = False
    while choice != True:
        decision = input("Enter the filename to delete (without extension): ").strip() + ".txt"

        if os.path.exists(decision):
            os.remove(decision)
            print("File deleted ✅")
            choice = True
            return
        else:
            print("The file does not exist 😖")

def menu():
    """
    Display the main menu and handle user choices.
    Loops until the user chooses to quit.
    """
    while True:
        print("📂 Text File Manager")
        print("1. Create a file")
        print("2. View a file")
        print("3. Edit a file")
        print("4. Delete a file")
        print("5. Quit")
        

        try:
            choice = int(input("Choose an option: "))
        except ValueError:
            print("❌ Invalid input. Please enter a number.\n")
            continue

        if choice == 1:
            create_file()
        elif choice == 2:
            view_file()
        elif choice == 3:
            edit_file()
        elif choice == 4:
            delete()
        elif choice == 5:
            print("👋 See ya!")
            break
        else:
            print("❌ Please choose a valid option (1-4).\n")

menu()