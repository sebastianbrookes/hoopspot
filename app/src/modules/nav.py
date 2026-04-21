# Idea borrowed from https://github.com/fsmosca/sample-streamlit-authenticator

# This file has functions to add links to the left sidebar based on the user's role.

import streamlit as st

# ---- General ----------------------------------------------------------------


def sidebar_brand():
    st.sidebar.markdown(
        """
        <div style="padding: 0.25rem 0 1rem 0;">
            <div style="
                display:flex;
                align-items:center;
                justify-content:center;
                padding:0.8rem;
                border-radius:16px;
                background:linear-gradient(180deg, rgba(15,23,42,0.92), rgba(15,23,42,0.72));
                border:1px solid rgba(148,163,184,0.12);
            ">
                <div style="
                    width:44px;
                    height:44px;
                    border-radius:14px;
                    display:flex;
                    align-items:center;
                    justify-content:center;
                    background:linear-gradient(135deg, rgba(249,115,22,0.18), rgba(234,88,12,0.28));
                    border:1px solid rgba(249,115,22,0.28);
                    flex-shrink:0;
                ">
                    <svg width="28" height="28" viewBox="0 0 52 52" fill="none" xmlns="http://www.w3.org/2000/svg">
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
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def home_nav():
    st.sidebar.page_link("Home.py", label="Home", icon="🏠")


def about_page_nav():
    st.sidebar.page_link("pages/30_About.py", label="About", icon="🧠")


# ---- Role: pickup_player ----------------------------------------------------


def pickup_home_nav():
    st.sidebar.page_link("pages/00_Pickup_Home.py", label="Court Finder", icon="🏀")


def pickup_profile_nav():
    st.sidebar.page_link("pages/01_Pickup_Profile.py", label="Profile", icon="👤")


def write_review_nav():
    st.sidebar.page_link("pages/02_Write_Review.py", label="Write Review", icon="⭐")


def log_game_nav():
    st.sidebar.page_link("pages/03_Log_Game.py", label="Log Game", icon="📝")


# ---- Role: competitive_player -----------------------------------------------


def competitive_home_nav():
    st.sidebar.page_link("pages/10_Competitive_Home.py", label="Dashboard", icon="🏠")


def leaderboard_nav():
    st.sidebar.page_link("pages/11_Leaderboard.py", label="Leaderboard", icon="🏆")


def tournaments_nav():
    st.sidebar.page_link("pages/12_Tournaments.py", label="Tournaments", icon="🥇")


def my_games_nav():
    st.sidebar.page_link("pages/13_My_Games.py", label="My Games", icon="🎮")


# ---- Role: administrator ----------------------------------------------------


def admin_home_nav():
    st.sidebar.page_link("pages/20_Admin_Home.py", label="System Admin", icon="🖥️")


def manage_courts_nav():
    st.sidebar.page_link("pages/22_Manage_Courts.py", label="Manage Courts", icon="🏀")


def moderate_reviews_nav():
    st.sidebar.page_link("pages/23_Manage_Reviews.py", label="Moderate Reviews", icon="⭐")


def manage_players_nav():
    st.sidebar.page_link("pages/24_Manage_Players.py", label="Manage Players", icon="👥")


# ---- Role: data_analyst -----------------------------------------------------


def analyst_overview_nav():
    st.sidebar.page_link("pages/40_Analyst_Profile.py", label="Overview", icon="📊")


def analyst_dashboard_nav():
    st.sidebar.page_link("pages/41_Analyst_Dashboard.py", label="Dashboards", icon="📈")


def analyst_heatmap_nav():
    st.sidebar.page_link("pages/42_Analyst_Heatmap.py", label="Heatmap", icon="🗺️")


def analyst_csv_nav():
    st.sidebar.page_link("pages/44_Analyst_CSV.py", label="CSV Export", icon="📥")


# ---- Sidebar assembly -------------------------------------------------------


def SideBarLinks(show_home=False):
    """
    Renders sidebar navigation links based on the logged-in user's role.
    The role is stored in st.session_state when the user logs in on Home.py.
    """

    sidebar_brand()

    if "authenticated" not in st.session_state:
        st.session_state.authenticated = False
        st.switch_page("Home.py")

    if show_home:
        home_nav()

    if st.session_state["authenticated"]:
        if st.session_state["role"] == "pickup_player":
            pickup_home_nav()
            pickup_profile_nav()
            write_review_nav()
            log_game_nav()

        if st.session_state["role"] == "competitive_player":
            competitive_home_nav()
            leaderboard_nav()
            tournaments_nav()
            my_games_nav()

        if st.session_state["role"] == "administrator":
            admin_home_nav()
            manage_courts_nav()
            moderate_reviews_nav()
            manage_players_nav()

        if st.session_state["role"] == "data_analyst":
            analyst_overview_nav()
            analyst_dashboard_nav()
            analyst_heatmap_nav()
            analyst_csv_nav()

    if st.session_state["authenticated"]:
        if st.sidebar.button("Logout"):
            del st.session_state["role"]
            del st.session_state["authenticated"]
            st.switch_page("Home.py")

            
