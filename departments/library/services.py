from typing import Dict


class LibraryService:
    """
    Service class for handling library-related queries
    """

    @staticmethod
    def get_book_information(isbn: str) -> Dict:
        """
        Retrieve book information based on ISBN
        :param isbn: International Standard Book Number
        :return: Dictionary with book details
        """
        book_database = {
            "9780123456789": {
                "title": "Introduction to Computer Science",
                "author": "John Smith",
                "publisher": "Tech Publications",
                "publication_year": 2023,
                "available": True,
                "location": "Main Library, Section A, Shelf 3"
            },
            "9789876543210": {
                "title": "Advanced Machine Learning",
                "author": "Emily Johnson",
                "publisher": "AI Press",
                "publication_year": 2022,
                "available": False,
                "location": "Research Library, Section B, Shelf 5"
            }
        }

        if isbn in book_database:
            return book_database[isbn]
        else:
            return {"error": "Book not found"}