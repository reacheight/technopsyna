from datetime import datetime
from technopsyna.config import update_delete_user_time, user_delete_time


class UserHeap:
    def __init__(self):
        self.last_check = datetime.now()
        self.table = {}

    def add(self, user_id: int) -> None:
        self.table[user_id] = datetime.now()

    def delete(self, user_id: int) -> None:
        self.table.pop(user_id, None)

    def is_check_time(self) -> bool:
        return datetime.now() - self.last_check >= update_delete_user_time

    def check(self) -> list:
        deletes = []
        for user_id, time in list(self.table.items()):
            # we make copy,
            # because we delete keys from this dict where iter for this dict
            if datetime.now() - time >= user_delete_time:
                deletes.append(user_id)
                self.table.pop(user_id, None)

        self.last_check = datetime.now()
        return deletes
