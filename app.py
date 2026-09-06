import streamlit as st
import folium
from streamlit_folium import st_folium
import plotly.express as px
import pandas as pd

# --------------------------------
# PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="LANDSIGHT AI",
    page_icon="🌍",
    layout="wide"
)

# --------------------------------
# SIDEBAR NAVIGATION
# --------------------------------

st.sidebar.title("🌍 LANDSIGHT AI")
st.sidebar.caption("Landslide Risk Monitoring System")

page = st.sidebar.radio(
    "Navigation",
    ["🏠 Dashboard", "🤖 AI Risk Analysis",
     "📊 Analytics", "🗺️ Risk Map"]
)

st.sidebar.divider()

st.sidebar.info(
    "AI-powered environmental monitoring for early landslide risk detection."
)

# --------------------------------
# DASHBOARD
# --------------------------------

if page == "🏠 Dashboard":

    st.title("🌍 LANDSIGHT AI")
    st.subheader("AI-Powered Landslide Risk Monitoring & Early Warning System")

    st.divider()

    st.header("📊 Live Risk Overview")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("🔴 High Risk Areas", "12")

    with col2:
        st.metric("🟠 Moderate Risk Areas", "28")

    with col3:
        st.metric("🟢 Low Risk Areas", "45")

    st.divider()

    st.header("🌍 System Overview")

    st.write("""
    LANDSIGHT AI analyzes environmental conditions including
    rainfall, slope, soil moisture, and elevation to identify
    potential landslide-risk areas.
    """)

    st.info("💡 Select an option from the sidebar to explore the system.")

# --------------------------------
# AI RISK ANALYSIS
# --------------------------------

elif page == "🤖 AI Risk Analysis":

    st.title("🤖 AI Landslide Risk Analysis")

    st.write(
        "Enter environmental conditions to evaluate potential landslide risk."
    )

    st.divider()

    col1, col2 = st.columns(2)

    with col1:

        location = st.selectbox(
            "📍 Select Location",
            ["Gangtok, Sikkim", "Mangan, Sikkim", "Namchi, Sikkim"]
        )

        rainfall = st.number_input(
            "🌧️ Rainfall (mm)",
            min_value=0.0,
            value=220.0
        )

        slope = st.number_input(
            "⛰️ Slope (Degrees)",
            min_value=0.0,
            max_value=90.0,
            value=42.0
        )

    with col2:

        soil_moisture = st.number_input(
            "💧 Soil Moisture (%)",
            min_value=0.0,
            max_value=100.0,
            value=78.0
        )

        elevation = st.number_input(
            "📏 Elevation (m)",
            min_value=0.0,
            value=1750.0
        )

    st.divider()

    if st.button("🚀 ANALYZE LANDSLIDE RISK",
                 use_container_width=True):

        # Prototype risk calculation
        risk_score = (
            rainfall * 0.15 +
            slope * 1.2 +
            soil_moisture * 0.8
        )

        risk_percentage = min(risk_score / 1.2, 100)

        st.header("📊 AI ANALYSIS RESULT")

        if risk_percentage >= 70:

            st.error(
                f"🔴 HIGH RISK — {risk_percentage:.1f}%"
            )

            st.warning(
                "⚠️ High-risk environmental conditions detected. "
                "Immediate monitoring is recommended."
            )

        elif risk_percentage >= 40:

            st.warning(
                f"🟠 MODERATE RISK — {risk_percentage:.1f}%"
            )

            st.info(
                "Increase environmental monitoring in this area."
            )

        else:

            st.success(
                f"🟢 LOW RISK — {risk_percentage:.1f}%"
            )

            st.success(
                "Continue regular environmental monitoring."
            )

        st.write(f"📍 **Location Analyzed:** {location}")

# --------------------------------
# ANALYTICS
# --------------------------------

elif page == "📊 Analytics":

    st.title("📊 Regional Risk Analytics")

    st.write(
        "Visual representation of current landslide risk distribution."
    )

    risk_data = pd.DataFrame({
        "Risk Level": [
            "High Risk",
            "Moderate Risk",
            "Low Risk"
        ],
        "Areas": [12, 28, 45]
    })

    chart = px.bar(
        risk_data,
        x="Risk Level",
        y="Areas",
        text="Areas",
        title="Current Landslide Risk Distribution"
    )

    st.plotly_chart(
        chart,
        use_container_width=True
    )

    st.divider()

    st.subheader("Risk Distribution Data")

    st.dataframe(
        risk_data,
        use_container_width=True
    )

# --------------------------------
# RISK MAP
# --------------------------------

elif page == "🗺️ Risk Map":

    st.title("🗺️ Live Landslide Risk Map")

    st.write(
        "Interactive visualization of monitored locations and their risk levels."
    )

    # Map centered around Sikkim
    risk_map = folium.Map(
        location=[27.3389, 88.6065],
        zoom_start=9
    )

    # Gangtok - High Risk
    folium.Marker(
        location=[27.3389, 88.6065],
        popup="Gangtok - HIGH RISK",
        tooltip="🔴 Gangtok"
    ).add_to(risk_map)

    # Mangan - Moderate Risk
    folium.Marker(
        location=[27.5090, 88.5280],
        popup="Mangan - MODERATE RISK",
        tooltip="🟠 Mangan"
    ).add_to(risk_map)

    # Namchi - Low Risk
    folium.Marker(
        location=[27.1650, 88.3630],
        popup="Namchi - LOW RISK",
        tooltip="🟢 Namchi"
    ).add_to(risk_map)

    st_folium(
        risk_map,
        width=1200,
        height=550
    )

    st.divider()

    st.subheader("Risk Legend")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.error("🔴 High Risk")

    with col2:
        st.warning("🟠 Moderate Risk")

    with col3:
        st.success("🟢 Low Risk")