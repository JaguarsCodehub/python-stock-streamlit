import streamlit as st
from pathlib import Path
from PIL import Image

# PATH SETTINGS
THIS_DIR = Path(__file__).parent if "__file__" in locals() else Path.cwd()
ASSETS_DIR = THIS_DIR / "assets"
STYLES_DIR = THIS_DIR / "styles"
CSS_FILE = STYLES_DIR / "main.css"

# General Settings
STRIPE_CHECKOUT="https://buy.stripe.com/test_7sI5oe6mNaeW2Eo3cc"

# Page Config
st.set_page_config(
      page_title="Trading with Python",
      page_icon="💹",
      initial_sidebar_state="expanded",
      layout="wide",
)

st.markdown(
    """
        <style>
            [data-testid="stAppViewContainer"] {
                background-image: url("https://www.smallcase.com/static/pngs/awi_landing/back.png");
                background-size: cover;
            }

            a {
                text-decoration: none !important;
                color: #ffffff !important;
            }

            .header {
                color: #FFF;
                font-size: 80px;
                font-family: "helvetica";
                font-weight: normal;
                letter-spacing: -1;
            }
            
            .button {
            appearance: button;
            background-color: #000;
            background-image: none;
            border: 1px solid #000;
            border-radius: 4px;
            box-shadow: #fff 4px 4px 0 0,#000 4px 4px 0 1px;
            box-sizing: border-box;
            color: #fff;
            cursor: pointer;
            display: inline-block;
            font-family: ITCAvantGardeStd-Bk,Arial,sans-serif;
            font-size: 14px;
            font-weight: 400;
            line-height: 20px;
            margin: 0 5px 10px 0;
            overflow: visible;
            padding: 12px 40px;
            text-align: center;
            text-transform: none;
            touch-action: manipulation;
            user-select: none;
            -webkit-user-select: none;
            vertical-align: middle;
            white-space: nowrap;
            }

            .button:focus {
            text-decoration: none;
            }

            .button:hover {
            text-decoration: none;
            }

            .button:active {
            box-shadow: rgba(0, 0, 0, .125) 0 3px 5px inset;
            outline: 0;
            }

            .button:not([disabled]):active {
            box-shadow: #fff 2px 2px 0 0, #000 2px 2px 0 1px;
            transform: translate(2px, 2px);
            }

            @media (min-width: 768px) {
            .button {
                padding: 12px 50px;
            }
            }

            .section {
            display: flex;
            flex-direction: row;
            justify-content: space-between;
            align-items: center;
            background-color: #000;
            color: #FFF;
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.1);
            padding: 60px;
            margin-bottom: 40px;
        }

        .section2 {
            height: 100vh;
            background-image: url("https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/images/options-join-bg__c017ffd02270a41ed801ba5122d5bf00.png");
            background-size: cover;
        }

        .section3 {
            height: 100vh;
            background-image: url("https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/images/intro-background@1x__a7e1489efad180ee10a6e4d50c56d857.png");
            background-size: cover;
        }

        .description2 {
            margin-bottom: 300px;
            text-align: center;
            align-items: center;
        }

        .header2 {
            font-size: 80px;
            font-family: "helvetica";
            font-weight: normal;
            letter-spacing: -1;
        }

        /* Style the image */
        .image {
            max-width: 50%;
            max-height: 400px;
            object-fit: contain;
        }
        </style>
    """,
    unsafe_allow_html=True
)
# First Section
with st.container():
    left_col, right_col = st.columns((1,1))
with right_col:
    product_image = Image.open(ASSETS_DIR / "fifth.png")
    st.image(product_image, width=500)
with left_col:
    
    st.title("Investing Build your portfolio starting with just $1")
    st.subheader("We are dedicated to providing our users with the best possible experience.")
    st.write("Invest in stocks, options, and ETFs at your pace and commission-free.")
    st.markdown(
        f'<button class="button"><a href={STRIPE_CHECKOUT} >💹Subscribe here</a></button>',
        unsafe_allow_html=True
    )

st.divider()

# Second Section
with st.container():
    left_col, right_col = st.columns((1,1))
with right_col:
    st.title("Crypto Dive right in without the commission fees")
    st.subheader("Other crypto exchanges charge up to 4% just to buy and sell crypto. We charge 0%. Get BTC, ETH, LTC, DOGE, and more with as little as $1.")
    st.write("We are dedicated to providing our users with the best possible experience.")
    st.markdown(
        f'<button class="button"><a  href={STRIPE_CHECKOUT} >💹Subscribe here</a></button>',
        unsafe_allow_html=True
    )
with left_col:
    product_image = Image.open(ASSETS_DIR / "second.png")
    st.image(product_image, width=500)

st.divider()

# Third Section
with st.container():
    left_col, right_col = st.columns((1,1))
with right_col:
    product_image = Image.open(ASSETS_DIR / "third.png")
    st.image(product_image, width=500)
with left_col:
    
    st.title("Retirement The only IRA with a match.")
    st.subheader("Introducing Stocks Retirement– Get a 1% match, custom recommended portfolios, and no commission fees.")
    st.write("We are dedicated to providing our users with the best possible experience.")
    st.markdown(
        f'<button class="button"><a href={STRIPE_CHECKOUT} >💹Subscribe here</a></button>',
        unsafe_allow_html=True
    )

st.divider()

# Fourth Section
section1 = """
<div class="section">
    <div class="description">
        <h1 class="header">24/7 live human support</h1>
        <p>Chat or request a call back on our website. We’re here for you and your investments, day or night.</p>
    </div>
    <img class="image" src="https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/images/options-vp-247__c00cf3f0e2078267a52bd6bfb55fce81.svg">
</div>
"""

st.markdown(f'<div class="">{section1}</div>', unsafe_allow_html=True)

# Fifth Section
section2 = """
<div class="section2">
    <div class="description2">
        <h1 class="header2">Level up your options strategies</h1>
        <p>Powerful. Smooth. Trades.</p>
    </div>
</div>
"""

st.markdown(f'<div class="">{section2}</div>', unsafe_allow_html=True)

st.divider()


# Sixth Section
with st.container():
    left_col, right_col = st.columns((1,1))
with right_col:
    st.title("Advanced Charts Fine-tune your trading strategy")
    st.subheader("Track and modify technical indicators—like moving average (MA).")
    st.write("We are dedicated to providing our users with the best possible experience.")
    st.markdown(
        f'<button class="button"><a  href={STRIPE_CHECKOUT} >💹Subscribe here</a></button>',
        unsafe_allow_html=True
    )
with left_col:
    product_image = Image.open(ASSETS_DIR / "sixth.png")
    st.image(product_image, width=500)

st.divider()

# Seventh Section
with st.container():
    left_col, right_col = st.columns((1,1))
with right_col:
    product_image = Image.open(ASSETS_DIR / "eight.png")
    st.image(product_image, width=500)
with left_col:
    
    st.title("Sign up and predict stocks in 5 minutes with no commission fees*")
    st.subheader("Protection for your coins, peace of mind for you")
    st.write("We are dedicated to providing our users with the best possible experience.")
    st.markdown(
        f'<button class="button"><a href={STRIPE_CHECKOUT} >💹Subscribe here</a></button>',
        unsafe_allow_html=True
    )

st.divider()

# Eigth Section
section3 = """
<div class="section3">
    <div class="description2">
        <h1 class="header2">Join a new generation of investors</h1>
        <p>Become a better investor on the go</p>
    </div>
</div>
"""

st.markdown(f'<div class="">{section3}</div>', unsafe_allow_html=True)

st.divider()