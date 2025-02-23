import requests
from bs4 import BeautifulSoup

def get_cve_description(cve_id):
    url = f"https://app.opencve.io/cve/{cve_id}"
    print(f"Fetching: {url}")  # print URL for debug

    try:
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(url, timeout=10, headers=headers)

        if response.status_code == 404:
            return f"⚠️ CVE {cve_id} not found on OpenCVE."

        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")

        # scrape the description (this is what happens when I'm not given an API...)
        desc_tag = soup.find("div", class_="box-body")

        if desc_tag:
            return desc_tag.text.strip()

        return "⚠️ No description found for this CVE."
    
    except requests.RequestException as e:
        print(f"⚠️ Request failed: {e}")
        return "⚠️ Error fetching CVE details."
