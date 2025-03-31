from typing import Dict, Optional

class CSEService:

    @staticmethod
    def get_course_info(course_code:str, semester:Optional[str]=None) -> Dict:
        """
        get information about specific course
        :param course_code: the course code (e.g., CSE101)
        :param semester: Optional semester (e.g., Spring 2025)
        :return: dictionary with course information
        """

        print("course_code is ",course_code)
        return {
            "course_code":course_code,
            "name":f"Introduction to {course_code}",
            "credits":3,
            "semester":semester or "Current",
            "description": f"This is a course about {course_code}",
            "professor":"Dr. Smith"
        }

    @staticmethod
    def get_professor_info(professor_name: Optional[str] = None, department:Optional[str]=None) -> Dict:
        """
        get information about professor
        :param professor_name: optional name of the professor
        :param department: optional name of the department
        :return: dictionary with professor information
        """
        professors = {
            "Dr. Smith": {"name": "Dr. Smith", "department": "Computer Science", "expertise": "AI",
                          "email": "smith@university.edu"},
            "Dr. Johnson": {"name": "Dr. Johnson", "department": "Computer Science", "expertise": "Web Development",
                            "email": "johnson@university.edu"}
        }

        if professor_name in professors:
            return professors[professor_name]
        else:
            return {"professors":list(professors.values())}