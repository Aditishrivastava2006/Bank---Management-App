import streamlit as st

# ---------- Page Config ----------
st.set_page_config(
    page_title="Bank Management App",
    page_icon="🏦",
    layout="centered"
)

# ---------- Session State ----------
if "balance" not in st.session_state:
    st.session_state.balance = 0

if "history" not in st.session_state:
    st.session_state.history = []

# ---------- UI ----------
st.title("🏦 Bank Management System")
st.caption("Mini Project using Streamlit (College Project)")

st.divider()

st.metric("💰 Current Balance", f"₹ {st.session_state.balance}")

amount = st.number_input(
    "Enter Amount",
    min_value=0,
    step=100
)

col1, col2 = st.columns(2)

with col1:
    if st.button("➕ Deposit", use_container_width=True):
        st.session_state.balance += amount
        st.session_state.history.append(f"Deposited ₹{amount}")
        st.success(f"₹{amount} deposited successfully!")

with col2:
    if st.button("➖ Withdraw", use_container_width=True):
        if amount <= st.session_state.balance:
            st.session_state.balance -= amount
            st.session_state.history.append(f"Withdrawn ₹{amount}")
            st.success(f"₹{amount} withdrawn successfully!")
        else:
            st.error("❌ Insufficient Balance")

st.divider()

# ---------- Transaction History ----------
st.subheader("📜 Transaction History")

if st.session_state.history:
    for i, item in enumerate(st.session_state.history, 1):
        st.write(f"{i}. {item}")
else:
    st.info("No transactions yet.")

st.divider()
st.caption("👩‍🎓 College Mini Project | Streamlit App")
       
