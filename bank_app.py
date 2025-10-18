import json
import random
import string
from pathlib import Path
import streamlit as st


# -------------------------------
# BANK CLASS
# -------------------------------
class Bank:
    database = 'data.json'
    data = []

    # Load data from JSON file
    try:
        if Path(database).exists():
            with open(database, 'r') as fs:
                data = json.load(fs)
        else:
            data = []
    except Exception as err:
        st.error(f"An exception occurred: {err}")
        data = []

    @classmethod
    def __update(cls):
        """Update JSON file with latest data"""
        with open(cls.database, 'w') as fs:
            json.dump(cls.data, fs, indent=4)

    @classmethod
    def __accountgenerate(cls):
        """Generate a random account number"""
        alpha = random.choices(string.ascii_uppercase, k=3)
        num = random.choices(string.digits, k=3)
        spchar = random.choices("!@#$%*", k=1)
        acc = alpha + num + spchar
        random.shuffle(acc)
        return "".join(acc)

    # -----------------------------
    # Bank operations
    # -----------------------------

    def createaccount(self, name, age, email, pin):
        if age < 18 or len(str(pin)) != 4:
            return "Sorry, you can't create an account (must be 18+ and 4-digit PIN)."

        info = {
            "name": name,
            "age": age,
            "email": email,
            "pin": pin,
            "accountNo": Bank.__accountgenerate(),
            "balance": 0
        }

        Bank.data.append(info)
        Bank.__update()
        return f"Account created successfully!\nAccount No: {info['accountNo']}"

    def find_user(self, accountnumber, pin):
        for user in Bank.data:
            if user['accountNo'] == accountnumber and user['pin'] == pin:
                return user
        return None

    def depositmoney(self, accountnumber, pin, amount):
        user = self.find_user(accountnumber, pin)
        if not user:
            return "Account not found."
        if amount <= 0 or amount > 10000:
            return "Invalid amount (must be between 1 and 10000)."

        user['balance'] += amount
        Bank.__update()
        return f"Deposited ₹{amount} successfully. New balance: ₹{user['balance']}"

    def withdrawmoney(self, accountnumber, pin, amount):
        user = self.find_user(accountnumber, pin)
        if not user:
            return "Account not found."
        if amount <= 0:
            return "Invalid amount."
        if user['balance'] < amount:
            return "Insufficient balance."

        user['balance'] -= amount
        Bank.__update()
        return f"Withdrew ₹{amount} successfully. Remaining balance: ₹{user['balance']}"

    def showdetails(self, accountnumber, pin):
        user = self.find_user(accountnumber, pin)
        if not user:
            return None
        return user

    def updatedetails(self, accountnumber, pin, name=None, email=None, new_pin=None):
        user = self.find_user(accountnumber, pin)
        if not user:
            return "No such user found."

        if name:
            user['name'] = name
        if email:
            user['email'] = email
        if new_pin:
            if len(str(new_pin)) == 4:
                user['pin'] = int(new_pin)

        Bank.__update()
        return "Details updated successfully!"

    def delete(self, accountnumber, pin):
        user = self.find_user(accountnumber, pin)
        if not user:
            return "No such account exists."
        Bank.data.remove(user)
        Bank.__update()
        return "Account deleted successfully."


# -------------------------------
# STREAMLIT APP UI
# -------------------------------
st.set_page_config(page_title="💰 Bank Management System", layout="centered")
st.title("🏦 Bank Management System")

bank = Bank()

menu = ["Create Account", "Deposit Money", "Withdraw Money", "Show Details", "Update Details", "Delete Account"]
choice = st.sidebar.selectbox("Select Operation", menu)

# CREATE ACCOUNT
if choice == "Create Account":
    st.subheader("🧾 Create New Account")
    name = st.text_input("Enter your name")
    age = st.number_input("Enter your age", min_value=0, step=1)
    email = st.text_input("Enter your email")
    pin = st.text_input("Set a 4-digit PIN", type="password")

    if st.button("Create Account"):
        if name and age and email and pin:
            result = bank.createaccount(name, age, email, int(pin))
            st.success(result)
        else:
            st.warning("Please fill all fields!")

# DEPOSIT MONEY
elif choice == "Deposit Money":
    st.subheader("💵 Deposit Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to deposit", min_value=1, step=1)

    if st.button("Deposit"):
        st.success(bank.depositmoney(acc, int(pin), amount))

# WITHDRAW MONEY
elif choice == "Withdraw Money":
    st.subheader("💸 Withdraw Money")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount to withdraw", min_value=1, step=1)

    if st.button("Withdraw"):
        st.success(bank.withdrawmoney(acc, int(pin), amount))

# SHOW DETAILS
elif choice == "Show Details":
    st.subheader("📜 Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Show"):
        details = bank.showdetails(acc, int(pin))
        if details:
            st.json(details)
        else:
            st.error("No account found with given details.")

# UPDATE DETAILS
elif choice == "Update Details":
    st.subheader("🛠 Update Account Details")
    acc = st.text_input("Account Number")
    pin = st.text_input("Old PIN", type="password")
    name = st.text_input("New Name (leave blank to skip)")
    email = st.text_input("New Email (leave blank to skip)")
    new_pin = st.text_input("New PIN (leave blank to skip)")

    if st.button("Update"):
        st.success(bank.updatedetails(acc, int(pin), name, email, new_pin))

# DELETE ACCOUNT
elif choice == "Delete Account":
    st.subheader("🗑 Delete Account")
    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete"):
        st.warning(bank.delete(acc, int(pin)))
