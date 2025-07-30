import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Zomato Data Analysis", layout="wide")
st.title("🍽️ Zomato Data Analysis Dashboard")

# --- Step 1: Select Data Source ---
data_source = st.radio("Select Data Source:", ["Upload your own CSV", "Use sample Zomato dataset"])

df = None  # Initialize dataframe

# --- Step 2: Load Data ---
if data_source == "Upload your own CSV":
    uploaded_file = st.file_uploader("Upload your Zomato dataset (CSV)", type=["csv"])
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
else:
    # Replace with your actual GitHub raw file link
    SAMPLE_CSV_URL = "https://raw.githubusercontent.com/PoojaJogdand4511/zomato-data-analysis-project/main/uploaded_data.csv"
    try:
        df = pd.read_csv(SAMPLE_CSV_URL)
        st.success("✅ Sample Zomato dataset loaded!")
    except Exception as e:
        st.error("⚠️ Failed to load sample dataset. Check your GitHub URL.")

# --- Step 3: If data is loaded, show insights ---
if df is not None:
    st.subheader("📊 Sample of Dataset")
    st.dataframe(df.head(10))

    st.subheader("🍴 Cuisine Distribution")
    if 'Cuisines' in df.columns:
        cuisine_counts = df['Cuisines'].value_counts().head(10)
        st.bar_chart(cuisine_counts)

    st.subheader("🏙️ Restaurant Types")
    if 'Restaurant Type' in df.columns:
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.countplot(data=df, y='Restaurant Type', order=df['Restaurant Type'].value_counts().index[:10], ax=ax)
        st.pyplot(fig)

    st.subheader("💰 Cost for Two Analysis")
    if 'Average Cost for two' in df.columns:
        fig2, ax2 = plt.subplots()
        sns.histplot(df['Average Cost for two'].dropna(), bins=20, kde=True, ax=ax2)
        st.pyplot(fig2)

    st.subheader("⭐ Ratings")
    if 'Aggregate rating' in df.columns:
        fig3, ax3 = plt.subplots()
        sns.histplot(df['Aggregate rating'].dropna(), bins=20, kde=True, ax=ax3)
        st.pyplot(fig3)
