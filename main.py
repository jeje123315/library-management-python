class Book:
    def __init__(self, title, author, year, status="Available"):
        self.title = title
        self.author = author
        self.year = year
        self.status = status

    def get_info(self):
        pass


class NovelBook(Book):
    def get_info(self):
        return f"Novel: {self.title} by {self.author}"

    def show_category(self):
        return "Category: Novel"


class EducationBook(Book):
    def get_info(self):
        return f"Education Book: {self.title} by {self.author}"

    def show_category(self):
        return "Category: Education"


# simpan data buku ke file
def save_to_file(books, filename="books.txt"):
    try:
        with open(filename, "w") as f:
            for book in books:
                if isinstance(book, NovelBook):
                    tipe = "Novel"
                else:
                    tipe = "Education"
                f.write(f"{tipe}|{book.title}|{book.author}|{book.year}|{book.status}\n")
        print("Data berhasil disimpan.")
    except IOError as e:
        print(f"Gagal menyimpan file: {e}")


# load data dari file saat program dijalankan
def load_from_file(filename="books.txt"):
    books = []
    try:
        with open(filename, "r") as f:
            for line in f:
                line = line.strip()
                if not line:
                    continue
                parts = line.split("|")
                if len(parts) != 5:
                    continue
                tipe, title, author, year, status = parts
                if tipe == "Novel":
                    book = NovelBook(title, author, year, status)
                elif tipe == "Education":
                    book = EducationBook(title, author, year, status)
                else:
                    continue
                books.append(book)
    except FileNotFoundError:
        pass
    except Exception as e:
        print(f"Error saat membaca file: {e}")
    return books


# tambah buku baru
def add_book(books):
    while True:
        tipe = input("Book Type (Novel/Education): ").strip()
        if tipe.lower() in ("novel", "education"):
            break
        print("Tipe buku harus Novel atau Education.")

    while True:
        title = input("Title: ").strip()
        if title:
            break
        print("Judul tidak boleh kosong.")

    while True:
        author = input("Author: ").strip()
        if author:
            break
        print("Author tidak boleh kosong.")

    while True:
        year = input("Year: ").strip()
        if year.isdigit():
            break
        print("Tahun harus berupa angka.")

    if tipe.lower() == "novel":
        book = NovelBook(title, author, year)
    else:
        book = EducationBook(title, author, year)

    books.append(book)
    print(f"Buku '{title}' berhasil ditambahkan!")
    save_to_file(books)


# tampilkan semua buku + statistik
def show_books(books):
    print("\n===== Daftar Buku =====")
    if not books:
        print("No books available.")
        return

    for i, book in enumerate(books, start=1):
        print(f"{i}. {book.get_info()}")
        print(f"   Year: {book.year} | Status: {book.status}")

    total = len(books)
    available = sum(1 for b in books if b.status == "Available")
    borrowed = total - available
    print(f"\nTotal Books: {total} | Available: {available} | Borrowed: {borrowed}")


# cari buku berdasarkan judul
def search_book(books):
    keyword = input("Masukkan judul yang dicari: ").strip()
    hasil = [b for b in books if keyword.lower() in b.title.lower()]

    if not hasil:
        print("Book not found.")
        return

    print(f"\nDitemukan {len(hasil)} buku:")
    for book in hasil:
        print(f"  - {book.get_info()} | Year: {book.year} | Status: {book.status}")


# pinjam buku
def borrow_book(books):
    title = input("Masukkan judul buku yang ingin dipinjam: ").strip()

    found = None
    for book in books:
        if book.title.lower() == title.lower():
            found = book
            break

    if not found:
        print("Book not found.")
        return

    if found.status == "Borrowed":
        print(f"'{found.title}' sedang dipinjam.")
        return

    found.status = "Borrowed"
    print(f"'{found.title}' berhasil dipinjam.")
    save_to_file(books)


# kembalikan buku
def return_book(books):
    title = input("Masukkan judul buku yang ingin dikembalikan: ").strip()

    found = None
    for book in books:
        if book.title.lower() == title.lower():
            found = book
            break

    if not found:
        print("Book not found.")
        return

    if found.status == "Available":
        print(f"'{found.title}' sudah tersedia, tidak perlu dikembalikan.")
        return

    found.status = "Available"
    print(f"'{found.title}' berhasil dikembalikan.")
    save_to_file(books)


def main():
    books = load_from_file()

    while True:
        print("\n===== Library Management System =====")
        print("1. Add Book")
        print("2. Show All Books")
        print("3. Search Book")
        print("4. Borrow Book")
        print("5. Return Book")
        print("6. Save Data to File")
        print("7. Exit")

        pilihan = input("Choose menu: ").strip()

        if pilihan not in ("1", "2", "3", "4", "5", "6", "7"):
            print("Pilihan tidak valid. Masukkan angka 1-7.")
            continue

        if pilihan == "1":
            add_book(books)
        elif pilihan == "2":
            show_books(books)
        elif pilihan == "3":
            search_book(books)
        elif pilihan == "4":
            borrow_book(books)
        elif pilihan == "5":
            return_book(books)
        elif pilihan == "6":
            save_to_file(books)
        elif pilihan == "7":
            print("Terima kasih, sampai jumpa!")
            break


if __name__ == "__main__":
    main()
