# ui.py

import tkinter as tk
from tkinter import messagebox
import calendar
from datetime import datetime

import styles
from data_store import BudgetData
import logic

class BudgetApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Budget Planner Anual")
        self.root.geometry("1050x650")
        self.root.configure(bg=styles.BG_MAIN)

        self.data = BudgetData()
        self.months = list(calendar.month_name)[1:]
        self.year = datetime.now().year

        self.selected_day = None

        self.month_var = tk.StringVar(value=self.months[0])# variabila tk care tine luna selectata

        # ===== MENIU =====
        self.menu_frame = tk.Frame(self.root, bg=styles.BG_MAIN)
        self.menu_frame.pack(fill="both", expand=True)

        tk.Label(
            self.menu_frame,
            text="Alege tipul de planificare:",
            font=styles.FONT_TITLE,
            bg=styles.BG_MAIN
        ).pack(pady=20)

        tk.Button(                     # buton „Plan pe zile” → deschide calendarul
            self.menu_frame,
            text="Plan pe zile",
            width=20,
            bg=styles.BTN_COLOR,
            fg=styles.BTN_TEXT,
            command=self.open_daily_budget
        ).pack(pady=10)

        tk.Button(              #buton „Plan pe luna” → deschide pagina de buget lunar
            self.menu_frame,
            text="Plan pe lună",
            width=20,
            bg=styles.BTN_COLOR,
            fg=styles.BTN_TEXT,
            command=self.open_monthly_budget
        ).pack(pady=10)

        # ===== DAILY PAGE =====
        self.daily_frame = tk.Frame(self.root, bg=styles.BG_MAIN) #Creează pagina „Plan pe zile”


        self.daily_top = tk.Frame(self.daily_frame, bg=styles.BG_PANEL)
        self.daily_top.pack(fill="x", padx=10, pady=10)

        tk.Button(        #Apasa → revii la meniu și se reseteaza.
            self.daily_top,
            text="⬅ Înapoi la meniu",
            bg=styles.BTN_BACK_BG,
            fg=styles.BTN_BACK_FG,
            command=self.back_to_menu
        ).pack(side="left", padx=5)

        tk.Label(self.daily_top, text="Venit lunar:", bg=styles.BG_PANEL).pack(side="left", padx=5)
        self.income_entry_daily = tk.Entry(self.daily_top, width=10)  #Caseta unde scrii venitul.
        self.income_entry_daily.pack(side="left")

        tk.Button(
            self.daily_top,
            text="Setează venitul",
            bg=styles.BTN_COLOR,
            fg=styles.BTN_TEXT,
            command=self.set_income_daily  #Când apeși „Setează venitul”, se citește venitul și se salvează.
        ).pack(side="left", padx=5)

        tk.Label(self.daily_top, text="Luna:", bg=styles.BG_PANEL).pack(side="left", padx=5)
        tk.OptionMenu(
            self.daily_top,
            self.month_var,
            *self.months,
            command=lambda _: (self.draw_calendar(), self.update_summary())
        ).pack(side="left")

        tk.Button(
            self.daily_top,
            text="Calculează anul",
            bg=styles.BTN_YEAR_BG,
            fg=styles.BTN_YEAR_FG,
            command=self.calc_year
        ).pack(side="right", padx=10)

        self.calendar_frame = tk.Frame(self.daily_frame, bg=styles.BG_PANEL, padx=10, pady=10) #creeaza calendarul
        self.calendar_frame.pack(side="left", padx=10, pady=10)

        self.right = tk.Frame(self.daily_frame, bg=styles.BG_PANEL, padx=20, pady=20) #creaza panoul din dreapta
        self.right.pack(side="right", fill="y")

        self.selected_day_label = tk.Label(self.right, text="Zi selectată: -", bg=styles.BG_PANEL)
        self.selected_day_label.pack(pady=5)

        tk.Label(self.right, text="Categorie", bg=styles.BG_PANEL).pack()
        self.day_cat = tk.Entry(self.right)
        self.day_cat.pack()

        tk.Label(self.right, text="Sumă", bg=styles.BG_PANEL).pack()
        self.day_amt = tk.Entry(self.right)
        self.day_amt.pack()

        tk.Button(
            self.right,
            text="Adaugă cheltuială",
            bg=styles.BTN_COLOR,
            fg=styles.BTN_TEXT,
            command=self.add_daily
        ).pack(pady=10)

        # ===== MONTHLY PAGE =====
        self.monthly_frame = tk.Frame(self.root, bg=styles.BG_MAIN)

        self.monthly_top = tk.Frame(self.monthly_frame, bg=styles.BG_PANEL)
        self.monthly_top.pack(fill="x", padx=10, pady=10)

        tk.Button(
            self.monthly_top,
            text="⬅ Înapoi la meniu",
            bg=styles.BTN_BACK_BG,
            fg=styles.BTN_BACK_FG,
            command=self.back_to_menu
        ).pack(side="left", padx=5)

        tk.Label(self.monthly_top, text="Luna:", bg=styles.BG_PANEL).pack(side="left", padx=5)
        tk.OptionMenu(
            self.monthly_top,
            self.month_var,
            *self.months,
            command=lambda _: self.update_summary()
        ).pack(side="left", padx=5)

        tk.Button(
            self.monthly_top,
            text="Calculează anul",
            bg=styles.BTN_YEAR_BG,
            fg=styles.BTN_YEAR_FG,
            command=self.calc_year
        ).pack(side="right", padx=10)

        self.monthly_body = tk.Frame(self.monthly_frame, bg=styles.BG_MAIN)
        self.monthly_body.pack(fill="both", expand=True, padx=10, pady=10)

        tk.Label(self.monthly_body, text="Venit lunar:", bg=styles.BG_MAIN).pack(pady=5)
        self.income_entry_monthly = tk.Entry(self.monthly_body, width=10)
        self.income_entry_monthly.pack(pady=5)

        tk.Button(
            self.monthly_body,
            text="Setează venitul",
            bg=styles.BTN_COLOR,
            fg=styles.BTN_TEXT,
            command=self.set_income_monthly
        ).pack(pady=5)

        tk.Label(self.monthly_body, text="Categorie", bg=styles.BG_MAIN).pack(pady=5)
        self.month_cat = tk.Entry(self.monthly_body)
        self.month_cat.pack()

        tk.Label(self.monthly_body, text="Sumă", bg=styles.BG_MAIN).pack(pady=5)
        self.month_amt = tk.Entry(self.monthly_body)
        self.month_amt.pack()

        tk.Button(
            self.monthly_body,
            text="Adaugă cheltuială lunară",
            bg=styles.BTN_COLOR,
            fg=styles.BTN_TEXT,
            command=self.add_monthly
        ).pack(pady=10)

        # ===== SUMMARY (comun) =====
        self.summary = tk.Text(self.root, height=6, bg=styles.SUMMARY_BG, font=styles.FONT_SUMMARY)
        # NU facem pack acum; apare doar când intri în buget

    # ---------- Navigare ----------
    def back_to_menu(self):
        self.daily_frame.pack_forget()
        self.monthly_frame.pack_forget()

        # reset TOTAL
        self.data.reset()
        self.selected_day = None
        self.month_var.set(self.months[0])

        self.income_entry_daily.delete(0, tk.END)
        self.income_entry_monthly.delete(0, tk.END)
        self.day_cat.delete(0, tk.END)
        self.day_amt.delete(0, tk.END)
        self.month_cat.delete(0, tk.END)
        self.month_amt.delete(0, tk.END)

        self.selected_day_label.config(text="Zi selectată: -")

        self.summary.delete("1.0", tk.END)
        self.summary.pack_forget()

        self.menu_frame.pack(fill="both", expand=True)

    def open_daily_budget(self):
        self.menu_frame.pack_forget()
        self.daily_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.summary.pack(fill="x", padx=10, pady=10)
        self.draw_calendar()
        self.update_summary()

    def open_monthly_budget(self):
        self.menu_frame.pack_forget()
        self.monthly_frame.pack(fill="both", expand=True, padx=10, pady=10)
        self.summary.pack(fill="x", padx=10, pady=10)
        self.update_summary()

    # ---------- Calendar ----------
    def draw_calendar(self):
        for w in self.calendar_frame.winfo_children():
            w.destroy()

        month = self.month_var.get()
        if not month:
            return

        m_index = self.months.index(month) + 1         #Transformă luna în număr și obține structura
        cal = calendar.monthcalendar(self.year, m_index)  # calendarului (săptămâni + zile).

        days = ["S", "M", "T", "W", "T", "F", "S"]
        for i, d in enumerate(days):
            tk.Label(              # Afișează antetul calendarului.
                self.calendar_frame,
                text=d,
                bg=styles.BG_PANEL,
                font=styles.FONT_CAL_HEADER
            ).grid(row=0, column=i)

        for r, week in enumerate(cal, start=1):
            for c, day in enumerate(week):
                if day == 0: #daca ziua nu e in luna
                    tk.Label(self.calendar_frame, text="", bg=styles.BG_PANEL).grid(row=r, column=c) #afiseaza un spatiu gol
                else:
                    has_data = month in self.data.daily_plan and day in self.data.daily_plan[month]#Verifică dacă ziua are cheltuieli
                    color = styles.DAY_DONE if has_data else "white" #verde → are cheltuieli, alb → nu are
                    tk.Button(   #creeaza butoanele pt zile din calendar
                        self.calendar_frame,
                        text=day,
                        width=4,
                        bg=color,
                        command=lambda d=day: self.select_day(d)
                    ).grid(row=r, column=c, padx=2, pady=2)

    def select_day(self, day: int):
        self.selected_day = day
        self.selected_day_label.config(text=f"Zi selectată: {day}") #Actualizează textul din dreapta („Zi selectată: 15”)

    # ---------- Actions ----------
    def set_income_daily(self):
        month = self.month_var.get()
        try:
            income = float(self.income_entry_daily.get()) #Citește venitul scris de utilizator și îl transformă în număr
        except:
            messagebox.showerror("Eroare", "Venit invalid")
            return
        logic.set_income(self.data, month, income)
        self.update_summary() #Salvează venitul în datele aplicației

    def set_income_monthly(self):
        month = self.month_var.get()
        try:
            income = float(self.income_entry_monthly.get())
        except:
            messagebox.showerror("Eroare", "Venit invalid")
            return
        logic.set_income(self.data, month, income)
        self.update_summary()

    def add_daily(self):
        if self.selected_day is None:
            messagebox.showerror("Eroare", "Selectează o zi!")
            return

        month = self.month_var.get()
        cat = self.day_cat.get().strip()
        if not cat:
            messagebox.showerror("Eroare", "Introdu o categorie!")
            return

        try:
            amt = float(self.day_amt.get()) #Ia suma scrisă și încearcă să o transforme în număr.
        except:
            messagebox.showerror("Eroare", "Sumă invalidă")
            return

        logic.add_daily_expense(self.data, month, self.selected_day, cat, amt)#Salvează cheltuiala în datele aplicației (logica e în logic.py).

        self.day_cat.delete(0, tk.END)
        self.day_amt.delete(0, tk.END)#Golește câmpurile „Categorie” și „Sumă” după salvare.

        self.draw_calendar()#reface cal. pt a colora ziua la care am adaugat cv
        self.update_summary()

    def add_monthly(self):
        month = self.month_var.get()#Ia luna selectată din dropdown.
        cat = self.month_cat.get().strip() #Ia categoria scrisă de utilizator și elimină spațiile inutile.
        if not cat:
            messagebox.showerror("Eroare", "Introdu o categorie!")
            return

        try:
            amt = float(self.month_amt.get())
        except:
            messagebox.showerror("Eroare", "Sumă invalidă")
            return

        logic.add_monthly_expense(self.data, month, cat, amt)

        self.month_cat.delete(0, tk.END)
        self.month_amt.delete(0, tk.END)

        self.update_summary()

    def update_summary(self):
        self.summary.delete("1.0", tk.END) #Șterge tot textul vechi din caseta de raport.

        month = self.month_var.get()
        income, exp_m, exp_d, balance = logic.monthly_summary(self.data, month)#Cere din logic.py:venitul,
                                                                   # cheltuieli lunare,cheltuieli zilnice,balanța
#le afiseaza in raport
        self.summary.insert(tk.END, f"Luna: {month}\n")
        self.summary.insert(tk.END, f"Venit: {income:.2f} lei\n")
        self.summary.insert(tk.END, f"Cheltuieli lunare: {exp_m:.2f} lei\n")
        self.summary.insert(tk.END, f"Cheltuieli zilnice: {exp_d:.2f} lei\n")
        self.summary.insert(tk.END, f"Balanță: {balance:.2f} lei\n")

    def calc_year(self):
        total_income, total_expenses, balance, category_totals = logic.annual_report(self.data)#le cere din logic.py

        if category_totals: #daca exista cat., creează o listă cu categoriile și sumele, ordonate descrescător.
            lines = [
                f"• {cat}: {amt:.2f} lei"
                for cat, amt in sorted(category_totals.items(), key=lambda x: x[1], reverse=True)
            ]
            categories_text = "\n".join(lines)
        else:
            categories_text = "Nu ai introdus cheltuieli în nicio categorie."

        messagebox.showinfo(
            "Rezultat anual",
            f"Venit total anual: {total_income:.2f} lei\n"
            f"Cheltuieli totale: {total_expenses:.2f} lei\n"
            f"Rămâi cu: {balance:.2f} lei\n\n"
            f"Cheltuieli pe categorii:\n{categories_text}"
        )
