import re

def validation_ip(ipv4):
    try:
        ipv4_regex = r'^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$'
        return bool(re.match(ipv4_regex, ipv4))
    except Exception:
        return False

def validation_md5(md5):
    try:
        md5_regex = r'^[0-9a-fA-F]{32}$'
        return bool(re.match(md5_regex, md5))
    except Exception:
        return False