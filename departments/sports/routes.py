from fastapi import APIRouter
from typing import Dict

from departments.sports.services import SportsService

router = APIRouter(prefix="/sports", tags=["Sports Department"])

@router.get("/events")
async def get_sports_events() -> Dict:
    """
    Retrieve sports events and facilities information
    :return: Dictionary with sports events and facilities details
    """
    return SportsService.get_sports_events()