"""
Configuration and styling for Bloomberg-style trading quotes app.
"""

# Page configuration
PAGE_CONFIG = {
    "page_title": "GLOOMBERG | Quote of the Day",
    "page_icon": "🖥️",
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

    /* Main container */
    .main .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: 1200px;
        margin: 0 auto;
    }

    /* Bloomberg header bar */
    .bloomberg-header {
        background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 100%);
        padding: 2rem 2.5rem;
        margin: -1rem -1rem 3rem -1rem;
        border-bottom: 4px solid #FFD700;
        box-shadow: 0 6px 12px rgba(255, 107, 0, 0.4);
    }

    .bloomberg-title {
        font-family: 'Inter', sans-serif;
        font-size: 3rem;
        font-weight: 800;
        color: #000000;
        margin: 0;
        letter-spacing: -1px;
        text-transform: uppercase;
    }

    .bloomberg-subtitle {
        font-family: 'Roboto Mono', monospace;
        font-size: 1rem;
        color: #1a1a1a;
        margin: 0.5rem 0 0 0;
        font-weight: 500;
        letter-spacing: 1px;
    }

    /* Market ticker bar */
    .ticker-bar {
        background-color: #0a0a0a;
        padding: 1rem 2rem;
        margin: 0 0 3rem 0;
        border-left: 5px solid #FF6B00;
        border-right: 5px solid #FF6B00;
        font-family: 'Roboto Mono', monospace;
        font-size: 0.9rem;
        display: flex;
        justify-content: space-between;
        align-items: center;
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.6);
    }

    .ticker-item {
        display: inline-block;
        margin-right: 2.5rem;
    }

    .ticker-label {
        color: #666666;
        margin-right: 0.7rem;
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

    /* Quote card */
    .quote-card {
        background: linear-gradient(135deg, #1a1a1a 0%, #0d0d0d 100%);
        border: 3px solid #FF6B00;
        border-radius: 12px;
        padding: 4rem 3rem;
        margin: 3rem 0;
        box-shadow: 0 12px 24px rgba(255, 107, 0, 0.3);
        position: relative;
        overflow: hidden;
    }

    .quote-card::before {
        content: '"';
        position: absolute;
        top: -30px;
        left: 30px;
        font-size: 180px;
        color: #FF6B00;
        opacity: 0.08;
        font-family: Georgia, serif;
        font-weight: bold;
    }

    .quote-header {
        font-family: 'Inter', sans-serif;
        font-size: 1.3rem;
        color: #FFD700;
        text-transform: uppercase;
        letter-spacing: 3px;
        margin-bottom: 2rem;
        font-weight: 700;
        border-bottom: 2px solid #333333;
        padding-bottom: 0.8rem;
        text-align: center;
    }

    .quote-text {
        font-family: 'Roboto Mono', monospace;
        font-size: 2.2rem;
        line-height: 1.7;
        color: #FFFFFF;
        font-weight: 500;
        text-align: center;
        padding: 2rem 1rem;
        position: relative;
        z-index: 1;
        text-shadow: 0 2px 4px rgba(0, 0, 0, 0.5);
    }

    .quote-footer {
        font-family: 'Roboto Mono', monospace;
        font-size: 0.9rem;
        color: #888888;
        text-align: center;
        margin-top: 2rem;
        padding-top: 1.5rem;
        border-top: 2px solid #333333;
    }

    /* Button styling */
    .stButton > button {
        background: linear-gradient(90deg, #FF6B00 0%, #FF8C00 100%);
        color: #000000;
        font-family: 'Inter', sans-serif;
        font-weight: 700;
        font-size: 1.1rem;
        border: none;
        border-radius: 6px;
        padding: 0.8rem 2rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        box-shadow: 0 4px 8px rgba(255, 107, 0, 0.3);
        transition: all 0.3s ease;
    }

    .stButton > button:hover {
        background: linear-gradient(90deg, #FF8C00 0%, #FFA500 100%);
        box-shadow: 0 6px 12px rgba(255, 107, 0, 0.5);
        transform: translateY(-2px);
    }

    /* Remove extra spacing */
    .element-container {
        margin: 0;
        padding: 0;
    }
</style>
"""
