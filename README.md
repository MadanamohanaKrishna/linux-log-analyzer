# Linux Log Analyzer

A Python-based cybersecurity tool that scans Linux authentication logs and detects potential SSH brute-force attacks.

## Features
- Detects repeated failed SSH login attempts
- Identifies suspicious IP addresses
- Adjustable detection threshold
- Reports top attack sources

## Usage

python log_analyzer.py auth.log 5

## Example Output

Possible Brute Force Attempts:

IP: 192.168.1.25 | Failed Attempts: 6

Top Failed Login Sources:
192.168.1.25 -> 6 attempts
10.0.0.3 -> 3 attempts

## Technologies
Python, Regex, Log Analysis

## Use Case
Helps system administrators and security analysts quickly identify brute-force SSH attacks from authentication logs.
