import pandas as pd
import matplotlib.pyplot as plt

# Citește dataset-ul generat la cerința 2
CSV_SIM = "simulare_vanzari_60zile.csv"
sim = pd.read_csv(CSV_SIM)

# Parse date
sim["Data"] = pd.to_datetime(sim["Data"], errors="coerce")

# ---------------------------------------------------------
# Evoluția veniturilor și profitului pe zile
daily = sim.groupby("Data", as_index=False).agg(
    Venit_zi=("Venit", "sum"),
    Profit_zi=("Profit", "sum"),
    Nr_promotii=("Promotie", "sum")
)

print("\n--- Primele zile (venit/profit) ---")
print(daily.head())

# Pregătire pentru vizualizare: grafic venit + profit
plt.figure()
plt.plot(daily["Data"], daily["Venit_zi"])
plt.title("Evoluția venitului zilnic (60 zile)")
plt.xlabel("Data")
plt.ylabel("Venit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
plt.plot(daily["Data"], daily["Profit_zi"])
plt.title("Evoluția profitului zilnic (60 zile)")
plt.xlabel("Data")
plt.ylabel("Profit")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Distribuția prețurilor și cantităților
plt.figure()
plt.hist(sim["Pret"], bins=20)
plt.title("Distribuția prețurilor (60 zile)")
plt.xlabel("Preț")
plt.ylabel("Frecvență")
plt.tight_layout()
plt.show()

plt.figure()
plt.hist(sim["Cantitate"], bins=10)
plt.title("Distribuția cantităților vândute (60 zile)")
plt.xlabel("Cantitate")
plt.ylabel("Frecvență")
plt.tight_layout()
plt.show()

# ---------------------------------------------------------
# Vizualizarea promoțiilor + impact
# Zile cu promoții active (cel puțin 1 linie promo)
daily["Promotie_activa"] = daily["Nr_promotii"] > 0

# Impact promoții asupra prețurilor: medie promo vs fără promo
avg_price_promo = sim.loc[sim["Promotie"] == True, "Pret"].mean()
avg_price_no = sim.loc[sim["Promotie"] == False, "Pret"].mean()

print("\nPreț mediu CU promoție:", avg_price_promo)
print("Preț mediu FĂRĂ promoție:", avg_price_no)

# Impact promoții asupra veniturilor/profitului: medii pe zile promo vs fără promo
impact = daily.groupby("Promotie_activa")[["Venit_zi", "Profit_zi"]].mean()
print("\n--- Impact promoții (medii pe zi) ---")
print(impact)

# Boxplot prețuri promo vs fără promo
plt.figure()
sim.boxplot(column="Pret", by="Promotie")
plt.suptitle("")
plt.title("Prețuri: promoție vs fără promoție")
plt.xlabel("Promoție")
plt.ylabel("Preț")
plt.tight_layout()
plt.show()
