import streamlit as st
from posthog import Posthog
import uuid

POSTHOG_API_KEY = st.secrets["POSTHOG_API_KEY"]

posthog = Posthog(
    project_api_key=POSTHOG_API_KEY,
    host="https://us.i.posthog.com"
)

def get_user_id():
    if "user_id" not in st.session_state:
        st.session_state.user_id = str(uuid.uuid4())

    return st.session_state.user_id


def track(event_name, properties=None):
    try:
        posthog.capture(
            distinct_id=get_user_id(),
            event=event_name,
            properties=properties or {},
        )
    except Exception:
        pass