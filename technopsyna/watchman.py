from datetime import datetime


class Watchman:
    def __init__(self, user_ttl):
        self.user_ttl = user_ttl
        self.users = {}

    def add(self, user_id: int) -> None:
        self.users[user_id] = datetime.now()

    def delete(self, user_id: int) -> None:
        self.users.pop(user_id, None)

    def get_users_to_kick(self):
        for user_id, time in list(self.users.items()):
            if datetime.now() - time >= self.user_ttl:
                self.users.pop(user_id, None)
                yield user_id
