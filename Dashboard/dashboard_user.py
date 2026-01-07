import streamlit as st
import pandas as pd
from utils import load_summary

st.set_page_config(
    page_title="Fynd Model Evaluation Dashboard",
    layout="wide"
)

st.title("📊 Fynd Feedback Rating Model — Evaluation Dashboard")

summary = load_summary()

if not summary:
    st.warning("No evaluation summary found. Please run API first.")
    st.stop()

for version, data in summary.items():

    st.header(f"🧩 Prompt Version {version}")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Reviews", data.get("total_entries", 0))
    col2.metric("Correct Predictions", data.get("correct", 0))
    col3.metric("Accuracy %", round(data.get("accuracy_percent", 0), 2))

    st.subheader("⭐ Star Rating Distribution")
    st.bar_chart(pd.Series(data["star_counts"]))

    st.subheader("🔍 Sample Evaluations")
    st.json(data.get("examples", []))

