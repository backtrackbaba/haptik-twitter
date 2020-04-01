from typing import List

from src.models.user import User


class UserRepository:

    def get_user_from_id(self, id) -> User:
        return User.query.filter_by(id=id).first_or_404()

    def get_user_from_username(self, username) -> User:
        return User.query.filter_by(username=username).first_or_404()

    def get_all_users(self) -> List:
        return User.query.all()
