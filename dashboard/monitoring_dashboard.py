import os
import pandas as pd
import streamlit as st
import plotly.express as px

INTERACTION_FILE = "monitoring/rag_interactions.csv"
FEEDBACK_FILE = "monitoring/user_feedback.csv"


def show_monitoring_dashboard():

    st.title("RAG Production Monitoring")
    st.caption(
        "Monitor usage, latency and user feedback "
        "for the AI Research Assistant."
    )

    # ==========================================
    # Load interaction data
    # ==========================================

    interactions = pd.DataFrame()

    if (
        os.path.exists(INTERACTION_FILE)
        and os.path.getsize(INTERACTION_FILE) > 0
    ):
        try:
            interactions = pd.read_csv(INTERACTION_FILE)
        except pd.errors.EmptyDataError:
            pass

    # ==========================================
    # Load feedback data
    # ==========================================

    feedback = pd.DataFrame()

    if (
        os.path.exists(FEEDBACK_FILE)
        and os.path.getsize(FEEDBACK_FILE) > 0
    ):
        try:
            feedback = pd.read_csv(FEEDBACK_FILE)
        except pd.errors.EmptyDataError:
            pass

    # ==========================================
    # KPIs
    # ==========================================

    total_queries = len(interactions)

    avg_latency = (
        interactions["response_time_seconds"].mean()
        if not interactions.empty
        and "response_time_seconds" in interactions.columns
        else 0
    )

    total_feedback = len(feedback)

    if (
        not feedback.empty
        and "feedback" in feedback.columns
    ):
        helpful = (
            feedback["feedback"]
            .astype(str)
            .str.lower()
            .eq("helpful")
            .sum()
        )

        helpful_rate = (
            helpful / total_feedback * 100
            if total_feedback > 0
            else 0
        )
    else:
        helpful_rate = 0

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Queries",
        total_queries
    )

    col2.metric(
        "Average Latency",
        f"{avg_latency:.2f}s"
    )

    col3.metric(
        "Feedback Received",
        total_feedback
    )

    col4.metric(
        "Helpful Rate",
        f"{helpful_rate:.1f}%"
    )

    st.divider()

    # ==========================================
    # Interaction monitoring
    # ==========================================

    st.subheader("RAG Interaction Monitoring")

    if interactions.empty:

        st.info(
            "No production interactions recorded yet."
        )

    else:

        if "timestamp" in interactions.columns:
            interactions["timestamp"] = pd.to_datetime(
                interactions["timestamp"],
                errors="coerce"
            )

        if "response_time_seconds" in interactions.columns:

            fig = px.line(
                interactions,
                x="timestamp",
                y="response_time_seconds",
                markers=True,
                title="RAG Response Latency"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        display_columns = [
            column for column in [
                "timestamp",
                "question",
                "retrieved_chunks",
                "response_time_seconds"
            ]
            if column in interactions.columns
        ]

        st.dataframe(
            interactions[display_columns],
            use_container_width=True,
            hide_index=True
        )

    st.divider()

    # ==========================================
    # User feedback
    # ==========================================

    st.subheader("User Feedback")

    if feedback.empty:

        st.info(
            "No user feedback recorded yet."
        )

    else:

        if "feedback" in feedback.columns:

            feedback_counts = (
                feedback["feedback"]
                .value_counts()
                .reset_index()
            )

            feedback_counts.columns = [
                "Feedback",
                "Count"
            ]

            fig = px.pie(
                feedback_counts,
                names="Feedback",
                values="Count",
                title="Helpful vs Not Helpful"
            )

            st.plotly_chart(
                fig,
                use_container_width=True
            )

        st.dataframe(
            feedback,
            use_container_width=True,
            hide_index=True
        )