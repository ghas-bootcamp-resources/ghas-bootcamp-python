from dataclasses import dataclass


@dataclass
class Book:
    id: int
    name: str
    author: str
    genre: str
    read: bool
