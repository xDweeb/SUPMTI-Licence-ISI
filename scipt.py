import os

BASE = "."  # Create folders in the current repo

structure = {
    "Semestre_5": [
        "Administration_SE_UNIX/Cours",
        "Administration_SE_UNIX/Travaux_Pratiques",
        "Administration_SE_UNIX/Ressources",

        "Administration_Windows/Cours",
        "Administration_Windows/TP",

        "Programmation_Objet_Java_I/Cours",
        "Programmation_Objet_Java_I/Exercices",
        "Programmation_Objet_Java_I/TP",

        "UML_Analyse_Conception/Cours",
        "UML_Analyse_Conception/Diagrammes/UseCase",
        "UML_Analyse_Conception/Diagrammes/Classe",
        "UML_Analyse_Conception/Diagrammes/Séquence",

        "Genie_Logiciel/Cours",
        "Genie_Logiciel/TD",

        "Bases_de_Donnees_PL_SQL/Cours",
        "Bases_de_Donnees_PL_SQL/Scripts_SQL",
        "Bases_de_Donnees_PL_SQL/PL_SQL",

        "Anglais_V/Leçons",
        "Anglais_V/Vocabulaire",

        "Francais_V/Fiches",
        "Francais_V/Exercices",

        "POO_Python/Cours",
        "POO_Python/Scripts",

        "Python_DataScience/Notebooks",
        "Python_DataScience/Mini_Projets",

        "Systeme_Gestion_Contenu_CMS/WordPress",
        "Systeme_Gestion_Contenu_CMS/Drupal",

        "TCP_IP/Cours",
        "TCP_IP/Wireshark",

        "Programmation_Client_Serveur/Cours",
        "Programmation_Client_Serveur/Exercices",
        "Programmation_Client_Serveur/Mini_Projets",
    ],

    "Semestre_6": [
        "Administration_Base_Donnees/Cours",
        "Administration_Base_Donnees/TP",
        "Administration_Base_Donnees/Ressources",

        "UML_Analyse_Conception_II/Cours",
        "UML_Analyse_Conception_II/Diagrammes/UseCase",
        "UML_Analyse_Conception_II/Diagrammes/Classe",
        "UML_Analyse_Conception_II/Diagrammes/Séquence",

        "Programmation_Objet_Java_II/Cours",
        "Programmation_Objet_Java_II/TP",

        "Droit_Civisme_Citoyennete/Cours",
        "Droit_Civisme_Citoyennete/Ressources",

        "Intelligence_Artificielle_Avancee/Cours",
        "Intelligence_Artificielle_Avancee/TP",
        "Intelligence_Artificielle_Avancee/Notebooks",

        "Anglais_VI/Leçons",
        "Anglais_VI/Vocabulaire",

        "Francais_VI/Fiches",
        "Francais_VI/Exercices",

        "PFC/Documents",
        "PFC/Planification",
        "PFC/Rapport",
        "PFC/Code",
    ],

    "Outils": [
        "Fiches_Memo",
    ]
}

def create_structure():
    for main_folder, subfolders in structure.items():
        for sub in subfolders:
            path = os.path.join(BASE, main_folder, sub)
            os.makedirs(path, exist_ok=True)
            print(f"[OK] Dossier créé: {path}")

            # Add Notes.md in module root
            module_root = sub.split("/")[0]
            notes_path = os.path.join(BASE, main_folder, module_root, "Notes.md")

            if not os.path.exists(notes_path):
                with open(notes_path, "w", encoding="utf-8") as f:
                    f.write(f"# Notes – {module_root.replace('_',' ')}\n")
                print(f"   -> Notes.md ajouté dans {module_root}")

    print("\n🎉 Structure complète (S5 + S6) créée avec succès!")

if __name__ == "__main__":
    create_structure()
