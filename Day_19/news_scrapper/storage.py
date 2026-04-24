import json
from datetime import datetime

class Storage:
    def __init__(self,filename):
        self.__filename = filename
        self.__data = []
    def add(self,items):
        self.__data.extend(items)
    def save(self):
        output = {
            "scrapped_at":datetime.now().strftime("%Y-%m-%d %H:%M"),
            "total":len(self.__data),
            "items":self.__data
        }
        with open(self.__filename,"w", encoding="utf-8") as f:
            json.dump(output,f,indent=4, ensure_ascii=False)
        print(f"✅ {len(self.__data)} items saved!")
    def load(self):
        try:
            with open(self.__filename, 'r') as f:
                data = json.load(f)
                self.__data = data.get("items", [])
                print(f"✅ {len(self.__data)} items loaded!")
                return self.__data
        except FileNotFoundError:
            print(f"❌ File is not found!")
            return []
    def get_all(self):
        return self.__data
    
    # Generator - filtered items
    def filter_by_keyword(self,keyword):
        for item in self.__data:
            title = item.get("title","").lower()
            if keyword.lower() in title:
                yield item