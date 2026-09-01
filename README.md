Security Log Analyzer

A beginner-friendly Python cybersecurity project that analyzes authentication logs, detects failed login attempts, identifies possible brute-force activity, and generates a CSV security report.

Features

- Reads security log files
- Detects failed login attempts
- Extracts source IP addresses
- Counts failed login attempts by IP
- Detects possible brute-force activity
- Assigns risk levels: LOW, MEDIUM, and HIGH
- Generates a security report
- Exports results to CSV
- Demonstrates basic SOC analyst skills

Project Files

- "security analyzer.py" — Main Python security log analyzer
- "auth.log" — Sample authentication security log
- "security_report.csv" — Generated security analysis report

Example Output

The analyzer checks the authentication log for failed login attempts and groups them by source IP address.

When an IP address reaches 5 or more failed login attempts, the analyzer generates an alert for possible brute-force activity.

The CSV report includes:

- IP Address
- Failed Attempts
- Risk Level
- Status

Skills Demonstrated

- Python
- Log analysis
- Authentication monitoring
- IP address analysis
- Brute-force detection
- CSV reporting
- Cybersecurity fundamentals
- Basic SOC analysis

How It Works

1. The program reads "auth.log".
2. It searches for failed login attempts.
3. Source IP addresses are extracted.
4. Failed attempts are counted by IP.
5. Risk levels are assigned based on the number of failed attempts.
6. Possible brute-force activity is identified.
7. Results are saved to "security_report.csv".

Future Improvements

- Add timestamp analysis
- Detect additional suspicious authentication patterns
- Add automatic alerting
- Build a simple SOC dashboard
- Support additional log formats

Author

Jawad Hussain
