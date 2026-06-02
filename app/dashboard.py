import streamlit as st
import pandas as pd
import json
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

# ─────────────────────────────────────────────
#  PAGE CONFIG
# ─────────────────────────────────────────────
st.set_page_config(
    page_title="Purplle Store Intelligence",
    page_icon="💜",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ─────────────────────────────────────────────
#  GLOBAL STYLES
# ─────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');

/* ---------- GLOBAL ---------- */

html, body, [class*="css"] {
    font-family: 'Inter', sans-serif;
}

#MainMenu, footer, header {
    visibility: hidden;
}

.block-container {
    padding: 1.5rem 2rem 3rem;
}

/* ---------- ANIMATIONS ---------- */

@keyframes fadeUp {
    from {
        opacity: 0;
        transform: translateY(18px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

/* ---------- SIDEBAR ---------- */

[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #1a0533 0%,
        #2d0a5e 50%,
        #1a0533 100%
    );
    border-right: 1px solid rgba(167,97,247,0.25);
}

[data-testid="stSidebar"] * {
    color: #ffffff !important;
}

[data-testid="stSidebar"] .stRadio label {
    font-size: 0.9rem !important;
}

[data-testid="stSidebar"] hr {
    border-color: rgba(167,97,247,0.3) !important;
}

/* ---------- TOP BANNER ---------- */

.top-banner {
    background: linear-gradient(
        135deg,
        #1a0533 0%,
        #4c1d95 50%,
        #1a0533 100%
    );
    border: 1px solid rgba(167,97,247,0.3);
    border-radius: 20px;
    padding: 1.5rem 2rem;
    margin-bottom: 1.5rem;

    animation: fadeUp .7s ease;
}

.banner-title {
    font-size: 1.8rem;
    font-weight: 700;
    color: white;
}

.banner-subtitle {
    color: #e9d5ff;
    font-size: 0.85rem;
}

.banner-badge {
    background: rgba(255,255,255,0.12);
    border-radius: 20px;
    padding: 0.4rem 0.9rem;
    color: white;
    font-size: 0.75rem;
    font-weight: 600;
}

/* ---------- KPI CARDS ---------- */

.kpi-card {
    background: linear-gradient(
        135deg,
        #1e0547 0%,
        #2d0a5e 100%
    );

    border: 1px solid rgba(167,97,247,0.3);
    border-radius: 18px;

    padding: 1.25rem 1.5rem;

    position: relative;
    overflow: hidden;

    transition: all .25s ease;
    animation: fadeUp .7s ease;
}

.kpi-card:hover {
    transform: translateY(-5px);
    box-shadow: 0 15px 40px rgba(124,58,237,.35);
}

.kpi-card::before {
    content: "";

    position: absolute;
    top: -40px;
    right: -40px;

    width: 120px;
    height: 120px;

    border-radius: 50%;

    background: rgba(255,255,255,.05);
}

.kpi-icon {
    font-size: 1.8rem;
    margin-bottom: .5rem;
}

.kpi-label {
    color: #e9d5ff;
    font-size: .75rem;
    font-weight: 600;
    text-transform: uppercase;
    letter-spacing: .08em;
}

.kpi-value {
    color: white;
    font-size: 2rem;
    font-weight: 700;
}

.kpi-delta {
    color: #7cf0b0;
    font-size: .8rem;
}

.kpi-delta.neg {
    color: #ff7b7b;
}

/* ---------- SECTION HEADER ---------- */

.section-header {
    display: flex;
    align-items: center;
    gap: .6rem;

    margin-top: 2rem;
    margin-bottom: 1rem;

    padding-bottom: .5rem;

    border-bottom: 1px solid rgba(167,97,247,.2);
}

.section-header h3 {
    color: #5B21B6;
    font-size: 1.15rem;
    font-weight: 700;
    margin: 0;
}

.section-icon {
    font-size: 1.2rem;
}

/* ---------- ZONE CARDS ---------- */

.zone-card {
    background: linear-gradient(
        135deg,
        #17033f,
        #26085f
    );

    border-radius: 14px;
    border: 1px solid rgba(167,97,247,.25);

    padding: 1rem;

    margin-bottom: .8rem;

    animation: fadeUp .7s ease;
}

.zone-card-title {
    color: #ffffff;
    font-weight: 700;
    font-size: .9rem;
    margin-bottom: .6rem;
}

.zone-stat-row {
    display: flex;
    justify-content: space-between;
    margin-bottom: .4rem;
}

.zone-stat-label {
    color: #e9d5ff;
    font-size: .8rem;
}

.zone-stat-value {
    color: white;
    font-size: .85rem;
    font-weight: 600;
}

/* ---------- INSIGHTS ---------- */

.insight-card {
    background: #1f1038;

    border-left: 5px solid #9b59f5;

    border-radius: 12px;

    padding: 1rem;

    margin-bottom: .8rem;

    color: white;

    font-size: .92rem;

    line-height: 1.6;

    font-weight: 500;

    animation: fadeUp .7s ease;
}

.insight-card strong {
    color: #FFD166;
    font-weight: 700;
}

/* ---------- TABS ---------- */

[data-baseweb="tab-list"] {
    background: rgba(45,10,94,.45) !important;

    border-radius: 10px;

    padding: 4px;

    gap: 4px;
}

[data-baseweb="tab"] {
    color: #d4b8fc !important;

    border-radius: 8px !important;

    font-size: .85rem !important;

    font-weight: 500 !important;
}

[aria-selected="true"][data-baseweb="tab"] {
    background: #7c3aed !important;
    color: white !important;
}

/* ---------- PROGRESS ---------- */

.stProgress > div > div > div {
    background-color: #9b59f5 !important;
}

/* ---------- DIVIDER ---------- */

.purple-divider {
    height: 2px;
    border: none;

    background: linear-gradient(
        90deg,
        #7c3aed,
        transparent
    );

    border-radius: 2px;

    margin: 1rem 0;
}

/* ---------- TABLE ---------- */

[data-testid="stDataFrame"] {
    border-radius: 12px;
    overflow: hidden;
}

/* ---------- SCROLLBAR ---------- */

::-webkit-scrollbar {
    width: 8px;
}

::-webkit-scrollbar-thumb {
    background: #7c3aed;
    border-radius: 10px;
}

::-webkit-scrollbar-track {
    background: rgba(0,0,0,0);
}
</style>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  PLOTLY THEME
# ─────────────────────────────────────────────
PLOTLY_LAYOUT = dict(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font=dict(family="Inter", color="#ffffff", size=12),
    margin=dict(l=0, r=0, t=30, b=0),
    legend=dict(
        bgcolor="rgba(26,5,51,0.6)",
        bordercolor="rgba(167,97,247,0.3)",
        borderwidth=1,
        font=dict(color="#c9a0f7"),
    ),
    xaxis=dict(
        gridcolor="rgba(167,97,247,0.1)",
        tickcolor="#7c3aed",
        linecolor="rgba(167,97,247,0.2)",
        tickfont=dict(color="#b89ad4"),
        title_font=dict(color="#b89ad4"),
    ),
    yaxis=dict(
        gridcolor="rgba(167,97,247,0.1)",
        tickcolor="#7c3aed",
        linecolor="rgba(167,97,247,0.2)",
        tickfont=dict(color="#b89ad4"),
        title_font=dict(color="#b89ad4"),
    ),
)

PURPLE_SEQ   = ["#3b0f8a", "#5a1db5", "#7c3aed", "#9b59f5", "#b989f9", "#d4b8fc"]
ZONE_COLORS  = ["#7c3aed", "#0ea5e9", "#f59e0b", "#10b981", "#ef4444", "#ec4899"]

# ─────────────────────────────────────────────
#  DATA LOAD
# ─────────────────────────────────────────────
@st.cache_data
def load_data():

    with open("outputs/events.json", "r") as f:
        events = json.load(f)

    try:
        with open("outputs/anomalies.json", "r") as f:
            anomalies = json.load(f)
    except:
        anomalies = []

    df = pd.DataFrame(events)

    return df, anomalies


try:
    df, anomalies = load_data()
    data_ok = True

except FileNotFoundError:

    np.random.seed(42)

    zones = [
        "ALPS",
        "SWISS BEAUTY",
        "LAKME",
        "FACES CANADA",
        "MAYBELLINE"
    ]

    n = 400

    df = pd.DataFrame({
        "visitor_id": [
            f"V{np.random.randint(1,80):03d}"
            for _ in range(n)
        ],
        "zone": np.random.choice(
            zones,
            n,
            p=[0.25, 0.18, 0.22, 0.15, 0.20]
        ),
        "dwell_seconds": np.random.exponential(
            45,
            n
        ).clip(5, 300).astype(int),
        "timestamp": pd.date_range(
            "2024-01-15 09:00",
            periods=n,
            freq="90s"
        ),
        "event_type": np.random.choice(
            ["entry", "exit", "dwell"],
            n,
            p=[0.4, 0.35, 0.25]
        )
    })

    anomalies = []

    data_ok = False


# ─────────────────────────────────────────────
#  DERIVED METRICS
# ─────────────────────────────────────────────

total_visitors = df["visitor_id"].nunique()

total_events = len(df)

total_anomalies = len(anomalies)

zone_visits = df["zone"].value_counts()

avg_dwell = df.groupby(
    "zone"
)["dwell_seconds"].mean()

overall_avg_dwell = (
    df["dwell_seconds"].mean()
    if "dwell_seconds" in df.columns
    else 0
)

top_zone = (
    zone_visits.idxmax()
    if not zone_visits.empty
    else "N/A"
)

has_ts = "timestamp" in df.columns

if has_ts:

    df["timestamp"] = pd.to_datetime(
        df["timestamp"]
    )

    df["hour"] = df["timestamp"].dt.hour

    peak_hour_val = (
        df["hour"]
        .value_counts()
        .idxmax()
    )

    peak_hour_str = f"{peak_hour_val:02d}:00"

else:

    peak_hour_str = "N/A"
    peak_hour_val = None

# ─────────────────────────────────────────────
# KPI CARDS
# ─────────────────────────────────────────────

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "👥 Visitors",
        total_visitors
    )

with col2:
    st.metric(
        "📊 Events",
        total_events
    )

with col3:
    st.metric(
        "🚨 Anomalies",
        total_anomalies
    )

with col4:
    st.metric(
        "⭐ Top Zone",
        top_zone
    )

# ─────────────────────────────────────────────
#  SIDEBAR
# ─────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding: 1rem 0 0.5rem;">
        <div style="font-size:2.4rem;">💜</div>
        <div style="color:#d4aaff; font-size:1rem; font-weight:700; margin-top:0.3rem;">Purplle</div>
        <div style="color:#7c5a9a; font-size:0.7rem; letter-spacing:0.12em; text-transform:uppercase;">Store Intelligence</div>
    </div>
    <hr/>
    """, unsafe_allow_html=True)

    st.markdown("**📍 Navigation**")
    page = st.radio(
        "",
        ["🏠  Overview", "📊  Zone Analytics", "🗺️  Heatmap", "🔍  Raw Events"],
        label_visibility="collapsed",
    )

    st.markdown("<hr/>", unsafe_allow_html=True)
    st.markdown("**⚙️ Filters**")

    selected_zones = st.multiselect(
        "Select Zones",
        options=df["zone"].unique().tolist(),
        default=df["zone"].unique().tolist(),
    )

    if "event_type" in df.columns:
        selected_events = st.multiselect(
            "Event Types",
            options=df["event_type"].unique().tolist(),
            default=df["event_type"].unique().tolist(),
        )
        df_f = df[df["zone"].isin(selected_zones) & df["event_type"].isin(selected_events)]
    else:
        df_f = df[df["zone"].isin(selected_zones)]

    st.markdown("<hr/>", unsafe_allow_html=True)
    if not data_ok:
        st.warning("⚠️ Demo data — connect `outputs/events.json`")
    else:
        st.success("✅ Live data connected")

    st.markdown("""
    <div style="color:#5a3f7a; font-size:0.65rem; text-align:center; margin-top:2rem;">
        Purplle Store Intelligence v1.0<br/>Powered by YOLOv8 + ByteTrack
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  TOP BANNER
# ─────────────────────────────────────────────
st.markdown(f"""
<div class="top-banner">
    <div>
        <p class="banner-title">💜 Purplle Store Intelligence Dashboard</p>
        <p class="banner-subtitle">Real-time visitor analytics · Zone performance · Dwell insights</p>
    </div>
    <div>
        <span class="banner-badge">🟢 LIVE</span>
    </div>
</div>
""", unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  HELPER — KPI card
# ─────────────────────────────────────────────
def kpi_card(icon, label, value, delta=None, delta_neg=False):
    delta_html = ""
    if delta:
        cls = "neg" if delta_neg else ""
        arrow = "▼" if delta_neg else "▲"
        delta_html = f'<div class="kpi-delta {cls}">{arrow} {delta}</div>'
    st.markdown(f"""
    <div class="kpi-card">
        <span class="kpi-icon">{icon}</span>
        <div class="kpi-label">{label}</div>
        <div class="kpi-value">{value}</div>
        {delta_html}
    </div>
    """, unsafe_allow_html=True)

def section_header(icon, title):
    st.markdown(f"""
    <div class="section-header">
        <span class="section-icon">{icon}</span>
        <h3>{title}</h3>
    </div>
    """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  ════════════  PAGE: OVERVIEW  ════════════
# ─────────────────────────────────────────────
if "Overview" in page:

    # ── KPI Row ──
    section_header("📈", "Key Performance Indicators")
    c1, c2, c3, c4, c5 = st.columns(5)
    with c1: kpi_card("👥", "Total Visitors",    f"{total_visitors:,}",       delta="vs yesterday")
    with c2: kpi_card("⚡", "Total Events",       f"{total_events:,}",         delta="session events")
    with c3: kpi_card("⏱️", "Avg Dwell Time",    f"{overall_avg_dwell:.0f}s",  delta="per visit")
    with c4: kpi_card("🏆", "Top Zone",           top_zone,                    delta="most traffic")
    with c5: kpi_card("🕐", "Peak Hour",          peak_hour_str,               delta="busiest slot")

    st.markdown("<div class='purple-divider'></div>", unsafe_allow_html=True)

    # ── Zone Visits + Dwell side by side ──
    col_l, col_r = st.columns(2, gap="large")

    with col_l:
        section_header("📊", "Zone Visit Distribution")
        zone_df = df_f["zone"].value_counts().reset_index()
        zone_df.columns = ["zone", "visits"]
        fig = px.bar(
            zone_df, x="visits", y="zone", orientation="h",
            color="visits", color_continuous_scale=PURPLE_SEQ,
            text="visits",
        )
        fig.update_traces(textposition="outside", textfont_color="#e8d5ff",
                          marker_line_width=0)
        fig.update_layout(**PLOTLY_LAYOUT, coloraxis_showscale=False,
                          height=300, title_text="")
        st.plotly_chart(fig, use_container_width=True)

    with col_r:
        section_header("⏱️", "Average Dwell Time by Zone")
        dwell_df = df_f.groupby("zone")["dwell_seconds"].mean().reset_index()
        dwell_df.columns = ["zone", "avg_dwell"]
        dwell_df = dwell_df.sort_values("avg_dwell", ascending=True)
        fig2 = px.bar(
            dwell_df, x="avg_dwell", y="zone", orientation="h",
            color="avg_dwell", color_continuous_scale=["#0ea5e9","#7c3aed","#f59e0b"],
            text=dwell_df["avg_dwell"].round(1).astype(str) + "s",
        )
        fig2.update_traces(textposition="outside", textfont_color="#e8d5ff",
                           marker_line_width=0)
        fig2.update_layout(**PLOTLY_LAYOUT, coloraxis_showscale=False,
                           height=300, title_text="")
        st.plotly_chart(fig2, use_container_width=True)

    # ── Hourly traffic (if timestamp available) ──
    if has_ts:
        section_header("🕐", "Hourly Visitor Traffic")
        hourly = df_f.groupby("hour")["visitor_id"].count().reset_index()
        hourly.columns = ["hour", "count"]
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=hourly["hour"], y=hourly["count"],
            mode="lines+markers",
            line=dict(color="#9b59f5", width=3),
            marker=dict(size=7, color="#d4b8fc", line=dict(width=2, color="#7c3aed")),
            fill="tozeroy",
            fillcolor="rgba(124,58,237,0.15)",
            name="Visitors",
        ))
        if peak_hour_val is not None:
            peak_y = hourly[hourly["hour"] == peak_hour_val]["count"].values
            if len(peak_y):
                fig3.add_trace(go.Scatter(
                    x=[peak_hour_val], y=[peak_y[0]],
                    mode="markers+text",
                    marker=dict(size=14, color="#f59e0b", symbol="star"),
                    text=["Peak"], textposition="top center",
                    textfont=dict(color="#f59e0b", size=11),
                    name="Peak",
                ))
        fig3.update_layout(**PLOTLY_LAYOUT, height=260,
                           xaxis=dict(**PLOTLY_LAYOUT["xaxis"], title="Hour of Day"),
                           yaxis=dict(**PLOTLY_LAYOUT["yaxis"], title="Events"))
        st.plotly_chart(fig3, use_container_width=True)

    # ── Insights Panel ──
    section_header("💡", "Business Insights")
    ic1, ic2 = st.columns(2)
    with ic1:
        st.markdown(f"""
        <div class="insight-card">
            🏆 <strong>{top_zone}</strong> is the highest traffic zone with
            <strong>{zone_visits.max():,}</strong> visits.
            Consider allocating additional staff and promotions here.
        </div>
        <div class="insight-card">⏱️ Average dwell across all zones is
        <strong>{overall_avg_dwell:.0f} seconds</strong> — consider engagement strategies for low-dwell zones.</div>
        """, unsafe_allow_html=True)
    with ic2:
        low_dwell_zone = avg_dwell.idxmin() if not avg_dwell.empty else "N/A"
        low_val = avg_dwell.min() if not avg_dwell.empty else 0
        st.markdown(f"""
        <div class="insight-card">⚠️ <strong>{low_dwell_zone}</strong> has the lowest average dwell of
        <strong>{low_val:.0f}s</strong> — review product placement or signage.</div>
        <div class="insight-card">📅 Peak shopping hour is <strong>{peak_hour_str}</strong>
        — schedule promotions and staff accordingly.</div>
        """, unsafe_allow_html=True)

# ─────────────────────────────────────────────
#  ════════  PAGE: ZONE ANALYTICS  ════════
# ─────────────────────────────────────────────
elif "Zone Analytics" in page:

    section_header("📊", "Zone-wise Performance")

    tabs = st.tabs([
        "📈 Visit Share",
        "⏱️ Dwell Analysis",
        "🥇 Zone Cards",
        "📉 Event Breakdown"
    ])

    # =====================================================
    # TAB 1 : VISIT SHARE
    # =====================================================
    with tabs[0]:

        col1, col2 = st.columns([1, 1])

        zone_counts = (
            df_f["zone"]
            .value_counts()
            .reset_index()
        )

        zone_counts.columns = [
            "zone",
            "count"
        ]

        with col1:

            fig = px.pie(
                zone_counts,
                values="count",
                names="zone",
                hole=0.55,
                color="zone",
                color_discrete_sequence=ZONE_COLORS
            )

            fig.update_traces(
                textinfo="percent+label",
                textfont_size=12,
                marker=dict(
                    line=dict(
                        color="#1a0533",
                        width=2
                    )
                )
            )

            fig.update_layout(
                height=420,
                paper_bgcolor="rgba(0,0,0,0)",
                plot_bgcolor="rgba(0,0,0,0)",
                font=dict(color="white"),
                annotations=[
                    dict(
                        text=f"<b>{total_visitors}</b><br>Visitors",
                        x=0.5,
                        y=0.5,
                        showarrow=False,
                        font=dict(
                            size=18,
                            color="#d4aaff"
                        )
                    )
                ]
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        with col2:

            section_header(
                "📊",
                "Visit Share by Zone"
            )

            total = zone_counts["count"].sum()

            for _, row in zone_counts.iterrows():

                pct = (
                    row["count"] / total
                ) * 100

                st.markdown(
                    f"""
                    **{row['zone']}**
                    """
                )

                st.progress(
                    int(pct)
                )

                st.caption(
                    f"{row['count']} visits ({pct:.1f}%)"
                )

    # =====================================================
    # TAB 2 : DWELL ANALYSIS
    # =====================================================
    with tabs[1]:

        dwell_box = df_f[
            ["zone", "dwell_seconds"]
        ].dropna()

        fig = px.box(
            dwell_box,
            x="zone",
            y="dwell_seconds",
            color="zone",
            points="outliers",
            color_discrete_sequence=ZONE_COLORS
        )

        fig.update_layout(
            height=420,
            showlegend=False,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )

        fig.update_yaxes(
            title="Dwell Time (Seconds)"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

        st.markdown(
            "### Dwell Statistics"
        )

        dwell_stats = (
            df_f.groupby("zone")
            ["dwell_seconds"]
            .agg(
                Mean="mean",
                Median="median",
                Max="max",
                Min="min"
            )
            .round(2)
        )

        st.dataframe(
            dwell_stats,
            use_container_width=True
        )

    # =====================================================
    # TAB 3 : ZONE CARDS
    # =====================================================
    with tabs[2]:

        cols = st.columns(3)

        zones_list = (
            df_f["zone"]
            .dropna()
            .unique()
        )

        for i, zone in enumerate(zones_list):

            zdf = df_f[
                df_f["zone"] == zone
            ]

            visits = len(zdf)

            unique_visitors = (
                zdf["visitor_id"]
                .nunique()
            )

            avg_dwell = (
                zdf["dwell_seconds"]
                .mean()
                if "dwell_seconds" in zdf.columns
                else 0
            )

            share = (
                visits /
                len(df_f)
            ) * 100

            with cols[i % 3]:

                st.markdown(
                    f"""
                    <div class="zone-card">
                        <div class="zone-card-title">
                            {zone}
                        </div>

                        <div class="zone-stat-row">
                            <span>Total Visits</span>
                            <span>{visits}</span>
                        </div>

                        <div class="zone-stat-row">
                            <span>Visitors</span>
                            <span>{unique_visitors}</span>
                        </div>

                        <div class="zone-stat-row">
                            <span>Avg Dwell</span>
                            <span>{avg_dwell:.1f}s</span>
                        </div>

                        <div class="zone-stat-row">
                            <span>Traffic Share</span>
                            <span>{share:.1f}%</span>
                        </div>
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # =====================================================
    # TAB 4 : EVENT BREAKDOWN
    # =====================================================
    with tabs[3]:

        zone_events = (
            df_f.groupby("zone")
            .size()
            .reset_index(name="count")
        )

        fig = px.bar(
            zone_events,
            x="zone",
            y="count",
            color="zone",
            text="count",
            color_discrete_sequence=ZONE_COLORS
        )

        fig.update_traces(
            textposition="outside"
        )

        fig.update_layout(
            height=420,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white"),
            showlegend=False
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )

# ─────────────────────────────────────────────
#  ════════════  PAGE: HEATMAP  ════════════
# ─────────────────────────────────────────────
elif "Heatmap" in page:

    section_header("🗺️", "Zone Activity Heatmap")

    if has_ts:
        hm_data = df_f.groupby(["hour","zone"]).size().reset_index(name="count")
        hm_pivot = hm_data.pivot(index="hour", columns="zone", values="count").fillna(0)

        fig = go.Figure(data=go.Heatmap(
            z=hm_pivot.values,
            x=hm_pivot.columns.tolist(),
            y=[f"{h:02d}:00" for h in hm_pivot.index],
            colorscale=[[0,"#1a0533"],[0.3,"#5a1db5"],
                        [0.6,"#9b59f5"],[1,"#f0c4ff"]],
            text=hm_pivot.values.astype(int),
            texttemplate="%{text}",
            textfont=dict(size=11, color="#fff"),
            hoverongaps=False,
            colorbar=dict(
                title="Events", tickfont=dict(color="#c9a0f7"),
                titlefont=dict(color="#c9a0f7"),
            ),
        ))
        fig.update_layout(**PLOTLY_LAYOUT, height=500,
                          xaxis=dict(**PLOTLY_LAYOUT["xaxis"], title="Zone"),
                          yaxis=dict(**PLOTLY_LAYOUT["yaxis"], title="Hour of Day"))
        st.plotly_chart(fig, use_container_width=True)

        # Dwell heatmap
        section_header("⏱️", "Dwell Time Heatmap (seconds)")
        dwell_hm = df_f.groupby(["hour","zone"])["dwell_seconds"].mean().reset_index()
        dwell_pv = dwell_hm.pivot(index="hour", columns="zone", values="dwell_seconds").fillna(0)
        fig2 = go.Figure(data=go.Heatmap(
            z=dwell_pv.values.round(0),
            x=dwell_pv.columns.tolist(),
            y=[f"{h:02d}:00" for h in dwell_pv.index],
            colorscale=[[0,"#0c1445"],[0.5,"#0ea5e9"],[1,"#7cf0b0"]],
            text=dwell_pv.values.round(0).astype(int),
            texttemplate="%{text}s",
            textfont=dict(size=10, color="#fff"),
            colorbar=dict(title="Avg Dwell (s)", tickfont=dict(color="#c9a0f7"),
                          titlefont=dict(color="#c9a0f7")),
        ))
        fig2.update_layout(**PLOTLY_LAYOUT, height=500)
        st.plotly_chart(fig2, use_container_width=True)
    else:
        # Fallback heatmap without timestamp
        section_header("📊", "Dwell × Zone Matrix")
        dwell_pv = df_f.groupby(["zone","visitor_id"])["dwell_seconds"].mean().unstack(fill_value=0)
        sample = dwell_pv.iloc[:, :20]
        fig = go.Figure(data=go.Heatmap(
            z=sample.values, x=sample.columns.tolist(),
            y=sample.index.tolist(),
            colorscale=[[0,"#1a0533"],[1,"#d4b8fc"]],
        ))
        fig.update_layout(**PLOTLY_LAYOUT, height=400)
        st.plotly_chart(fig, use_container_width=True)
        st.info("No `timestamp` column — showing zone × visitor dwell matrix instead.")

# ─────────────────────────────────────────────
#  ════════════  PAGE: RAW EVENTS  ════════════
# ─────────────────────────────────────────────
elif "Raw Events" in page:

    section_header("🔍", "Raw Events")

    c1, c2, c3 = st.columns(3)
    c1.metric("Filtered Rows", f"{len(df_f):,}")
    c2.metric("Unique Visitors", f"{df_f['visitor_id'].nunique():,}")
    c3.metric("Zones", f"{df_f['zone'].nunique()}")

    st.markdown("<br>", unsafe_allow_html=True)

    search = st.text_input("🔎 Search visitor ID or zone", "")
    if search:
        display_df = df_f[
            df_f["visitor_id"].astype(str).str.contains(search, case=False) |
            df_f["zone"].astype(str).str.contains(search, case=False)
        ]
    else:
        display_df = df_f

    # ── Raw Events (original logic — unchanged) ──
    st.subheader("Raw Events")
    st.dataframe(display_df, use_container_width=True, height=480)

    st.download_button(
        "⬇️  Download filtered CSV",
        data=display_df.to_csv(index=False).encode(),
        file_name="purplle_events_filtered.csv",
        mime="text/csv",
    )
