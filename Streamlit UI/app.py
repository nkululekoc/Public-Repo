import streamlit as st


st.title("Support Ticket Classifier")

message = st.text_area("Paste customer message here", height = 20)

tone = st.selectbox("Response tone", ["Emphathetic","Professional","Firm"])

if st.button("Analyse & Respond"):
    st.write("Results will appear here - Gemini integration coming Saturday")

