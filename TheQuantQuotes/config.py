"""
Configuration and styling for Bloomberg-style trading quotes app.
"""

# Page configuration
PAGE_CONFIG = {
    "page_title": "GLOOMBERG | Quote of the Day",
    "page_icon": "🖥️🖥️",
    "layout": "wide",
    "initial_sidebar_state": "collapsed"
}

# Bloomberg-style CSS
BLOOMBERG_CSS = """
<style>
    /* Import Bloomberg-style fonts */
    @import url('https://fonts.googleapis.com/css2?family=Roboto+Mono:wght@400;500;700&family=Inter:wght@400;600;700;800&display=swap');

    /* Global styles */
    .stApp {
        background-color: #000000;
        color: #FF6B00;
    }

    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Main container - TIGHTER LAYOUT */
    .main .block-container {
        padding-top: 0.5rem;
        padding-bottom: 0.5rem;
        padding-left: 1rem;
        padding-right: 1rem;
        max-width: 100%;
        margin: 0 auto;
    }

    /* Reduce gap between elements */
    .element-container {
        margin: 0 !important;
        padding: 0 !important;
    }

    .stVerticalBlockBorderWrapper {
        gap: 0.25rem !important;
    }

    /* Bloomberg header bar - COMPACT */
    .bloomberg-header {
        background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 100%);
        padding: 1rem 1.5rem;
        margin: -0.5rem -1rem 1rem -1rem;
        border-bottom: 3px solid #FFD700;
        box-shadow: 0 4px 8px rgba(255, 107, 0, 0.4);
    }

    .bloomberg-title {
        font-family: 'Inter', sans-serif;
        font-size: 2.2rem;
        font-weight: 800;
        color: #000000;
        margin: 0;
        letter-spacing: -1px;
        text-transform: uppercase;
    }

    .bloomberg-subtitle {
        font-family: 'Roboto Mono', monospace;
        font-size: 0.75rem;
        color: #1a1a1a;
        margin: 0.25rem 0 0 0;
        font-weight: 500;
        letter-spacing: 1px;
    }

    /* Market ticker bar */
    .ticker-bar {
        background-color: #0a0a0a;
        padding: 0.8rem 1.5rem;
        margin: 0 0 1.5rem 0;
        border-left: 4px solid #FF6B00;
        border-right: 4px solid #FF6B00;
        font-family: 'Roboto Mono', monospace;
        font-size: 0.85rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 2px 6px rgba(0, 0, 0, 0.6);
    }

    .ticker-item {
        display: inline-block;
        margin-right: 1.5rem;
    }

    .ticker-label {
        color: #666666;
        margin-right: 0.5rem;
        font-weight: 500;
    }

    .ticker-value-up {
        color: #00FF00;
        font-weight: 700;
    }

    .ticker-value-down {
        color: #FF0000;
        font-weight: 700;
    }

    .ticker-time {
        color: #FFD700;
        font-weight: 600;
    }

    /* Quote card - COMPACT */
    .quote-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
        border: 2px solid #FF6B00;
        border-radius: 8px;
        padding: 2rem 2rem;
        margin: 0.75rem 0;
        box-shadow: 0 8px 16px rgba(255, 107, 0, 0.3);
        position: relative;
        overflow: hidden;
    }

    .quote-card::before {
        content: '"';
        position: absolute;
        top: -20px;
        left: 15px;
        font-size: 100px;
        color: #FF6B00;
        opacity: 0.08;
        font-family: Georgia, serif;
        font-weight: bold;
    }

    .quote-header {
        font-family: 'Inter', sans-serif;
        font-size: 1rem;
        color: #FFD700;
        text-transform: uppercase;
        letter-spacing: 2px;
        margin-bottom: 1rem;
        font-weight: 700;
        border-bottom: 1px solid #333333;
        padding-bottom: 0.5rem;
        text-align: center;
    }

    .quote-text {
        font-family: 'Roboto Mono', monospace;
        font-size: 1.5rem;
        line-height: 1.5;
        color: #FFFFFF;
        font-weight: 500;
        text-align: center;
        padding: 1rem 0.5rem;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }

    .quote-footer {
        font-family: 'Roboto Mono', monospace;
        font-size: 0.75rem;
        color: #888888;
        text-align: center;
        margin-top: 0.75rem;
        padding-top: 0.75rem;
        border-top: 1px solid #333333;
    }

    /* Clock container - TIGHTER */
    .clock-container {
        background: linear-gradient(135deg, #0a0a0a 0%, #1a1a1a 100%);
        padding: 0.8rem 1.5rem;
        margin: 0 0 1rem 0;
        border-left: 3px solid #FF6B00;
        border-right: 3px solid #FF6B00;
        border-radius: 6px;
        box-shadow: 0 2px 8px rgba(0, 0, 0, 0.6);
    }

    /* Engagement stats display */
    .engagement-stats {
        display: flex;
        gap: 2rem;
        justify-content: center;
        margin-top: 0.5rem;
        margin-bottom: 0.5rem;
        font-family: 'Roboto Mono', monospace;
        font-size: 0.85rem;
        color: #FFD700;
    }

    .stat-item {
        display: flex;
        align-items: center;
        gap: 0.3rem;
    }

    /* Button styling - COMPACT */
    .stButton > button {
        background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 100%);
        color: #000000;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 0.9rem;
        border: none;
        border-radius: 4px;
        padding: 0.5rem 1.5rem;
        text-transform: uppercase;
        letter-spacing: 0.5px;
        box-shadow: 0 3px 6px rgba(255, 107, 0, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #FF8C00 0%, #FFA500 100%);
        box-shadow: 0 4px 10px rgba(255, 107, 0, 0.5);
        transform: translateY(-1px);
    }

    /* Selectbox styling */
    .stSelectbox {
        margin: 0 !important;
        padding: 0 !important;
    }

    /* Reduce metric spacing */
    [data-testid="metric-container"] {
        gap: 0 !important;
    }

    .stMetric {
        padding: 0 !important;
    }

</style>
"""
