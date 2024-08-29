import os
import pandas as pd

# Chemin vers le répertoire contenant les fichiers de résultats
results_dir = '/home/brice/evals/results/'
output_file = '/home/brice/evals/recapitulatif_resultats.xlsx'

# Liste pour stocker les données
data = []

# Parcourir tous les fichiers dans le répertoire des résultats
for filename in os.listdir(results_dir):
    if filename.endswith('_results.txt'):
        filepath = os.path.join(results_dir, filename)
        
        # Ouvrir et lire le fichier
        with open(filepath, 'r') as file:
            content = file.read().strip()
            # Extraire le nom de l'élève à partir du nom du fichier
            student_name = filename.split('_')[0]
            # Extraire le score à partir du contenu du fichier
            score_part = content.split()[-1]  # Dernière partie ex: "8/10"
            score, total_questions = score_part.split('/')  # Diviser en deux parties "8", "10."
            # Nettoyer et convertir en entier
            score = int(score.strip())
            total_questions = int(total_questions.strip().replace('.', ''))
            # Ajouter les données à la liste
            data.append({
                'Nom': student_name,
                'Score': score,
                'Total': total_questions
            })

# Convertir les données en DataFrame pandas
df = pd.DataFrame(data)

# Sauvegarder les données dans un fichier Excel
df.to_excel(output_file, index=False)

print(f"Les résultats ont été concaténés dans le fichier : {output_file}")

