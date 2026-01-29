# main.py

import tkinter as tk
from ui import BudgetApp

def main():
    root = tk.Tk()
    app = BudgetApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
