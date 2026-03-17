# Lead Finder — Setup Guide

## One-time setup (5 minutes)

### 1. Get your free Yelp API key
1. Go to https://www.yelp.com/developers/v3/manage_app
2. Sign in or create a free account
3. Click **Create New App**
4. Fill in any app name (e.g. "Groundwork Leads"), agree to terms, submit
5. Copy your **API Key**

### 2. Add your key
In the `outreach/` folder, create a file called `.env` and paste:
```
YELP_API_KEY=your_key_here
```

### 3. Install dependencies
Open Terminal, navigate to the outreach folder, and run:
```
cd /Users/evanbaukol/Sites/groundwork-studio/outreach
pip install -r requirements.txt
```

---

## Running the script

```
python leads.py "industry" "City, State"
python leads.py "industry" "City, State" --limit 100
```

### Examples
```
python leads.py "pool service" "Phoenix, AZ"
python leads.py "plumber" "Scottsdale, AZ" --limit 100
python leads.py "electrician" "Mesa, AZ"
python leads.py "hvac" "Chandler, AZ" --limit 100
python leads.py "roofing" "Tempe, AZ"
python leads.py "auto repair" "Gilbert, AZ"
python leads.py "pest control" "Phoenix, AZ"
python leads.py "gym" "Scottsdale, AZ"
```

---

## Reading your results

Results are saved as a CSV in `outreach/output/`. Open it in Excel or Google Sheets.

- **🔴 No website** — best leads, message these first
- **🟡 Broken website** — great leads, broken site = urgent need
- **🟢 Has website** — lower priority, only message if you want more volume

The **Outreach Script** column has a ready-to-send text message for each business. Just copy and send.

---

## Limits

- Free Yelp API: **500 calls/day**
- Each `--limit 50` run = 1 API call
- Each `--limit 100` run = 2 API calls
- You can run dozens of searches per day before hitting the limit
