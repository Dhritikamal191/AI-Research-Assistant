import os
import pandas as pd
import plotly.express as px
import streamlit as st

RESULTS_FILE = "evaluation/results.csv"


def show_evaluation_dashboard():

    st.title("RAG Evaluation Dashboard")
    st.caption(
        "Monitor retrieval quality and generation performance using RAGAS metrics."
    )

    # -----------------------------
    # Check evaluation data
    # -----------------------------

    if not os.path.exists(RESULTS_FILE):
        st.info("No evaluation results available yet.")
        return

    if os.path.getsize(RESULTS_FILE) == 0:
        st.info(
            "Evaluation results are currently empty. "
            "Run RAGAS evaluation when API quota is available."
        )
        return

    df = pd.read_csv(RESULTS_FILE)

    if df.empty:
        st.info("No completed evaluations available.")
        return

    # -----------------------------
    # KPI metrics
    # -----------------------------

    avg_faithfulness = df["faithfulness"].mean()
    avg_relevancy = df["answer_relevancy"].mean()

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Questions Evaluated",
        len(df)
    )

    col2.metric(
        "Avg. Faithfulness",
        f"{avg_faithfulness:.3f}"
    )

    col3.metric(
        "Avg. Answer Relevancy",
        f"{avg_relevancy:.3f}"
    )

    st.divider()

    # -----------------------------
    # Overall quality
    # -----------------------------

    overall_score = (
        avg_faithfulness + avg_relevancy
    ) / 2

    st.subheader("Overall RAG Quality")

    st.progress(
        min(max(float(overall_score), 0.0), 1.0)
    )

    if overall_score >= 0.85:
        st.success(
            f"Excellent RAG quality — {overall_score:.3f}"
        )

    elif overall_score >= 0.70:
        st.info(
            f"Good RAG quality — {overall_score:.3f}"
        )

    elif overall_score >= 0.50:
        st.warning(
            f"Moderate RAG quality — {overall_score:.3f}"
        )

    else:
        st.error(
            f"RAG quality needs improvement — {overall_score:.3f}"
        )

    st.divider()

    # -----------------------------
    # Metric comparison
    # -----------------------------

    st.subheader("Metric Comparison")

    metric_df = pd.DataFrame({
        "Metric": [
            "Faithfulness",
            "Answer Relevancy"
        ],
        "Score": [
            avg_faithfulness,
            avg_relevancy
        ]
    })

    fig = px.bar(
        metric_df,
        x="Metric",
        y="Score",
        text_auto=".3f",
        range_y=[0, 1]
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    # -----------------------------
    # Per-question performance
    # -----------------------------

    st.subheader("Question-Level Performance")

    question_df = df[
        [
            "question",
            "faithfulness",
            "answer_relevancy"
        ]
    ].set_index("question")

    st.bar_chart(question_df)

    # -----------------------------
    # Detailed results
    # -----------------------------

    st.subheader("Evaluation Details")

    display_columns = [
        col for col in [
            "question",
            "faithfulness",
            "answer_relevancy",
            "retrieved_contexts",
            "status"
        ]
        if col in df.columns
    ]

    st.dataframe(
        df[display_columns],
        use_container_width=True,
        hide_index=True
    )