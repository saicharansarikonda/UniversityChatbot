from fastapi import APIRouter
from typing import Dict

from departments.career.services import CareerService

router = APIRouter(prefix="/career", tags=["Career Services Department"])

@router.get("/resources")
async def get_career_resources(
    resource_type: str,
    job_type: str
) -> Dict:
    """
    Retrieve career services and job resources information
    :param resource_type: Type of career resource (REQUIRED)
    :param job_type: Type of job (REQUIRED)
    :return: Dictionary with career services details
    """
    return CareerService.get_career_resources(
        resource_type=resource_type,
        job_type=job_type
    )