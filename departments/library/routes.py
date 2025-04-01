from fastapi import APIRouter
from typing import Dict

from departments.library.services import LibraryService

router = APIRouter(prefix="/library", tags=["Library Department"])

@router.get("/book")
async def get_book_information(isbn: str) -> Dict:
    """
    Retrieve book information
    :param isbn: International Standard Book Number (REQUIRED)
    :return: Dictionary with book details
    """
    return LibraryService.get_book_information(isbn)