import re

def parse_log(log_line):
    pattern = r"Failed password for (invalid user )?(?P<user>\w+) from (?P<ip>\d+\.\d+\.\d+\.\d+)"
    match = re.search(pattern, log_line)

    if match:
        return {
            "user": match.group("user"),
            "ip": match.group("ip"),
            "status": "failed"
        }
    return None