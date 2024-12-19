import tkinter as tk
from tkinter import messagebox, simpledialog

class BankingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Banking Application")
        self.root.geometry("300x400")
        self.balance = 0.0

        # Background color
        self.root.config(bg="purple")
        
        # Title label
        self.title_label = tk.Label(self.root, text="Banking Application", font=("Helvetica", 24), bg="#5F9EA0", fg="white")
        self.title_label.pack(pady=10)

        # Balance Label
        self.balance_label = tk.Label(self.root, text=f"Balance: ${self.balance:.2f}", font=("Helvetica", 18), bg="#5F9EA0", fg="white")
        self.balance_label.pack(pady=10)

        # Deposit Button
        self.deposit_button = tk.Button(self.root, text="Deposit", font=("Helvetica", 14), bg="#4CAF50", fg="white", command=self.deposit)
        self.deposit_button.pack(pady=10, fill='x')

        # Withdraw Button
        self.withdraw_button = tk.Button(self.root, text="Withdraw", font=("Helvetica", 14), bg="#F44336", fg="white", command=self.withdraw)
        self.withdraw_button.pack(pady=10, fill='x')

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", font=("Helvetica", 14), bg="#808080", fg="white", command=self.root.quit)
        self.exit_button.pack(pady=10, fill='x')

    def update_balance(self):
        self.balance_label.config(text=f"Balance: ${self.balance:.2f}")

    def deposit(self):
        amount = self.prompt_amount("deposit")
        if amount is not None:
            self.balance += amount
            self.update_balance()
            messagebox.showinfo("Deposit Successful", f"${amount:.2f} deposited successfully!")

    def withdraw(self):
        amount = self.prompt_amount("withdraw")
        if amount is not None:
            if amount > self.balance:
                messagebox.showerror("Insufficient Funds", "You do not have enough balance to withdraw this amount!")
            else:
                self.balance -= amount
                self.update_balance()
                messagebox.showinfo("Withdraw Successful", f"${amount:.2f} withdrawn successfully!")

    def prompt_amount(self, action):
        amount = simpledialog.askfloat("Amount", f"Enter amount to {action}:", parent=self.root, minvalue=0)
        if amount is None or amount <= 0:
            messagebox.showerror("Invalid Amount", "Please enter a valid positive amount!")
            return None
        return amount

if __name__ == "__main__":
    root = tk.Tk()
    app = BankingApp(root)
    root.mainloop()



