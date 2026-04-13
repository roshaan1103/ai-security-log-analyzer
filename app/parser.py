import re


def parse_log(log_line):
    pattern = r"(?P<timestamp>\w+ \d+ \d+:\d+:\d+).*sshd.*: (?P<status>Failed|Accepted) password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"

    match = re.search(pattern, log_line)

    if match:
        return {
            "timestamp": match.group("timestamp"),
            "user": match.group("user"),
            "ip": match.group("ip"),
            "status": match.group("status").lower()
        }
    return None