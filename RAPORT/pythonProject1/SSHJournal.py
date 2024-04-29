import sys

from SSHLogEntry import *
class SSHLogJournal:
    def __init__(self):
        self.entries = []

    def __len__(self):
        return len(self.entries)

    def __iter__(self):
        return iter(self.entries)

    def __contains__(self, item):
        return item in self.entries

    def append(self, log_entry_str):
        if isinstance(log_entry_str, str):
            log_entry = None
            if "Failed password" in log_entry_str:
                log_entry = PasswordRejected(log_entry_str)
            elif "Accepted password" in log_entry_str:
                log_entry = PasswordAccepted(log_entry_str)
            elif "error" in log_entry_str.lower():
                log_entry = ErrorLog(log_entry_str)
            else:
                log_entry = CustomLog(log_entry_str)

            if log_entry.validate():
                self.entries.append(log_entry)
        else:
            print("Invalid log entry format.")

    def get_logs_by_criteria(self, criteria):
        filtered_logs = []
        for entry in self.entries:
            if criteria(entry):
                filtered_logs.append(entry)
        return filtered_logs


if __name__ == "__main__":

    journal = SSHLogJournal()


    for line in sys.stdin:
        journal.append(line.strip())


    print("Liczba wpisów w dzienniku:", len(journal))


    print("Wpisy w dzienniku:")
    for entry in journal:
        print(entry)


    print("Czy określony wpis jest w dzienniku?")
    test_entry = PasswordRejected("Dec 10 06:55:46 LabSZ sshd[24200]: Failed password for invalid user webmaster from 173.234.31.186")
    print(test_entry in journal)


    print("Filtrowanie wpisów w dzienniku:")
    filtered_logs = journal.get_logs_by_criteria(lambda entry: "183" in entry.get_raw_content)
    for entry in filtered_logs:
        print(entry)
