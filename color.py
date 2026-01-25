"""
color model
"""

# Color code ANSI
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
RESET = "\033[0m"

def print_success(message):
    """print message in green"""
    print(f"{GREEN} {message} {RESET}")

def print_error(message):
    """print message in red"""
    print(f"{RED} {message} {RESET}")

def print_result(message):
    """print result in blue"""
    print(f"{BLUE} {message} {RESET}")

