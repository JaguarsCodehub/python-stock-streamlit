import streamlit as st

# General Settings
STRIPE_CHECKOUT="https://buy.stripe.com/test_7sI5oe6mNaeW2Eo3cc"

st.set_page_config(
      page_title="Subscribtion App",
      page_icon="💳",
      initial_sidebar_state="collapsed",
      layout="wide"
)

st.markdown(
      """
        <style>
            .section {
            height: 100vh;
            background-image: url("https://cdn.robinhood.com/assets/generated_assets/brand/_next/static/images/options-join-bg__c017ffd02270a41ed801ba5122d5bf00.png");
            background-size: cover;
        }
        .header2 {
            font-size: 90px;
        }

        a {
            text-decoration: none !important;
            color: #ffffff !important;
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

        </style>
      """,
      unsafe_allow_html=True
)

section1 = """
<div class="section">
    <div class="description2">
        <h1 class="header2">Our platform is available for a fee-based subscription</h1>
        <p>We are dedicated to providing our users with the best possible experience. That's why our website is equipped with powerful search tools, customizable dashboards, and detailed analytics that give users the insights they need to succeed in today's fast-paced financial markets.</p>
    </div>
</div>
"""

st.markdown(f'<div class="">{section1}</div>', unsafe_allow_html=True)
st.markdown(
        f'<button class="button"><a href={STRIPE_CHECKOUT}>💹Subscribe here</a></button>',
        unsafe_allow_html=True
    )
