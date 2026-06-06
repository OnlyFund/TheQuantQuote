"""
Bloomberg-style Trading Quotes App - Live Clock with Arrow
Compatible with Streamlit 1.57
"""

import streamlit as st
from streamlit_autorefresh import st_autorefresh
import arrow
import urllib.parse

from quotes_generator import QuoteGenerator, TRADING_QUOTES
from quote_engagement import add_like, add_share, get_quote_engagement
from analytics import track
from config import PAGE_CONFIG, BLOOMBERG_CSS


# ============================================================================
# PAGE CONFIGURATION
# ============================================================================

st.set_page_config(**PAGE_CONFIG)
st_autorefresh(interval=1000, key="clock_refresh")
if "app_loaded" not in st.session_state:
    st.session_state.app_loaded = True
    try:
        track("app_opened")
    except Exception:
        pass


# ============================================================================
# CSS
# ============================================================================

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

.stColumn { text-align: center; }

div[data-testid="stMetricValue"] {
    font-family: 'Roboto Mono', monospace;
    font-size: 2rem;
    color: #00FF00 !important;
    font-weight: 700;
    letter-spacing: 2px;
}

div[data-testid="stMetricLabel"],
div[data-testid="stMetricLabel"] div,
div[data-testid="stMetricLabel"] span,
div[data-testid="stMetricLabel"] p {
    color: #FFD700 !important;  /* or #FFFFFF */
    
div[data-testid="stMetricLabel"] {
    font-family: 'Inter', sans-serif;
    font-size: 0.85rem;
    color: #FF6B00 !important;
    text-transform: uppercase;
    letter-spacing: 2px;
    font-weight: 600;
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
# INITIALIZE GENERATOR (STATLESS VERSION)
# ============================================================================

if "generator" not in st.session_state:
    st.session_state.generator = QuoteGenerator(TRADING_QUOTES)

if "current_quote" not in st.session_state:
    st.session_state.current_quote = st.session_state.generator.get_random_quote()


# ============================================================================
# HEADER
# ============================================================================

st.markdown("""
<div class="bloomberg-header">
    <div class="bloomberg-title">🖥️🖥️ GLOOMBERG</div>
    <div class="bloomberg-subtitle">
        Options & Derivatives | Market Intelligence | Sell-Side & Buy-Side
    </div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# WORLD CLOCK - SIDE BY SIDE
# ============================================================================

st.markdown("""
<div class="clock-container">
    <h4 style="text-align:center;color:#FF6B00;margin-bottom:1rem;">
        GLOBAL MARKET HOURS
    </h4>
</div>
""", unsafe_allow_html=True)

now = arrow.now()

ny_time = now.to('America/New_York').format('HH:mm:ss')
london_time = now.to('Europe/London').format('HH:mm:ss')
tokyo_time = now.to('Asia/Tokyo').format('HH:mm:ss')

col1, col2, col3 = st.columns(3, gap="large")

with col1:
    st.metric(label="NEW YORK", value=ny_time)

with col2:
    st.metric(label="LONDON", value=london_time)

with col3:
    st.metric(label="TOKYO", value=tokyo_time)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================================
# QUOTE DISPLAY
# ============================================================================

current_quote = st.session_state.current_quote

if (
    "last_tracked_quote" not in st.session_state
    or st.session_state.last_tracked_quote != current_quote
):
    track(
        "quote_viewed",
        {"quote": current_quote[:100]}
    )
    st.session_state.last_tracked_quote = current_quote


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
# ENGAGEMENT
# ============================================================================

likes, shares = get_quote_engagement(current_quote)

st.markdown(f"""
<div class="engagement-stats">
    <div class="stat-item">❤️ <strong>{likes}</strong> Likes</div>
    <div class="stat-item">🔗 <strong>{shares}</strong> Shares</div>
</div>
""", unsafe_allow_html=True)


# ============================================================================
# BUTTONS
# ============================================================================

col1, col2, col3, col4 = st.columns([1.5, 1, 1, 1.5])


# ----------------------------
# LIKE
# ----------------------------
with col2:
    if st.button("❤️ LIKE", use_container_width=True):
        track("quote_liked", {"quote": current_quote})

        new_likes = add_like(current_quote)
        st.success(f"Liked! Total: {new_likes}")
        st.rerun()


# ----------------------------
# SHARE
# ----------------------------
with col3:
    share_option = st.selectbox(
        "🔗 SHARE TO:",
        ["-- Select Platform --", "𝕏 Twitter", "💼 LinkedIn", "f Facebook", "📧 Email"],
        label_visibility="collapsed"
    )

    if share_option != "-- Select Platform --":
        share_text = f'"{current_quote}" - GLOOMBERG Trading Quotes'
        encoded_text = urllib.parse.quote(share_text)
        quote_url = "https://github.com/harel2706/TheQuantQuote"

        links = {
            "𝕏 Twitter": f"https://twitter.com/intent/tweet?text={encoded_text}&url={quote_url}",
            "💼 LinkedIn": f"https://www.linkedin.com/sharing/share-offsite/?url={quote_url}",
            "f Facebook": f"https://www.facebook.com/sharer/sharer.php?u={quote_url}",
            "📧 Email": f"mailto:?subject={urllib.parse.quote('GLOOMBERG Quote')}&body={urllib.parse.quote(share_text)}",
        }

        track(
            "quote_shared",
            {
                "quote": current_quote,
                "platform": share_option,
            }
        )

        add_share(current_quote, share_option)

        st.success(f"Shared to {share_option}")
        st.markdown(f"[Open link]({links[share_option]})", unsafe_allow_html=True)


# ============================================================================
# NEW QUOTE (FULLY RANDOMIZED NOW)
# ============================================================================

with col2:
    if st.button("🔄 NEW QUOTE", use_container_width=True):
        track("new_quote_requested", {"previous_quote": current_quote})

        # 🔥 stateless random selection every time
        st.session_state.current_quote = st.session_state.generator.get_random_quote()

        st.rerun()
