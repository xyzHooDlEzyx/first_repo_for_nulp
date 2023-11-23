from bookshelf import Book
from bookshelf import BookShop


def main():
    song_of_ice_and_fire = Book("Song of Ice and Fire", "J. Martin", 400, 200, 1000, 250)
    harry_potter = Book("Harry Potter", "Joanne Rowling", 400, 100, 8000, 4000)
    jojo_bizarre_adventures = Book("JoJo Bizarre Adventures", "H. Araki", 900, 300, 10000, 8000)

    bookshop = BookShop()
    bookshop.add_book(song_of_ice_and_fire)
    bookshop.add_book(harry_potter)
    bookshop.add_book(jojo_bizarre_adventures)

    get_top_price_books = bookshop.get_top_books_by_price(2)
    get_top_sales_books = bookshop.get_top_books_by_sales(2)

    print("\nTop books by price:")
    for book in top_price_books:
        print(book)
    print("\nTop books by sales:")
    for book in top_sales_books:
        print(book)

    bookshop.del_book(book1)


if __name__ == '__main__':
    main()
