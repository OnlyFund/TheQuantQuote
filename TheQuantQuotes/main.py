"""
Bloomberg-style Trading Quotes App - Live Clock with Arrow
Compatible with Streamlit 1.57
"""

import streamlit as st
import arrow
import time
from quotes_generator import QuoteGenerator
from config import PAGE_CONFIG, BLOOMBERG_CSS

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(**PAGE_CONFIG)

# Enhanced CSS
ENHANCED_CSS = BLOOMBERG_CSS + """
<style>
    .clock-container {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        padding: 1.5rem 2rem;
        margin: 0 0 2rem 0;
        border-left: 5px solid #FF6B00;
        border-right: 5px solid #FF6B00;
        border-radius: 8px;
        box-shadow: 0 4px 12px rgba(0, 0, 0, 0.6);
    }

    .stColumn {
        text-align: center;
    }

    /* Metric Value (Time) - Green */
    div[data-testid="stMetricValue"] {
        font-family: 'Roboto Mono', monospace;
        font-size: 2rem;
        color: #00FF00 !important;
        font-weight: 700;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
    }

    /* Metric Label (City Names) - Orange */
    div[data-testid="stMetricLabel"] {
        font-family: 'Inter', sans-serif;
        font-size: 0.85rem;
        color: #FF6B00 !important;
        text-transform: uppercase;
        letter-spacing: 2px;
        font-weight: 600;
    }

    /* Additional specificity for nested elements */
    .clock-container div[data-testid="stMetricLabel"] {
        color: #FF6B00 !important;
    }

    .clock-container div[data-testid="stMetricLabel"] > div {
        color: #FF6B00 !important;
    }

    /* Target all text inside metric labels */
    [data-testid="stMetricLabel"] * {
        color: #FF6B00 !important;
    }

    /* Force override for metric labels */
    .clock-container div[data-testid="stMetricLabel"] > div {
        color: #FF6B00 !important;
    }

    .clock-container label {
        color: #FF6B00 !important;
    }
</style>
"""

st.markdown(ENHANCED_CSS, unsafe_allow_html=True)

# ============================================================================
# INITIALIZE QUOTE GENERATOR
# ============================================================================

if 'generator' not in st.session_state:
    st.session_state.generator = QuoteGenerator(history_size=30)

if 'current_quote' not in st.session_state:
    st.session_state.current_quote = st.session_state.generator.get_random_quote()

# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
<div class="bloomberg-header">
    <div class="bloomberg-title">🖥️🖥️ GLOOMBERG</div>
    <div class="bloomberg-subtitle">Options & Derivatives | Market Intelligence | Sell-Side & Buy-Side</div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# WORLD CLOCK - STATIC (Updates on button click)
# ============================================================================

st.markdown('<div class="clock-container">', unsafe_allow_html=True)

col1, col2, col3 = st.columns(3)

now = arrow.now()
ny_time = now.to('America/New_York').format('HH:mm:ss')
london_time = now.to('Europe/London').format('HH:mm:ss')
tokyo_time = now.to('Asia/Tokyo').format('HH:mm:ss')

with col1:
    st.metric("NEW YORK", ny_time)

with col2:
    st.metric("LONDON", london_time)

with col3:
    st.metric("TOKYO", tokyo_time)

st.markdown('</div>', unsafe_allow_html=True)

# ============================================================================
# MAIN QUOTE DISPLAY
# ============================================================================

current_quote = st.session_state.current_quote
current_date = arrow.now().format('MMMM DD, YYYY')

st.markdown(f"""
<div class="quote-card">
    <div class="quote-header">💬 Quote of the Day</div>
    <div class="quote-text">{current_quote}</div>
    <div class="quote-footer">
        {current_date} | Trading Desk Wisdom
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# NEW QUOTE BUTTON (CENTERED)
# ============================================================================

col1, col2, col3 = st.columns([1, 1, 1])

with col2:
    if st.button("🔄 NEW QUOTE", use_container_width=True):
        st.session_state.current_quote = st.session_state.generator.get_random_quote()
        st.rerun()
