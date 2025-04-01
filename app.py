import pandas as pd
import plotly.express as px
import streamlit as st


df = pd.read_csv('vehicles_us.csv')


# cleaning the Dataframe
## correcting 'model_year' and 'cylinders' to int
df['model_year'] = df['model_year'].astype('Int64')
df['cylinders'] = df['cylinders'].astype('Int64')

## replacing NaN values for 'unknown' in 'paint_color
df['paint_color'] = df['paint_color'].fillna('unknown')

## calculating mean mileage per year of production
mean_mileage = df['odometer'].groupby(df['model_year']).mean()
mean_mileage.dropna()
## calculating an overal mean mileage 
total_odometer_mean = df['odometer'].mean()
## assigning mean values in place of NaN
df['odometer'] = df['odometer'].fillna(df['model_year'].map(mean_mileage))
df['odometer'] = df['odometer'].fillna(total_odometer_mean)

## re-assigning values for 'is_4wd'
df['is_4wd'] = df['is_4wd'].replace(1.0, True)
df['is_4wd'] = df['is_4wd'].fillna(False).astype(bool)


st.header('Welcome to the "Vehicels_us" Web-App', divider='rainbow')

st.subheader('distribution of cars by model year', divider=True)

chart1 = px.histogram(df, x='model_year').update_layout(bargap=0.2)
st.write(chart1)

st.subheader('Correlation between model year and price', divider=True)

price_avg = df.groupby('model_year').agg(price=('price', 'mean'))
chart2 = px.scatter(price_avg, x=price_avg.index, y='price')

show_last_20_years = st.checkbox('Show only last 20 years', value=False, label_visibility="visible")
if show_last_20_years:
    last_20_years = price_avg.loc[2000:]
    chart2 = px.scatter(last_20_years, x=last_20_years.index, y='price')

st.plotly_chart(chart2)
