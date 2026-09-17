import pandas as pd

# 1. Load your CSV
df = pd.read_csv("tunisia_ndvi.csv")

# 2. Hardcoded PCODE dictionary matching the exact spelling in your GeoJSON
pcode_to_name = {
    "TN11": "Tunis",
    "TN12": "Ariana",
    "TN13": "Ben Arous",
    "TN14": "Mannouba",  # Spelled with double 'n' in your GeoJSON
    "TN15": "Nabeul",
    "TN16": "Zaghouan",
    "TN17": "Bizerte",
    "TN21": "Beja",
    "TN22": "Jandouba",  # Spelled with 'a' in your GeoJSON
    "TN23": "Le kef",    # Lowercase 'k' in your GeoJSON
    "TN24": "Siliana",
    "TN31": "Sousse",
    "TN32": "Monastir",
    "TN33": "Mahdia",
    "TN34": "Sfax",
    "TN41": "Kairouan",
    "TN42": "Kasserine",
    "TN43": "Sidi Bouzid",
    "TN51": "Gabes",
    "TN52": "Mednine",   # Spelled without second 'e' in your GeoJSON
    "TN53": "Tataouine",
    "TN61": "Gafsa",
    "TN62": "Tozeur",
    "TN63": "Kebili",
    
    # The 6 Regional level codes found in your CSV
    "TN1": "Nord-Est Region",
    "TN2": "Nord-Ouest Region",
    "TN3": "Centre-Est Region",
    "TN4": "Centre-Ouest Region",
    "TN5": "Sud-Est Region",
    "TN6": "Sud-Ouest Region"
}

# 3. Automatically detect the ID column
id_column = None
for col in df.columns:
    if df[col].astype(str).str.upper().str.contains("TN").any():
        id_column = col
        break

if not id_column:
    print("Error: Could not find the 'TN' ID column.")
else:
    # 4. Clean the CSV column (removes spaces/dashes, makes uppercase)
    cleaned_ids = df[id_column].astype(str).str.upper().str.replace("-", "").str.replace(" ", "")
    
    # 5. Map the cleaned IDs to the GeoJSON names
    # Using the exact name of the GeoJSON property: gouv_fr
    df["gouv_fr"] = cleaned_ids.map(pcode_to_name)
    
    # 6. Save the fixed CSV
    output_file = "tunisia_ndvi_4_fixed.csv"
    df.to_csv(output_file, index=False)
    
    print(f"Success! Fixed data saved to {output_file}")
    print("\nPreview of the mapped data:")
    print(df[[id_column, "gouv_fr"]].head(24))