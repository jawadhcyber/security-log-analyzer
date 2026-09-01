from collections import Counter

LOG_FILE = "auth.log"
FAILED_LOGIN_THRESHOLD = 5

failed_attempts = Counter()

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" in line:
                parts = line.split()

                if "from" in parts:
                    ip = parts[parts.index("from") + 1]
                    failed_attempts[ip] += 1

except FileNotFoundError:
    print(f"Error: {LOG_FILE} was not found.")
    exit()

print("=== Security Log Analyzer ===")
print()

if not failed_attempts:
    print("No failed login attempts detected.")
else:
    print("Failed login attempts by IP:")

    for ip, count in failed_attempts.items():
        print(f"{ip}: {count} failed attempts")

        if count >= FAILED_LOGIN_THRESHOLD:
            print(f"  ALERT: Possible brute-force activity from {ip}")
