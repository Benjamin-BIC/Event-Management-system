from typing import List, Optional
from schemas.user import User, UserCreate


class UserService:
    def __init__(self):
        self.users_db = []
        self.next_id = 1

    def create_user(self, user: UserCreate) -> User:
        db_user = User(id=self.next_id, **user.model_dump())
        self.users_db.append(db_user)
        self.next_id += 1
        return db_user

    def get_user(self, user_id: int) -> Optional[User]:
        for user in self.users_db:
            if user.id == user_id:
                return user
        return None

    def get_users(self) -> List[User]:
        return self.users_db

    def update_user(self, user_id: int, user: UserCreate) -> Optional[User]:
        for i, user in enumerate(self.users_db):
            if user.id == user_id:
                updated_user = user.model_copy(update=user.model_dump())
                self.users_db[i] = updated_user
                return updated_user
        return None
    
    def delete_user(self, user_id: int) -> bool:
        initial_len = len(self.users_db)
        self.users_db = [user for user in self.users_db if user.id != user_id]
        return len(self.users_db) != initial_len
    
user_service = UserService()