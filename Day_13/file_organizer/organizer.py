import os
import shutil
from pathlib import Path
from .config import FILE_CATEGORIES, LOG_FILE
from .logger import log_action

class FileOrganizer:
    def __init__(self,target_folder):
        self.target_folder = Path(target_folder)
        self.__moved_files = 0
        self.__log = []
    def __get_category(self,extension):
        for category,extensions in FILE_CATEGORIES.items():
            if extension.lower() in extensions:
                return category
        return "Others"
    def __create_folder(self,folder_name):
        folder_path = self.target_folder / folder_name
        folder_path.mkdir(exist_ok=True)
        return folder_path
    
    @log_action
    def organize(self):
        if not self.target_folder.exists():
            raise FileNotFoundError(f"Folder is not found{self.target_folder}")
        files = [f for f in self.target_folder.iterdir() if f.is_file()]
        if not files:
            print(f"Folder already empty/organized.")
            return
        print(f"{len(files)} files found - organizing...")
        for file in files:
            try:
                extension = file.suffix
                category = self.__get_category(extension)
                dest_folder = self.__create_folder(category)
                dest_path = dest_folder / file.name

                if dest_path.exists():
                    base = file.stem
                    ext = file.suffix
                    counter = 1
                    while dest_path.exists():
                        dest_path = dest_folder / f"{base}_{counter}{ext}"
                        counter+=1

                shutil.move(str(file), str(dest_path))
                self.__moved_files += 1
                self.__log.append(f" {file.name} -> {category}/")
                print(f" {file.name} -> {category}/")
            except Exception as e:
                self.__log.append(f" {file.name} - Error: {e}")
                print(f" {file.name} - Error: {e}")
        self.__save_log()
        print(f"\n Complete! {self.__moved_files} files organized!")

    def __save_log(self):
        with open(LOG_FILE, "a") as f:
            import datetime
            f.write(f"\n--- {datetime.datetime.now()} ---\n")
            for entry in self.__log:
                f.write(entry + "\n")

    def get_report(self):
        print(f"\n Organizer Report")
        print(f"{'='*35}")
        print(f"Target Folder: {self.target_folder}")
        print(f"Files Moved: {self.__moved_files}")

        #Generator for counting categories
        categories = list(self.__get_categories())
        for cat, count in categories:
            print(f" {cat}:{count} files.")
    
    def __get_categories(self):
        for category in FILE_CATEGORIES.keys():
            folder = self.target_folder / category
            if folder.exists():
                count = len(list(folder.iterdir()))
                yield category, count