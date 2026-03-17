#!/usr/bin/env python3
"""
Groundwork Studio — Lead Finder
Usage: python leads.py "pool service" "Phoenix, AZ"
       python leads.py "plumber" "Scottsdale, AZ" --limit 100
"""

import argparse
import csv
import os
import sys
import requests
from datetime import date
from dotenv import load_dotenv

load_dotenv()

YELP_API_KEY = os.getenv("YELP_API_KEY")
YELP_SEARCH_URL = "https://api.yelp.com/v3/businesses/search"
TIMEOUT = 5  # seconds for website check

# Industry display names for scripts
INDUSTRY_LABELS = {
    "pool service": "pool company",
    "plumber": "plumber",
    "plumbing": "plumber",
    "electrician": "electrician",
    "electrical": "electrician",
    "hvac": "HVAC company",
    "roofing": "roofing company",
    "roofer": "roofing company",
    "painting": "painting company",
    "painter": "painting company",
    "landscaping": "landscaping company",
    "landscaper": "landscaping company",
    "auto repair": "auto repair shop",
    "cleaning": "cleaning company",
    "pest control": "pest control company",
    "gym": "gym",
    "fitness": "gym",
    "restaurant": "restaurant",
}


def get_industry_label(industry: str) -> str:
    return INDUSTRY_LABELS.get(industry.lower(), industry)


def build_script(status: str, industry_label: str) -> str:
    if status == "none":
        return (
            f"Hey, hope business is going well. Noticed you don't have a website yet — "
            f"for a {industry_label}, that means homeowners who are ready to book are moving on "
            f"before they ever reach you. We build clean, modern sites for local service companies "
            f"that start pulling in new calls within a couple of weeks — take a look at teamground.work. Interested?\n\n"
            f"Evan · Groundwork Studio"
        )
    elif status == "broken":
        return (
            f"Hey, hope business is going well. Noticed your website isn't loading properly — "
            f"for a {industry_label}, that's quietly turning away customers who are ready to book "
            f"before they ever reach you. We can get you a clean, working site that starts pulling "
            f"in new calls within a couple of weeks — take a look at teamground.work. Interested?\n\n"
            f"Evan · Groundwork Studio"
        )
    else:
        return (
            f"Hey, hope business is going well. Took a look at your site — it has the feel of "
            f"something built a long time ago and hasn't kept up with the business you're probably "
            f"running today. Customers sizing up a {industry_label} will move on quickly if the site "
            f"doesn't inspire confidence. We build clean, modern sites for local service companies — "
            f"take a look at teamground.work. Interested?\n\n"
            f"Evan · Groundwork Studio"
        )


def check_website(url: str) -> str:
    if not url:
        return "none"
    try:
        r = requests.get(url, timeout=TIMEOUT, allow_redirects=True)
        if r.status_code >= 400:
            return "broken"
        return "has_website"
    except Exception:
        return "broken"


def fetch_businesses(industry: str, location: str, limit: int) -> list:
    if not YELP_API_KEY:
        print("ERROR: YELP_API_KEY not found. Did you set it in outreach/.env?")
        sys.exit(1)

    headers = {"Authorization": f"Bearer {YELP_API_KEY}"}
    businesses = []
    offset = 0
    per_page = 50

    print(f"\nSearching Yelp for '{industry}' in '{location}'...")

    while len(businesses) < limit:
        params = {
            "term": industry,
            "location": location,
            "limit": min(per_page, limit - len(businesses)),
            "offset": offset,
        }
        try:
            r = requests.get(YELP_SEARCH_URL, headers=headers, params=params, timeout=10)
            r.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f"Yelp API error: {e}")
            break

        data = r.json()
        batch = data.get("businesses", [])
        if not batch:
            break

        businesses.extend(batch)
        offset += len(batch)

        total = data.get("total", 0)
        print(f"  Fetched {len(businesses)} of {min(total, limit)} businesses")

        if offset >= total:
            break

    return businesses


def process_leads(businesses: list, industry: str) -> list:
    industry_label = get_industry_label(industry)
    leads = []

    print(f"\nChecking {len(businesses)} websites...")

    for i, biz in enumerate(businesses, 1):
        name = biz.get("name", "")
        phone = biz.get("phone", "")
        location = biz.get("location", {})
        address = ", ".join(filter(None, [
            location.get("city", ""),
            location.get("state", ""),
        ]))
        url = biz.get("url", "")  # This is the Yelp URL
        website = biz.get("website") or ""  # Business's own website (may not be in basic API)

        # Yelp basic search doesn't return the business website directly —
        # it returns the Yelp page URL. We flag no-website based on whether
        # the business has a website field populated.
        status = check_website(website) if website else "none"

        script = build_script(status, industry_label)

        priority = {"none": 1, "broken": 2, "has_website": 3}[status]

        leads.append({
            "priority": priority,
            "Business Name": name,
            "Phone": phone,
            "Address": address,
            "Website Status": status,
            "Website URL": website or "(none)",
            "Yelp Page": url,
            "Outreach Script": script,
        })

        # Progress indicator
        status_icon = {"none": "🔴", "broken": "🟡", "has_website": "🟢"}.get(status, "?")
        print(f"  [{i}/{len(businesses)}] {status_icon} {name}")

    # Sort: no website first, broken second, has website last
    leads.sort(key=lambda x: x["priority"])

    return leads


def save_csv(leads: list, industry: str, location: str) -> str:
    safe_industry = industry.replace(" ", "-").lower()
    safe_location = location.replace(", ", "-").replace(" ", "-").lower()
    filename = f"leads-{safe_industry}-{safe_location}-{date.today()}.csv"
    filepath = os.path.join(os.path.dirname(__file__), "output", filename)

    os.makedirs(os.path.dirname(filepath), exist_ok=True)

    fieldnames = ["Business Name", "Phone", "Address", "Website Status",
                  "Website URL", "Yelp Page", "Outreach Script"]

    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames, extrasaction="ignore")
        writer.writeheader()
        writer.writerows(leads)

    return filepath


def print_summary(leads: list):
    none_count = sum(1 for l in leads if l["Website Status"] == "none")
    broken_count = sum(1 for l in leads if l["Website Status"] == "broken")
    has_count = sum(1 for l in leads if l["Website Status"] == "has_website")

    print(f"\n{'='*50}")
    print(f"  RESULTS SUMMARY")
    print(f"{'='*50}")
    print(f"  🔴 No website:      {none_count:>4}  (highest priority)")
    print(f"  🟡 Broken website:  {broken_count:>4}  (high priority)")
    print(f"  🟢 Has website:     {has_count:>4}  (low priority)")
    print(f"  {'─'*30}")
    print(f"  Total leads:        {len(leads):>4}")
    print(f"{'='*50}")


def main():
    parser = argparse.ArgumentParser(
        description="Find local businesses with bad or missing websites."
    )
    parser.add_argument("industry", help='Industry to search, e.g. "pool service"')
    parser.add_argument("location", help='City and state, e.g. "Phoenix, AZ"')
    parser.add_argument("--limit", type=int, default=50, help="Max businesses to fetch (default: 50)")
    args = parser.parse_args()

    businesses = fetch_businesses(args.industry, args.location, args.limit)

    if not businesses:
        print("No businesses found. Try a different industry or location.")
        sys.exit(0)

    leads = process_leads(businesses, args.industry)
    filepath = save_csv(leads, args.industry, args.location)

    print_summary(leads)
    print(f"\n  CSV saved to: {filepath}\n")


if __name__ == "__main__":
    main()
