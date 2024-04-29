import sys
from abc import ABC, abstractmethod
import re

class SSHLogEntry(ABC):
    def __init__(self, log_entry):
        self.log_entry = log_entry
        self.time = None
        self.host_name = None
        self._raw_content = None
        self.pid = None
        self.parse_log_entry()

    def parse_log_entry(self):
        regex_pattern = r'(\w{3}\s+\d{1,2}\s\d{2}:\d{2}:\d{2}) (\w+) sshd\[(\d+)\]: (.*)'
        match = re.match(regex_pattern, self.log_entry)
        if match:
            self.time = match.group(1)
            self.host_name = match.group(2)
            self._raw_content = match.group(4)
            self.pid = match.group(3)

    @property
    def get_raw_content(self):
        return self._raw_content

    @abstractmethod
    def validate(self):
        pass

    @property
    def has_ip(self):
        ip_pattern = r'\b(?:\d{1,3}\.){3}\d{1,3}\b'  # IP pattern
        return bool(re.search(ip_pattern, self._raw_content))

    # >, <, ==, repr methods
    def __repr__(self):
        return f"SSHLogEntry(log_entry='{self.log_entry}')"

    def __eq__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.log_entry == other.log_entry
        return False

    def __lt__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.time < other.time
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, SSHLogEntry):
            return self.time > other.time
        return NotImplemented


class PasswordRejected(SSHLogEntry):
    def __init__(self, log_entry):
        super().__init__(log_entry)

    def validate(self):
        return "Failed password" in self._raw_content

class PasswordAccepted(SSHLogEntry):
    def __init__(self, log_entry):
        super().__init__(log_entry)

    def validate(self):
        return "Accepted password" in self._raw_content

class ErrorLog(SSHLogEntry):
    def __init__(self, log_entry):
        super().__init__(log_entry)

    def validate(self):
        return "error" in self._raw_content.lower()

class CustomLog(SSHLogEntry):
    def __init__(self, log_entry):
        super().__init__(log_entry)

    def validate(self):
        return True

if __name__ == "__main__":
    for line in sys.stdin:

        rejected_log = PasswordRejected(line)
        accepted_log = PasswordAccepted(line)
        error_log = ErrorLog(line)
        custom_log = CustomLog(line)


        # print(rejected_log.has_ip)
        # print(rejected_log.get_raw_content)
        # print(accepted_log.validate())
        # print(error_log.validate())
        # print(custom_log.validate())
