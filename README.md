# Python Whatsapp Bot

A simple Flask-based WhatsApp bot for automated conversations and responses, focused on providing visa and travel advice via WhatsApp using the Meta (Facebook) Graph API.

---

## Project Structure

```
.
├── app.py                 # Main Flask app handling webhooks and routing
├── services.py            # Core logic to process and respond to WhatsApp messages
├── sett.py                # Configuration file for tokens and endpoints
├── requierements.txt      # Python dependencies
└── .gitignore
```

---

## How it Works

- **Flask Web Server** (`app.py`):  
  Exposes HTTP endpoints (`/Welcome` and `/webhook`) for WhatsApp webhooks. It verifies tokens and processes incoming WhatsApp messages.

- **Configuration** (`sett.py`):  
  Stores sensitive information such as API tokens and the WhatsApp endpoint URL.

- **Message Handling** (`services.py`):  
  Parses incoming messages, determines their type (text, button, list, etc.), and formulates appropriate responses.
  - Recognizes keywords (e.g., "hola", "visa estudiante", "turista usa") and returns interactive menus, information, or further questions.
  - Supports WhatsApp features like text replies, button replies, list replies, sending documents, stickers, and reactions.
  - Handles user flows for information gathering, such as asking for contact details or guiding the user through visa requirements by country and type.

- **Requirements** (`requierements.txt`):  
  Lists all the Python packages needed for deployment (Flask, requests, etc.).

---

## Example Conversation Flow

1. **User says "hola"**  
   → Bot replies with a greeting and presents interactive options (e.g., types of visas or destinations).

2. **User selects "Visa Estudiante"**  
   → Bot asks for the country of interest and provides basic visa requirements for that country.

3. **Bot can send documents, stickers, or request more info**  
   → Example: If the user is interested in "Visa USA", the bot lists all required documents and costs, and can ask if they want to be contacted by an advisor.

4. **Session Management**  
   → If the user types "si", the bot collects contact information for follow-up.

---

## Quick Start

1. **Clone the repository**

   ```sh
   git clone https://github.com/StebanJrb/Python-WhatsappBot.git
   cd Python-WhatsappBot
   ```

2. **Install dependencies**

   ```sh
   pip install -r requierements.txt
   ```

3. **Configure API tokens**  
   Edit `sett.py` and update the `token`, `whatsapp_token`, and `whatsapp_url` with your own credentials.

4. **Run the bot**

   ```sh
   python app.py
   ```

   The Flask server will start, ready to receive WhatsApp webhook events.

---

## Features

- Automated WhatsApp replies for visa and travel inquiries
- Interactive WhatsApp menus (buttons, lists)
- Customizable flows for various destinations and visa types
- Easy to extend with additional questions or document requests
- Flask-based, lightweight, and easy to deploy

---

## Notes

- You need a WhatsApp Business API account and proper credentials from Meta (Facebook) to use this bot.
- All conversational logic is currently hardcoded in `services.py` but can be extended or localized as needed.

---

**Contact**  
Developed by StebanJrb  
[GitHub Repository](https://github.com/StebanJrb/Python-WhatsappBot)
