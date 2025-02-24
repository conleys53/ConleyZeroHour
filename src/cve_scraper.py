import requests
import time
import google.generativeai as genai

API_KEY_FILE = "api.txt"

def get_api_key():

    try:
        with open(API_KEY_FILE, "r") as f:
            return f.read().strip()
    except FileNotFoundError:
        return None

def get_cve_description(cve_id, api_key):
    url = f"https://app.opencve.io/cve/{cve_id}"
    print(f"Fetching: {url}")

    response = requests.get(url)
    if response.status_code != 200:
        print(f"⚠️ Request failed: {response.status_code} {response.reason}")
        return "⚠️ No description found."

    # extract CVE description from OpenCVE (I should of stuck with APIs)
    start_marker = '<p class="cve-description">'
    end_marker = "</p>"
    start = response.text.find(start_marker) + len(start_marker)
    end = response.text.find(end_marker, start)
    if start == -1 or end == -1:
        return "⚠️ No description found."

    full_description = response.text[start:end].strip()

    # summarize with AI
    return simplify_cve_description(full_description, api_key)

def simplify_cve_description(description, api_key, retries=1):
    prompt = (
        "Summarize this security issue **clearly in 175 characters or less**. "
        "Do not use technical jargon. Avoid words like exploit, attack, or hacker:\n\n" #apparently these words cause issues??? according to random stackexchange user..
        f"{description}"
    )

    genai.configure(api_key=api_key)
    model = genai.GenerativeModel("gemini-pro")

    for attempt in range(retries + 1):
        try:
            response = model.generate_content(prompt)

            if response and hasattr(response, "candidates") and response.candidates:
                candidate = response.candidates[0]
                if hasattr(candidate, "content") and hasattr(candidate.content, "parts") and candidate.content.parts:
                    text = candidate.content.parts[0].text.strip()
                    return text if len(text) <= 175 else text[:172] + "..."

            print("⚠️ AI returned an empty or invalid response.")
            if attempt < retries:
                print("🔄 Retrying AI request...")
                time.sleep(1)
            else:
                return "⚠️ AI summarization failed."

        except Exception as e:
            print(f"⚠️ AI error: {str(e)}")
            if attempt < retries:
                print("🔄 Retrying AI request...")
                time.sleep(1)
            else:
                return "⚠️ AI summarization failed."

    return "⚠️ AI summarization failed."