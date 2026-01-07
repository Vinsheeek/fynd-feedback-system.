import streamlit as st
import pandas as pd
import json
from pathlib import Path

SUMMARY_FILE = Path("../data/summary.json")

st.set_page_config(
    page_title="Fynd Model Admin Dashboard",
    layout="wide"
)

st.title("🧠 Fynd Feedback Rating — Admin Evaluation Dashboard")

# ----------------------------
# Load summary.json
# ----------------------------
if not SUMMARY_FILE.exists():
    st.error(f"Summary file not found at: {SUMMARY_FILE}")
    st.stop()

summary = json.loads(SUMMARY_FILE.read_text())

# Convert to table format
rows = []
for version, data in summary.items():
    rows.append({
        "Prompt Version": version,
        "Total Entries": data.get("total_entries", 0),
        "Correct": data.get("correct", 0),
        "Incorrect": data.get("incorrect", 0),
        "Accuracy %": round(data.get("accuracy_percent", 0), 2)
    })

df = pd.DataFrame(rows)


# ----------------------------
# Global overview
# ----------------------------
st.subheader("📊 Model Performance Overview")

st.dataframe(df, use_container_width=True)


# ----------------------------
# Comparison charts
# ----------------------------
col1, col2 = st.columns(2)

with col1:
    st.subheader("🏆 Accuracy Comparison")
    st.bar_chart(df.set_index("Prompt Version")["Accuracy %"])

with col2:
    st.subheader("📥 Data Volume per Prompt")
    st.bar_chart(df.set_index("Prompt Version")["Total Entries"])


# ----------------------------
# Deep dive per version
# ----------------------------
st.subheader("🔎 Version-wise Error Analysis")

for version, data in summary.items():

    st.markdown(f"### ⚡ Prompt Version **{version}**")

    colA, colB, colC = st.columns(3)

    with colA:
        st.metric("Total Reviews", data.get("total_entries", 0))

    with colB:
        st.metric("Correct Predictions", data.get("correct", 0))

    with colC:
        st.metric("Incorrect Predictions", data.get("incorrect", 0))


    # Star counts distribution
    if "star_counts" in data:
        st.write("⭐ Star Rating Distribution")
        st.bar_chart(pd.Series(data["star_counts"]))

    # Show mismatch examples
    st.write("❌ Sample Mismatch Examples")

    examples = data.get("examples", [])

    bad_cases = [e for e in examples if e.get("predicted") != e.get("actual")]

    if bad_cases:
        st.json(bad_cases)
    else:
        st.success("No mismatch examples recorded.")
