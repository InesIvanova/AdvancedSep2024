from abc import ABC, abstractmethod


class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter(ABC):
    @abstractmethod
    def format(self, book: Book) -> str:
        pass


class PaperFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:-2]


class A4Formatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content


class ClickbaitFormatter(Formatter):
    def format(self, book: Book) -> str:
        return book.content[:10]



class Printer:
    def get_book(self, formatter: Formatter, book: Book):
        return formatter.format(book)



book = Book("Some long title here")
p  = Printer()
paper = PaperFormatter()
c = ClickbaitFormatter()
print(p.get_book(c, book))
