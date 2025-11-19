import os
import comtypes.client

# Folder where DOC/DOCX are stored
folder = r"C:\Users\xdweb\OneDrive\Desktop\SUPMTI-Licence-ISI\Pdfs"

# Start Word COM automation
word = comtypes.client.CreateObject("Word.Application")
word.Visible = 0  # Word runs in background

for file in os.listdir(folder):
    if file.lower().endswith((".doc", ".docx")):
        input_path = os.path.abspath(os.path.join(folder, file))
        output_path = os.path.splitext(input_path)[0] + ".pdf"

        print(f"Converting: {file} --> {os.path.basename(output_path)}")

        # Open document
        doc = word.Documents.Open(input_path)

        # Save as PDF (format 17)
        doc.SaveAs(output_path, FileFormat=17)
        doc.Close()

word.Quit()

print("\n🎉 Tous les fichiers DOC/DOCX ont été convertis en PDF dans le même dossier !")
