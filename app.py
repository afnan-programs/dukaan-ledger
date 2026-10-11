import streamlit as st

st.set_page_config(
    page_title="Dukaan Ledger",
    page_icon="📊",
    layout="wide"
)

st.title("Dukaan Ledger")
st.write("Wholesale Business Management System")
st.divider()
st.subheader("Business Overview")
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Sales", "Rs. 0")

with col2:
    st.metric("Outstanding Payments", "Rs. 0")

with col3:
    st.metric("Stock Items", "0")

st.divider()

st.subheader("Quick Actions")

option = st.selectbox(
    "Select an action",
    ("Select an Option","Add New Sale", "Add New Purchase", "View Sales Report", "View Purchase Report", "View Customer Ledger", "Manage Stock")
)

if option != "Select an Option":
    st.info(f"{option} functionality is under development.")
