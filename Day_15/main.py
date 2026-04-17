# HTTPS METHODS TO REMEMBER
# GET      --> Get Data        (see menu)
# POST     --> Send Data       (Give Order)
# PUT      --> Update Data     (Change Order)
# DELETE   --> Remove Data     (Cancel Order)

# Status Codes -- Very Important
# 200  --> OK               - everything is fine!
# 201  --> Created          - New Data formed.
# 400  --> Bad Request      - You mistake
# 401  --> Unathorized      - Login
# 404  --> Not found        - Thing not found
# 500  --> Server Error     - Server mistake


import requests
# Simple GET request
response = requests.get("https://api.github.com/users/mhassan619")
# Check status
print(response.status_code)  # 200
# Get JSON data
data = response.json()
print(data['name'])
print(data["public_repos"])
print(data["followers"])


# Requests with parameters
# Query Parameters
import requests
params = {
    "q":"python",
    "sort":"stars",
    "order":"desc"
}
response = requests.get(
    "https://api.github.com/search/repositories",
    params=params
)
data = response.json()
repos = data["items"]
for repo in repos[:5]:  #top 5 
    print(f" {repo['name']} - {repo['stargazers_count']}")


# With Headers --- Authentication:
import requests
headers = {
    "Authorization":"Bearer YOUR_GITHUB_TOKEN",
    "Content-Type":"application/json"
}
response = requests.get(
    "https://api.github.com/user",
    headers=headers
)
print(response.json())


# With Error Handling --- Professional:
import requests
def fetch_data(url):
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status() #raise error on 4xx/5xx
        return response.json()
    except requests.exceptions.Timeout:
        print("Request timeout - Server not replied.")
    except requests.exceptions.ConnectionError:
        print("Check Internet Connections!")
    except requests.exceptions.HTTPError as e:
        print(f" HTTP Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")
    return None
data = fetch_data("https://api.github.com/users/mhassan619")
if data:
    print(f"Name: {data.get('name','N/A')}")
    print(f"Public Repos: {data['public_repos']}")
    print(f"Followers: {data['followers']}")
    print(f"Location: {data.get('location','N/A')}")