from collections import defaultdict
from datetime import datetime

LOG_FILE = "auth.log"
FAILED_LOGIN_THRESHOLD = 5
TIME_WINDOW_MINUTES = 1

failed_attempts = defaultdict(list)

try:
    with open(LOG_FILE, "r") as file:
        for line in file:
            if "Failed password" in line and "from" in line:
                parts = line.split()

                ip = parts[parts.index("from") + 1]

                timestamp = " ".join(parts[:3])

                log_time = datetime.strptime(
                    f"2026 {timestamp}",
                    "%Y %b %d %H:%M:%S"
                )

                failed_attempts[ip].append(log_time)

except FileNotFoundError:
    print(f"ERROR: {LOG_FILE} was not found.")
    exit()

print("=== Security Log Analyzer ===")
print()

if not failed_attempts:
    print("No failed login attempts detected.")

else:
    print("Failed login attempts by IP:")
    print()

    for ip, timestamps in failed_attempts.items():

        total_attempts = len(timestamps)

        print(f"{ip}: {total_attempts} failed attempts")

        # Determine severity
        if total_attempts >= 10:
            severity = "HIGH"
        elif total_attempts >= 5:
            severity = "MEDIUM"
        else:
            severity = "LOW"

        print(f"  Severity: {severity}")

        # Check for brute-force activity
        for i in range(len(timestamps)):

            window_start = timestamps[i]
            count = 0

            for timestamp in timestamps[i:]:

                difference = (
                    timestamp - window_start
                ).total_seconds()

                if difference <= TIME_WINDOW_MINUTES * 60:
                    count += 1
                else:
                    break

            if count >= FAILED_LOGIN_THRESHOLD:

                print(
                    f"  ALERT: Possible brute-force activity from {ip}"
                )

                print(
                    f"  Detection: {count} attempts within "
                    f"{TIME_WINDOW_MINUTES} minute"
                )

                break

        print()
