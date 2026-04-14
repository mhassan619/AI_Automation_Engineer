from file_organizer.organizer import FileOrganizer
# making test folder
import os
os.makedirs("test_folder", exist_ok=True)
# making test files
test_files = [
    "report.pdf","photo.jpg","video.mp4",
    "script.py","music.mp3","notes.txt",
    "archive.zip","image2.png","data.xlsx"
]
for fname in test_files:
    with open(f"test_folder/{fname}", "w") as f:
        f.write("test content")
# Now organize
organizer = FileOrganizer("test_folder")
organizer.organize()
organizer.get_report()