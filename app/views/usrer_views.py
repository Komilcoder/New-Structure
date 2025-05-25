from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.user_schema import UserCreate, UserRead, UserUpdate
from app.services.user_service import UserService
from app.repository.user_repository import UserRepository
from app.database import get_db
from sqlalchemy.exynt.asyncio import AsyncSession

router = APIRouter(
    prefix="/users",
    tags=["users"]
)

class UserView:
    def __init__(self, service: UserService = Depends()):
        self.service = service

    async def get_service(self, db:AsyncSession) -> UserService:
        return UserService(UserRepository(db))
    
    async def create_user(self, user: UserCreate, db: AsyncSession = Depends(get_db)):
        service = await self.get_service(db)
        return await service.create_user(user) 
    

  

user_view = UserView()

router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)(user_view.create_user)
router.get("/", response_model=List[UserRead])(user_view.get_users)
router.get("/{user_id}", response_model=UserRead)(user_view.get_user)
router.put("/{user_id}", response_model=UserRead)(user_view.update_user)
router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT)(user_view.delete_user)