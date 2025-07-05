import streamlit as st
import pandas as pd
import requests
import os

st.set_page_config(page_title="GPT PayAudit", layout="wide")
st.title("💳 GPT-PayAudit – Smart Payment Anomaly Detector")

# 📤 Upload section
uploaded_file = st.file_uploader("Upload Payment CSV", type="csv")

if uploaded_file:
    with st.spinner("Uploading file..."):
        response = requests.post(
            "http://localhost:8000/upload/",
            files={"file": uploaded_file.getvalue()},
            headers={"accept": "application/json"}
        )

    if response.status_code == 200:
        st.success("✅ File uploaded successfully!")
        filename = uploaded_file.name

        # 🔍 Analyze file
        with st.spinner("Analyzing for anomalies..."):
            analyze_url = f"http://localhost:8000/analyze/{filename}"
            result = requests.get(analyze_url).json()

        st.subheader("🧠 GPT Audit Summary")
        st.markdown(result["gpt_summary"])

        st.subheader("⚠️ Flagged Transactions")
        flagged_df = pd.DataFrame(result["raw"])
        st.dataframe(flagged_df, use_container_width=True)

        # 📊 Vendor Anomaly Chart
        if "Vendor" in flagged_df.columns:
            st.subheader("📊 Vendor-wise Anomalies")
            vendor_chart = flagged_df["Vendor"].value_counts()
            st.bar_chart(vendor_chart)

        # 📊 Monthly Spend Chart
        if "Date" in flagged_df.columns and "Amount" in flagged_df.columns:
            st.subheader("📆 Monthly Spend (Flagged)")
            flagged_df["Date"] = pd.to_datetime(flagged_df["Date"])
            flagged_df["Month"] = flagged_df["Date"].dt.to_period("M").astype(str)
            monthly_chart = flagged_df.groupby("Month")["Amount"].sum()
            st.line_chart(monthly_chart)

        # 📥 Download PDF Report
        st.subheader("📥 Download Full Report")
        pdf_path = f"data/{filename}_report.pdf"
        if os.path.exists(pdf_path):
            with open(pdf_path, "rb") as f:
                st.download_button(
                    label="📄 Download Audit Report (PDF)",
                    data=f,
                    file_name=f"{filename}_report.pdf",
                    mime="application/pdf"
                )
        else:
            st.warning("⚠️ Report not generated yet.")

    else:
        st.error("❌ Upload failed. Try again.")
