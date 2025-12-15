import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

class Logic:
    def __init__(self):
        self.data = []

    def load_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader) # Пропускаємо заголовок
                self.data = [row for row in reader if row]
            return True
        except:
            return False

class App:
    def __init__(self, root):
        self.logic = Logic()
        self.root = root
        self.root.title("Farma Inc. - File checker")
        self.root.geometry("920x640")

        # Кнопка + Пошук
        top_frame = tk.Frame(root)
        top_frame.pack(fill=tk.X, padx=10, pady=10)

        # 1. Кнопка
        btn = tk.Button(top_frame, text=" Завантажити CSV", command=self.open_file, bg="#ddd")
        btn.pack(side=tk.LEFT)

        # 2. Пошук 
        tk.Label(top_frame, text=" Пошук:").pack(side=tk.LEFT, padx=(20, 5))
        
        self.search_var = tk.StringVar()
        self.search_var.trace("w", self.update_table) # Магія: слідкує за введенням тексту
        entry = tk.Entry(top_frame, textvariable=self.search_var, width=30)
        entry.pack(side=tk.LEFT)

        # --- ТАБЛИЦЯ ---
        columns = ("ID", "Date", "Type", "Severity", "Description")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")
        
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100 if col != "Description" else 300)

        self.tree.pack(expand=True, fill='both', padx=10, pady=(0, 10))

    def open_file(self):
        filename = filedialog.askopenfilename(filetypes=[("CSV", "*.csv")])
        if filename:
            if self.logic.load_csv(filename):
                self.update_table() # Оновлюємо таблицю після завантаження
            else:
                messagebox.showerror("Помилка", "Не вдалося прочитати файл")

    def update_table(self, *args):
        """Ця функція одночасно і показує дані, і фільтрує їх"""
        query = self.search_var.get().lower() # Текст з пошуку (маленькими літерами)
        
        # 1. Очищення
        for row in self.tree.get_children():
            self.tree.delete(row)

        # 2. Фільтрація та додавання
        for row in self.logic.data:
            # Перетворюємо весь рядок в текст і шукаємо там наш запит
            if query in str(row).lower():
                self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()