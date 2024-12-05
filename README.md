# My First Streamlit Dashboard

## Project Description
This project is a Streamlit dashboard application designed to analyze and visualize air quality data. It leverages popular Python libraries such as Pandas, Matplotlib, Seaborn, and Streamlit to provide an interactive experience for users to explore air quality metrics over time.

## Features
- **Date Filtering**: Users can filter data by date range using a sidebar widget.
- **Mean Pollutants Display**: The dashboard displays the mean values of different pollutants.
- **Pollutants Growth Visualization**: Users can visualize the growth of selected pollutants over the years for each station.
- **Pollutants Mean for Each Station**: A bar chart showing the total mean of pollutants for each station.

## Setup Environment
To set up the environment, use the following commands:
```
conda create --name main-ds python=3.11
conda activate main-ds
pip install numpy pandas scipy matplotlib seaborn jupyter streamlit
```

## Run Streamlit App
To run the Streamlit app, execute the following command:
```
streamlit run dashboard.py
```


## Access the Dashboard
You can access the dashboard online via the following link:
[Click here: Access via streamlit.app](https://first-dash-ageee.streamlit.app/)
or go to: https://first-dash-ageee.streamlit.app/

<img width="1237" alt="image" src="https://github.com/Ageee26/first-dashboard-repo/assets/43106236/9188f73f-80ff-4f29-a22c-27fec408457f">

## Usage Examples
Here are some usage examples to get you started:
1. **Filtering Data by Date**: Use the date input widget in the sidebar to filter the data by a specific date range.
2. **Visualizing Pollutants**: Select a pollutant type from the dropdown to see its growth over the years across different stations.
3. **Pollutants Mean by Station**: View the bar chart to understand the average levels of various pollutants at each station.

## Credits
This project was developed by Farhan Akhtar Gymnasiar. Special thanks to the contributors and the open-source community for their support and resources.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.
