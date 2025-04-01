from typing import Dict

class CareerService:
    """
    Service class for handling career-related queries
    """

    @staticmethod
    def get_career_resources(
        resource_type: str,
        job_type: str
    ) -> Dict:
        """
        Retrieve career services and job resources information
        :param resource_type: Type of career resource (e.g., 'internship', 'resume', 'events')
        :param job_type: Type of job (e.g., 'internship', 'full-time')
        :return: Dictionary with career services details
        """

        career_data = {
            "events": {
                "tech_internship": [
                    {
                        "event_name": "Tech Industry Career Fair",
                        "date": "2024-05-15",
                        "type": "internship",
                        "participating_companies": ["Google", "Microsoft", "Amazon"]
                    }
                ],
                "startup_networking": [
                    {
                        "event_name": "Startup Networking Night",
                        "date": "2024-06-20",
                        "type": "full-time",
                        "participating_companies": ["Local Tech Startups"]
                    }
                ]
            },
            "internships": {
                "tech": [
                    {
                        "title": "Software Engineering Internship",
                        "company": "Tech Innovations Inc.",
                        "type": "internship",
                        "duration": "3-6 months"
                    }
                ],
                "data_science": [
                    {
                        "title": "Data Science Internship",
                        "company": "Data Driven Solutions",
                        "type": "internship",
                        "duration": "Summer Program"
                    }
                ]
            },
            "resume_services": {
                "tech": [
                    {
                        "service_name": "Tech Industry Resume Review",
                        "description": "Professional resume critique for tech roles",
                        "availability": "Monday-Friday, 9 AM - 4 PM"
                    }
                ],
                "general": [
                    {
                        "service_name": "General Resume Review",
                        "description": "Comprehensive resume critique",
                        "availability": "By appointment"
                    }
                ]
            }
        }

        resource_type = resource_type.lower()
        job_type = job_type.lower()

        if resource_type not in career_data:
            return {"error": f"Resource type '{resource_type}' not found"}

        filtered_resources = career_data[resource_type].get(job_type, [])

        return {
            "resource_type": resource_type,
            "job_type": job_type,
            "resources": filtered_resources
        }