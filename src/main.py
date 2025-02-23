import requests
import json
import platform
from datetime import datetime, timedelta
from plyer import notification
from cve_scraper import get_cve_description

#I SHOULD OF ORGANIZED THIS ENTIRE THING CONSIDERABLY BETTER.

DAYS_BACK = 7  # check past 7 days for security updates
MSRC_API_URL = "https://api.msrc.microsoft.com/cvrf/v2.0/updates"
NOTIFIED_VULNS_FILE = "notified_vulnerabilities.json"

def get_windows_version():
    version = platform.version()
    build = platform.win32_ver()[1]
    release = platform.release()

    if release == "10":
        full_version = f"Windows 10 (Build: {build})"
    elif release == "11":
        full_version = f"Windows 11 {platform.win32_ver()[0]} (Build: {build})"
    else:
        full_version = f"Windows {release} (Build: {build})"

    print(f"Current OS: {full_version}")
    return full_version, build

def fetch_security_updates():
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        response = requests.get(MSRC_API_URL, headers=headers)
        response.raise_for_status()
        data = response.json()

        # filter updates by date
        cutoff_date = datetime.utcnow() - timedelta(days=DAYS_BACK)
        filtered_updates = []

        for update in data.get("value", []):
            release_date_str = update.get("CurrentReleaseDate", "")
            if release_date_str:
                release_date = datetime.strptime(release_date_str, "%Y-%m-%dT%H:%M:%SZ")
                if release_date >= cutoff_date:
                    filtered_updates.append(update)

        print(f"Fetched {len(filtered_updates)} security updates from the past {DAYS_BACK} days.\n")
        return filtered_updates

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching MSRC updates: {e}")
        return []

def fetch_cvrf_severity(cvrf_url):
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    try:
        response = requests.get(cvrf_url, headers=headers)
        response.raise_for_status()
        data = response.json()

        vulnerabilities = data.get("Vulnerability", [])
        highest_severity = "Unknown"

        for vuln in vulnerabilities:
            threats = vuln.get("Threats", [])
            for threat in threats:
                if "Description" in threat:
                    severity = threat["Description"].get("Value", "Unknown")
                    if severity in ["Critical", "Important"]:  # prioritize critical threats
                        highest_severity = severity

        return highest_severity

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Error fetching CVRF file: {e}")
        return "Unknown"

def load_notified_vulnerabilities():
    try:
        with open(NOTIFIED_VULNS_FILE, "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return {}

def save_notified_vulnerabilities(vulnerabilities):
    with open(NOTIFIED_VULNS_FILE, "w") as f:
        json.dump(vulnerabilities, f)

def check_critical_vulnerabilities():
    windows_version, build_number = get_windows_version()
    updates = fetch_security_updates()
    notified_vulns = load_notified_vulnerabilities()
    critical_issues = {}

    if not updates:
        print("No security updates found.\n")
        return

    for update in updates:
        cvrf_url = update.get("CvrfUrl", "")

        if not cvrf_url:
            print(f"⚠️ No CVRF URL for {update.get('DocumentTitle', 'Unknown Title')}.")
            continue

        severity = fetch_cvrf_severity(cvrf_url)
        print(f"🔍 Checking: {update.get('DocumentTitle', 'Unknown Title')} (Severity: {severity})")

        if severity in ["Critical", "Important"]:
            cve_id = update.get("ID", "Unknown CVE")
            if cve_id not in notified_vulns:
                description = get_cve_description(cve_id)  # fetch simplified description
                critical_issues[cve_id] = description
                notified_vulns[cve_id] = severity  # mark it as notified

    if critical_issues:
        notify_user(windows_version, critical_issues)
        save_notified_vulnerabilities(notified_vulns)

def notify_user(windows_version, critical_issues):
    for cve_id, description in critical_issues.items():
        max_length = 250 - len(cve_id) - 2
        if len(description) > max_length:
            description = description[:max_length] + "..."  # notifications apparently have 250 or so max characters

        message = f"{cve_id}: {description}"
        notification.notify(
            title="⚠️ Windows Security Alert",
            message=message,
            app_name="Conley ZeroHour",
            timeout=10
        )
        print(f"ALERT: {message}")

if __name__ == "__main__":
    check_critical_vulnerabilities()