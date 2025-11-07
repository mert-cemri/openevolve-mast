import subprocess
def get_system_uptime():
    """
    Get the current system uptime.
    """
    uptime_str = subprocess.check_output(["uptime"])
    return uptime_str.decode("utf-8").strip()