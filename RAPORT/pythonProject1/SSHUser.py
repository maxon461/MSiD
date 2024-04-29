from datetime import datetime

class SSHUser:
    def __init__(self, username: str, last_login: datetime):
        self.username = username
        self.last_login = last_login

    def validate(self) -> bool:

        if len(self.username) >= 4:
            return True
        else:
            return False

class SSHLogEntry:
    def __init__(self, log_entry: str):
        self.log_entry = log_entry

class PasswordRejected(SSHLogEntry):
    pass

class SSHLogJournal:
    def __init__(self):
        self.entries = []

    def append(self, log_entry: SSHLogEntry):
        self.entries.append(log_entry)

if __name__ == "__main__":

    journal = SSHLogJournal()


    journal.append(PasswordRejected("Dec 10 06:55:46 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186"))


    users = [
        SSHUser("user1", datetime(2023, 1, 1)),
        SSHUser("user2", datetime(2023, 1, 2)),
        SSHUser("user3", datetime(2023, 1, 3))
    ]


    all_objects = journal.entries + users


    for obj in all_objects:
        if isinstance(obj, SSHUser):
            print(f"User '{obj.username}' validation result: {obj.validate()}")
        elif isinstance(obj, SSHLogEntry):
            print("SSHLogEntry object.")
        else:
            print("Unknown object type.")
