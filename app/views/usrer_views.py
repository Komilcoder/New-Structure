from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from app.schemas.user import UserCreate
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
    

  

