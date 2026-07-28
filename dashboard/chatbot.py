import streamlit as st
from src.rag_pipeline import rag_query
from src.memory import memory
from monitoring.logger import log_feedback

def show_chatbot():

    st.title("💬 Chat")

    question = st.chat_input("Ask anything...")

    if question:

        with st.chat_message("user"):

            st.write(question)

        result = rag_query(question)

        memory.add(
            question,
            result["answer"]
        )

        st.session_state["last_question"] = question
        st.session_state["last_answer"] = result["answer"]
        st.session_state["feedback_given"] = False

        with st.chat_message("assistant"):

             if not st.session_state.get("feedback_given", False):
                 
                col1 , col2 = st.columns(2)

                with col1:
                     if st.button("👍 Helpful", key="helpful"):
                        log_feedback(
                st.session_state["last_question"],
                st.session_state["last_answer"],
                "helpful"
                 )
                st.session_state["feedback_given"] = True
                st.success("Feedback recorded!")

                with col2:
                     if st.button("👎 Not Helpful", key="not_helpful"):
                        log_feedback(
                st.session_state["last_question"],
                st.session_state["last_answer"],
                "not_helpful"
                )
                st.session_state["feedback_given"] = True
                st.success("Feedback recorded!")

             placeholder = st.empty()

             placeholder.markdown (result["answer"])                

             st.markdown(result["answer"])

             for source in result["sources"]:

                st.write(
                    f"📄 {source['document']} | Page {source['page']}"
                )