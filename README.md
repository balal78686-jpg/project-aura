# Project AURA — Starter Kit

A local, beginner-friendly research and **paper-trading** prototype.

## What this version does
- Lets you upload historical price data as a CSV.
- Calculates fast and slow moving averages.
- Simulates a long-only strategy with a configurable transaction-fee assumption.
- Compares the simulation with buy-and-hold.
- Shows maximum drawdown and exports a paper-trading log.

## What it does NOT do
- It is not a trained predictive AI model.
- It does not place real trades.
- It does not connect to a broker, exchange, bank account or crypto wallet.
- It does not promise profits or provide personalised investment advice.

## Run it (Windows, Mac or Linux)
1. Install Python 3.10 or newer from https://www.python.org/downloads/
2. Open a terminal in this folder.
3. Create a virtual environment (recommended):
   - Windows: `py -m venv .venv` then `.venv\\Scripts\\activate`
   - Mac/Linux: `python3 -m venv .venv` then `source .venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Start the app: `streamlit run app.py`
6. Your browser should open the AURA dashboard.

If you do not want to install anything yet, upload this folder to a private GitHub repository and use a supported Streamlit hosting workflow only after reviewing privacy and deployment settings. Do not upload passwords, API keys or personal financial data.

## CSV format
Required columns:
- `Date` — dates such as `2025-01-02`
- `Close` — numeric closing prices

Optional columns: `Open`, `High`, `Low`, `Volume`.

Use trustworthy data you are entitled to use. Check data licensing and timestamps. Do not treat sample data as real market data.

## Safe development roadmap
1. Learn to run the paper-trading app.
2. Test on multiple historical periods and assets.
3. Keep a separate out-of-sample period.
4. Include realistic spreads, slippage, fees and taxes.
5. Paper trade in real time for a sustained period.
6. Get independent review before any live deployment.
7. If a broker integration is ever added, use trade-only permissions, disable withdrawals, store secrets securely, set strict loss limits and keep a manual kill switch.

With a £50 budget, the recommended first step is to keep the money uninvested while learning and testing.
