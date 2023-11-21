import pytest
class Book:
    def __init__(self, title, author, pages, price, quantity, sales):
        self.title = title
        self.author = author
        self.pages = pages
        self.price = price
        self.quantity = quantity
        self.sales = sales

    def __str__(self):
        return f"{self.title} by {self.author}"

    def __repr__(self):
        return f"Book({self.title}, {self.author}, {self.price}, {self.pages}, {self.quantity}, {self.sales})"


class BookShop:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def del_book(self, book):
        self.books.remove(book)

    def top_books_by_price(self, n):
        sorted_books = sorted(self.books, key=lambda x: x.price, reverse=True)
        return sorted_books[:n]

    def top_books_by_sales(self, n):
        sorted_books = sorted(self.books, key=lambda x: x.sales, reverse=True)
        return sorted_books[:n]
