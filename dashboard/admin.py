"""
admin.py
----------
Admin Dashboard
"""

import os
import pandas as pd
import streamlit as st
import plotly.express as px

from src.memory import memory


def show_admin():

    st.title("🛠 Admin Dashboard")

    st.markdown("---")

    # ----------------------------
    # Metrics
    # ----------------------------

    pdf_count = 0

    if os.path.exists("data/uploads"):

        pdf_count = len([
            f for f in os.listdir("data/uploads")
            if f.endswith(".pdf")
        ])

    question_count = len(memory.get_history())

    vector_status = "Available" if os.path.exists(
        "vectorstore/faiss_index/index.faiss"
    ) else "Not Created"

    feedback_file = "artifacts/feedback.csv"

    helpful = 0
    not_helpful = 0

    if os.path.exists(feedback_file):

        feedback_df = pd.read_csv(feedback_file)

        helpful = (
            feedback_df["Rating"] == "Helpful"
        ).sum()

        not_helpful = (
            feedback_df["Rating"] == "Not Helpful"
        ).sum()

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("📄 PDFs", pdf_count)

    col2.metric("💬 Questions", question_count)

    col3.metric("👍 Helpful", helpful)

    col4.metric("🗄 Vector DB", vector_status)

    st.markdown("---")

    # ----------------------------
    # Model Information
    # ----------------------------

    st.subheader("🤖 Model Information")

    model_info = pd.DataFrame({

        "Component":[

            "LLM",

            "Embedding",

            "Vector Database",

            "Retriever"

        ],

        "Model":[

            "Llama 3.3 70B",

            "all-MiniLM-L6-v2",

            "FAISS",

            "Hybrid Search"

        ]

    })

    st.dataframe(
        model_info,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------
    # Feedback Analytics
    # ----------------------------

    st.subheader("📈 Feedback Analytics")

    if os.path.exists(feedback_file):

        chart = px.pie(

            feedback_df,

            names="Rating",

            title="User Feedback Distribution"

        )

        st.plotly_chart(
            chart,
            use_container_width=True
        )

        st.dataframe(

            feedback_df.tail(10),

            use_container_width=True

        )

    else:

        st.info("No feedback available.")

    st.markdown("---")

    # ----------------------------
    # System Status
    # ----------------------------

    st.subheader("⚙ System Status")

    status = pd.DataFrame({

        "Component":[

            "Uploads Folder",

            "Vector Store",

            "Logs",

            "Artifacts"

        ],

        "Status":[

            os.path.exists("data/uploads"),

            os.path.exists("vectorstore"),

            os.path.exists("logs"),

            os.path.exists("artifacts")

        ]

    })

    st.dataframe(
        status,
        use_container_width=True
    )

    st.markdown("---")

    # ----------------------------
    # Log Size
    # ----------------------------

    st.subheader("📜 Log Information")

    log_file = "logs/research_assistant.log"

    if os.path.exists(log_file):

        size = round(

            os.path.getsize(log_file)/1024,

            2

        )

        st.metric(
            "Log Size (KB)",
            size
        )

    else:

        st.info("No logs found.")

    st.markdown("---")

    # ----------------------------
    # Maintenance
    # ----------------------------

    st.subheader("🧹 Maintenance")

    c1, c2, c3 = st.columns(3)

    with c1:

        if st.button("Clear Chat"):

            memory.clear()

            st.success("Conversation Cleared")

    with c2:

        if st.button("Delete Feedback"):

            if os.path.exists(feedback_file):

                os.remove(feedback_file)

                st.success("Feedback Deleted")

    with c3:

        if st.button("Delete Logs"):

            if os.path.exists(log_file):

                os.remove(log_file)

                st.success("Logs Deleted")