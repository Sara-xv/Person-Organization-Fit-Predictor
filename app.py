import streamlit as st
import pandas as pd
import joblib
import plotly.graph_objects as go
import shap

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="SynapseTech HR Analytics",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded"
)

# =====================================================
# THEME MANAGER
# =====================================================

theme = st.sidebar.selectbox(
    "Theme",
    ["System", "Light", "Dark"]
)

LIGHT_THEME = """
<style>

.main{
background:#F8FAFC;
}

.block-container{
padding-top:2rem;
}

.metric-card{
background:white;
padding:1.5rem;
border-radius:18px;
box-shadow:0 4px 12px rgba(0,0,0,0.05);
border:1px solid #E5E7EB;
}

.glass{
background:white;
border-radius:20px;
padding:20px;
box-shadow:0px 8px 24px rgba(0,0,0,.05);
}

h1,h2,h3{
font-weight:700;
}

</style>
"""

DARK_THEME = """
<style>

.main{
background:#0F172A;
color:white;
}

.block-container{
padding-top:2rem;
}

.metric-card{
background:#1E293B;
padding:1.5rem;
border-radius:18px;
border:1px solid #334155;
}

.glass{
background:#1E293B;
border-radius:20px;
padding:20px;
border:1px solid #334155;
}

</style>
"""

SYSTEM_THEME = """
<style>

@media (prefers-color-scheme: dark){

.main{
background:#0F172A;
color:white;
}

}

@media (prefers-color-scheme: light){

.main{
background:#F8FAFC;
}

}

</style>
"""

if theme == "Light":
    st.markdown(LIGHT_THEME, unsafe_allow_html=True)

elif theme == "Dark":
    st.markdown(DARK_THEME, unsafe_allow_html=True)

else:
    st.markdown(SYSTEM_THEME, unsafe_allow_html=True)

# =====================================================
# MODEL LOADER
# =====================================================

@st.cache_resource
def load_artifacts():

    model = joblib.load(
        "random_forest_fit_model.pkl"
    )

    columns = joblib.load(
        "model_features_columns.pkl"
    )

    return model, columns

try:
    model, expected_columns = load_artifacts()

except Exception as e:

    st.error(
        f"Model loading error:\n{e}"
    )

    st.stop()

# =====================================================
# STATUS FUNCTIONS
# =====================================================

def get_status_text(score):

    if score >= 70:
        return "Excellent Fit"

    elif score >= 45:
        return "Moderate Fit"

    return "High Risk"


def get_status_color(score):

    if score >= 70:
        return "#10B981"

    elif score >= 45:
        return "#F59E0B"

    return "#EF4444"


def get_status_icon(score):

    if score >= 70:
        return "🟢"

    elif score >= 45:
        return "🟡"

    return "🔴"


# =====================================================
# PERSONALITY PROFILE
# =====================================================

def personality_profile(
        openness,
        conscientiousness,
        extraversion,
        agreeableness,
        neuroticism
):

    profile = []

    if openness > 4:
        profile.append("Innovative")

    if conscientiousness > 4:
        profile.append("Highly Reliable")

    if extraversion > 4:
        profile.append("Socially Active")

    if agreeableness > 4:
        profile.append("Collaborative")

    if neuroticism > 4:
        profile.append("Stress Sensitive")

    if len(profile) == 0:
        profile.append("Balanced")

    return profile

# =====================================================
# MODEL PREDICTION
# =====================================================

def predict_fit(
        openness,
        conscientiousness,
        extraversion,
        agreeableness,
        neuroticism,
        department,
        leadership
):

    input_data = {

        "pers_openness": openness,

        "pers_conscientiousness":
            conscientiousness,

        "pers_extraversion":
            extraversion,

        "pers_agreeableness":
            agreeableness,

        "pers_neuroticism":
            neuroticism,

        "department":
            department,

        "manager_leadership_style":
            leadership
    }

    input_df = pd.DataFrame(
        [input_data]
    )

    encoded = pd.get_dummies(
        input_df,
        columns=[
            "department",
            "manager_leadership_style"
        ]
    )

    final_df = pd.DataFrame(
        0,
        index=[0],
        columns=expected_columns
    )

    for col in encoded.columns:

        if col in final_df.columns:

            final_df[col] = encoded[col]

    prediction = model.predict(
        final_df
    )[0]

    return round(float(prediction), 1)

# =====================================================
# SHAP EXPLAINER
# =====================================================

@st.cache_resource
def create_explainer():

    try:

        return shap.TreeExplainer(model)

    except:

        return None

explainer = create_explainer()

# =====================================================
# HEADER
# =====================================================

st.title(
    "🧠 SynapseTech HR Analytics"
)

st.caption(
    "Personality–Organization Fit Prediction Platform"
)

st.divider()

# =====================================================
# SIDEBAR
# =====================================================

with st.sidebar:

    st.header("Configuration")

    show_technical = st.toggle(
        "Technical View",
        value=False
    )

    st.divider()

    st.markdown(
        """
### Score Interpretation

🟢 70 - 100
Excellent

🟡 45 - 70
Moderate

🔴 0 - 45
High Risk
"""
    )

    if show_technical:

        st.info(
            f"""
Model Type:
Random Forest

Features:
{len(expected_columns)}
"""
        )

# =====================================================
# INPUT SECTION
# =====================================================

st.subheader(
    "Employee Assessment"
)

col1, col2 = st.columns(2)

with col1:

    openness = st.slider(
        "Openness",
        1.0,
        5.0,
        3.5,
        0.1,
        help="Creativity, curiosity and openness to new experiences"
    )

    conscientiousness = st.slider(
        "Conscientiousness",
        1.0,
        5.0,
        3.5,
        0.1,
        help="Organization, reliability and self-discipline"
    )

    extraversion = st.slider(
        "Extraversion",
        1.0,
        5.0,
        3.5,
        0.1,
        help="Energy, sociability and assertiveness"
    )

with col2:

    agreeableness = st.slider(
        "Agreeableness",
        1.0,
        5.0,
        3.5,
        0.1,
        help="Cooperation, trust and empathy"
    )

    neuroticism = st.slider(
        "Neuroticism",
        1.0,
        5.0,
        2.5,
        0.1,
        help="Tendency toward anxiety and emotional reactivity"
    )
    # =====================================================
# ORGANIZATION DATA
# =====================================================

st.divider()

st.subheader(
    "Organization Context"
)

colA, colB = st.columns(2)

with colA:

    departments = [

        "Engineering",
        "Sales",
        "Marketing",
        "Product Management",
        "Data Science",
        "HR"

    ]

    department = st.selectbox(
        "Department",
        departments
    )

with colB:

    leadership_styles = [

        "Democratic",
        "Supportive",
        "Autocratic"

    ]

    leadership = st.selectbox(
        "Leadership Style",
        leadership_styles
    )

# =====================================================
# PERSONALITY RADAR CHART
# =====================================================

st.divider()

st.subheader(
    "Personality Radar"
)

radar_categories = [

    "Openness",
    "Conscientiousness",
    "Extraversion",
    "Agreeableness",
    "Neuroticism"

]

radar_values = [

    openness,
    conscientiousness,
    extraversion,
    agreeableness,
    neuroticism

]

fig_radar = go.Figure()

fig_radar.add_trace(

    go.Scatterpolar(

        r=radar_values,

        theta=radar_categories,

        fill="toself",

        name="Profile"

    )

)

fig_radar.update_layout(

    polar=dict(

        radialaxis=dict(

            visible=True,

            range=[1, 5]

        )

    ),

    showlegend=False,

    height=450

)

st.plotly_chart(
    fig_radar,
    use_container_width=True
)

# =====================================================
# PROFILE SUMMARY
# =====================================================

profile = personality_profile(
    openness,
    conscientiousness,
    extraversion,
    agreeableness,
    neuroticism
)

st.info(
    " | ".join(profile)
)

# =====================================================
# PREDICTION BUTTON
# =====================================================

st.divider()

predict_clicked = st.button(

    "Predict Organization Fit",

    use_container_width=True,

    type="primary"

)

# =====================================================
# SESSION STATE
# =====================================================

if "prediction" not in st.session_state:

    st.session_state.prediction = None

# =====================================================
# RUN PREDICTION
# =====================================================

if predict_clicked:

    with st.spinner(
        "Analyzing compatibility..."
    ):

        prediction = predict_fit(

            openness,

            conscientiousness,

            extraversion,

            agreeableness,

            neuroticism,

            department,

            leadership

        )

        st.session_state.prediction = prediction

# =====================================================
# RESULT SECTION
# =====================================================

if st.session_state.prediction is not None:

    prediction = st.session_state.prediction

    st.divider()

    st.subheader(
        "Prediction Result"
    )

    # =====================================
    # KPI CARDS
    # =====================================

    col1, col2, col3 = st.columns(3)

    with col1:

        st.metric(
            "Fit Score",
            f"{prediction:.1f}"
        )

    with col2:

        st.metric(
            "Status",
            get_status_text(prediction)
        )

    with col3:

        st.metric(
            "Department",
            department
        )

    # =====================================
    # MODERN PROGRESS RING
    # =====================================

    color = get_status_color(
        prediction
    )

    fig_ring = go.Figure(

        data=[

            go.Pie(

                values=[
                    prediction,
                    100 - prediction
                ],

                hole=0.78,

                sort=False,

                textinfo="none"

            )

        ]

    )

    fig_ring.update_traces(

        marker=dict(

            colors=[
                color,
                "#E5E7EB"
            ]

        )

    )

    fig_ring.update_layout(

        annotations=[

            dict(

                text=f"{prediction:.0f}%",

                x=0.5,

                y=0.5,

                font_size=32,

                showarrow=False

            )

        ],

        height=420,

        margin=dict(
            t=20,
            b=20,
            l=20,
            r=20
        ),

        showlegend=False

    )

    st.plotly_chart(
        fig_ring,
        use_container_width=True
    )

    # =====================================
    # STATUS CARD
    # =====================================

    status_icon = get_status_icon(
        prediction
    )

    status_text = get_status_text(
        prediction
    )

    st.markdown(

        f"""
### {status_icon} {status_text}

Current estimated compatibility score:

## {prediction:.1f}/100
"""
    )

    # =====================================
    # HIRING DECISION
    # =====================================

    if prediction >= 70:

        st.success(
            """
Recommended Action:

Proceed with hiring.

The candidate appears to have a
strong fit with the selected
organizational environment.
"""
        )

    elif prediction >= 45:

        st.warning(
            """
Recommended Action:

Hire with support plan.

Consider onboarding support,
mentoring and frequent feedback.
"""
        )

    else:

        st.error(
            """
Recommended Action:

Further assessment advised.

Review role alignment,
leadership style and placement.
"""
        )

    # =====================================
    # STRENGTHS
    # =====================================

    st.divider()

    st.subheader(
        "Potential Strengths"
    )

    strengths = []

    if openness >= 4:

        strengths.append(
            "Innovation and adaptability"
        )

    if conscientiousness >= 4:

        strengths.append(
            "Reliability and discipline"
        )

    if agreeableness >= 4:

        strengths.append(
            "Collaboration and teamwork"
        )

    if extraversion >= 4:

        strengths.append(
            "Stakeholder communication"
        )

    if neuroticism <= 2:

        strengths.append(
            "Emotional stability under pressure"
        )

    if strengths:

        for item in strengths:

            st.success(item)

    else:

        st.info(
            "No dominant strengths detected."
        )

    # =====================================
    # CHALLENGES
    # =====================================

    st.subheader(
        "Potential Challenges"
    )

    challenges = []

    if neuroticism >= 4:

        challenges.append(
            "Higher sensitivity to stress"
        )

    if department == "Sales" and extraversion < 3:

        challenges.append(
            "Sales role may require more social interaction"
        )

    if leadership == "Autocratic" and openness > 4:

        challenges.append(
            "Creative individuals may prefer greater autonomy"
        )

    if conscientiousness < 2.5:

        challenges.append(
            "May require stronger structure and planning"
        )

    if challenges:

        for item in challenges:

            st.warning(item)

    else:

        st.success(
            "No major risks identified."
        )

        # =====================================================
# ADVANCED ANALYTICS
# =====================================================

if st.session_state.prediction is not None:

    prediction = st.session_state.prediction

    st.divider()

    st.header(
        "Advanced Analytics"
    )

    # =================================================
    # REBUILD FEATURE VECTOR
    # =================================================

    input_data = {

        "pers_openness": openness,

        "pers_conscientiousness":
            conscientiousness,

        "pers_extraversion":
            extraversion,

        "pers_agreeableness":
            agreeableness,

        "pers_neuroticism":
            neuroticism,

        "department":
            department,

        "manager_leadership_style":
            leadership

    }

    input_df = pd.DataFrame(
        [input_data]
    )

    encoded = pd.get_dummies(
        input_df,
        columns=[
            "department",
            "manager_leadership_style"
        ]
    )

    final_df = pd.DataFrame(
        0,
        index=[0],
        columns=expected_columns
    )

    for col in encoded.columns:

        if col in final_df.columns:

            final_df[col] = encoded[col]

    # =================================================
    # SHAP EXPLANATION
    # =================================================

    st.subheader(
        "Model Explanation"
    )

    if explainer is not None:

        try:

            shap_values = explainer.shap_values(
                final_df
            )

            if isinstance(
                shap_values,
                list
            ):
                shap_values = shap_values[0]

            contributions = pd.DataFrame({

                "Feature":
                    final_df.columns,

                "Impact":
                    shap_values[0]

            })

            contributions["AbsImpact"] = (
                contributions["Impact"]
                .abs()
            )

            contributions = (
                contributions
                .sort_values(
                    "AbsImpact",
                    ascending=False
                )
                .head(10)
            )

            fig_shap = go.Figure()

            fig_shap.add_trace(

                go.Bar(

                    x=contributions[
                        "Impact"
                    ],

                    y=contributions[
                        "Feature"
                    ],

                    orientation="h"

                )

            )

            fig_shap.update_layout(

                title="Top Influential Features",

                height=500

            )

            st.plotly_chart(
                fig_shap,
                use_container_width=True
            )

            st.dataframe(
                contributions[
                    [
                        "Feature",
                        "Impact"
                    ]
                ],
                use_container_width=True
            )

        except Exception as e:

            st.warning(
                f"SHAP unavailable: {e}"
            )

    else:

        st.info(
            "SHAP explainer not available."
        )

    # =================================================
    # SCENARIO ANALYSIS
    # =================================================

    st.divider()

    st.subheader(
        "Scenario Simulation"
    )

    scenarios = []

    for dep in departments:

        score = predict_fit(

            openness,

            conscientiousness,

            extraversion,

            agreeableness,

            neuroticism,

            dep,

            leadership

        )

        scenarios.append({

            "Department":
                dep,

            "Score":
                score

        })

    scenario_df = pd.DataFrame(
        scenarios
    )

    scenario_df = scenario_df.sort_values(
        "Score",
        ascending=False
    )

    st.dataframe(
        scenario_df,
        use_container_width=True
    )

    best_department = (
        scenario_df
        .iloc[0]["Department"]
    )

    best_score = (
        scenario_df
        .iloc[0]["Score"]
    )

    # =================================================
    # DEPARTMENT COMPARISON CHART
    # =================================================

    fig_departments = go.Figure()

    fig_departments.add_trace(

        go.Bar(

            x=scenario_df[
                "Department"
            ],

            y=scenario_df[
                "Score"
            ]

        )

    )

    fig_departments.update_layout(

        title=
        "Predicted Fit by Department",

        height=450

    )

    st.plotly_chart(
        fig_departments,
        use_container_width=True
    )

    # =================================================
    # LEADERSHIP SIMULATION
    # =================================================

    st.subheader(
        "Leadership Style Impact"
    )

    leadership_results = []

    for style in leadership_styles:

        score = predict_fit(

            openness,

            conscientiousness,

            extraversion,

            agreeableness,

            neuroticism,

            department,

            style

        )

        leadership_results.append({

            "Leadership":
                style,

            "Score":
                score

        })

    leadership_df = pd.DataFrame(
        leadership_results
    )

    st.dataframe(
        leadership_df,
        use_container_width=True
    )

    # =================================================
    # EXECUTIVE SUMMARY
    # =================================================

    st.divider()

    st.header(
        "Executive Summary"
    )

    summary = []

    if prediction >= 70:

        summary.append(
            "Strong overall fit detected."
        )

    elif prediction >= 45:

        summary.append(
            "Moderate fit with development opportunities."
        )

    else:

        summary.append(
            "Low fit detected. Additional assessment recommended."
        )

    summary.append(
        f"Best department: {best_department}"
    )

    summary.append(
        f"Potential score: {best_score}"
    )

    if neuroticism >= 4:

        summary.append(
            "Stress-management support may be beneficial."
        )

    if openness >= 4:

        summary.append(
            "Candidate may thrive in innovative environments."
        )

    if conscientiousness >= 4:

        summary.append(
            "Strong execution and accountability profile."
        )

    for item in summary:

        st.markdown(
            f"• {item}"
        )

    # =================================================
    # STRATEGIC RECOMMENDATION
    # =================================================

    st.divider()

    st.subheader(
        "Strategic Recommendation"
    )

    if prediction >= 70:

        st.success(
            """
Recommended Strategy

• Fast-track onboarding

• Assign meaningful projects early

• Provide growth opportunities

• Monitor engagement quarterly
"""
        )

    elif prediction >= 45:

        st.warning(
            """
Recommended Strategy

• Structured onboarding

• Mentorship support

• Monthly performance reviews

• Development-focused coaching
"""
        )

    else:

        st.error(
            """
Recommended Strategy

• Re-evaluate placement

• Explore alternative departments

• Conduct additional assessment

• Consider leadership environment fit
"""
        )