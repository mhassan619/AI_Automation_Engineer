from datetime import datetime
import json
import os

# Pure Python functions without @tool decorator

def get_current_time(query: str = "") -> str:
    """Get current date and time for scheduling queries."""
    now = datetime.now()
    return f"Current: {now.strftime('%A, %B %d, %Y at %I:%M %p')}"

def save_lead(info: str) -> str:
    """Save potential customer contact information."""
    try:
        leads = []
        if os.path.exists("leads.json"):
            with open("leads.json", "r") as f:
                leads = json.load(f)
        
        leads.append({
            "info": info,
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M"),
            "status": "new"
        })
        
        with open("leads.json", "w") as f:
            json.dump(leads, f, indent=4)
        
        return "✅ Lead saved! Our team will contact you within 24 hours."
    except Exception as e:
        return f"❌ Error: {e}"

def calculate_project_cost(project_type: str) -> str:
    """Calculate estimated project cost."""
    costs = {
        "chatbot": ("PKR 50,000 - 150,000", "2-4 weeks"),
        "scraping": ("PKR 20,000 - 80,000", "1-2 weeks"),
        "dashboard": ("PKR 30,000 - 100,000", "1-3 weeks"),
        "agent": ("PKR 80,000 - 200,000", "4-8 weeks"),
    }
    
    project_lower = project_type.lower()
    for key, (price, timeline) in costs.items():
        if key in project_lower:
            return f"Project: {key.title()}\nCost: {price}\nTimeline: {timeline}"
    
    return "Project type nahi pehchana. Try: chatbot/scraping/dashboard/agent"