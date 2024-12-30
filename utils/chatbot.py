import streamlit as st
from openai import OpenAI
from utils.translations import get_translations  # Import the translation utility

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def chatbot(chat_context="Provide context for your question"):
    """
    A Streamlit-based chatbot interface using OpenAI's API.

    Parameters:
    chat_context (str): Default context to provide for the chatbot.
    """

    # Retrieve the user's preferred language from session state, defaulting to English
    language = st.session_state.get("language", "English")
    translations = get_translations(language)  # Load translations for the selected language

    # Sidebar header
    st.sidebar.subheader(translations.get("chat_sidebar_header", "💬 Chat with ChatGPT"))

    # Initialize chat history in session state if not already present
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Input fields for context and user question
    st.sidebar.write(f"### {translations.get('chat_context_label', 'Context')}")
    # chat_context_input = st.sidebar.text_area(
    #     translations.get("chat_context_placeholder", "Provide context for your question"),
    #     chat_context,
    #     key="chat_context_input"
    # )

    st.sidebar.write(f"### {translations.get('chat_question_label', 'Your Question')}")
    chat_prompt = st.sidebar.text_input(
        translations.get("chat_prompt_placeholder", "Ask a question"),
        key="chat_prompt"
    )

    # Interaction buttons for asking a question or clearing the conversation
    col1, col2 = st.sidebar.columns([1, 1])
    
    with col1:
        if st.button(translations.get("ask_button", "Ask ChatGPT"), key="ask_chat_button"):
            if chat_prompt.strip():  # Ensure the user provided a valid question
                with st.spinner(translations.get("loading_message", "Processing your question...")):
                    try:
                        # Send the context and question to the OpenAI API
                        response = client.chat.completions.create(
                            model="gpt-4o",  # Specify the model
                            messages=[
                                {"role": "system", "content": str(chat_context)},
                                {"role": "user", "content": chat_prompt}
                            ]
                        )
                        # Extract the response content
                        answer = response.choices[0].message.content.strip()
                        # Save the question and answer to the chat history
                        st.session_state.chat_history.append({"question": chat_prompt, "response": answer})
                    except Exception as e:
                        st.sidebar.error(f"{translations.get('error_message', 'An error occurred')}: {e}")
            else:
                st.sidebar.error(translations.get("invalid_question_error", "Please enter a valid question!"))

    with col2:
        if st.button(translations.get("clear_button", "Clear Conversation"), key="clear_chat_button"):
            # Clear the chat history
            st.session_state.chat_history = []

    # Display the chat history in reverse chronological order
    st.sidebar.write(f"### {translations.get('history_label', 'Conversation History')}")
    if st.session_state.chat_history:
        for entry in st.session_state.chat_history[::-1]:
            st.sidebar.markdown(f"**🧑 {translations.get('user_label', 'You')}:** {entry['question']}")
            st.sidebar.markdown(f"**🤖 {translations.get('bot_label', 'ChatGPT')}:** {entry['response']}")
            st.sidebar.markdown("---")
    else:
        st.sidebar.write(translations.get("no_history_message", "No conversation history yet. Start by asking a question!"))
