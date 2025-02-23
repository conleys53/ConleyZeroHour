# Conley ZeroHour
*Tired of Windows repeatedly nagging you about updates with overcomplicated tech jargon?*<br />

**Conley ZeroHour** simplifies operating system security by detecting Windows vulnerabilities and using AI to explain them in plain, easy-to-understand language! Built for nosu.io's "robhacks" hackathon, this tool passively monitors your system in the background for the newest security threats, fetching real-time data using Microsoft's MSRC API.

## Features
- Automatic detection of user's current Windows version and build
- Fetches security updates from MSRC API
- Identifies the most pressing, dangerous vulnerabilities for your version
- Pulls CVE descriptions via OpenCVE scraping for context
- Notifications for critical/important security risks
- **THIS PROGRAM IS A WORK IN PROGRESS, IT IS NOT COMPLETE.**

## Installation
1. Clone the repository:
git clone https://github.com/conleys53/ConleyZeroHour.git 

2. CD to the downloaded directory:
*cd ConleyZeroHour*

2. Install dependencies:
*pip install -r requirements.txt*

## Usage
Run the program:
*python src/main.py*

## Requirements (pip install -r requirements.txt while in directory`)
- Python 3.x
- `requests`
- `plyer`
- `beautifulsoup4`
- More requirements listed as new features added.

**⚠️ Disclaimer: This tool is still simply a proof of concept, not a replacement for Windows security!**
