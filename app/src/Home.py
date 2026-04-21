import logging

import streamlit as st

from modules.nav import SideBarLinks
from modules.styles import inject_css

logging.basicConfig(
    format="%(filename)s:%(lineno)s:%(levelname)s -- %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

st.set_page_config(layout="wide", page_title="HoopSpot")

st.session_state["authenticated"] = False

SideBarLinks(show_home=True)

ROLE_CONFIGS = [
    {
        "role": "pickup_player",
        "title": "Pickup Player",
        "subtitle": "Find nearby runs, check in, and rate courts after you hoop.",
        "page": "pages/00_Pickup_Home.py",
        "accent": "PP",
        "users": [
            {
                "label": "Marcus Reyes",
                "first_name": "Marcus",
                "last_name": "Reyes",
                "location": "Roxbury, MA",
                "player_id": 1,
            },
            {
                "label": "Jordan Cross",
                "first_name": "Jordan",
                "last_name": "Cross",
                "location": "Back Bay, MA",
                "player_id": 2,
            },
            {
                "label": "Nina Flores",
                "first_name": "Nina",
                "last_name": "Flores",
                "location": "Fenway, MA",
                "player_id": 4,
            },
        ],
    },
    {
        "role": "competitive_player",
        "title": "Competitive Player",
        "subtitle": "Track rankings, enter tournaments, and review recent results.",
        "page": "pages/10_Competitive_Home.py",
        "accent": "CP",
        "users": [
            {
                "label": "Aaliyah Carter",
                "first_name": "Aaliyah",
                "last_name": "Carter",
                "player_id": 3,
            },
            {
                "label": "Devin Brooks",
                "first_name": "Devin",
                "last_name": "Brooks",
                "player_id": 6,
            },
            {
                "label": "Cam Nguyen",
                "first_name": "Cam",
                "last_name": "Nguyen",
                "player_id": 12,
            },
        ],
    },
    {
        "role": "administrator",
        "title": "System Administrator",
        "subtitle": "Moderate content, manage courts, and keep the platform healthy.",
        "page": "pages/20_Admin_Home.py",
        "accent": "SA",
        "users": [
            {
                "label": "Devon Williams",
                "first_name": "Devon",
                "last_name": "Williams",
            },
            {
                "label": "Rina Patel",
                "first_name": "Rina",
                "last_name": "Patel",
            },
            {
                "label": "Chris Monroe",
                "first_name": "Chris",
                "last_name": "Monroe",
            },
        ],
    },
    {
        "role": "data_analyst",
        "title": "Data Analyst",
        "subtitle": "Analyze activity trends, heatmaps, and exports across Boston.",
        "page": "pages/40_Analyst_Profile.py",
        "accent": "DA",
        "users": [
            {
                "label": "Priya Nair",
                "first_name": "Priya",
                "last_name": "Nair",
            },
            {
                "label": "Mason Lee",
                "first_name": "Mason",
                "last_name": "Lee",
            },
            {
                "label": "Elena Torres",
                "first_name": "Elena",
                "last_name": "Torres",
            },
        ],
    },
]

PAGE_CSS = """
.stApp {
    background: #020617;
}
.block-container {
    max-width: 1180px !important;
    padding-top: 3.5rem !important;
    padding-bottom: 2rem !important;
}
.hero-shell {
    display: flex;
    gap: 1.25rem;
    align-items: center;
    margin-bottom: 1rem;
}
.logo-wrap {
    width: 84px;
    height: 84px;
    border-radius: 24px;
    background: linear-gradient(135deg, rgba(249,115,22,0.18), rgba(234,88,12,0.28));
    border: 1px solid rgba(249,115,22,0.28);
    display: flex;
    align-items: center;
    justify-content: center;
    box-shadow: 0 24px 60px rgba(249,115,22,0.16);
    flex-shrink: 0;
}
.hero-kicker {
    display: inline-flex;
    align-items: center;
    padding: 6px 12px;
    border-radius: 999px;
    background: rgba(249,115,22,0.12);
    border: 1px solid rgba(249,115,22,0.2);
    color: #FDBA74;
    font-family: 'Outfit', sans-serif;
    font-size: 0.76rem;
    font-weight: 600;
    letter-spacing: 0.05em;
    text-transform: uppercase;
    margin-bottom: 0.85rem;
}
.hero-title {
    font-family: 'Outfit', sans-serif;
    font-size: 4rem;
    line-height: 0.95;
    letter-spacing: -0.06em;
    font-weight: 800;
    color: #F8FAFC;
    margin: 0;
}
.hero-title span {
    color: #F97316;
}
.hero-copy {
    font-family: 'Outfit', sans-serif;
    font-size: 1.02rem;
    color: #94A3B8;
    max-width: 700px;
    margin: 0.85rem 0 0 0;
}
.section-label {
    font-family: 'Outfit', sans-serif;
    font-size: 0.82rem;
    color: #CBD5E1;
    margin: 2rem 0 1rem 0;
}
.role-card {
    background: linear-gradient(180deg, rgba(15,23,42,0.92), rgba(15,23,42,0.72));
    border: 1px solid rgba(148,163,184,0.14);
    border-radius: 20px;
    padding: 1.25rem;
    min-height: 100%;
    box-shadow: inset 0 1px 0 rgba(255,255,255,0.03);
}
.role-head {
    display: flex;
    align-items: center;
    gap: 0.9rem;
    margin-bottom: 0.8rem;
}
.role-badge {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    background: linear-gradient(135deg, #F97316, #EA580C);
    display: flex;
    align-items: center;
    justify-content: center;
    color: #fff;
    font-family: 'Outfit', sans-serif;
    font-size: 0.84rem;
    font-weight: 700;
    letter-spacing: 0.04em;
}
.role-title {
    font-family: 'Outfit', sans-serif;
    font-size: 1.05rem;
    font-weight: 700;
    color: #F8FAFC;
    margin: 0;
}
.role-copy {
    font-family: 'Outfit', sans-serif;
    font-size: 0.86rem;
    color: #94A3B8;
    line-height: 1.5;
    margin: 0 0 1rem 0;
}
.login-hint {
    font-family: 'Outfit', sans-serif;
    font-size: 0.76rem;
    color: #64748B;
    margin-top: 0.35rem;
}
"""

st.markdown(inject_css(PAGE_CSS), unsafe_allow_html=True)


def set_session_value(key, value):
    if value is None:
        st.session_state.pop(key, None)
    else:
        st.session_state[key] = value


def login_as(role_config, user):
    st.session_state["authenticated"] = True
    st.session_state["role"] = role_config["role"]
    set_session_value("first_name", user.get("first_name"))
    set_session_value("last_name", user.get("last_name"))
    set_session_value("location", user.get("location"))
    set_session_value("player_id", user.get("player_id"))

    logger.info("Logging in as %s: %s", role_config["role"], user["label"])
    st.switch_page(role_config["page"])


logger.info("Loading the Home page of the app")

st.markdown(
    """
    <div class="hero-shell">
        <div class="logo-wrap">
            <svg width="52" height="52" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
                <rect x="1.5" y="1.5" width="49" height="49" rx="14" fill="#111827" stroke="#FB923C" stroke-width="1.5"/>
                <circle cx="26" cy="20" r="11" stroke="#F97316" stroke-width="2.5"/>
                <path d="M15 20H37" stroke="#F97316" stroke-width="2"/>
                <path d="M26 9V31" stroke="#F97316" stroke-width="2"/>
                <path d="M18.5 12.5C23.5 16 28.5 24 33.5 27.5" stroke="#F97316" stroke-width="2"/>
                <path d="M16 35H36" stroke="#CBD5E1" stroke-width="2.5" stroke-linecap="round"/>
                <path d="M18 35L20 41" stroke="#CBD5E1" stroke-width="2" stroke-linecap="round"/>
                <path d="M22 35L23.5 42" stroke="#CBD5E1" stroke-width="2" stroke-linecap="round"/>
                <path d="M26 35V42" stroke="#CBD5E1" stroke-width="2" stroke-linecap="round"/>
                <path d="M30 35L28.5 42" stroke="#CBD5E1" stroke-width="2" stroke-linecap="round"/>
                <path d="M34 35L32 41" stroke="#CBD5E1" stroke-width="2" stroke-linecap="round"/>
            </svg>
        </div>
        <div>
            <h1 class="hero-title">Hoop<span>Spot</span></h1>
            <p class="hero-copy">
                Choose a role, select a mock user for that persona, and log in without a password.
                Each selector below mimics a different front-end user flow in the app.
            </p>
        </div>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-label">Log in as a mock user</div>', unsafe_allow_html=True)

first_row = st.columns(2, gap="large")
second_row = st.columns(2, gap="large")

for col, role_config in zip(first_row + second_row, ROLE_CONFIGS):
    with col:
        st.markdown(
            f"""
            <div class="role-card">
                <div class="role-head">
                    <div class="role-badge">{role_config["accent"]}</div>
                    <div class="role-title">{role_config["title"]}</div>
                </div>
                <p class="role-copy">{role_config["subtitle"]}</p>
            </div>
            """,
            unsafe_allow_html=True,
        )

        options = [user["label"] for user in role_config["users"]]
        selected_label = st.selectbox(
            f"{role_config['title']} mock users",
            options,
            key=f"{role_config['role']}_user_select",
        )
        selected_user = next(
            user for user in role_config["users"] if user["label"] == selected_label
        )

        if st.button(
            f"Login as {selected_user['first_name']}",
            key=f"{role_config['role']}_login",
            type="primary",
            use_container_width=True,
        ):
            login_as(role_config, selected_user)

