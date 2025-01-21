from typing import Optional
from fastapi import HTTPException, status

from models.user import User as UserModel
from models.user import Rol as RolModel
from schemas.user import User as UserScheme
from config.configuration import PWD_ADMIN, PWD_CONTEXT, ROLES


class UserService():
    """Class for management User Model."""

    def __init__(self, db) -> None:
        self.db = db

    @classmethod
    def initial_migration(cls, db) -> None:
        """Function for create user management if not exist'

        Args:
            db (_type_): _description_
        """
        # Create roles
        for rol_name in ROLES:
            role_db = db.query(RolModel).filter(
                RolModel.name == rol_name).first()
            if not role_db:
                role_db = RolModel(name=rol_name)
                db.add(role_db)
                db.commit()
                db.refresh(role_db)

        # Check if admin user exists
        admin_user = db.query(UserModel).filter(
            UserModel.username == "admin").first()
        if not admin_user:
            hashed_password = PWD_CONTEXT.hash(PWD_ADMIN)
            admin_user = UserModel(
                username="admin", 
                password=hashed_password,
                rol_id=1)
            db.add(admin_user)
            db.commit()
            db.close()

    def get_user(self, username: str) -> UserModel:
        """Method for get user using username."""
        result = self.db.query(UserModel).filter(
            UserModel.username == username).first()
        return result
            
    def validate_user(self, username: str, password: str) -> Optional[UserModel]:
        """Method for validate user in login."""
        result = self.db.query(UserModel).filter(
            UserModel.username == username).first()
        if result:
            is_valid_pwd = PWD_CONTEXT.verify(password, result.password)
            if is_valid_pwd:
                return result

    def create_user(self, user: UserScheme) -> UserModel:
        """Method for create user in model db."""
        user_db = self.db.query(UserModel).filter(
            UserModel.username == user.username).first()
        if user_db:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Username already exist!",
            )

        user.password = PWD_CONTEXT.hash(user.password)
        new_user = UserModel(**user.dict())
        self.db.add(new_user)
        self.db.commit()
        return new_user
