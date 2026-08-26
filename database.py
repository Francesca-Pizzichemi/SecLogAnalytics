import sqlite3


def connect_database():
    return sqlite3.connect("security.db")


def create_table(cursor):
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS security_events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        timestamp TEXT NOT NULL,
        event_type TEXT NOT NULL,
        username TEXT NOT NULL,
        ip_address TEXT NOT NULL,

        UNIQUE(timestamp, event_type, username, ip_address)
    )
    """)


def import_log(cursor, log_file_path):
    with open(log_file_path, "r") as log_file:

        for line in log_file:
            line = line.strip()

            if not line:
                continue

            parts = line.split()

            timestamp = parts[0]
            event_type = parts[1]
            username = parts[2].split("=")[1]
            ip_address = parts[3].split("=")[1]

            cursor.execute("""
            INSERT OR IGNORE INTO security_events (
                timestamp,
                event_type,
                username,
                ip_address
            )
            VALUES (?, ?, ?, ?)
            """, (
                timestamp,
                event_type,
                username,
                ip_address
            ))


def get_total_events(cursor):
    cursor.execute("""
    SELECT COUNT(*)
    FROM security_events
    """)

    return cursor.fetchone()[0]


def get_failed_logins_by_ip(cursor):
    cursor.execute("""
    SELECT
        ip_address,
        COUNT(*) AS failed_attempts
    FROM security_events
    WHERE event_type = 'LOGIN_FAILED'
    GROUP BY ip_address
    ORDER BY failed_attempts DESC
    """)

    return cursor.fetchall()


def get_failed_logins_by_user(cursor):
    cursor.execute("""
    SELECT
        username,
        COUNT(*) AS failed_attempts
    FROM security_events
    WHERE event_type = 'LOGIN_FAILED'
    GROUP BY username
    ORDER BY failed_attempts DESC
    """)

    return cursor.fetchall()


def get_login_count(cursor, event_type):
    cursor.execute("""
    SELECT COUNT(*)
    FROM security_events
    WHERE event_type = ?
    """, (event_type,))

    return cursor.fetchone()[0]


def get_failed_events(cursor):
    cursor.execute("""
    SELECT
        timestamp,
        username,
        ip_address
    FROM security_events
    WHERE event_type = 'LOGIN_FAILED'
    ORDER BY ip_address, username, timestamp
    """)

    return cursor.fetchall()