# Handle JSON List of objects 
import requests
response = requests.get("https://api.github.com/users/mhassan619/repos")
repos = response.json()

# Filter - Only stars waly repos
popular = [r for r in repos if r["stargazers_count"] > 0]

# Sort them
sorted_repos = sorted(repos,key=lambda r: r['stargazers_count'], reverse=True)

# Get only Important fields
clean_data = []
for repo in repos:
    clean_data.append({
        "name":repo['name'],
        "stars":repo['stargazers_count'],
        "language":repo.get('language',"N/A"),
        "url":repo['html_url']
    })
print(clean_data)