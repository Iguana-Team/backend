from fastapi import APIRouter
from src.schema.ai import StaffPublicRequest
from src.dto.staff_public_dto import StaffPublicDTO
from src.adapter.sql.repo.ai import AIModelRepository
from src.adapter.sql.session import Database
from typing import List 
router = APIRouter(prefix="/ai", tags=["AI"])
repo = AIModelRepository(Database().session)


@router.post("staff")
async def match_staff(request: StaffPublicRequest) -> list:
    tmp = await repo.match_staff(
        StaffPublicDTO(
            id=request.id,
            func_block=request.func_block,
            division1=request.division1,
            division2=request.division2,
            division3=request.division3,
            division4=request.division4,
            post=request.post,
            role=request.role,
            lname=request.lname,
            fname=request.fname
        )
    )

    res = []
    for staff in tmp:
        res += [staff.to_dict()]
    return res
