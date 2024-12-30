def get_translations(language):
    """
    Returns a dictionary of translated strings based on the selected language.

    Parameters:
    language (str): Language choice, e.g., "Français" or "English".

    Returns:
    dict: Dictionary containing translated strings for the application.
    """
    if language == "Français":
        return {
            # Tabs and main sections
            "tabs": ["Prix des Cryptos", "Calculateur de Taxes Crypto", "Données Historiques"],
            "prices": "Prix des Cryptos",
            "tax_calculator": "Calculateur de Taxes Crypto",
            "historic": "Données Historiques",
            # Labels related to cryptocurrencies
            "crypto_selection": "Choisissez des cryptomonnaies :",
            "show_prices": "Afficher les prix",
            "select_crypto_history": "Choisissez une cryptomonnaie pour les données historiques :",
            "time_range": "Sélectionnez une plage de temps :",
            "compare_cryptos": "Comparer les cryptos",
            # Labels for the tax calculator
            "tax_calc_header": "Calculateur de Taxes sur les Cryptos",
            "tax_explanation": "### Comment les calculs sont effectués :",
            "tax_gain_loss": "**Gains/Pertes Totaux**",
            "tax_amount": "**Taxes à payer**",
            "buy_price": "Prix d'achat par unité (USD) :",
            "sell_price": "Prix de vente par unité (USD) :",
            "quantity": "Quantité (en unités) :",
            "fees": "Frais totaux (USD) :",
            "tax_rate": "Taux d'imposition (%) :",
            "calculate_tax": "Calculer les taxes sur les cryptos",
            # Status messages
            "loading_message": "Chargement de la liste des cryptomonnaies...",
            "error_message": "Impossible de récupérer les données.",
            # Labels for historic data
            "historic_data_header": "Données Historiques de la Cryptomonnaie",
            "show_historic": "Afficher les données historiques",
            # Labels for the chatbot
            "chat_sidebar_header": "💬 Discutez avec ChatGPT",
            "chat_context_label": "Contexte",
            "chat_context_placeholder": "Fournissez le contexte de votre question",
            "chat_question_label": "Votre Question",
            "chat_prompt_placeholder": "Posez une question",
            "ask_button": "Demander à ChatGPT",
            "clear_button": "Effacer la conversation",
            "invalid_question_error": "Veuillez entrer une question valide !",
            "history_label": "Historique des conversations",
            "user_label": "Vous",
            "bot_label": "ChatGPT",
            "no_history_message": "Aucun historique de conversation pour le moment. Posez une question pour commencer !"
        }
    else:
        return {
            # Tabs and main sections
            "tabs": ["Crypto Prices", "Crypto Tax Calculator", "Historic Data"],
            "prices": "Crypto Prices",
            "tax_calculator": "Crypto Tax Calculator",
            "historic": "Historic Data",
            # Labels related to cryptocurrencies
            "crypto_selection": "Select cryptocurrencies:",
            "show_prices": "Show Prices",
            "select_crypto_history": "Select a cryptocurrency for historic data:",
            "time_range": "Select a time range:",
            "compare_cryptos": "Compare Cryptos",
            # Labels for the tax calculator
            "tax_calc_header": "Crypto Tax Calculator",
            "tax_explanation": "### How the calculations are performed:",
            "tax_gain_loss": "**Total Gain/Loss**",
            "tax_amount": "**Tax to Pay**",
            "buy_price": "Buy Price per Unit (USD):",
            "sell_price": "Sell Price per Unit (USD):",
            "quantity": "Quantity (in units):",
            "fees": "Total Fees (USD):",
            "tax_rate": "Tax Rate (%):",
            "calculate_tax": "Calculate Crypto Taxes",
            # Status messages
            "loading_message": "Loading cryptocurrency list...",
            "error_message": "Failed to fetch data.",
            # Labels for historic data
            "historic_data_header": "Historic Data of Cryptocurrency",
            "show_historic": "Show Historic Data",
            # Labels for the chatbot
            "chat_sidebar_header": "💬 Chat with ChatGPT",
            "chat_context_label": "Context",
            "chat_context_placeholder": "Provide context for your question",
            "chat_question_label": "Your Question",
            "chat_prompt_placeholder": "Ask a question",
            "ask_button": "Ask ChatGPT",
            "clear_button": "Clear Conversation",
            "invalid_question_error": "Please enter a valid question!",
            "history_label": "Conversation History",
            "user_label": "You",
            "bot_label": "ChatGPT",
            "no_history_message": "No conversation history yet. Start by asking a question!"
        }