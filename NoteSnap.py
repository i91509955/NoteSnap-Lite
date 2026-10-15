
import json
from pathlib import Path

# Store notes in a file beside this Python program.
FILE_PATH = Path(__file__).with_name("notes.json")


def load_notes():
    """Load saved notes from the file."""
    if not FILE_PATH.exists():
        return []

    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, OSError):
        print("Could not read the notes file.")
        return []


def save_notes(notes):
    """Save all notes to the file."""
    with open(FILE_PATH, "w", encoding="utf-8") as file:
        json.dump(notes, file, indent=4, ensure_ascii=False)


def add_note():
    notes = load_notes()

    subject = input("Enter subject: ").strip()
    title = input("Enter note title: ").strip()
    content = input("Enter your note: ").strip()

    if not subject or not title or not content:
        print("Please fill in all three fields.")
        return

    note = {
        "subject": subject,
        "title": title,
        "content": content
    }

    notes.append(note)
    save_notes(notes)

    print("Note saved successfully!")


def view_notes():
    notes = load_notes()

    if not notes:
        print("No notes saved yet.")
        return

    for number, note in enumerate(notes, start=1):
        print(f"\n--- Note {number} ---")
        print(f"Subject: {note['subject']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")



def search_notes():
    notes = load_notes()

    keyword = input(
        "Search by subject, title, or content: "
    ).strip().lower()

    if not keyword:
        print("Please enter a search term.")
        return

    matches = [
        note for note in notes
        if keyword in note["subject"].lower()
        or keyword in note["title"].lower()
        or keyword in note["content"].lower()
    ]

    if not matches:
        print("No matching notes found.")
        return

    for note in matches:
        print(f"\nSubject: {note['subject']}")
        print(f"Title: {note['title']}")
        print(f"Content: {note['content']}")



def main():
    while True:
        print("\n===== NoteSnap Lite =====")
        print("1. Add a note")
        print("2. View all notes")
        print("3. Search notes")
        print("4. Exit")

        choice = input("Choose an option: ").strip()

        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            search_notes()
        elif choice == "4":
            print("Thank you for using NoteSnap!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, 3, or 4.")


if __name__ == "__main__":
    main()