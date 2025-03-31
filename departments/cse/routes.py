from fastapi import APIRouter, Depends
from typing import Dict, Optional

from models.schema import CourseInfoRequest, ProfessorInfoRequest, Department
from departments.cse.services import CSEService
from utils.tools import tool_registry

router = APIRouter(prefix="/cse",tags=["Comptuer Science Department"])

@router.get("/course")
async def course_info(course_code:str, semester:Optional[str]=None) -> Dict:
    """
    get information about a specific course
    :param course_code: code of the course
    :param semester: optional semester
    :return: dict of course information
    """

    return CSEService.get_course_info(course_code,semester)


@router.get("/professor")
async def professor_info(professor_name:Optional[str]=None, department:Optional[str]=None) -> Dict:
    """
    get information about professor
    :param professor_name: name of the professor
    :param department: name of the department
    :return: dictionary of professor information
    """
    return CSEService.get_professor_info(professor_name,department)