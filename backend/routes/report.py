from fastapi import APIRouter

router = APIRouter(prefix="/report", tags=["Report"])

@router.get("/")
def get_report():
    return {"message": "📄 Audit report coming soon"}
