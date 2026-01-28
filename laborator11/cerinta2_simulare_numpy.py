import numpy as np
import pandas as pd

rng = np.random.default_rng(42)

# === Setări ===
start_date = pd.Timestamp("2024-01-01")
days = pd.date_range(start_date, periods=60, freq="D")

produse = ["Mouse", "Tastatura", "Monitor", "Laptop", "Casti",
           "Telefon", "Tableta", "Imprimanta", "Televizor", "Camera Foto"]

rows = []

for d in days:
    # 1) număr aleator de produse/zi (linii): 5..15
    n = rng.integers(5, 16)

    # produse aleator
    prod = rng.choice(produse, size=n, replace=True)

    # 2) preț ~ Normal(40, 8), forțat pozitiv
    pret = rng.normal(loc=40, scale=8, size=n)
    pret = np.clip(pret, 1, None)

    # 3) cantitate ~ Uniform între 1 și 10 (întreg)
    cant = rng.integers(1, 11, size=n)

    # 4) promoții 30%: -20% la preț
    promo = rng.random(size=n) < 0.30
    pret_final = pret * np.where(promo, 0.8, 1.0)

    for p, c, pr, pr_flag in zip(prod, cant, pret_final, promo):
        rows.append({
            "Data": d,
            "Produs": p,
            "Cantitate": int(c),
            "Pret": float(pr),
            "Promotie": bool(pr_flag)
        })

sim = pd.DataFrame(rows)

# 5) Total vânzări per zi (pret*cant) la nivel de linie
sim["Venit"] = sim["Pret"] * sim["Cantitate"]

# 6) Profit: marjă 30% din preț => profit = 0.30 * venit
sim["Profit"] = sim["Venit"] * 0.30

# Agregare pe zi
daily = sim.groupby("Data", as_index=False).agg(
    Venit_zi=("Venit", "sum"),
    Profit_zi=("Profit", "sum"),
    Nr_linii=("Produs", "size"),
    Nr_promotii=("Promotie", "sum"),
)

# 7) Statistici: mean/min/max pentru preț, cantitate, profituri (pe zi)
pret_stats = sim["Pret"].agg(["mean", "min", "max"])
cant_stats = sim["Cantitate"].agg(["mean", "min", "max"])
profit_zi_stats = daily["Profit_zi"].agg(["mean", "min", "max"])

# 8) Totaluri pe 60 zile
total_vanzari = float(sim["Venit"].sum())
total_profit = float(sim["Profit"].sum())

print("\n--- Statistici preț ---")
print(pret_stats)

print("\n--- Statistici cantitate ---")
print(cant_stats)

print("\n--- Statistici profit zilnic ---")
print(profit_zi_stats)

print("\nTOTAL vânzări (60 zile):", total_vanzari)
print("TOTAL profit (60 zile):", total_profit)

# Salvare pentru cerința 3
OUT_FILE = "simulare_vanzari_60zile.csv"
sim.to_csv(OUT_FILE, index=False)
print(f"\nDataset salvat în: {OUT_FILE}")
