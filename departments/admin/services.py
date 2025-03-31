from typing import Dict, Optional


class AdminService:
    """
    Service class for handling administrative queries
    """

    @staticmethod
    def get_academic_calendar_info(semester: Optional[str] = None) -> Dict:
        """
        Retrieve academic calendar information
        :param semester: Optional semester to get specific calendar details
        :return: Dictionary with academic calendar information
        """
        calendar_info = {
            "current_semester": "Spring 2024",
            "key_dates": [
                {"event": "Registration Start", "date": "January 15, 2024"},
                {"event": "Classes Begin", "date": "February 1, 2024"},
                {"event": "Mid-Term Exams", "date": "March 15-19, 2024"},
                {"event": "Final Exams", "date": "May 10-14, 2024"},
                {"event": "Semester Ends", "date": "May 15, 2024"}
            ]
        }

        return calendar_info

    @staticmethod
    def get_administrative_contact(contact_type: Optional[str] = None) -> Dict:
        """
        Retrieve administrative contact information
        :param contact_type: Optional type of administrative contact
        :return: Dictionary with contact details
        """
        contacts = {
            "registrar": {
                "name": "User1",
                "email": "registrar@university.edu",
                "phone": "+1 (555) 123-4567",
                "office_hours": "Monday-Friday, 9 AM - 4 PM"
            },
            "admissions": {
                "name": "User 2",
                "email": "admissions@university.edu",
                "phone": "+1 (555) 987-6543",
                "office_hours": "Monday-Thursday, 10 AM - 5 PM"
            },
            "student_affairs": {
                "name": "User3",
                "email": "studentaffairs@university.edu",
                "phone": "+1 (555) 246-8101",
                "office_hours": "Tuesday-Friday, 8 AM - 3 PM"
            }
        }

        if contact_type and contact_type.lower() in contacts:
            return contacts[contact_type.lower()]

        return {"available_contacts": list(contacts.keys())}