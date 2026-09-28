SecLog Analytics is a Python-based security log analysis tool that stores authentication events in a SQLite database, analyzes them using SQL, and detects suspicious login activity such as potential brute-force attacks.
The project was developed as a practical exercise in Python, SQL, SQLite, log analysis, and basic cybersecurity threat detection.



Features
- Parses authentication events from a security log file
- Stores security events in a SQLite database
- Prevents duplicate event insertion
- Counts successful and failed login attempts
- Groups failed login attempts by IP address
- Identifies the most targeted user accounts
- Detects potential brute-force attacks
- Uses configurable time-based detection rules
- Generates a command-line security report
