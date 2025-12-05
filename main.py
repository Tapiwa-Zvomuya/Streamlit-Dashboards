import streamlit as st

# Set page config
st.set_page_config(page_title="HBR - Uber Case Study Dashboard", layout="wide")

# Header with two logos and centered title
col1, col2, col3 = st.columns([1, 4, 1])

with col1:
    st.image("left_logo.png", use_column_width=True)

with col2:
    st.markdown(
        """
        <h1 style='text-align: center;'>HBR - Uber Case Study Dashboard</h1>
        """,
        unsafe_allow_html=True
    )

with col3:
    st.image("right_logo.png", use_column_width=True)

# Tabs
metadata_tab, dictionary_tab, viz_tab = st.tabs(["Metadata", "Data Dictionary", "Visualizations"])

with metadata_tab:
    st.header("Metadata")
    st.write("Add your metadata information here.")

with dictionary_tab:
    st.header("Data Dictionary")
    st.write("Add your data dictionary here.")

with viz_tab:
    st.header("Visualizations")
    st.write("Add your charts and visualizations here.")

