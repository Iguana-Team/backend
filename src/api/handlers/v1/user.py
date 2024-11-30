from fastapi import APIRouter
from src.schema.user import RegisterUserRequest
from src.adapter.sql.repo.user import UserRepository
from src.adapter.sql.session import Database
from src.dto.user_dto import UserDTO
router = APIRouter(prefix="/user", tags=["User"])
repo = UserRepository(Database().session)


@router.post("")
async def register_user(request: RegisterUserRequest):
    return await repo.singup(
        UserDTO(
            id=request.id,
            username=request.username,
            password=request.password,
            permission=request.permission
        )
    )
