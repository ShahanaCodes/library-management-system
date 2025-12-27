#library management system
class Book:
    def display_info(self):
        print(f"📖 {self.title} by {self.author}")


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)
        print(f"✅ '{book.title}' added to the library.")

    def show_books(self):
        if not self.books:
            print("📚 No books in the library.")
        else:
            print("\n--- Library Books 📚 ---")
            for book in self.books:
                book.display_info()

    def search_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                print(f"🔍 Found: {book.title} by {book.author}")
                return
        print("❌ Book not found.")

    def remove_book(self, title):
        for book in self.books:
            if book.title.lower() == title.lower():
                self.books.remove(book)
                print(f"🗑️ '{book.title}' removed from the library.")
                return
        print("❌ Book not found.")


def main():
    library = Library()

    while True:
        print("\n===== Library Menu 📖 =====")
        print("1. Add Book ➕")
        print("2. Show All Books 📚")
        print("3. Search Book 🔍")
        print("4. Remove Book 🗑️")
        print("5. Exit ❌")

        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter author name: ")
            new_book = Book(title, author)
            library.add_book(new_book)

        elif choice == "2":
            library.show_books()

        elif choice == "3":
            title = input("Enter book title to search: ")
            library.search_book(title)

        elif choice == "4":
            title = input("Enter book title to remove: ")
            library.remove_book(title)

        elif choice == "5":
            print("🙏 Thank you for using the Library System!")
            break

        else:
            print("⚠️ Invalid choice! Try again.")


if __name__ == "__main__":
    main()

