# car_web_tool
Software Development Tools: Project for sprint 6

## Description

This project is a web tool that helps users analyze and visualize car price trends based on historical data stored in 'vehicles_us.csv'. 
It uses Plotly and Streamlit to provide interactive charts and graphs.
The app is developed to be run on-line via render.com, but can be installed and run locally.

## Installation

To run this project locally, follow these steps:
1. make sure you have pandas, plotly and streamlit installed in your Python enviroment.
   if not, use: pip install -r requirements.txt
2. Clone the repository: git clone https://github.com/danportnoy95/car_web_tool.git
3. Go to the project directory and run the app using the command: streamlit run app.py

## Usage

After launching the app you will see 2 charts

### distribution of cars by model year
Shows you how many cars were listed in the database for each year. 
Notice! There are some intresting outliers from the start of the century, and substantial numbers from the 90's onward.

### Correlation between model year and price
Shows you the average price for each year listed in the database.
Because of the interesting outliers mentioned, and because most people dont buy too old used cars, this chart has a check box to show you only the average for the last 20 years.
