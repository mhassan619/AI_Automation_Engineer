## GitHub API Explorer
import requests
import json
class GitHubAnalyzer:
    def __init__(self,username):
        self.username = username
        self.__base_url = "https://api.github.com"
        self.__headers = {"Accept":"application/vnd.github.v3+json"}
    def __fetch(self,endpoint):
        try:
            url = f"{self.__base_url}{endpoint}"
            response = requests.get(url, headers=self.__headers,timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError:
            print(f"Error: {response.status_code}")
        except requests.exceptions.ConnectionError:
            print(f"Error: Please check your internet connection")
            return None
    def get_profile(self):
        data = self.__fetch(f"/users/{self.username}")
        if data:
            print(f"\n{'='*40}")
            print(f"    GitHub Profile: {self.username}")
            print(f"{'='*40}")
            print(f"Name: {data.get('name','N/A')}")
            print(f"Bio: {data.get('bio','N/A')}")
            print(f"Public Repos: {data['public_repos']}")
            print(f"Followers: {data['followers']}")
            print(f"Following: {data['following']}")
            print(f"{'='*40}")
    def get_repos(self):
        data = self.__fetch(f"/users/{self.username}/repos")
        if data:
            print(f"\n Repositories of {self.username}")
            print(f"{'-'*40}")
            for repo in self.__repo_generator(data):
                print(f" ⭐ {repo['stargazers_count']} | {repo['name']}")
    def __repo_generator(self,repos):
        sorted_repos = sorted(
            repos,
            key=lambda r: r['stargazers_count'],
            reverse=True
        )
        for repo in sorted_repos:
            yield repo
    def save_profile(self,filename):
        data = self.__fetch(f"/users/{self.username}")
        if data:
            with open(filename,"w") as f:
                json.dump(data,f,indent=4)
            print(f"✅ Profile saved to {filename}")
analyzer = GitHubAnalyzer("mhassan619")
analyzer.get_profile()
analyzer.get_repos()
analyzer.save_profile("my_github_profile.json")