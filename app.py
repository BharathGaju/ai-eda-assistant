import streamlit as st
import pandas as pd
from groq import Groq
import matplotlib.pyplot as plt

import os
from dotenv import load_dotenv

load_dotenv()


# Groq API setup
API_KEY = os.getenv("GROQ_API_KEY")
client = Groq(api_key=API_KEY)

# Page title
st.title("🤖 AI-Powered EDA Assistant")
st.write("Upload a CSV file and I'll analyze it for you!")

# File uploader
uploaded_file = st.file_uploader("Choose a CSV file", type="csv")

if uploaded_file is not None:
    st.success("✅ File uploaded successfully!")

    # Read CSV
    df = pd.read_csv(uploaded_file)

    # Preview
    st.subheader("📋 Preview of your data")
    st.dataframe(df.head(10))

    # Basic info
    st.subheader("📊 Basic Information")
    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", df.shape[0])
    col2.metric("Columns", df.shape[1])
    col3.metric("Missing Values", df.isnull().sum().sum())

    # Statistical summary
    st.subheader("📈 Statistical Summary")
    st.dataframe(df.describe())

    # Column types
    st.subheader("🔍 Column Data Types")
    col_info = pd.DataFrame({
        'Column': df.columns,
        'Data Type': df.dtypes.values,
        'Missing Values': df.isnull().sum().values
    })
    st.dataframe(col_info)
    # Visualizations
    st.subheader("📊 Visualizations")

    # Get numeric columns only
    numeric_cols = df.select_dtypes(include='number').columns.tolist()

    if len(numeric_cols) >= 2:
        col1, col2 = st.columns(2)

        with col1:
            st.write("**Distribution Plot**")
            selected_col = st.selectbox("Select column", numeric_cols)
            fig, ax = plt.subplots()
            df[selected_col].hist(ax=ax, bins=20, color='skyblue', edgecolor='black')
            ax.set_title(f"Distribution of {selected_col}")
            ax.set_xlabel(selected_col)
            ax.set_ylabel("Frequency")
            st.pyplot(fig)

        with col2:
            st.write("**Correlation Heatmap**")
            fig2, ax2 = plt.subplots()
            import seaborn as sns
            sns.heatmap(df[numeric_cols].corr(), annot=True, fmt=".2f", cmap="coolwarm", ax=ax2)
            ax2.set_title("Correlation Heatmap")
            st.pyplot(fig2)

    # AI Analysis button
    st.subheader("🧠 AI Analysis")
    if st.button("✨ Generate AI Insights"):
        with st.spinner("AI is analyzing your data..."):

            # Prepare data summary for AI
            summary = f"""
            Dataset has {df.shape[0]} rows and {df.shape[1]} columns.
            Columns: {list(df.columns)}
            Data types: {df.dtypes.to_dict()}
            Statistical summary: {df.describe().to_string()}
            Missing values: {df.isnull().sum().to_dict()}
            """

            # Send to Groq AI
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a data analyst expert. Analyze the dataset and provide clear, useful insights."},
                    {"role": "user", "content": f"Analyze this dataset and give me: 1) Key insights 2) Interesting patterns 3) Any concerns or anomalies 4) Suggestions for further analysis\n\n{summary}"}
                ]
            )

            # Display AI response
            st.markdown(response.choices[0].message.content)
            # Chat with AI about your data
    st.subheader("💬 Ask AI About Your Data")
    user_question = st.text_input("Ask anything about your dataset...", 
                                   placeholder="e.g. What is the relationship between Income and Miles?")

    if user_question:
        with st.spinner("AI is thinking..."):
            summary = f"""
            Dataset has {df.shape[0]} rows and {df.shape[1]} columns.
            Columns: {list(df.columns)}
            Statistical summary: {df.describe().to_string()}
            """

            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": "You are a data analyst expert. Answer questions about the dataset clearly and concisely."},
                    {"role": "user", "content": f"Dataset info:\n{summary}\n\nQuestion: {user_question}"}
                ]
            )

            st.markdown("**🤖 AI Answer:**")
            st.markdown(response.choices[0].message.content)

else:
    st.info("👆 Please upload a CSV file to get started")