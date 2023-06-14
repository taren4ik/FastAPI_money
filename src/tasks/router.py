from fastapi import APIRouter, Depends
from starlette.background import BackgroundTasks

from .tasks import send_email_report_dashboard

from src.auth.base_config import current_user

router = APIRouter(
    prefix='/report',
    tags=['Report']
)


@router.get('/dashboard')
def get_dashboard_report(user=Depends(current_user)):
    send_email_report_dashboard.delay(user.username)
    return {
        "status": 200,
        "data": "Письмо отправителя",
        "details": None
    }
