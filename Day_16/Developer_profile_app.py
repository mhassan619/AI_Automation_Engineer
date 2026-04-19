import requests
import json
from datetime import datetime
class DeveloperProfile:
    def __init__(self,github_username):
        self.username = github_username
        self.__github_data = None
        self.__repos_data = None
    def fetch_all(self):
        # Fetching Github Profile
        r1 = requests.get(f"https://api.github.com/users/{self.username}")
        if r1.status_code == 200:
            self.__github_data = r1.json()
        # Fetching Repos
        r2 = requests.get(f"https://api.github.com/users/{self.username}/repos")
        if r2.status_code == 200:
            self.__repos_data = r2.json()
        print("✅ Data Fetched!")
    def top_languages(self):
        # Make a Generator - that yeilds a language of every repo
        if self.__repos_data:
            for repo in self.__repos_data:
                lang = repo.get("language")
                if lang:
                    yield lang
    def language_stats(self):
        languages = {}
        for lang in self.top_languages():
            languages[lang] = languages.get(lang, 0) + 1
            return dict(sorted(
                languages.items(),
                key=lambda x: x[1],
                reverse=True
            ))
    def full_report(self):
        if not self.__github_data:
            print("❌ Please Fetch Data First!")
            return
        d = self.__github_data
        print(f"{'='*45}")
        print(f"  DEVELOPER PROFILE REPORT")
        print(f"{'='*45}")
        print(f"  Username: {d.get('login')}")
        print(f"  Name: {d.get('name','N/A')}")
        print(f"  Repos: {d.get('public_repos')}")
        print(f"  Followers: {d.get('followers')}")
        print(f"  Joined: {d.get('created_at','')[:10]}")
        print(f"{'-'*45}")

        # Language Stat
        print(f"  📊 Languages Used: ")
        for lang, count in self.language_stats().items():
            bar = "❗" * count
            print(f"  {lang:<15} {bar} ({count})")
        print(f"{'-'*45}")
        # Top 3 Repos
        if self.__repos_data:
            top3 = sorted(
                self.__repos_data,
                key=lambda r: r['stargazers_count'],
                reverse=True
            )[:3]
            print(f"  ⭐ Top Repositories: ")
            for repo in top3:
                print(f"  --> {repo['name']} ({repo.get('language','N/A')})")
        print(f"{'='*45}")
    def save_report(self):
        report = {
            "username":self.username,
            "generated_at":datetime.now().strftime("%Y-%m-%d %H:%M"),
            "profile":self.__github_data,
            "language_stats":self.language_stats(),
        }
        filename = f"{self.username}_repo.json"
        with open(filename,'w') as f:
            json.dump(report,f,indent=4)
        print("✅ Report Saved: {filename}")
# Now Test
dev = DeveloperProfile("mhassan619")
dev.fetch_all()
dev.full_report()
dev.save_report()