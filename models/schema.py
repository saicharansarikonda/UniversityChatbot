from typing import Dict, List, Optional, Any
from enum import Enum
from pydantic import BaseModel, Field

class Department(str,Enum):
    CSE = "Computer Science Department"
    LIBRARY = "Library"
    ADMIN = "Administration"
    FINANCE = "Finance"
    SPORTS = "Sports Department"
    CAREER = "Career Services"

class ChatRequest(BaseModel):
    query: str = Field(...,description="User query for the chatbot")

class ChatResponse(BaseModel):
    department: Optional[str] = Field(None, description="The department handling query")
    status: str = Field(...,description="Status of the response: success, need_more_info, error")
    response: Optional[str] = Field(None, description="Response from the chatbot")
    required_info: Optional[Dict[str,str]] = Field(None, description="Information needed from the user")
    used_info: Optional[Dict[str,Any]] = Field(None, description="Information used in the query")
    message: Optional[str] = Field(None, description="Error message if status is error")


#CSE Department APIs schemas
class CourseInfoRequest(BaseModel):
    course_code: str = Field(...,description="The course code, e.g., 'CS101'")
    semester: Optional[str] = Field(None, description="The semester, e.g., 'Spring 2025'")


class ProfessorInfoRequest(BaseModel):
    professor_name: Optional[str] = Field(None, description="The professor's name")
    department: Optional[str] = Field(None, description="The department name, e.g., 'Computer Science'")


#Library APIs schemas
class BookInfoRequest(BaseModel):
    title: Optional[str] = Field(None, description="The book title")
    author: Optional[str] = Field(None, description="The book author")
    isbn: Optional[str] = Field(None, description="The book ISBN")


#Administration APIs schemas
class AdmissionInfoRequest(BaseModel):
    program: str = Field(..., description="The program name, e.g., 'Computer Science', 'MBA'")
    semester: Optional[str] = Field(None, description="The semester, e.g., 'Spring 2025'")


#Finance APIs schemas
class FeeInfoRequest(BaseModel):
    student_id: str = Field(..., description="The Student ID")
    semester: Optional[str] = Field(None, description="The semester, e.g., 'Spring 2025'")

class ScholarshipInfoRequest(BaseModel):
    program: str = Field(..., description="The program name")
    criteria: Optional[str] = Field(None, description="Scholarship criteria, e.g., 'merit', 'need-based'")


#Sports APIs schemas
class SportsEventsRequest(BaseModel):
    event_type: Optional[str] = Field(None, description="The type of sport event, e.g., 'basketball', 'football'")
    date: Optional[str] = Field(None, description="The date of the event, e.g., '2025-04-10'")

class TeamInfoRequest(BaseModel):
    team_name: str = Field(..., description="The team name, e.g., 'Eagles Basketball'")


#Career APIs schemas
class JobInfoRequest(BaseModel):
    job_type: Optional[str] = Field(None, description="The job type, e.g., 'internship', 'full-time'")
    company: Optional[str] = Field(None, description="The company name")

class ResumeReviewRequest(BaseModel):
    student_id: str = Field(..., description="The student ID")
    review_type: Optional[str] = Field(None, description="Type of review, e.g., 'quick', 'comprehensive'")




#Query Classifier Model
class QueryClassification(BaseModel):
    department: Department = Field(..., description="The university department that can handle this query")
    reason: str = Field(..., description="Reason for selecting this department")
    required_info: Dict[str,Any] = Field(..., description="Information needed to fulfill the request")