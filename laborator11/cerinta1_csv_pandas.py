import pandas as pd

# === 1) Încarcă CSV-ul companiei ===
CSV_FILE = "vanzari_companie - vanzari_companie.csv"

df = pd.read_csv(CSV_FILE)
df["Data"] = pd.to_datetime(df["Data"], errors="coerce")
df["Venit"] = df["Cantitate"] * df["Pret"]
df["An-Luna"] = df["Data"].dt.to_period("M").astype(str)

print("Interval date în CSV:", df["Data"].min(), "->", df["Data"].max())

# ---------------------------------------------------------
# A) Care sunt cele mai vândute produse pe lună?
# (afișăm TOATE produsele pe lună, ordonate descrescător după cantitate)
qty_month_product = df.groupby(["An-Luna", "Produs"], as_index=False)["Cantitate"].sum()
qty_month_product = qty_month_product.sort_values(["An-Luna", "Cantitate"], ascending=[True, False])

print("\n--- Produse vândute pe lună (ordonate după cantitate descrescător) ---")
print(qty_month_product)

# (opțional) Top 3 produse/lună
TOP_N = 3
top_n = qty_month_product.groupby("An-Luna").head(TOP_N)
print(f"\n--- TOP {TOP_N} produse pe lună ---")
print(top_n)

# ---------------------------------------------------------
# B) Venitul total pe fiecare produs
venit_produs = df.groupby("Produs", as_index=False)["Venit"].sum().sort_values("Venit", ascending=False)

print("\n--- Venit total pe produs ---")
print(venit_produs)

# ---------------------------------------------------------
# C) Filtrare pe interval (exemplu 01.01.2024 - 31.03.2024)
start = pd.Timestamp("2024-01-01")
end = pd.Timestamp("2024-03-31")

filtrat = df[(df["Data"] >= start) & (df["Data"] <= end)].sort_values("Data")

print("\n--- Filtrare 01.01.2024 - 31.03.2024 ---")
print(filtrat)
print("Număr rânduri filtrate:", len(filtrat))

# ---------------------------------------------------------
# D) Grupare după lună/an pentru venit mediu lunar
# - venit total lunar (sumă)
venit_total_lunar = df.groupby("An-Luna", as_index=False)["Venit"].sum().sort_values("An-Luna")

# - venit mediu lunar (media valorii unei vânzări/înregistrări în luna respectivă)
venit_mediu_lunar = df.groupby("An-Luna", as_index=False)["Venit"].mean().sort_values("An-Luna")

print("\n--- Venit total lunar ---")
print(venit_total_lunar)

print("\n--- Venit mediu lunar (media pe înregistrare) ---")
print(venit_mediu_lunar)
