import streamlit as st
import pandas as pd
import numpy as np
from pathlib import Path

st.set_page_config(page_title="Project AURA", page_icon="🤖", layout="wide")
st.title("🤖 Project AURA")
st.caption("A beginner-friendly research and paper-trading prototype. It does not place real trades or predict guaranteed profits.")

st.warning(
    "SIMULATION ONLY — No broker connection, no live orders, and no investment advice. "
    "Past performance does not predict future results. Do not use this prototype to decide "
    "how to invest money without independent research."
)

with st.sidebar:
    st.header("Strategy settings")
    fast = st.number_input("Fast moving average (days)", min_value=2, max_value=100, value=10)
    slow = st.number_input("Slow moving average (days)", min_value=3, max_value=300, value=30)
    fee_pct = st.number_input("Estimated fee per transaction (%)", min_value=0.0, max_value=5.0, value=0.2, step=0.05)
    initial_cash = st.number_input("Simulated starting balance (£)", min_value=10.0, value=1000.0, step=50.0)

st.subheader("1. Load historical price data")
st.write("Upload a CSV with columns named `Date` and `Close` (optional: `Open`, `High`, `Low`, `Volume`).")
uploaded = st.file_uploader("Upload CSV", type=["csv"])

def sample_data():
    # Deterministic illustrative data only; not actual market prices.
    rng = np.random.default_rng(7)
    dates = pd.date_range(end=pd.Timestamp.today().normalize(), periods=180, freq="B")
    returns = rng.normal(0.0003, 0.012, len(dates))
    close = 100 * np.cumprod(1 + returns)
    return pd.DataFrame({"Date": dates, "Close": close})

if uploaded:
    try:
        raw = pd.read_csv(uploaded)
        if not {"Date", "Close"}.issubset(raw.columns):
            st.error("CSV must contain Date and Close columns.")
            st.stop()
        df = raw.copy()
        df["Date"] = pd.to_datetime(df["Date"], errors="coerce")
        df["Close"] = pd.to_numeric(df["Close"], errors="coerce")
        df = df.dropna(subset=["Date", "Close"]).sort_values("Date")
    except Exception as e:
        st.error(f"Could not read the CSV: {e}")
        st.stop()
else:
    st.info("No CSV uploaded. Showing clearly labelled synthetic example data.")
    df = sample_data()

if len(df) < max(fast, slow) + 2:
    st.error("Not enough rows for these moving-average settings. Upload more history or reduce the periods.")
    st.stop()
if fast >= slow:
    st.error("Fast moving average must be shorter than the slow moving average.")
    st.stop()

df["Fast_MA"] = df["Close"].rolling(int(fast)).mean()
df["Slow_MA"] = df["Close"].rolling(int(slow)).mean()
# Signal uses information available at the prior close; execution is modelled at next row's close.
df["Target"] = (df["Fast_MA"] > df["Slow_MA"]).astype(int)
df["Position"] = df["Target"].shift(1).fillna(0)
df["Market_Return"] = df["Close"].pct_change().fillna(0)
df["Turnover"] = df["Position"].diff().abs().fillna(df["Position"])
fee = fee_pct / 100
df["Strategy_Return"] = df["Position"] * df["Market_Return"] - df["Turnover"] * fee
df["BuyHold_Value"] = initial_cash * (1 + df["Market_Return"]).cumprod()
df["Strategy_Value"] = initial_cash * (1 + df["Strategy_Return"]).cumprod()
df["Drawdown"] = df["Strategy_Value"] / df["Strategy_Value"].cummax() - 1

start_val = float(df["Strategy_Value"].iloc[0])
end_val = float(df["Strategy_Value"].iloc[-1])
total_return = (end_val / initial_cash - 1) * 100
buyhold_return = (float(df["BuyHold_Value"].iloc[-1]) / initial_cash - 1) * 100
max_dd = float(df["Drawdown"].min()) * 100
trades = int(df["Turnover"].sum())

st.subheader("2. Paper strategy results")
c1, c2, c3, c4 = st.columns(4)
c1.metric("Simulated ending value", f"£{end_val:,.2f}", f"{total_return:+.2f}%")
c2.metric("Buy-and-hold comparison", f"{buyhold_return:+.2f}%")
c3.metric("Maximum drawdown", f"{max_dd:.2f}%")
c4.metric("Position changes", str(trades))

chart = df.set_index("Date")[["Strategy_Value", "BuyHold_Value"]].rename(
    columns={"Strategy_Value": "AURA simulated strategy", "BuyHold_Value": "Buy and hold"}
)
st.line_chart(chart)
st.caption("The strategy is a simple moving-average example, not a trained AI model. Results depend on the uploaded data, settings, fees and simplified execution assumptions.")

st.subheader("3. Latest research snapshot")
latest = df.iloc[-1]
col1, col2, col3 = st.columns(3)
col1.metric("Latest close in uploaded data", f"{latest['Close']:.4f}")
col2.metric("Fast average", "—" if pd.isna(latest["Fast_MA"]) else f"{latest['Fast_MA']:.4f}")
col3.metric("Slow average", "—" if pd.isna(latest["Slow_MA"]) else f"{latest['Slow_MA']:.4f}")
if latest["Target"] == 1:
    st.info("Rule-based signal: trend filter is ON. This is not a buy instruction.")
else:
    st.info("Rule-based signal: trend filter is OFF. This is not a sell instruction.")

st.subheader("4. Export your paper-trading log")
export = df[["Date", "Close", "Fast_MA", "Slow_MA", "Position", "Market_Return", "Strategy_Return", "Strategy_Value", "Drawdown"]]
st.download_button("Download results CSV", export.to_csv(index=False).encode("utf-8"), "aura_paper_trading_log.csv", "text/csv")

with st.expander("Important limitations and next steps"):
    st.markdown("""
    - This app does not connect to an exchange, broker, bank account or wallet.
    - It does not send orders or hold funds.
    - The default dataset is synthetic and must not be mistaken for real prices.
    - A moving-average crossover is a teaching example, not evidence of a profitable edge.
    - Before considering live use, add robust data validation, out-of-sample testing, walk-forward testing,
      slippage, realistic fees, tax records, operational monitoring and independent security review.
    - Never give an AI or third party withdrawal access to your funds.
    """)
