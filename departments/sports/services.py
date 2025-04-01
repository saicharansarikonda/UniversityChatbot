from typing import Dict, List

class SportsService:
    """
    Service class for handling sports-related queries
    """

    @staticmethod
    def get_sports_events() -> Dict:
        """
        Retrieve current sports events information
        :return: Dictionary with sports events details
        """
        return {
            "upcoming_events": [
                {
                    "event_name": "Basketball Tournament",
                    "date": "2024-04-15",
                    "location": "University Sports Complex",
                    "teams": ["Eagles", "Hawks", "Wolves"]
                },
                {
                    "event_name": "Soccer Championship",
                    "date": "2024-05-20",
                    "location": "Main Stadium",
                    "teams": ["Strikers", "Rovers", "United"]
                }
            ],
            "sports_facilities": [
                {
                    "name": "Main Gymnasium",
                    "sports": ["Basketball", "Volleyball"],
                    "operating_hours": "6:00 AM - 10:00 PM"
                },
                {
                    "name": "Soccer Field",
                    "sports": ["Soccer", "Football"],
                    "operating_hours": "7:00 AM - 9:00 PM"
                }
            ]
        }