import requests
class CountryInfo:
    def __init__(self,country_name):
        self.country = country_name
        self.__data = None
    def fetch(self):
        url = f"https://restcountries.com/v3.1/name/{self.country}"
        response = requests.get(url)
        if response.status_code == 200:
            self.__data = response.json()[0] # Pehla result
            return True
        return False
    def display(self):
        if not self.__data:
            print("❌ Please Fetch Data firstly!")
            return 
        d = self.__data
        print(f"\n{'='*40}")
        print(f"🌍 {d.get('name',{}).get('common','N/A')}")
        print(f"{'='*40}")
        print(f"  Capital: {d.get('capital',['N/A'])[0]}")
        print(f"  Population: {d.get('population',0):,}")
        print(f"  Region: {d.get('region','N/A')}")

        # Currency 
        currencies = d.get('currencies',{})
        for code, info in currencies.items():
            print(f"  Currency: {info['name']} ({code})")

        # Languages
        languages = d.get('languages',{})
        langs = list(languages.values())
        print(f"  Languages: {', '.join(langs)}")
        print(f"{'='*40}")

# Now Test code
country = CountryInfo("pakistan")
if country.fetch():
    country.display()