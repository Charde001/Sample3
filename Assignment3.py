import streamlit as st
import numpy as np
import pandas as pd
import random

# Function to generate a normal distribution
def generate_normal_distribution(mean, std, n):
  data = np.random.normal(mean, std, n)
  return data

# Function to plot the histogram of a normal distribution
def plot_histogram(data):
  st.barplot(data)

# Function to download the generated data as a .csv file
def download_data(data):
  df = pd.DataFrame(data)
  df.to_csv('normal_distribution.csv', index=False)

# Main function
def main():
  # Set the title of the app
  st.title('Normal Distribution App')

  # Inputs
  mean = st.slider('Mean', 0, 100, 50)
  std = st.slider('Standard deviation', 0, 10, 2)
  n = st.slider('Number of samples', 10, 1000, 100)

  # Generate the normal distribution
  data = generate_normal_distribution(mean, std, n)

  # Plot the histogram of the normal distribution
  if st.button('Plot histogram'):
    plot_histogram(data)

  # Download the generated data as a .csv file
  if st.button('Download data'):
    download_data(data)

if __name__ == '__main__':
  main()
