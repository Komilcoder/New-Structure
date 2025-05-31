import asyncio
from typing import List, Optional

from app.models.user import User, UserCreate, UserUpdate  # Model va schemas import qilinadi
from app.database import get_user_db  # Foydalanuvchi uchun DB funksiyasi

class UserService:
    def __init__(self, db):
        self.db = db

    # Yangi foydalanuvchi yaratish
    async def create_user(self, user_create: UserCreate) -> User:
        user = await self.db.create(user_create)
        return user

    # Foydalanuvchini ID orqali olish
    async def get_user(self, user_id: int) -> Optional[User]:
        user = await self.db.get(user_id)
        return user

    # Barcha foydalanuvchilarni olish
    async def get_all_users(self) -> List[User]:
        users = await self.db.get_all()
        return users

    # Foydalanuvchini yangilash
    async def update_user(self, user_id: int, user_update: UserUpdate) -> Optional[User]:
        user = await self.db.update(user_id, user_update)
        return user

    # Foydalanuvchini o'chirish
    async def delete_user(self, user_id: int) -> bool:
        result = await self.db.delete(user_id)
        return result

# UserService obyektini yaratish uchun yordamchi funksiya
async def get_user_service():
    db = await get_user_db()
    return UserService(db)