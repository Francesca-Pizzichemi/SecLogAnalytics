from database import (
    connect_database,
    create_table,
    import_log,
    get_total_events,
    get_failed_logins_by_ip,
    get_failed_logins_by_user,
    get_login_count,
    get_failed_events
)

from detector import detect_brute_force


print("SecLog Analytics started")


# --------------------------------------------------
# DATABASE
# --------------------------------------------------

connection = connect_database()
cursor = connection.cursor()

create_table(cursor)

import_log(cursor, "security.log")

connection.commit()


# --------------------------------------------------
# REPORT
# --------------------------------------------------

print("\n==============================")
print("     SECLOG ANALYTICS")
print("==============================")


total_events = get_total_events(cursor)

print(f"\nTotal security events: {total_events}")


# Failed logins by IP

print("\nFailed login attempts by IP:")

failed_by_ip = get_failed_logins_by_ip(cursor)

for ip_address, failed_attempts in failed_by_ip:

    print(
        f"{ip_address}: "
        f"{failed_attempts} failed attempts"
    )


# Most targeted users

print("\nMost targeted users:")

failed_by_user = get_failed_logins_by_user(cursor)

for username, failed_attempts in failed_by_user:

    print(
        f"{username}: "
        f"{failed_attempts} failed attempts"
    )


successful_logins = get_login_count(
    cursor,
    "LOGIN_SUCCESS"
)

failed_logins = get_login_count(
    cursor,
    "LOGIN_FAILED"
)

print(f"\nSuccessful logins: {successful_logins}")
print(f"Failed logins: {failed_logins}")


# --------------------------------------------------
# THREAT DETECTION
# --------------------------------------------------

print("\n==============================")
print("       THREAT DETECTION")
print("==============================")


failed_events = get_failed_events(cursor)

threats = detect_brute_force(failed_events)


if threats:

    for threat in threats:

        print(
            f"\n[{threat['risk']}] "
            f"BRUTE-FORCE ATTACK DETECTED"
        )

        print(
            f"Source IP: "
            f"{threat['ip_address']}"
        )

        print(
            f"Target user: "
            f"{threat['username']}"
        )

        print(
            f"Failed attempts: "
            f"{threat['attempts']}"
        )

        print(
            f"Time window: "
            f"{threat['time_window']:.0f} seconds"
        )

else:
    print("\nNo brute-force attacks detected.")


# --------------------------------------------------
# SUMMARY
# --------------------------------------------------

print("\n==============================")
print("          SUMMARY")
print("==============================")

print(f"Events analyzed: {total_events}")
print(f"Threats detected: {len(threats)}")


connection.close()

print("\nAnalysis completed.")