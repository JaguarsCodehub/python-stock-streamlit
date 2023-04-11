import streamlit as st
from datetime import date

import yfinance as yf
from prophet import Prophet
from prophet.plot import plot_plotly
from plotly import graph_objs as go

st.set_page_config(
      page_title="Multi Page App",
      page_icon="💹",
      initial_sidebar_state="collapsed"
)

st.markdown(
      """
        <style>
            [data-testid="stAppViewContainer"] {
                    background-image: url("https://www.smallcase.com/static/pngs/awi_landing/back.png");
                    background-size: cover;
            }
        </style>
      """,
      unsafe_allow_html=True
)

START = "2015-01-01"
TODAY = date.today().strftime("%Y-%m-%d")


st.sidebar.success("This is a sidebar")

st.title("Stock Prediction & Analysis")

stocks = ("AAPL", "GOOG", "MSFT", "GME", "TSLA", "AMZN", "NFLX")
selected_stock = st.selectbox("Select dataset for prediction", stocks)

n_years = st.slider("Years of prediction:", 1 , 4)
period = n_years * 365


@st.cache_data
def load_data(ticker):
    data = yf.download(ticker, START, TODAY)
    data.reset_index(inplace=True)
    return data

	
data_load_state = st.text('Loading data...')
data = load_data(selected_stock)
data_load_state.text('Loading data... done!')

st.subheader('Raw data')
st.write(data.tail())

# Plot raw data
def plot_raw_data():
	fig = go.Figure()
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Open'], name="stock_open"))
	fig.add_trace(go.Scatter(x=data['Date'], y=data['Close'], name="stock_close"))
	fig.layout.update(title='Time Series data with Rangeslider', xaxis_rangeslider_visible=True)
	st.plotly_chart(fig)
	
plot_raw_data()

# Predict forecast with Prophet.
df_train = data[['Date','Close']]
df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})

m = Prophet()
m.fit(df_train)
future = m.make_future_dataframe(periods=period)
forecast = m.predict(future)

# Show and plot forecast
st.subheader('Forecast data')
st.write(forecast.tail())
    
st.subheader(f'Forecast plot for {n_years} years')
fig1 = plot_plotly(m, forecast)
st.plotly_chart(fig1)

st.subheader("Forecast components")
fig2 = m.plot_components(forecast)
st.write(fig2)

