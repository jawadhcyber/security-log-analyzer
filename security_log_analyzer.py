from collections import Counter
import csv

LOG_FILE = "auth.log"
REPORT_FILE = "security_report.csv"
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
    print()

    for ip, count in failed_attempts.items():
        print(f"{ip}: {count} failed attempts")

        if count >= FAILED_LOGIN_THRESHOLD:
            print(f"  ALERT: Possible brute-force activity from {ip}")

# Create security report CSV
with open(REPORT_FILE, "w", newline="") as csvfile:
    writer = csv.writer(csvfile)

    writer.writerow(["IP Address", "Failed Attempts", "Status"])

    for ip, count in failed_attempts.items():
        if count >= FAILED_LOGIN_THRESHOLD:
            status = "Possible Brute-Force Activity"
        else:
            status = "Normal"

        writer.writerow([ip, count, status])

print()
print(f"Security report saved to {REPORT_FILE}")
