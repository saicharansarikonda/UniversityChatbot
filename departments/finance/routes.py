from fastapi import APIRouter
from typing import Dict, Optional

from departments.finance.services import FinanceService

router = APIRouter(prefix="/finance", tags=["Finance Department"])

@router.get("/fees")
async def get_fee_information(
    semester: Optional[str] = None
) -> Dict:
    """
    Retrieve fee information
    :param semester: Optional semester to get specific fee details
    :return: Dictionary with fee information
    """
    return FinanceService.get_fee_information(semester)