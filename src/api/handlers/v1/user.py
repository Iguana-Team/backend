from fastapi import APIRouter
from src.schema.user import SingUpUserRequest, LoginUserRequest
from src.adapter.sql.repo.user import UserRepository
from src.adapter.sql.session import Database
from src.dto.user_dto import UserDTO, process_password
router = APIRouter(prefix="/user", tags=["User"])
repo = UserRepository(Database().session)


@router.post("/signup")
async def signup_user(request: SingUpUserRequest):
    return await repo.signup(
        UserDTO(
            id=request.id,
            username=request.username,
            password=process_password(request.password),
            permission=request.permission
        )
    )


@router.post("/login")
async def login_user(request: LoginUserRequest):
    return await repo.login(
        UserDTO(
            id=request.id,
            username=request.username,
            password=process_password(request.password),
            permission=request.permission
        )
    )
