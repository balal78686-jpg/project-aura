
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Project AURA",
    page_icon="🚀",
    layout="wide"
)

st.title("🚀 PROJECT AURA")
st.caption("AI-powered online income and market research centre")

st.sidebar.title("AURA CONTROL")
page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Market Watchlist",
        "Online Business",
        "Budget Tracker",
        "Automation Centre"
    ]
)

if page == "Dashboard":
    st.header("Your Command Centre")
    st.success("Project AURA is online!")

    col1, col2, col3 = st.columns(3)
    col1.metric("Starting Budget", "50")
    col2.metric("Monthly Goal", "To be set")
    col3.metric("System Status", "Online")

    st.subheader("Your AURA Mission")
    st.write("""
    Build and research online income opportunities,
    analyse markets and track business performance.
    """)

    st.info("Next milestone: Connect live market data and AI analysis.")

elif page == "Market Watchlist":
    st.header("📈 Market Watchlist")
    st.write("Your research workspace.")

    asset = st.text_input("Enter an asset", "Bitcoin")
    category = st.selectbox(
        "Category",
        ["Cryptocurrency", "Stocks", "Forex", "Other"]
    )

    if st.button("Add to research list"):
        st.success(f"{asset} added to your research notes.")
        st.write("Category:", category)

    st.caption("No live prices or trading signals are connected yet.")

elif page == "Online Business":
    st.header("🛒 Online Business Research")

    idea = st.text_input("Business or product idea")
    notes = st.text_area("Research notes")

    if st.button("Save research"):
        st.success("Research submitted for this session.")
        st.write("Idea:", idea)
        st.write("Notes:", notes)

elif page == "Budget Tracker":
    st.header("💰 Budget Tracker")

    budget = st.number_input(
        "Starting budget",
        min_value=0.0,
        value=50.0
    )

    spent = st.number_input(
        "Money spent",
        min_value=0.0,
        value=0.0
    )

    st.metric("Remaining Budget", f"{budget - spent:.2f}")

    if spent > budget:
        st.warning("You have exceeded your starting budget.")

elif page == "Automation Centre":
    st.header("🤖 Automation Centre")

    st.write("Automation features will be added in later stages.")

    st.checkbox("Enable market research alerts")
    st.checkbox("Enable business opportunity alerts")
    st.checkbox("Enable monthly performance reviews")

    st.warning("These are planning controls only. No alerts are currently sent.")
