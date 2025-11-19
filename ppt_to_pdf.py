import os
import comtypes.client

# Folder where PPT/PPTX are stored
folder = r"C:\Users\xdweb\OneDrive\Desktop\SUPMTI-Licence-ISI\Pdfs"

# Start PowerPoint COM automation
powerpoint = comtypes.client.CreateObject("PowerPoint.Application")
powerpoint.Visible = 1

for file in os.listdir(folder):
    if file.lower().endswith((".ppt", ".pptx")):
        input_path = os.path.abspath(os.path.join(folder, file))
        output_path = os.path.splitext(input_path)[0] + ".pdf"

        print(f"Converting: {file} --> {os.path.basename(output_path)}")

        presentation = powerpoint.Presentations.Open(input_path)
        presentation.SaveAs(output_path, 32)  # 32 = PDF format
        presentation.Close()

powerpoint.Quit()

print("\n🎉 Tous les fichiers PPT/PPTX ont été convertis en PDF dans le même dossier !")
