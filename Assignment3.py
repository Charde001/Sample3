import numpy as np
import matplotlib.pyplot as plt
import streamlit as st

import pandas as pd

st.title("This is My App")

uploaded_file = st.file_uploader("upload file", type={"csv", "txt"})

if uploaded_file is not None:

    df = pd.read_csv(uploaded_file)

    st.write(df)

# Set the page title
st.set_page_config(page_title="Normal Distribution App")

# App title
st.title("Normal Distribution Generator")

# Sidebar for user input
st.sidebar.header("Input Parameters")

mean = st.sidebar.number_input("Mean", value=0.0)
std_dev = st.sidebar.number_input("Standard Deviation", value=1.0)
num_samples = st.sidebar.number_input("Number of Samples", value=100)

# Generate random data
np.random.seed(42)  # Set seed for reproducibility
data = np.random.normal(mean, std_dev, num_samples)

# Histogram
st.header("Histogram")
plt.hist(data, bins='auto', color='blue', alpha=0.7)
plt.xlabel("Value")
plt.ylabel("Frequency")
st.pyplot(plt)

# Download data as CSV
if st.button("Download Data as CSV"):
    df = pd.DataFrame(data, columns=["Generated Data"])
    csv = df.to_csv(index=False)
    st.download_button("Download CSV", data=csv, file_name="generated_data.csv", mime="text/csv")

# Information about the data
st.write("Generated Data Statistics:")
st.write("- Mean:", np.mean(data))
st.write("- Standard Deviation:", np.std(data))
st.write("- Number of Samples:", num_samples)

