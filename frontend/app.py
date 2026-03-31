"""
INTERRA – Mockup Viewer
Three-screen prototype for human-in-the-loop table search in data lakes.
Edit the SCREENS list to update any screen.
"""

import streamlit as st
import httpx
import pandas as pd

BACKEND_URL = "http://backend:8000"

# ── Page config ───────────────────────────────────────────────────────────────
st.set_page_config(page_title="INTERRA", layout="wide", initial_sidebar_state="expanded")

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
/* Hide Streamlit chrome */
#MainMenu, footer, header { visibility: hidden; }

/* Badge circles for numbered items */
.badge {
    display: inline-flex; align-items: center; justify-content: center;
    width: 32px; height: 32px; min-width: 32px;
    border-radius: 50%; color: white; font-weight: 700; font-size: 15px;
    margin-right: 10px;
}
.badge-table { background-color: #2e6db4; }
.badge-op    { background-color: #2a7d6b; }

/* Card wrapper */
.rec-card {
    display: flex; align-items: flex-start;
    background: #fafbfd; border: 1px solid #dde3ed; border-radius: 6px;
    padding: 14px 16px; margin-bottom: 10px;
}
.op-card-wrap .rec-card { max-width: 340px; }
.rec-card-body { flex: 1; }
.rec-card-name { font-weight: 700; font-size: 18px; color: #1b2a4a; }
.rec-card-desc { font-size: 16px; color: #555; margin-top: 4px; line-height: 1.55; }

/* Session pills */
.pill {
    display: inline-block; padding: 5px 14px; border-radius: 14px;
    font-size: 14px; font-weight: 600; margin: 4px 4px 4px 0;
    border: 1.5px solid;
}
.pill-accepted { color: #217a5b; border-color: #217a5b; background: #eef8f4; }
.pill-rejected { color: #c0392b; border-color: #c0392b; background: #fdf2f0; }
.pill-neutral  { color: #2e6db4; border-color: #2e6db4; background: #eef4fc; }

/* Explanation box */
.explain-box {
    background: #edf7f1; border: 1px solid #a3d4b5; border-radius: 6px;
    padding: 16px 20px; margin-top: 14px;
}
.explain-label { color: #2a6e44; font-weight: 700; font-size: 18px; margin-bottom: 6px; }
.explain-text  { color: #3a3a3a; font-size: 16px; line-height: 1.6; }

/* Chat-style request box */
.request-wrapper {
    background: #ffffff;
    border: 2px solid #d0d5dd;
    border-radius: 12px;
    padding: 14px 16px 8px 16px;
    margin-top: 4px;
    box-shadow: 0 1px 4px rgba(0,0,0,0.06);
    display: flex;
    align-items: flex-start;
    gap: 12px;
}
.request-icon { font-size: 26px; margin-top: 4px; }
.request-inner { flex: 1; }

div[data-testid="stTextArea"] textarea {
    background-color: #f9fafb;
    border: 1.5px solid #e0e3e8;
    border-radius: 8px;
    color: #2c2c2c;
    font-size: 16px;
    line-height: 1.55;
    padding: 12px 14px;
}
div[data-testid="stTextArea"] textarea:focus {
    border-color: #2e6db4;
    box-shadow: 0 0 0 3px rgba(46, 109, 180, 0.15);
    background-color: #ffffff;
}

/* Table preview area */
.preview-header {
    display: flex; align-items: center; gap: 10px;
    margin-bottom: 8px;
}
.preview-title {
    font-weight: 700; font-size: 18px; color: #1b2a4a;
}
.preview-tag {
    background: #2e6db4; color: white; border-radius: 5px;
    padding: 3px 10px; font-size: 13px; font-weight: 600;
}

/* Navigation indicator */
.nav-indicator {
    text-align: center; font-size: 15px; font-weight: 600; color: #555;
    padding-top: 6px;
}
</style>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SCREEN DATA – edit content here
# ══════════════════════════════════════════════════════════════════════════════

SCREENS = [
    # ── Screen 1: Exploratory ─────────────────────────────────────────────────
    {
        "label": "Stage 1: Exploratory",
        "title": "INTERRA Interface \u2013 Exploratory Stage",
        "request": "Find tables about public transit usage and income levels in the city.",
        "session_items": [
            ("neutral",  "New session"),
            ("neutral",  "No prior feedback"),
        ],
        "tables": [
            ("T1", "bus_ridership_2022",
             "Monthly bus ridership counts per route and borough."),
            ("T3", "neighbourhood_income_census",
             "Median household income, poverty rate, and employment status per census tract."),
            ("T4", "transit_accessibility_index",
             "Transit-access score per neighborhood, joinable on tract ID."),
        ],
        "operations": [
            ("Compare",   "Compare ridership patterns with neighborhood socioeconomic indicators."),
            ("Join",      "Join ridership and census data through tract-level identifiers."),
            ("Aggregate", "Summarize values by borough or tract for exploratory analysis."),
        ],
        "explanation": (
            "The request is still broad, so the system prioritizes summary-level tables "
            "and comparison-oriented operations that support high-level exploratory analysis."
        ),
    },

    # ── Screen 2: Predictive ──────────────────────────────────────────────────
    {
        "label": "Stage 2: Predictive",
        "title": "INTERRA Interface \u2013 Predictive Stage",
        "request": (
            "I want to predict commute mode choice from income and neighborhood "
            "transit access. Can I also get individual-level data?"
        ),
        "session_items": [
            ("accepted", "Accepted: T1, T3"),
            ("rejected", "Rejected: T4 \u2013 too coarse-grained"),
            ("neutral",  "Clarified goal: predictive modeling"),
            ("neutral",  "Need: individual-level data"),
        ],
        "tables": [
            ("T6", "commute_survey_microdata",
             "Individual-level survey records with commute mode, duration, and self-reported income bracket."),
            ("T3", "neighbourhood_income_census",
             "Socioeconomic covariates for enrichment."),
            ("T4", "transit_accessibility_index",
             "Joinable neighborhood transit-access feature table."),
        ],
        "operations": [
            ("Join",     "Join microdata with census and accessibility features."),
            ("Filter",   "Restrict to relevant geography or subgroup before modeling."),
            ("Validate", "Validate key overlap before integration."),
        ],
        "explanation": (
            "After the clarification, the system infers a predictive goal and promotes "
            "individual-level and feature-rich tables, together with model-preparation operations."
        ),
    },

    # ── Screen 3: Validation ──────────────────────────────────────────────────
    {
        "label": "Stage 3: Validation",
        "title": "INTERRA Interface \u2013 Validation Stage",
        "request": (
            "Can I check whether the census tract IDs in the survey data actually "
            "overlap with those in the income table before joining?"
        ),
        "session_items": [
            ("accepted", "Accepted: T6, T3"),
            ("accepted", "Accepted operation: Join"),
            ("neutral",  "Current goal: validate integration feasibility"),
        ],
        "tables": [
            ("T6", "commute_survey_microdata",
             "Main individual-level integration target."),
            ("T3", "neighbourhood_income_census",
             "Main socioeconomic integration target."),
            ("T1", "bus_ridership_2022",
             "Optional aggregate fallback if tract-level overlap is incomplete."),
        ],
        "operations": [
            ("Validate", "Check overlap of tract identifiers before joining."),
            ("Filter",   "Restrict to shared keys if overlap is partial."),
            ("Join",     "Proceed with integration after validation."),
        ],
        "explanation": (
            "The current goal is pre-join validation, so the system prioritizes "
            "overlap checking and filtering before integration."
        ),
    },
]


# ══════════════════════════════════════════════════════════════════════════════
# Data fetching
# ══════════════════════════════════════════════════════════════════════════════

@st.cache_data(ttl=300)
def fetch_table(table_key: str) -> pd.DataFrame | None:
    """Fetch table data from backend and return as DataFrame."""
    try:
        resp = httpx.get(f"{BACKEND_URL}/tables/{table_key}", timeout=5)
        if resp.status_code == 200:
            return pd.DataFrame(resp.json()["rows"])
    except Exception:
        pass
    return None


# ══════════════════════════════════════════════════════════════════════════════
# Reusable components
# ══════════════════════════════════════════════════════════════════════════════

def RequestBox(text: str, screen_idx: int) -> None:
    """Chat-style input box pre-filled with the user's request."""
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown(
        '<div class="request-wrapper">'
        '  <div class="request-icon">&#128100;</div>'
        '  <div class="request-inner">',
        unsafe_allow_html=True,
    )
    st.text_area(
        "User request",
        value=text,
        height=80,
        key=f"req_{screen_idx}",
        label_visibility="collapsed",
        placeholder="Type your request here...",
    )
    st.markdown('</div></div>', unsafe_allow_html=True)
    st.markdown(
        '<div style="text-align:right; margin-top:-8px;">'
        '  <span style="background:#1b2a4a; color:white; padding:10px 32px; '
        '  border-radius:8px; font-size:18px; font-weight:600; cursor:pointer;">'
        '  Send</span>'
        '</div>',
        unsafe_allow_html=True,
    )


def SessionPanel(items: list) -> None:
    """Sidebar status panel showing session state as colored pills."""
    st.markdown("**Session state**")
    pills_html = ""
    for kind, text in items:
        pills_html += f'<span class="pill pill-{kind}">{text}</span> '
    st.markdown(pills_html, unsafe_allow_html=True)


def RecommendedTables(tables: list, screen_idx: int) -> None:
    """Clickable table cards. Selecting one stores its key in session state."""
    st.markdown("**Recommended tables**")
    for i, (tid, name, desc) in enumerate(tables, 1):
        # Card HTML
        st.markdown(
            f'<div class="rec-card">'
            f'  <span class="badge badge-table">{i}</span>'
            f'  <div class="rec-card-body">'
            f'    <div class="rec-card-name">{tid} &ndash; {name}</div>'
            f'    <div class="rec-card-desc">{desc}</div>'
            f'  </div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        # Small view button
        col_btn, col_pad = st.columns([1, 2])
        with col_btn:
            clicked = st.button(
                f"View {tid}",
                key=f"select_{screen_idx}_{tid}",
                use_container_width=True,
            )
        if clicked:
            st.session_state.selected_table = tid
            st.session_state.selected_table_name = name
            st.rerun()


def RecommendedOperations(operations: list) -> None:
    """Card list of recommended operations with numbered green badges."""
    st.markdown("**Recommended operations**")
    html = '<div class="op-card-wrap">'
    for i, (name, desc) in enumerate(operations, 1):
        html += (
            f'<div class="rec-card">'
            f'  <span class="badge badge-op">{i}</span>'
            f'  <div class="rec-card-body">'
            f'    <div class="rec-card-name">{name}</div>'
            f'    <div class="rec-card-desc">{desc}</div>'
            f'  </div>'
            f'</div>'
        )
    html += '</div>'
    st.markdown(html, unsafe_allow_html=True)


def ExplanationPanel(text: str) -> None:
    """Bottom box explaining why these recommendations are shown."""
    st.markdown(
        f'<div class="explain-box">'
        f'  <div class="explain-label">Why these recommendations now</div>'
        f'  <div class="explain-text">{text}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )


def TablePreview() -> None:
    """Show the selected table's data in a preview area."""
    if "selected_table" not in st.session_state:
        st.info("Click **View** on a recommended table above to preview its data.")
        return

    tid = st.session_state.selected_table
    name = st.session_state.get("selected_table_name", tid)

    st.markdown(
        f'<div class="preview-header">'
        f'  <span class="preview-tag">{tid}</span>'
        f'  <span class="preview-title">{name}</span>'
        f'</div>',
        unsafe_allow_html=True,
    )

    df = fetch_table(tid)
    if df is not None:
        st.dataframe(df, use_container_width=False, hide_index=True, height=200)
        st.caption(f"{len(df)} rows \u00d7 {len(df.columns)} columns")
    else:
        st.warning(f"Could not load data for {tid}. Is the backend running?")


def NavigationControls(current: int, total: int) -> None:
    """Previous / screen indicator / Next row."""
    col_prev, col_ind, col_next = st.columns([1, 2, 1])
    with col_prev:
        if st.button("\u2190 Previous", disabled=(current == 0), use_container_width=True):
            st.session_state.screen = current - 1
            # Clear table selection when changing screen
            st.session_state.pop("selected_table", None)
            st.session_state.pop("selected_table_name", None)
            st.rerun()
    with col_ind:
        label = SCREENS[current]["label"]
        st.markdown(
            f'<div class="nav-indicator">{label} &nbsp;\u2502&nbsp; {current + 1} / {total}</div>',
            unsafe_allow_html=True,
        )
    with col_next:
        if st.button("Next \u2192", disabled=(current == total - 1), use_container_width=True):
            st.session_state.screen = current + 1
            st.session_state.pop("selected_table", None)
            st.session_state.pop("selected_table_name", None)
            st.rerun()


# ══════════════════════════════════════════════════════════════════════════════
# App layout
# ══════════════════════════════════════════════════════════════════════════════

# Initialise state
if "screen" not in st.session_state:
    st.session_state.screen = 0

# ── Sidebar: menu + stage navigation + session state ─────────────────────────
SIDEBAR_ITEMS = [
    "Home",
    "Search Workspace",
    "Data Lake",
    "Recommended Tables",
    "Recommended Operations",
    "Intention View",
    "Session History",
    "Saved Results",
]

with st.sidebar:
    st.image("_interra_logo.png", width=130)
    for item in SIDEBAR_ITEMS:
        st.page_link("app.py", label=item, icon=None)

    st.divider()

    st.markdown("### Stage")
    for i, s in enumerate(SCREENS):
        is_active = (i == st.session_state.screen)
        if st.button(
            s["label"],
            key=f"nav_{i}",
            use_container_width=True,
            type="primary" if is_active else "secondary",
        ):
            st.session_state.screen = i
            st.session_state.pop("selected_table", None)
            st.session_state.pop("selected_table_name", None)
            st.rerun()

    st.divider()
    SessionPanel(SCREENS[st.session_state.screen]["session_items"])

idx   = st.session_state.screen
scr   = SCREENS[idx]
total = len(SCREENS)

# ── Header ────────────────────────────────────────────────────────────────────
st.title(scr["title"])

# ── Recommendations + Table preview ──────────────────────────────────────────
col_tables, col_ops, col_preview = st.columns([2, 1.5, 2.5], gap="medium")
with col_tables:
    RecommendedTables(scr["tables"], idx)
with col_ops:
    RecommendedOperations(scr["operations"])
with col_preview:
    st.markdown("**Table Preview**")
    TablePreview()

# ── Explanation (full width) ─────────────────────────────────────────────────
ExplanationPanel(scr["explanation"])

# ── Request text box (bottom, full width) ─────────────────────────────────────
RequestBox(scr["request"], idx)

# ── Navigation (bottom) ──────────────────────────────────────────────────────
st.divider()
NavigationControls(idx, total)
