import streamlit as st
from chat.message_encoding import get_encoding_length, query_message_prompt
from langchain.chat_models import ChatOpenAI
from langchain.schema import ChatMessage, SystemMessage

from streamlit_youtube_chatbot.chat.stream_handler import StreamHandler
from streamlit_youtube_chatbot.streamlit_components.sidebar import sidebar

system_prompt = """Verhalte dich wie ein Gründungs-Bot. Dein Kontext ist das Transkript einer YouTube-Videoserie namens "Existenzgründung Schritt für Schritt: Von der passenden Rechtsform bis zum Jahresabschluss". Der Moderator legt dabei einen Schwerpunkt auf die Gründung eines Einzelunternehmens. Deine Hauptaufgabe ist die Beantwortung von Fragen im Zusammenhang mit dieser Videoserie. Verwende nur diese Informationen und beziehe keine zusätzlichen externen Quellen ein. Deine Antwort sollte sich auf diesen Kontext stützen. Sei bei deinen Antworten so genau wie möglich."""


st.set_page_config(page_title="Gründungs-Bot", page_icon="‍🏢", layout="wide")
st.header("🏢Gründungs-Bot")

sidebar()

if "messages" in st.session_state:
    for msg in st.session_state.messages:
        st.chat_message(msg.role).write(msg.content)

if "token_count" not in st.session_state:
    st.session_state["token_count"] = 0

if "prompts" not in st.session_state:
    st.session_state["prompts"] = [SystemMessage(role="system", content=system_prompt)]
    st.session_state.token_count += get_encoding_length(system_prompt)

if prompt := st.chat_input():
    # if st.session_state["OPENAI_API_KEY"] == "":
    #     st.info("Please add your OpenAI API key to continue.")
    #     st.stop()

    if "messages" not in st.session_state:
        st.session_state["messages"] = [ChatMessage(role="user", content=prompt)]
    else:
        st.session_state.messages.append(ChatMessage(role="user", content=prompt))

    st.chat_message("user").write(prompt)

    with st.chat_message("assistant"):
        stream_handler = StreamHandler(st.empty())
        llm = ChatOpenAI(
            openai_api_key=st.secrets["OPENAI_API_KEY"],
            streaming=True,
            callbacks=[stream_handler],
        )
        query_message = query_message_prompt(prompt, st.secrets["OPENAI_API_KEY"])
        st.session_state.token_count += get_encoding_length(query_message)
        st.session_state.prompts.append(ChatMessage(role="user", content=query_message))
        while st.session_state.token_count >= 4000:
            pop_user_message = st.session_state.prompts.pop(1).content
            st.session_state.token_count -= get_encoding_length(pop_user_message)
            pop_assistant_message = st.session_state.prompts.pop(1)
            st.session_state.token_count -= get_encoding_length(pop_assistant_message)

        response = llm(st.session_state.prompts)
        st.session_state.prompts.append(
            ChatMessage(role="assistant", content=response.content)
        )
        st.session_state.messages.append(
            ChatMessage(role="assistant", content=response.content)
        )
