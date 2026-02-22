import streamlit as st
from pathlib import Path
import json
import random
import string

# ================= BANK CLASS =================
class Bank:
    database = "data.json"
    data = []

    # Load data
    if Path(database).exists():
        with open(database, "r") as fs:
            data = json.load(fs)
    else:
        data = []

    @classmethod
    def update(cls):
        with open(cls.database, "w") as fs:
            json.dump(cls.data, fs, indent=4)

    @staticmethod
    def generateAcc():
        digits = random.choices(string.digits, k=4)
        alpha = random.choices(string.ascii_letters, k=4)
        acc = digits + alpha
        random.shuffle(acc)
        return "".join(acc)

bank = Bank()

# ================= STREAMLIT UI =================
st.set_page_config(page_title="Bank App", page_icon="🏦")
st.title("🏦 Bank Management System")

menu = st.sidebar.selectbox(
    "Select Operation",
    ["Create Account", "Deposit Money", "Withdraw Money", "Account Details", "Delete Account"]
)

# ================= CREATE ACCOUNT =================
if menu == "Create Account":
    st.header("🆕 Create Account")

    name = st.text_input("Name")
    age = st.number_input("Age", min_value=1)
    phone = st.text_input("Phone Number")
    email = st.text_input("Email")
    pin = st.text_input("4 Digit PIN", type="password")

    if st.button("Create Account"):
        if age > 18 and len(pin) == 4 and len(phone) == 10:
            acc_no = Bank.generateAcc()
            info = {
                "name": name,
                "age": age,
                "phoneNo": int(phone),
                "email": email,
                "pin": int(pin),
                "account_no": acc_no,
                "balance": 0
            }
            Bank.data.append(info)
            Bank.update()

            st.success("✅ Account Created Successfully")
            st.info(f"Your Account Number: {acc_no}")
        else:
            st.error("❌ Invalid Details")

# ================= DEPOSIT =================
elif menu == "Deposit Money":
    st.header("💰 Deposit Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, max_value=10000)

    if st.button("Deposit"):
        user = [i for i in Bank.data if i["account_no"] == acc and i["pin"] == int(pin)]

        if not user:
            st.error("❌ User not found")
        else:
            user[0]["balance"] += amount
            Bank.update()
            st.success("✅ Amount Credited")

# ================= WITHDRAW =================
elif menu == "Withdraw Money":
    st.header("💸 Withdraw Money")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")
    amount = st.number_input("Amount", min_value=1, max_value=10000)

    if st.button("Withdraw"):
        user = [i for i in Bank.data if i["account_no"] == acc and i["pin"] == int(pin)]

        if not user:
            st.error("❌ User not found")
        elif user[0]["balance"] < amount:
            st.error("❌ Insufficient Balance")
        else:
            user[0]["balance"] -= amount
            Bank.update()
            st.success("✅ Amount Debited")

# ================= DETAILS =================
elif menu == "Account Details":
    st.header("📄 Account Details")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("View Details"):
        user = [i for i in Bank.data if i["account_no"] == acc and i["pin"] == int(pin)]

        if not user:
            st.error("❌ User not found")
        else:
            st.json(user[0])

# ================= DELETE =================
elif menu == "Delete Account":
    st.header("🗑️ Delete Account")

    acc = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password")

    if st.button("Delete Account"):
        user = [i for i in Bank.data if i["account_no"] == acc and i["pin"] == int(pin)]

        if not user:
            st.error("❌ User not found")
        else:
            Bank.data.remove(user[0])
            Bank.update()
            st.success("✅ Account Deleted Successfully")
