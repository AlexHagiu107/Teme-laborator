# logic.py

from typing import Dict, Tuple
from data_store import BudgetData

def set_income(data: BudgetData, month: str, income: float) -> None:
    data.monthly_income[month] = income #Salvează venitul în dicționarul monthly_income pentru luna respectivă.

#adaugă suma la categoria X în luna Y
def add_monthly_expense(data: BudgetData, month: str, category: str, amount: float) -> None:
    data.monthly_plan.setdefault(month, {})
    data.monthly_plan[month][category] = data.monthly_plan[month].get(category, 0.0) + amount

#în luna X, în ziua Y, la categoria Z, adaugă suma
def add_daily_expense(data: BudgetData, month: str, day: int, category: str, amount: float) -> None:
    data.daily_plan.setdefault(month, {})
    data.daily_plan[month].setdefault(day, {})
    data.daily_plan[month][day][category] = data.daily_plan[month][day].get(category, 0.0) + amount


def monthly_summary(data: BudgetData, month: str) -> Tuple[float, float, float, float]:
    """Returnează: income, monthly_expenses, daily_expenses, balance"""
    income = float(data.monthly_income.get(month, 0.0))#Ia venitul lunii; dacă nu există, 0.
    expenses_monthly = sum(data.monthly_plan.get(month, {}).values()) #Ia toate sumele din cheltuielile lunare și le adună.
    expenses_daily = sum(sum(day.values()) for day in data.daily_plan.get(month, {}).values())
    balance = income - expenses_monthly - expenses_daily
    return income, expenses_monthly, expenses_daily, balance

def annual_report(data: BudgetData) -> Tuple[float, float, float, Dict[str, float]]:
    """Returnează: total_income, total_expenses, balance, category_totals"""
    total_income = sum(data.monthly_income.values()) #Adună toate veniturile salvate pe luni.

#Pentru fiecare lună (m), adună categoriile, apoi adună lunile între ele.
    total_monthly_expenses = sum(sum(m.values()) for m in data.monthly_plan.values())

    #Cheltuieli anuale (zilnice)
    total_daily_expenses = sum(
        sum(sum(day.values()) for day in month.values())
        for month in data.daily_plan.values()
    )

#Total cheltuieli + balanță
    total_expenses = total_monthly_expenses + total_daily_expenses
    balance = total_income - total_expenses

    category_totals: Dict[str, float] = {}#Dicționar gol care va ține totalul pe categorie.

#Adună categoriile din planul lunar
    for m in data.monthly_plan.values():
        for cat, amt in m.items():
            category_totals[cat] = category_totals.get(cat, 0.0) + amt

#Adună categoriile din planul zilnic
    for m in data.daily_plan.values():
        for d in m.values():
            for cat, amt in d.items():
                category_totals[cat] = category_totals.get(cat, 0.0) + amt

    return total_income, total_expenses, balance, category_totals #Return final
