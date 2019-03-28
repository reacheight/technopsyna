from datetime import datetime, timedelta


class UserHeap:
    def __init__(self):
        self.table = {}

    def add(self, user_id: int) -> None:
        self.table[user_id] = datetime.now()

    def delete(self, user_id: int) -> None:
        if self.table.get(user_id):
            del self.table[user_id]

    def check(self) -> list:
        deletes = []
        for user_id, time in list(self.table.values()):
            if datetime.now() - time >= timedelta(seconds=20):
                deletes.append(user_id)
                del self.table[user_id]

        return deletes
