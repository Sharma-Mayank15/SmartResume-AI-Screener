from fastapi import APIRouter

router = APIRouter(prefix="/users", tags=["users"])

@router.get("/me")
async def read_current_user():
    return {"message": "Current user route"}
