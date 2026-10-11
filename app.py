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