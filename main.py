import tkinter as tk
from tkinter import ttk, filedialog, messagebox
import csv

# логіка
class Logic:
    def __init__(self):
        self.data = []  #список усіх рядків

    def load_csv(self, filename):
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader)  # Пропускаємо шапку 
                # Зберігаємо всі рядки у список
                self.data = [row for row in reader if row]
            return True
        except:
            return False

# Тільки вигляд
class App:
    def __init__(self, root):
        self.logic = Logic()
        self.root = root
        self.root.title("Farma Inc. - Incident Review")
        self.root.geometry("700x450")

        #  Кнопка
        btn = tk.Button(root, text=" Завантажити CSV", command=self.open_file, bg="#ddd", font=("Arial", 10))
        btn.pack(pady=10)

        # Таблиця 
        columns = ("ID", "Date", "Type", "Severity", "Description")
        self.tree = ttk.Treeview(root, columns=columns, show="headings")

        # налаштування колонок
        for col in columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, width=100 if col != "Description" else 300)

        self.tree.pack(expand=True, fill='both', padx=10, pady=(0, 10))

    def open_file(self):
        # вибір файла
        filename = filedialog.askopenfilename(filetypes=[("CSV Files", "*.csv")])
        
        if filename:
            if self.logic.load_csv(filename):
                self.show_data()
            else:
                messagebox.showerror("Помилка", "Не вдалося відкрити файл!")

    def show_data(self):
        # очищення таблиці
        for row in self.tree.get_children():
            self.tree.delete(row)

        # нові дані
        for row in self.logic.data:
            self.tree.insert("", tk.END, values=row)

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()

    
