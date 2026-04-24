class Display:
    @staticmethod
    def items(items, title="Results"):
        print(f"\n{'='*50}")
        print(f"  🗒️ {title}")
        print(f"{'='*50}")
        for i, item in enumerate(items,1):
            print(f"\n {i}. {item.get('title','N/A')[:55]}")
            print(f"  Source: {item.get('source','N/A')}")
            if item.get('score'):
                print(f"    Score: {item.get('score','N/A')}")
        print(f"\n{'='*50}")
        print(f"  Total: {len(items)} items")
        print(f"{'='*50}")