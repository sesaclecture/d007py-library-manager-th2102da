
from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Iterable
from library.models.book import Book

class BaseService(ABC):
    """서비스 공통 인터페이스.
    TODO: 아래 메서드를 하위 클래스에서 구현하도록 하세요.
    """

    def __init__(self) -> None:
        self._books = []

    @abstractmethod
    def add_book(self, book: Book) -> None:
        ...
        # self._books.append(book)
        pass

    @abstractmethod
    def remove_book(self, title: str) -> None:
        ...
        # for book in self._books:
        #     if book.title != title:
        #         self._book.remove(book)
        #     return 
        # raise ValueError(f"Not Exists")
        pass

    @abstractmethod
    def list_books(self) -> Iterable[Book]:
        ...
        # return self._books
        pass

    @abstractmethod
    def find_book(self, title: str) -> Book:
        ...
        # for book in self._books:
        #     if book.title == title:
        #         return book
        #     raise ValueError(f"NOPE")
        pass