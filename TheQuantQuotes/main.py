"""
Bloomberg-style Trading Quotes App - Live Clock with Arrow
Compatible with Streamlit 1.57
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh
import arrow
import urllib.parse
from quotes_generator import QuoteGenerator,TRADING_QUOTES
from export_quote import generate_quote_image
from config import PAGE_CONFIG, BLOOMBERG_CSS
from quote_engagement import (
    add_like,
    add_share,
    get_quote_engagement,
)

# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(**PAGE_CONFIG)
st_autorefresh(interval=1000, key="clock_refresh")
from analytics import track
if 'app_loaded' not in st.session_state:
    track('app_opened')
    st.session_state.app_loaded = True

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
        color: #ffffff !important;
        font-weight: 700;
        letter-spacing: 2px;
        text-shadow: 0 0 10px rgba(0, 255, 0, 0.3);
    }

    /* Metric Label (City Names) - Orange */
    div[data-testid="stMetricLabel"] p {
    color: #FF6B00 !important;
    font-family: 'Inter', sans-serif;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-size: 0.8rem;
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

    /* Engagement stats display */
    .engagement-stats {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 1rem;
        font-family: 'Roboto Mono', monospace;
        font-size: 0.9rem;
        color: #FFD700;
    }

    .stat-item {
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
</style>
"""

st.markdown(ENHANCED_CSS, unsafe_allow_html=True)

# ============================================================================
# INITIALIZE QUOTE GENERATOR & ENGAGEMENT
# ============================================================================

if 'generator' not in st.session_state:
    st.session_state.generator = QuoteGenerator(TRADING_QUOTES)

if 'current_quote' not in st.session_state:
    st.session_state.current_quote = st.session_state.generator.get_random_quote()

# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
<div class="bloomberg-header">
    <div class="bloomberg-title">🖥️🖥️ GLOOMBERG </div>
    <div class="bloomberg-subtitle">Options & Derivatives | Market Intelligence | Sell-Side & Buy-Side (and everything in between) </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# WORLD CLOCK - STATIC (Updates on button click)
# ============================================================================

st.markdown("""
<div class="clock-container">
    <h4 style="text-align:center;color:#FF6B00;margin-bottom:1rem;">
        GLOBAL MARKET CLOCK
    </h4>
</div>
""", unsafe_allow_html=True)

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

if (
    "last_tracked_quote" not in st.session_state
    or st.session_state.last_tracked_quote != current_quote
):
    track(
        "quote_viewed",
        {
            "quote": current_quote[:100]
        }
    )

    st.session_state.last_tracked_quote = current_quote

current_date = arrow.now().format('MMMM DD, YYYY')

st.markdown(f"""
<div class="quote-card">
    <div class="quote-header">💬 Quote of the Day</div>
    <div class="quote-text">{current_quote}</div>
    <div class="quote-footer">
        {current_date} | Trading Desks Ancient Wisdom
    </div>
</div>
""", unsafe_allow_html=True)

# ============================================================================
# ENGAGEMENT METRICS (Just display, no footer stats)
# ============================================================================

likes, shares = get_quote_engagement(current_quote)

st.markdown(f"""
<div class="engagement-stats">
    <div class="stat-item">❤️ <strong>{likes}</strong> Likes</div>
""", unsafe_allow_html=True)

# ============================================================================
# ENGAGEMENT + ACTIONS (CLEAN LAYOUT)
# ============================================================================

col1, col2, col3 = st.columns([1, 1, 1])

with col2:

    # NEW QUOTE BUTTON (TOP)
    if st.button(
    "🔄 NEW QUOTE",
    use_container_width=True,
    key="new_quote_button"
):
        track(
            "new_quote_requested",
            {"previous_quote": current_quote}
        )

        st.session_state.current_quote = (
            st.session_state.generator.get_random_quote()
        )

        st.rerun()

    st.markdown("<div style='height:10px'></div>", unsafe_allow_html=True)

    # LIKE BUTTON (DIRECTLY BELOW)
    if st.button("❤️ LIKE", use_container_width=True, key="like_btn"):

        track(
            "quote_liked",
            {"quote": current_quote}
        )

        new_likes = add_like(current_quote)

        st.success(f"Quote liked! Total: {new_likes}")
        st.rerun()


        st.rerun()
