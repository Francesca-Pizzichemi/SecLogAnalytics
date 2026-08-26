*# SecLog Analytics*



*SecLog Analytics is a Python-based security log analysis tool that stores authentication events in a SQLite database, analyzes them using SQL, and detects suspicious login activity such as potential brute-force attacks.*



*The project was developed as a practical exercise in Python, SQL, SQLite, log analysis, and basic cybersecurity threat detection.*



*## Features*



*- Parses authentication events from a security log file*

*- Stores security events in a SQLite database*

*- Prevents duplicate event insertion*

*- Counts successful and failed login attempts*

*- Groups failed login attempts by IP address*

*- Identifies the most targeted user accounts*

*- Detects potential brute-force attacks*

*- Uses configurable time-based detection rules*

*- Generates a command-line security report*





*## Project Structure*



*```text*

*SecLogAnalytics/*

*│*

*├── main.py*

*├── database.py*

*├── detector.py*

*├── security.log*

*├── .gitignore*

*└── README.md*

*main.py*



*Coordinates the application workflow and generates the final security report.*



*database.py*



*Handles:*



*SQLite database connection*

*table creation*

*log event insertion*

*SQL queries*

*security statistics*

*detector.py*



*Contains the threat detection logic used to identify suspicious authentication activity.*



*security.log*



*Contains synthetic sample authentication events used to demonstrate and test the application.*



*Detection Logic*


*The current version detects a potential brute-force attack when:*

*the same source IP address*

*targets the same user account*

*with at least 5 failed login attempts*

*within 60 seconds*

*SQL Analysis*

*Security events are stored in a SQLite database and analyzed using SQL queries.*



