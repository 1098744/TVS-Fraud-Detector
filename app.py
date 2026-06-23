import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(
    page_title="TVS Motor Insurance Fraud Detector",
    layout="wide"
)

# TVS Logo
st.image("tvs.png", width=300)

# Title
st.title("TVS Motor Insurance Fraud Detector")

st.markdown("---")

st.write("Upload an Excel or CSV claim file for fraud analysis.")

# Upload File
uploaded_file = st.file_uploader(
    "Upload Claim File",
    type=["xlsx", "xls", "csv"]
)

if uploaded_file is not None:

    st.success("✅ File Uploaded Successfully")

    st.write("### File Name")
    st.write(uploaded_file.name)

    # Read File
    try:

        if uploaded_file.name.endswith(".csv"):
            df = pd.read_csv(uploaded_file)
        else:
            df = pd.read_excel(uploaded_file)

        st.write("### Claim Data Preview")
        st.dataframe(df)

        if st.button("🔍 Analyze Fraud"):

            fraud_score = 0

            # Sample Fraud Rules
            if len(df) > 10:
                fraud_score += 20

            if len(df) > 50:
                fraud_score += 20

            if len(df) > 100:
                fraud_score += 20

            st.success("✅ Fraud Analysis Completed")

            st.metric(
                label="Fraud Score",
                value=f"{fraud_score}%"
            )

            if fraud_score >= 60:
                st.error("🔴 HIGH FRAUD RISK")

            elif fraud_score >= 30:
                st.warning("🟡 MEDIUM FRAUD RISK")

            else:
                st.success("🟢 LOW FRAUD RISK")

    except Exception as e:
        st.error(f"Error reading file: {e}")

st.markdown("---")
st.caption("TVS Motor Insurance Fraud Detection System")