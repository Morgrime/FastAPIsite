from fastapi import APIRouter

router = APIRouter()

@router.post('/login', tags=['login'])
async def login_endpoint():
    pass