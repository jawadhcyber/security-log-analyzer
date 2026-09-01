
Security Log Analyzer

A Python-based security log analyzer designed to identify failed login attempts, suspicious IP addresses, and possible brute-force activity.

This project demonstrates basic SOC Analyst and cybersecurity log-analysis skills.

Features

- Analyzes authentication logs
- Detects failed login attempts
- Extracts source IP addresses
- Counts failed login attempts by IP
- Detects possible brute-force activity
- Uses a time-based detection window
- Assigns LOW, MEDIUM, and HIGH severity levels
- Handles missing log files

Detection Logic

Failed Login Detection

The analyzer searches the log for failed SSH authentication attempts containing:

Failed password

Brute-Force Detection

The analyzer generates an alert when an IP address produces:

- 5 or more failed attempts
- Within 1 minute

Severity Levels

Failed Attempts| Severity
1–4| LOW
5–9| MEDIUM
10+| HIGH

Technologies Used

- Python 3
- File Handling
- "collections"
- "datetime"
- Log Analysis
- Basic Threat Detection

Project Structure

Security-Log-Analyzer/
│
├── README.md
├── auth.log
├── security_log_analyzer.py
└── security_log_analyzer_v2.py

Example Output

=== Security Log Analyzer ===

Failed login attempts by IP:

192.168.1.10: 5 failed attempts
  Severity: MEDIUM
  ALERT: Possible brute-force activity from 192.168.1.10
  Detection: 5 attempts within 1 minute

10.0.0.5: 1 failed attempts
  Severity: LOW

How It Works

1. The program opens the authentication log.
2. It searches for failed password attempts.
3. It extracts the source IP address.
4. It counts attempts from each IP.
5. It assigns a severity level.
6. It checks whether multiple attempts occurred within the detection window.
7. It generates an alert for possible brute-force activity.

Skills Demonstrated

- Security log analysis
- Authentication-event monitoring
- IP address analysis
- Brute-force detection
- Basic threat detection
- Python scripting
- SOC fundamentals

Future Improvements

- Add CSV report generation
- Add more authentication-event types
- Add username analysis
- Add configurable detection thresholds
- Add a graphical dashboard
- Add automated security reports
- Add support for additional log formats

Disclaimer

This project is for educational and cybersecurity learning purposes. The included "auth.log" contains sample data created for testing and does not contain real security logs.
