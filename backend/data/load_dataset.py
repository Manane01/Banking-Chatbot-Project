from datasets import load_dataset
import pandas as pd
import os

# Dossier de sauvegarde
DATA_DIR = os.path.join(os.path.dirname(__file__), "bitext_data")
os.makedirs(DATA_DIR, exist_ok=True)

def download_bitext_dataset():

    # Téléchargement du dataset
    dataset = load_dataset("bitext/Bitext-retail-banking-llm-chatbot-training-dataset")

    # On récupère la partie "train" (principale)
    df = pd.DataFrame(dataset["train"])

    # Aperçu du dataset
    print(df.head())

    print("\nColonnes disponibles :", list(df.columns))

    # Sauvegarde locale
    csv_path = os.path.join(DATA_DIR, "bitext_banking_dataset.csv")
    df.to_csv(csv_path, index=False)
    print(f"\nDataset sauvegardé dans : {csv_path}")

    return df


if __name__ == "__main__":
    download_bitext_dataset()
