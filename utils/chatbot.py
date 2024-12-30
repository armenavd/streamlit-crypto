import streamlit as st
from openai import OpenAI

# Initialiser le client OpenAI
client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

def chatbot(chat_context="Fournissez le contexte de votre question (par exemple, cryptos sélectionnées, période)"):
    # En-tête de la barre latérale
    st.sidebar.subheader("💬 Discutez avec ChatGPT")

    # Initialiser l'état de session pour l'historique des conversations
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Champs de texte pour le contexte et la question
    st.sidebar.write("### Contexte")
    chat_context_input = st.sidebar.text_area("Contexte", chat_context, key="chat_context_input")

    st.sidebar.write("### Votre Question")
    chat_prompt = st.sidebar.text_input("Posez une question", key="chat_prompt")

    # Boutons d'interaction
    col1, col2 = st.sidebar.columns([1, 1])
    with col1:
        if st.button("Demander à ChatGPT", key="ask_chat_button"):
            if chat_prompt.strip():
                with st.spinner("Traitement de votre question..."):
                    try:
                        # Appel à l'API OpenAI via le client
                        response = client.chat.completions.create(
                            model="gpt-4o",  # Modèle spécifié
                            store=True,  # Option "store" pour conserver l'état
                            messages=[
                                {"role": "system", "content": chat_context_input},
                                {"role": "user", "content": chat_prompt}
                            ]
                        )
                        # Extraire la réponse
                        answer = response.choices[0].message.content.strip()
                        # Ajouter à l'historique des conversations
                        st.session_state.chat_history.append({"question": chat_prompt, "response": answer})
                    except Exception as e:
                        st.sidebar.error(f"❗ Une erreur s'est produite : {e}")
            else:
                st.sidebar.error("❗ Veuillez entrer une question valide !")

    with col2:
        if st.button("Effacer la conversation", key="clear_chat_button"):
            st.session_state.chat_history = []

    # Afficher l'historique des conversations
    st.sidebar.write("### Historique des conversations")
    if st.session_state.chat_history:
        for entry in st.session_state.chat_history[::-1]:
            st.sidebar.markdown(f"**🧑 Vous :** {entry['question']}")
            st.sidebar.markdown(f"**🤖 ChatGPT :** {entry['response']}")
            st.sidebar.markdown("---")
    else:
        st.sidebar.write("Aucun historique de conversation pour le moment. Commencez par poser une question !")
