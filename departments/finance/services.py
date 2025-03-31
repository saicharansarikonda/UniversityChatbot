from typing import Dict, Optional


class FinanceService:
    """
    Service class for handling finance-related queries with a standardized fee structure
    """

    BASE_FEE_STRUCTURE = {
        "total_fees": 5000,
        "breakdown": {
            "tuition": 3500,
            "hostel": 1000,
            "library_fee": 300,
            "student_activities": 200
        }
    }

    @staticmethod
    def get_fee_information(semester: Optional[str] = None) -> Dict:
        """
        Retrieve fee information
        :param semester: Optional semester to get specific fee details
        :return: Dictionary with fee information
        """
        fee_info = FinanceService.BASE_FEE_STRUCTURE.copy()


        if semester:
            fee_info["semester"] = semester

        return fee_info