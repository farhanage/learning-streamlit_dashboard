import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import os
sns.set(style='dark')

# Load Data
current_directory = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(current_directory, 'main_data.csv')
df = pd.read_csv(files_location)


# Convert Datetime Data
df['timestamp'] = pd.to_datetime(df['timestamp'])

# widget date input sebagai filter pada bagian sidebar.
min_date = df["timestamp"].min()
max_date = df["timestamp"].max()

with st.sidebar:
    # Mengambil start_date & end_date dari date_input
    start_date, end_date = st.date_input(
        label='Rentang Waktu', min_value=min_date,
        max_value=max_date,
        value=[min_date, max_date]
    )

# Data terfilter
df = df[(df["timestamp"] >= str(start_date)) & (df["timestamp"] <= str(end_date))]

## Visualisasi
st.header('Air Quality Analysis Dashboard')

st.subheader('Total Mean of pollutants')

pollutant_types = df.columns[0:6]

# Calculate mean of all columns
mean_values = df.mean(numeric_only=True)
mean_values = mean_values.reset_index()

# Display mean values
col0, col1, col2 = st.columns(3)
with col0:
    st.metric(label=pollutant_types[0], value=round(mean_values[0][0], 1))

with col1:
    st.metric(label=pollutant_types[1], value=round(mean_values[0][1], 1))

with col2:
    st.metric(label=pollutant_types[2], value=round(mean_values[0][2], 1))

col3, col4, col5 = st.columns(3)
with col3:
    st.metric(label=pollutant_types[3], value=round(mean_values[0][3], 1))

with col4:
    st.metric(label=pollutant_types[4], value=round(mean_values[0][4], 1))

with col5:
    st.metric(label=pollutant_types[5], value=round(mean_values[0][5], 1))

st.subheader('Pollutants Growth')

# Filter by pollutant type
selected_pollutant = st.selectbox('Select Pollutant Type', pollutant_types)

# Plot pollutants growth for each stations
df['year'] = df['timestamp'].dt.year

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(35, 15))
df.groupby(['year', 'station'])[selected_pollutant].mean().unstack().plot(figsize=(10, 6), color=plt.cm.tab20.colors, ax=ax)
ax.set_title(f'Progress of {selected_pollutant} Pollutant by Year and Station', loc="center", fontsize=20)
ax.set_ylabel('Mean Pollutant')
ax.set_xlabel('Year')
ax.tick_params(axis='y', labelsize=20)
ax.tick_params(axis='x', labelsize=15)
ax.legend(fontsize=15, bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)

st.subheader('Pollutants Mean for Each Station')

# Plot total mean of pollutants for each station
fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(35, 15))
pollutant = ['PM2.5','PM10','SO2','NO2','CO','O3']
df.groupby('station')[pollutant].mean().plot.bar(stacked=True, ax=ax)
ax.set_title(f'Total mean of pollutant for each station', loc="center", fontsize=50)
ax.set_ylabel('Pollutant Mean')
ax.set_xlabel('Station')
ax.tick_params(axis='y', labelsize=40)
ax.tick_params(axis='x', labelsize=30)
ax.legend(fontsize=30, bbox_to_anchor=(1.05, 1), loc='upper left')
st.pyplot(fig)
