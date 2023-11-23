import pytest

class Book:
    def __init__(self, title, author, pages, price, quantity, sales):
        self._title = title
        self._author = author
        self._pages = pages
        self._price = price
        self._quantity = quantity
        self._sales = sales

    def __str__(self):
        return f"{self._title} by {self._author}"

    def __repr__(self):
        return f"Book({self._title}, {self._author}, {self._price}, {self._pages}, {self._quantity}, {self._sales})"


class BookShop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def del_book(self, book):
        self.books.remove(book)

    def get_top_books_by_price(self, n):
        sorted_books = sorted(self.books, key=lambda x: x.price, reverse=True)
        return sorted_books[:n]

    def get_top_books_by_sales(self, n):
        sorted_books = sorted(self.books, key=lambda x: x.sales, reverse=True)
        return sorted_books[:n]
