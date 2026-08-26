from datetime import datetime


BRUTE_FORCE_THRESHOLD = 5
TIME_WINDOW_SECONDS = 60


def detect_brute_force(failed_events):

    login_groups = {}

    for timestamp_text, username, ip_address in failed_events:

        key = (ip_address, username)

        if key not in login_groups:
            login_groups[key] = []

        timestamp = datetime.fromisoformat(timestamp_text)

        login_groups[key].append(timestamp)

    threats = []

    for (ip_address, username), timestamps in login_groups.items():

        for start in range(len(timestamps)):

            end = start + BRUTE_FORCE_THRESHOLD - 1

            if end >= len(timestamps):
                break

            time_difference = (
                timestamps[end] - timestamps[start]
            ).total_seconds()

            if time_difference <= TIME_WINDOW_SECONDS:

                threat = {
                    "type": "BRUTE_FORCE",
                    "risk": "HIGH",
                    "ip_address": ip_address,
                    "username": username,
                    "attempts": BRUTE_FORCE_THRESHOLD,
                    "time_window": time_difference
                }

                threats.append(threat)

                break

    return threats