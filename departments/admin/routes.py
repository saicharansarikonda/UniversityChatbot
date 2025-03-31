from fastapi import APIRouter
from typing import Dict, Optional

from departments.admin.services import AdminService

router = APIRouter(prefix="/admin", tags=["Administration Department"])

@router.get("/academic-calendar")
async def academic_calendar(semester: Optional[str] = None) -> Dict:
    """
    Get academic calendar information
    :param semester: Optional semester to get specific calendar details
    :return: Dictionary of academic calendar information
    """
    return AdminService.get_academic_calendar_info(semester)

@router.get("/contacts")
async def administrative_contacts(contact_type: Optional[str] = None) -> Dict:
    """
    Get administrative contact information
    :param contact_type: Optional type of administrative contact
    :return: Dictionary of contact details
    """
    return AdminService.get_administrative_contact(contact_type)
