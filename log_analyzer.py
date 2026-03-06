import re
import sys
from collections import defaultdict

def analyze_log(log_file, threshold):
    failed_attempts = defaultdict(int)

    # Regex pattern to extract IP from failed SSH login attempts
    pattern = r"Failed password.*from (\d+\.\d+\.\d+\.\d+)"

    try:
        with open(log_file, "r") as file:
            for line in file:
                match = re.search(pattern, line)
                if match:
                    ip = match.group(1)
                    failed_attempts[ip] += 1
    except FileNotFoundError:
        print(f"Error: File '{log_file}' not found.")
        sys.exit(1)

    if not failed_attempts:
        print("No failed login attempts found.")
        return

    print("\n=== Possible Brute Force Attempts ===\n")

    detected = False
    for ip, count in failed_attempts.items():
        if count >= threshold:
            print(f"IP: {ip} | Failed Attempts: {count}")
            detected = True

    if not detected:
        print("No IP exceeded the threshold.")

    print("\n=== Top Failed Login Sources ===\n")

    sorted_ips = sorted(failed_attempts.items(), key=lambda x: x[1], reverse=True)

    for ip, count in sorted_ips[:5]:
        print(f"{ip} -> {count} attempts")

    print("\nAnalysis complete.\n")


def main():
    if len(sys.argv) < 2:
        print("Usage: python log_analyzer.py <logfile> [threshold]")
        sys.exit(1)

    log_file = sys.argv[1]
    threshold = int(sys.argv[2]) if len(sys.argv) > 2 else 5

    analyze_log(log_file, threshold)


if __name__ == "__main__":
    main()
