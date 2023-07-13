import streamlit as st

from streamlit_youtube_chatbot.streamlit_components.faq import faq


def sidebar():
    with st.sidebar:
        st.markdown(
            "## Wie benutzt man es\n"
            "Stellen Sie eine Frage zu der [Videoserie](https://www.youtube.com/watch?v=DZwfmbhpIEw&list=PLH9wSb4VQN3WbpGmMs2Vl-uB16ra_tMna)💬\n"
        )
        st.session_state["MODEL_TYP"] = "gpt-3.5-turbo"

        st.markdown("---")
        st.markdown("# Über")
        st.markdown(
            "🚀Der Gründungs-Bot bietet Empfehlungen zur Unternehmensgründung basierend auf der YouTube-Videoserie "
            '"Existenzgründung Schritt für Schritt: Von der passenden Rechtsform bis zum Jahresabschluss".'
        )
        st.markdown("Das ist nur ein MVP. 🔨")
        st.markdown(
            "Made by [MarkusOdenthal](https://www.linkedin.com/in/markus-odenthal/)"
        )
        st.markdown("---")

        faq()
