# Zomato-Gen-AI-Internship-Assignment   

## Solution and Fullfilment of Assignment Requirements

### 1. Web Scraper Component and Knowledge Base Creation 

It consists of three Python scripts:
- `menu_scraper.py` — Scrapes menu items, descriptions, prices, and special attributes.
- `info_scraper.py` — Scrapes general restaurant information like name, address, hours, phone, and images.
- `format.py` — Cleans, formats, and combines scraped data into a unified structured JSON.


### 1. Web Scraping
Instead of manually collecting restaurant data, we automate it by scraping multiple restaurant websites.  
We capture:
- Restaurant name , address, timings and contact details.
- Menu items with:
  - Description
  - Price
  - Dietary options (e.g., vege tarian/non-vegetarian)
  - Spice level (if available)

Both `menu_scraper.py` and `info_scraper.py` takes care of following : 

- Implementing error handling to avoid crashes if some fields are missing.
- Respect the site's `robots.txt` to avoid scraping restricted areas.
- Organize extracted data into clean intermediate JSON files.

---

### 2. Knowledge Base Creation

Once raw data is scraped:
- `format.py` processes both the **restaurant info** and the **menu items**.
- It **normalizes** the text (removing extra spaces, cleaning HTML artifacts).
- It **indexes** data efficiently, associating each restaurant with its menu.
- It finally generates a structured `knowledgebase.json`, ready for future chatbot integration.

### Below is the `knowledgebase.json` structure
Restaurant data (per restaurant):

```
{
    "name": "...",
    "menu_items": [...],
    "dietary_options": "...",
    "price_range": "...", 
    "address": "...",
    "opening_hours": "...",
    "image_url": "...",
    "phone_number": "..."
}
```
Menu Item Data (per dish):

```
{
    "name": "...",
    "description": "...",
    "price": "amount in rupees",
    "attributes": {
        "veg_nonveg": "...",
        "category": "...",
        "spice_level": 0/1/2 based on spices
    }
}
```
### Running web scraping component
inside web scraping component follow the below commands

1. install required libraries
```
pip install -r requirements.txt
```
it will install all the required libraries

2. Run web scraping python Files
```
python3 run main.py
```
It will create a restaurant.json with unfiltered data

3. Format and generate the knowledge base:
```
python3 format.py
```
It will create a Knowledgebase.json with cleaned data
