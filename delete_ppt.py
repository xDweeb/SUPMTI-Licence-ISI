import os

# Folder where PPT/PPTX are stored
folder = r"C:\Users\xdweb\OneDrive\Desktop\SUPMTI-Licence-ISI\Pdfs"

deleted = 0

for file in os.listdir(folder):
    if file.lower().endswith((".ppt", ".pptx")):
        file_path = os.path.join(folder, file)
        print(f"Deleting: {file}")
        os.remove(file_path)
        deleted += 1

if deleted == 0:
    print("No PPT or PPTX files found.")
else:
    print(f"\n🎉 {deleted} fichier(s) PPT/PPTX ont été supprimés.")
