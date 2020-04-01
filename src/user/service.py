from typing import List

from src import cache
from src.models.user import User
from src.user.repository import UserRepository
from src.utils.utils import cache_key_generator


class UserService:
    def __init__(self):
        self.user_repository = UserRepository()

    @cache.cached(timeout=300, key_fn=cache_key_generator)
    def get_user_from_id(self, id: int) -> User:
        """
        Cached as the user details aren't currently editable. If it becomes editable in the future then purging would be
        handled by the save_user method
        """
        return self.user_repository.get_user_from_id(id)

    @cache.cached(timeout=300, key_fn=cache_key_generator)
    def get_user_from_username(self, username: str) -> User:
        """
        Cached as the user details aren't currently editable. If it becomes editable in the future then purging would be
        handled by the save_user method
        """
        return self.user_repository.get_user_from_username(username)

    def get_users_from_ids(self, ids: List[int]):
        ids_mapping = {}
        for id in ids:
            user = self.get_user_from_id(id)
            ids_mapping[id] = user
        return ids_mapping

    def get_all_users(self) -> List:
        return self.user_repository.get_all_users()

    def save_user(self):
        raise NotImplementedError
