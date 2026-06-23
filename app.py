import streamlit as st
import pandas as pd
import numpy as np
import io

# Set up the Streamlit Page Configuration 
st.set_page_config(
    page_title="Universal AI Data Cleaning Pipeline",
    layout="wide" # Switched to wide layout for side-by-side controls
)

# Create main header
st.title("🛠️ Universal AI Data Cleaning Pipeline")
st.write("Upload *any* CSV file, select your custom cleaning rules, and instantly download a polished Excel spreadsheet.")

st.divider()

# File uploader widget
uploaded_file = st.file_uploader("Choose any CSV file", type=["csv"])

if uploaded_file is not None:
    # Read the data once
    df_raw = pd.read_csv(uploaded_file)
    all_columns = df_raw.columns.tolist()

    st.success("File uploaded successfully!")
    
    # Create side-by-side layout: Left for options, Right for preview
    col1, col2 = st.columns([1, 2])

    with col1:
        st.subheader("⚙️ Cleaning Configuration")
        
        # Rule 1: Select columns to strip currency symbols and force to numeric
        numeric_cols = st.multiselect(
            "Select columns to clean as Numeric (removes $, commas, etc.):",
            options=all_columns
        )
        
        # Rule 2: Fix negatives
        fix_negatives = st.checkbox("Convert negative values to NaN in numeric columns", value=True)
        
        # Rule 3: Drop missing rows
        drop_nans = st.checkbox("Drop rows containing missing (NaN) values", value=True)
        
        # Rule 4: Cast column data types
        st.markdown("---")
        st.write("**Integer Conversion**")
        int_cols = st.multiselect("Select columns to force into integers (e.g., IDs):", options=all_columns)

    with col2:
        st.subheader("📋 Original Data Preview")
        st.dataframe(df_raw.head(10))

    st.divider()

    # Processing the button
    if st.button("🚀 Run Custom Cleaning Pipeline"):
        with st.spinner("Executing your custom cleaning rules..."):
            
            # Start with a clean copy of raw data
            df_cleaned = df_raw.copy()

            # 1. Handle Currency / Numeric cleaning on user-selected columns
            for col in numeric_cols:
                df_cleaned[col] = df_cleaned[col].astype(str).str.replace('$', '', regex=False)
                df_cleaned[col] = df_cleaned[col].str.replace(',', '', regex=False) # handle thousands separators
                df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce')

            # 2. Handle Negative values if checked
            if fix_negatives and len(numeric_cols) > 0:
                for col in numeric_cols:
                    df_cleaned.loc[df_cleaned[col] < 0, col] = np.nan

            # 3. Drop missing values if checked
            if drop_nans:
                df_cleaned = df_cleaned.dropna().copy()

            # 4. Handle Integer conversions
            for col in int_cols:
                if col in df_cleaned.columns:
                    df_cleaned[col] = pd.to_numeric(df_cleaned[col], errors='coerce').fillna(0).astype(int)

            # --- Output Display ---
            st.success("Pipeline executed successfully based on your rules!")
            st.subheader("✨ Cleaned Data Preview")
            st.dataframe(df_cleaned.head(10))

            # Prepare the excel download link memory
            buffer = io.BytesIO()
            with pd.ExcelWriter(buffer, engine="openpyxl") as writer:
                df_cleaned.to_excel(writer, index=False, sheet_name="Cleaned Data")

            # Create download button
            st.download_button(
                label="📥 Download Cleaned Excel Report",
                data=buffer.getvalue(),
                file_name="custom_cleaned_data.xlsx",
                mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
            )