# data_store.py

from dataclasses import dataclass, field
from typing import Dict

MonthName = str
Category = str
Day = int

@dataclass
class BudgetData:
    # {month: {category: amount}}
    monthly_plan: Dict[MonthName, Dict[Category, float]] = field(default_factory=dict)

    # {month: {day: {category: amount}}}
    daily_plan: Dict[MonthName, Dict[Day, Dict[Category, float]]] = field(default_factory=dict)

    # {month: income}
    monthly_income: Dict[MonthName, float] = field(default_factory=dict)

    def reset(self) -> None:
        self.monthly_plan.clear()
        self.daily_plan.clear()
        self.monthly_income.clear()
