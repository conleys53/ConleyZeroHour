# Conley ZeroHour
*Tired of Windows repeatedly nagging you about updates with overcomplicated tech jargon?*<br />

**Conley ZeroHour** simplifies down operating system security by detecting critical Windows vulnerabilities and using AI models to explain them in more simplistic, easy-to-understand language! Built for [nosu.io's "robhacks" hackathon](https://www.nosu.io/hackathons/robhacks), this tool automatically monitors for the newest security threats for Windows, fetching real-time data using Microsoft's MSRC API.

A **built-executable** of the program can be hypothetically configured to *run on startup*, allowing users to automatically scan for **critical** security flaws every single time they boot into their operating system, automatically closing once the scan is finished to save resources. This means that the latest vulnerabilities can be detected and explained in **real-time**, ensuring that users are both aware of and fully understand the newest vulnerabilities for their system **before they become a problem**. Clicking the vulnerability notifications launches the Window's Update panel, allowing for fast and seamless protection.

---

## The Reality of the Application
Let's be real—**Conley ZeroHour is far from perfect.** It relies on:<br />
<br />
❌ A **free** Gemini AI model, leading to *delays, failures, and unreliable summarization attempts*.<br />
❌ **Janky web scraping**, which is a considerably unstable way to fetch data from websites.<br />
❌ **Spaghetti code**, patched together during the past 24 hours with more of a focus of actually building as opposed to running efficiently.<br />
<br />
Despite these limitations, this program is designed to be a **proof-of-concept**: <br />

💡**AI should be used to simplify technology** for users, not make it considerably more complicated.

### Why This Concept Matters
As computers get more sophisticated, the knowledge gap gets *further and further*. Most users have no idea **what a CVE is**, or why a **zero-day exploit** is dangerous. AI-powered simplification can:<br />
<br />
✅**Help children and elderly users** understand security risks on their devices.<br />
✅**Inform non-technical users** about the security of their devices and encourage informed update decisions.<br />
✅**Improve tech support and business communication** by reducing workload and clarifying issues for customers.<br />
<br />

This places AI in a fantastic position for ensuring the continued future of **Accessibility!**
AI could easily **translate complex errors** in to common language, explaining:<br />
<br />
✅**Why an issue occurred and exactly how to fix and prevent it.**<br />
✅**Performance tweaks for computers, recommendations for hardware upgrades.**<br />
✅**How to troubleshoot issues based on your experience level or age.**<br />
<br />

Although **Conley ZeroHour** remains a *prototype* of these types of systems, it highlights exactly how AI can **make technology much clearer, more accessible, and user-friendly for everyone**.


## Features
- Automatic detection of user's current Windows version and build
- Fetches security updates from MSRC API
- Identifies the most pressing, dangerous vulnerabilities for your version
- Pulls CVE descriptions via OpenCVE scraping for context
- Notifications for critical/important security risks
- Clicking notifications open Windows Update panel
- Log ensures that same insecurities aren't shown repeatedly
- **THIS PROGRAM IS A WORK IN PROGRESS, IT IS NOT COMPLETE.**

## Installation
1. Clone the repository:<br />
*git clone https://github.com/conleys53/ConleyZeroHour.git*<br />
*cd ConleyZeroHour/src*

2. Install dependencies:<br />
*pip install -r requirements.txt*

3. Acquire Google API key:<br />
Go to the [Google AI Studio](https://aistudio.google.com/welcome) and generate a Gemini API key. Copy this key and paste it into *src/api.txt*.

4. Build .exe:<br />
*python setup.py build*

5. Run Conley ZeroHour:<br />
The compiled .exe will be located in: *build/exe.win-amd64-3.10/*


## Requirements (pip install -r requirements.txt while in directory`)
- Python 3.x
- requests
- beautifulsoup4
- google-generativeai
- pywin32
- win10toast_click
- cx_Freeze
- More requirements listed as new features added.

## 📌 Dependencies & Attribution

This project utilizes the following third-party libraries and APIs:

- **[Google Gemini AI](https://ai.google.dev/)** – AI used to generate simplified descriptions of vulnerabilities.
- **[Microsoft MSRC API](https://github.com/microsoft/MSRC-Microsoft-Security-Updates-API)** – Used to pull Windows security updates.
- **[OpenCVE](https://www.opencve.io/)** – Scraped to find vulnerability details for context.
- **[win10toast_click](https://pypi.org/project/win10toast-click/)** – Windows notifications, along with click redirection support.
- **[Requests](https://docs.python-requests.org/en/latest/)** – Used for HTTP requests to APIs.
- **[BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/)** – Parses HTML for CVE scraping.
- **[cx_Freeze](https://pypi.org/project/cx-Freeze/)** – Used to convert the program into a headless executable.

All external libraries are used in accordance with their respective licenses.

## IMPORTANT NOTES AND DISCLAIMERS
1. **⚠️ This tool is still simply a proof of concept, not practical in it's current form!**
2. **⚠️ You must assign a Google Gemini API key before running the program!**
3. **⚠️ IMPORTANT: THE FIRST EXECUTION OF THE PROGRAM WILL DETECT CVE-2025-1594; THIS IS NOT LEGITIMATE, IT IS SIMPLY A DEMONSTRATION.⚠️**
