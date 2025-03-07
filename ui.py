# import streamlit as st
# from main import invokeChatbot
# from time import sleep
# import os
# import json


# SESSION_FILE = "chat_history.json"


# def load_chat_history():
    
#     if os.path.exists(SESSION_FILE):
#         with open(SESSION_FILE , "r") as f:
#             return json.load(f)
#     return [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries."}]

        

# def save_chat_history():
    
#     try:
#         with open(SESSION_FILE, "r") as file:
#             return json.load(file)
#     except FileNotFoundError:
#         return [] 


# st.title("Medical Chatbot")

# if "messages" not in st.session_state:
#     sleep(0.5)
#     st.session_state.messages = load_chat_history()


# for message in st.session_state.messages:
#     with st.chat_message(message["role"]):
#         st.markdown(message["content"])

# if prompt := st.chat_input(placeholder="Send your query"):
#     st.session_state.messages.append({"role": "user", "content": prompt})
#     with st.chat_message("user"):
#         st.markdown(prompt)

#     with st.spinner("Thinking..."):
#         response = invokeChatbot(prompt)

#     st.session_state.messages.append({"role": "ai", "content": response})
#     with st.chat_message("ai"):
#         st.markdown(response)


#     save_chat_history()



# import streamlit as st
# from main import invokeChatbot
# from time import sleep
# import os
# import json
# from PIL import Image

# # Constants
# PRIMARY_COLOR = "#30D4B3"
# SECONDARY_COLOR = "#2B4C7E"  # Complementary dark blue color
# SESSION_FILE = "chat_history.json"

# # Set page configuration
# st.set_page_config(
#     page_title="Medical Chatbot",
#     page_icon="🏥",
#     layout="centered"
# )

# # Custom CSS for better visual appeal and text readability
# st.markdown(f"""
# <style>
#     /* Overall page styling */
#     .stApp {{
#         background-color: #000000; /* Changed to black background */
#     }}
    
#     /* Main container styling */
#     .main .block-container {{
#         padding: 2rem;
#         max-width: 800px;
#         background-color: #1E1E1E; /* Darker background for main container */
#         border-radius: 15px;
#         box-shadow: 0 6px 16px rgba(0,0,0,0.3);
#         margin-top: 20px;
#     }}
    
#     /* Header styling */
#     .header {{
#         display: flex;
#         align-items: center;
#         margin-bottom: 25px;
#         background-color: #2D2D2D; /* Darker header */
#         padding: 15px;
#         border-radius: 12px;
#         box-shadow: 0 2px 10px rgba(0,0,0,0.2);
#     }}
    
#     .logo-container {{
#         background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
#         width: 50px;
#         height: 50px;
#         border-radius: 10px;
#         display: flex;
#         align-items: center;
#         justify-content: center;
#         margin-right: 15px;
#         box-shadow: 0 4px 8px rgba(48, 212, 179, 0.3);
#     }}
    
#     .title {{
#         color: #FFFFFF; /* White text for better contrast */
#         font-size: 28px;
#         font-weight: 600;
#         margin: 0;
#     }}
    
#     /* Chat container styling */
#     .chat-container {{
#         background-color: #2D2D2D; /* Darker chat container */
#         border-radius: 12px;
#         padding: 20px;
#         margin: 20px 0;
#         box-shadow: 0 2px 10px rgba(0,0,0,0.2);
#         max-height: 500px;
#         overflow-y: auto;
#     }}
    
#     /* Message styling */
#     .user-message {{
#         background-color: #3A3A3A; /* Darker user message */
#         color: #FFFFFF; /* White text */
#         padding: 12px 18px;
#         border-radius: 18px 18px 0 18px;
#         margin: 10px 0;
#         max-width: 80%;
#         align-self: flex-end;
#         margin-left: auto;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
#         font-size: 16px;
#         line-height: 1.5;
#         font-weight: 400;
#     }}
    
#     .ai-message {{
#         background-color: {PRIMARY_COLOR};
#         color: white;
#         padding: 12px 18px;
#         border-radius: 18px 18px 18px 0;
#         margin: 10px 0;
#         max-width: 80%;
#         box-shadow: 0 1px 3px rgba(0,0,0,0.2);
#         font-size: 16px;
#         line-height: 1.5;
#         font-weight: 400;
#     }}
    
#     /* Input area styling */
#     .input-container {{
#         background-color: #2D2D2D; /* Darker input container */
#         padding: 15px;
#         border-radius: 12px;
#         box-shadow: 0 2px 10px rgba(0,0,0,0.2);
#         margin-top: 20px;
#     }}
    
#     .stTextInput > div > div > input {{
#         background-color: #3A3A3A; /* Darker input field */
#         color: #FFFFFF; /* White text */
#         font-size: 16px;
#         border: 2px solid #4A4A4A;
#         border-radius: 8px;
#         padding: 12px 15px;
#         height: 50px;
#         box-shadow: none !important;
#     }}
    
#     .stTextInput > div > div > input:focus {{
#         border-color: {PRIMARY_COLOR};
#         box-shadow: 0 0 0 2px {PRIMARY_COLOR}33 !important;
#     }}
    
#     /* Button styling */
#     .stButton > button {{
#         background: linear-gradient(135deg, {PRIMARY_COLOR}, #28B99E);
#         color: white;
#         font-weight: 600;
#         border: none;
#         border-radius: 8px;
#         padding: 10px 20px;
#         height: 45px;
#         transition: all 0.3s ease;
#         box-shadow: 0 4px 8px rgba(48, 212, 179, 0.3);
#     }}
    
#     .stButton > button:hover {{
#         transform: translateY(-2px);
#         box-shadow: 0 6px 12px rgba(48, 212, 179, 0.4);
#     }}
    
#     .clear-button > button {{
#         background: linear-gradient(135deg, #3A3A3A, #2D2D2D); /* Darker clear button */
#         color: #CCCCCC;
#     }}
    
#     /* Footer styling */
#     .footer {{
#         background-color: #2D2D2D; /* Darker footer */
#         padding: 15px;
#         border-radius: 12px;
#         margin-top: 20px;
#         text-align: center;
#         font-size: 14px;
#         color: #CCCCCC; /* Light gray text */
#         box-shadow: 0 2px 10px rgba(0,0,0,0.2);
#     }}

#     /* Hide Streamlit branding */
#     #MainMenu, footer, header {{
#         visibility: hidden;
#     }}
    
#     /* Text styling for subtitle */
#     .subtitle {{
#         color: #CCCCCC; /* Light gray text */
#         font-size: 16px;
#         margin-top: -10px;
#         margin-bottom: 25px;
#     }}
# </style>
# """, unsafe_allow_html=True)

# def load_chat_history():
#     if os.path.exists(SESSION_FILE):
#         with open(SESSION_FILE, "r") as f:
#             return json.load(f)
#     return [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]

# def save_chat_history(messages):
#     with open(SESSION_FILE, "w") as f:
#         json.dump(messages, f)

# # Initialize session state for messages
# if "messages" not in st.session_state:
#     sleep(0.5)
#     st.session_state.messages = load_chat_history()

# # Added a key for tracking form submission
# if "submitted" not in st.session_state:
#     st.session_state.submitted = False

# # Header
# col1, col2 = st.columns([1, 5])
# with col1:
#     try:
#         image = Image.open("MRC-white-tm.png")
    
#         # Resize the image (set desired width and height)
#         new_width = 300  # Set your desired width
#         new_height = 200  # Set your desired height
#         resized_image = image.resize((new_width, new_height))
        
#         # Display the resized image
#         st.image(resized_image, use_container_width=True)
#     except:
#         st.markdown(f'<div style="background-color: {PRIMARY_COLOR}; width: 50px; height: 50px; border-radius: 10px; display: flex; align-items: center; justify-content: center;"><span style="color: white; font-size: 24px;">🏥</span></div>', unsafe_allow_html=True)
        
# with col2:
#     st.markdown('<h1 style="color: #30D4B3; font-size: 40px; font-weight: 600; margin: 0;">Medical Chatbot</h1>', unsafe_allow_html=True)

# # Subtitle
# st.markdown(
#     """
#     <p class="subtitle">
#         Your trusted AI assistant for medical information and guidance
#     </p>
#     """, 
#     unsafe_allow_html=True
# )

# # Display chat messages
# st.markdown('<div class="chat-container">', unsafe_allow_html=True)
# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="ai-message">{message["content"]}</div>', unsafe_allow_html=True)
# st.markdown('</div>', unsafe_allow_html=True)

# # Create a form for user input
# st.markdown('<div class="input-container">', unsafe_allow_html=True)

# # Callback for form submission
# def handle_submit():
#     if st.session_state.user_input and st.session_state.user_input.strip():
#         # Set submitted flag to True
#         st.session_state.submitted = True
#         # Store the current input
#         st.session_state.current_input = st.session_state.user_input

# # Use a form with a callback
# with st.form(key="chat_form", clear_on_submit=True):
#     prompt = st.text_input("", placeholder="Type your medical question here...", key="user_input")
    
#     col1, col2 = st.columns([4, 1])
#     with col2:
#         submit_button = st.form_submit_button("Send", on_click=handle_submit)

# # Clear chat button outside the form
# col1, col2 = st.columns([4, 1])
# with col2:
#     st.markdown('<div class="clear-button">', unsafe_allow_html=True)
#     clear_button = st.button("Clear Chat")
#     st.markdown('</div>', unsafe_allow_html=True)
    
# st.markdown('</div>', unsafe_allow_html=True)

# # Process form submission
# if st.session_state.submitted:
#     # Get the stored input
#     user_message = st.session_state.current_input
    
#     # Add user message to chat
#     st.session_state.messages.append({"role": "user", "content": user_message})
    
#     with st.spinner(""):
#         response = invokeChatbot(user_message)
    
#     # Add AI response to chat
#     st.session_state.messages.append({"role": "ai", "content": response})
#     save_chat_history(st.session_state.messages)
    
#     # Reset the submitted flag
#     st.session_state.submitted = False
    
#     # Use rerun to update the UI
#     st.rerun()

# # Clear chat history
# if clear_button:
#     st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]
#     save_chat_history(st.session_state.messages)
#     st.rerun()

# # Footer
# st.markdown(
#     """
#     <div class="footer">
#         <p><strong>Important:</strong> This chatbot provides general information only and is not a substitute for professional medical advice.</p>
#         <p>Always consult with a qualified healthcare provider for personal medical concerns.</p>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

import streamlit as st
from main import invokeChatbot
from time import sleep
import os
import json
from PIL import Image


PRIMARY_COLOR = "#30D4B3"
SECONDARY_COLOR = "#2B4C7E"  
SESSION_FILE = "chat_history.json"


st.set_page_config(
    page_title="Medical Chatbot",
    page_icon="🏥",
    layout="centered"
)


st.markdown(f"""
<style>
    /* Overall page styling */
    .stApp {{
        background: linear-gradient(135deg, #000428, #004e92); /* Dark gradient background */
        color: white;
        font-family: 'Arial', sans-serif;
    }}
    
    /* Main container styling */
    .main .block-container {{
        padding: 2rem;
        max-width: 800px;
        background: rgba(0, 0, 0, 0.6); /* Semi-transparent black */
        backdrop-filter: blur(10px); /* Glass morphism effect */
        border-radius: 20px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-top: 20px;
    }}
    
    /* Header styling */
    .header {{
        display: flex;
        align-items: center;
        margin-bottom: 25px;
        background: rgba(0, 0, 0, 0.4);
        padding: 15px;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }}
    
    .logo-container {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        width: 50px;
        height: 50px;
        border-radius: 12px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 15px;
        box-shadow: 0 0 20px {PRIMARY_COLOR};
    }}
    
    .title {{
        color: {PRIMARY_COLOR};
        font-size: 32px;
        font-weight: 700;
        margin: 0;
        text-shadow: 0 0 10px {PRIMARY_COLOR};
    }}
    
    /* Chat container styling */
    .chat-container {{
        background: rgba(0, 0, 0, 0.4);
        border-radius: 15px;
        padding: 20px;
        margin: 20px 0;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        max-height: 500px;
        overflow-y: auto;
        position: relative;
    }}
    
    /* Loading spinner styling */
    .loading-spinner {{
        position: absolute;
        bottom: 20px;
        left: 50%;
        transform: translateX(-50%);
        display: flex;
        justify-content: center;
        align-items: center;
        background: rgba(0, 0, 0, 0.6);
        padding: 10px;
        border-radius: 8px;
        backdrop-filter: blur(5px);
    }}
    
    .loading-spinner::after {{
        content: "";
        width: 20px;
        height: 20px;
        border: 3px solid {PRIMARY_COLOR};
        border-top: 3px solid transparent;
        border-radius: 50%;
        animation: spin 1s linear infinite;
        box-shadow: 0 0 10px {PRIMARY_COLOR};
    }}
    
    @keyframes spin {{
        0% {{ transform: rotate(0deg); }}
        100% {{ transform: rotate(360deg); }}
    }}
    
    /* Message styling */
    .user-message {{
        background: rgba(255, 255, 255, 0.1);
        color: white;
        padding: 12px 18px;
        border-radius: 18px 18px 0 18px;
        margin: 10px 0;
        max-width: 80%;
        align-self: flex-end;
        margin-left: auto;
        box-shadow: 0 0 10px rgba(255, 255, 255, 0.2);
        font-size: 16px;
        line-height: 1.5;
        font-weight: 400;
        backdrop-filter: blur(5px);
    }}
    
    .ai-message {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        color: white;
        padding: 12px 18px;
        border-radius: 18px 18px 18px 0;
        margin: 10px 0;
        max-width: 80%;
        box-shadow: 0 0 20px {PRIMARY_COLOR};
        font-size: 16px;
        line-height: 1.5;
        font-weight: 400;
    }}
    
    /* Input area styling */
    .input-container {{
        background: rgb(245, 50, 240);
        padding: 15px;
        border-radius: 15px;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
        margin-top: 20px;
    }}
    
    .stTextInput > div > div > input {{
        background: rgba(116, 148, 185 0.37);
        color: white;
        font-size: 16px;
        border: 2px solid rgba(26, 3, 3, 0);
        border-radius: 8px;
        padding: 12px 15px;
        height: 50px;
        box-shadow: none !important;
        backdrop-filter: blur(5px);
    }}
    
    .stTextInput > div > div > input:focus {{
        border-color: {PRIMARY_COLOR};
        box-shadow: 0 0 10px {PRIMARY_COLOR} !important;
    }}
    
    /* Button styling */
    .stButton > button {{
        background: linear-gradient(135deg, {PRIMARY_COLOR}, {SECONDARY_COLOR});
        color: white;
        font-weight: 600;
        border: none;
        border-radius: 8px;
        padding: 10px 20px;
        height: 45px;
        transition: all 0.3s ease;
        box-shadow: 0 0 20px {PRIMARY_COLOR};
    }}
    
    /* NEON SEND BUTTON STYLING */
    .send-button > button {{
        background: rgba(16, 226, 241, 0.99);
        color: #000;
        font-weight: 600;
        border: 2px solid #0ff;
        border-radius: 8px;
        padding: 10px 20px;
        height: 45px;
        position: relative;
        overflow: hidden;
        text-transform: uppercase;
        letter-spacing: 2px;
        box-shadow: 0 0 25px #0ff;
        text-shadow: 0 0 5px #0ff, 0 0 10px #0ff;
        transition: all 0.3s ease;
    }}
    
    .send-button > button:hover {{
        background: rgba(16, 226, 241, 0.99); !important;
        color: white !important;
        box-shadow: 0 0 40px #0ff;
        text-shadow: none;
    }}
    
    .send-button > button::before {{
        background: rgba(16, 226, 241, 0.99);
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: rgba(255, 255, 255, 0.1);
        transition: 0.5s;
        animation: neon-scan 3s infinite;
    }}

    .b {{
        background: rgba(16, 226, 241, 0.99);
    }}
    
    @keyframes neon-scan {{
        0% {{ left: -100%; }}
        50% {{ left: 100%; }}
        100% {{ left: 100%; }}
    }}
    
    .clear-button > button {{
        background: rgba(255, 255, 255, 0.1);
        color: #CCCCCC;
        border: 1px solid rgba(255, 255, 255, 0.2);
    }}
    
    /* Footer styling */
    .footer {{
        background: rgba(0, 0, 0, 0.4);
        padding: 15px;
        border-radius: 15px;
        margin-top: 20px;
        text-align: center;
        font-size: 14px;
        color: #CCCCCC;
        backdrop-filter: blur(5px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4);
    }}
    /* Hide Streamlit branding */
    #MainMenu, footer, header {{
        visibility: hidden;
    }}
    
    /* Text styling for subtitle */
    .subtitle {{
        color: #CCCCCC;
        font-size: 16px;
        margin-top: -10px;
        margin-bottom: 25px;
        text-shadow: 0 0 10px {PRIMARY_COLOR};
    }}
</style>
""", unsafe_allow_html=True)


# def load_chat_history():
#     if os.path.exists(SESSION_FILE):
#         with open(SESSION_FILE, "r") as f:
#             return json.load(f)
#     return [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]

# def save_chat_history(messages):
#     with open(SESSION_FILE, "w") as f:
#         json.dump(messages, f)

# if "messages" not in st.session_state:
#     sleep(0.5)
#     st.session_state.messages = load_chat_history()


# if "submitted" not in st.session_state:
#     st.session_state.submitted = False


# import streamlit as st
# from PIL import Image

# col1, col2, col3 = st.columns([1, 5, 1])  
# with col2:
#     try:
#         image = Image.open("MRC-white-tm (1).png")
#         resized_image = image.resize((500, 100))  

        
#         st.markdown(
#             "<div style='display: flex; justify-content: center;'>",
#             unsafe_allow_html=True,
#         )
#         st.image(resized_image)
#         st.markdown("</div>", unsafe_allow_html=True)

#     except:
#         st.markdown(
#             f"""
#             <div style="display: flex; justify-content: center; align-items: center;">
#                 <div style="background-color: #30D4B3; width: 100px; height: 100px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
#                     <span style="color: white; font-size: 50px;">🏥</span>
#                 </div>
#             </div>
#             """,
#             unsafe_allow_html=True,
#         )

# st.markdown(
#     """
#     <h1 style="text-align: center; color: #30D4B3; font-size: 20px; font-weight: 800; margin-top: 0px;">
#         Medical Chatbot
#     </h1>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     """
#     <p style="text-align: center; font-size: 20px; color: #CCCCCC; margin-top: -10px;">
#         Your trusted AI assistant for medical information and guidance
#     </p>
#     """,
#     unsafe_allow_html=True
# )

# st.markdown(
#     "<hr style='border: 2px solid #30D4B3; border-radius: 5px; margin-top: -5px;'>", 
#     unsafe_allow_html=True
# )

# for message in st.session_state.messages:
#     if message["role"] == "user":
#         st.markdown(f'<div class="user-message">{message["content"]}</div>', unsafe_allow_html=True)
#     else:
#         st.markdown(f'<div class="ai-message">{message["content"]}</div>', unsafe_allow_html=True)


# if st.session_state.submitted:
#     st.markdown('<div class="loading-spinner"></div>', unsafe_allow_html=True)

# st.markdown('</div>', unsafe_allow_html=True)


# def handle_submit():
#     if st.session_state.user_input and st.session_state.user_input.strip():
#         st.session_state.submitted = True
#         st.session_state.current_input = st.session_state.user_input

# # Apply custom CSS to style the submit button as "Send"
# st.markdown(
#     """
#     <style>
#         div[data-testid="stForm"] button {
#             display: flex;
#             justify-content: center;
#             align-items: center;
#             background-color: #007bff;
#             color: white;
#             border: none;
#             padding: 8px 16px;
#             border-radius: 5px;
#             cursor: pointer;
#             font-size: 16px;
#             width: 100%;
#             text-align: center;
#         }
#         div[data-testid="stForm"] button:hover {
#             background-color: #0056b3;
#         }
#     </style>
#     """, 
#     unsafe_allow_html=True
# )

# # Chat input form
# with st.form(key="chat_form", clear_on_submit=True):
#     st.text_input("", placeholder="Type your medical question here...", key="user_input")
#     submit_button = st.form_submit_button("Send", on_click=handle_submit)  # Ensuring only one send button

# # Clear button with a unique key
# clear_button = st.button("Clear Chat", key="clear_chat_button")

# # Initialize messages
# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]

# # Process user input
# if st.session_state.get("submitted"):
#     user_message = st.session_state.current_input
#     st.session_state.messages.append({"role": "user", "content": user_message})
    
#     with st.spinner("Thinking..."):
#         response = "This is a dummy response."  # Replace with invokeChatbot(user_message)
    
#     st.session_state.messages.append({"role": "ai", "content": response})
#     st.session_state.submitted = False
#     st.rerun()

# # Handle chat clearing
# if clear_button:
#     st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]
#     st.rerun()

# # Footer notice
# st.markdown(
#     """
#     <div class="footer">
#         <p><strong>Important:</strong> This chatbot provides general information only and is not a substitute for professional medical advice.</p>
#         <p>Always consult with a qualified healthcare provider for personal medical concerns.</p>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# col1, col2 = st.columns([4, 1])
# with col2:
#     clear_button = st.button("Clear Chat")

# if "messages" not in st.session_state:
#     st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]

# if st.session_state.get("submitted"):
#     user_message = st.session_state.current_input
#     st.session_state.messages.append({"role": "user", "content": user_message})
    
#     with st.spinner("Thinking..."):
#         response = "This is a dummy response."  # Replace with invokeChatbot(user_message)
    
#     st.session_state.messages.append({"role": "ai", "content": response})
#     st.session_state.submitted = False
#     st.rerun()

# if clear_button:
#     st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]
#     st.rerun()

# st.markdown(
#     """
#     <div class="footer">
#         <p><strong>Important:</strong> This chatbot provides general information only and is not a substitute for professional medical advice.</p>
#         <p>Always consult with a qualified healthcare provider for personal medical concerns.</p>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )

# col1, col2 = st.columns([4, 1])
# with col2:
#     st.markdown('<div class="clear-button">', unsafe_allow_html=True)
#     clear_button = st.button("Clear Chat")
#     st.markdown('</div>', unsafe_allow_html=True)
    
# st.markdown('</div>', unsafe_allow_html=True)


# if st.session_state.submitted:
#     user_message = st.session_state.current_input
    

#     st.session_state.messages.append({"role": "user", "content": user_message})
    
#     with st.spinner(""):
#         response = invokeChatbot(user_message)
    
#     st.session_state.messages.append({"role": "ai", "content": response})
#     save_chat_history(st.session_state.messages)
#     st.session_state.submitted = False
    
#     st.rerun()

# if clear_button:
#     st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]
#     save_chat_history(st.session_state.messages)
#     st.rerun()

# st.markdown(
#     """
#     <div class="footer">
#         <p><strong>Important:</strong> This chatbot provides general information only and is not a substitute for professional medical advice.</p>
#         <p>Always consult with a qualified healthcare provider for personal medical concerns.</p>
#     </div>
#     """, 
#     unsafe_allow_html=True
# )




# def handle_submit():
#     if st.session_state.user_input and st.session_state.user_input.strip():
#         st.session_state.submitted = True
#         st.session_state.current_input = st.session_state.user_input

# with st.form(key="chat_form", clear_on_submit=True):
#     prompt = st.text_input("", placeholder="Type your medical question here...", key="user_input")
    
#     col1, col2 = st.columns([4, 1])
#     with col2:

#         st.markdown("""
# <style>
# /* Define the neon button style */
# .send-button01 button {
#     background-color:rgb(13, 236, 169); /* Neon red color */
#     border: none;
#     color: white;
#     padding: 10px 20px;
#     text-align: center;
#     text-decoration: none;
#     display: inline-block;
#     font-size: 16px;
#     border-radius: 5px;
#     cursor: pointer;
#     box-shadow: 0 0 10px #ff6f61, 0 0 20px #ff6f61, 0 0 30px #ff6f61, 0 0 40px #ff6f61;
#     transition: all 0.3s ease;
# }

# /* Hover effect for the neon button */
# .send-button button:hover {
#     background-color: #ff3c2f; /* Slightly darker neon red */
#     box-shadow: 0 0 15px #ff3c2f, 0 0 25px #ff3c2f, 0 0 40px #ff3c2f, 0 0 50px #ff3c2f;
# }
# </style>
# """, unsafe_allow_html=True)

#         # Apply the new neon send button styling class
#         st.markdown('<div class="send-button01">', unsafe_allow_html=True)
#         submit_button = st.form_submit_button("Send", on_click=handle_submit)
#         st.markdown('</div>', unsafe_allow_html=True)


SESSION_FILE = "chat_history.json"

# Load chat history from file
def load_chat_history():
    if os.path.exists(SESSION_FILE):
        with open(SESSION_FILE, "r") as f:
            return json.load(f)
    return [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]

# Save chat history to file
def save_chat_history(messages):
    with open(SESSION_FILE, "w") as f:
        json.dump(messages, f)

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = load_chat_history()

if "submitted" not in st.session_state:
    st.session_state.submitted = False

# Display header with logo
col1, col2, col3 = st.columns([1, 5, 1])
with col2:
    try:
        image = Image.open("MRC-white-tm.png")
        resized_image = image.resize((500, 100))
        st.markdown(
            "<div style='display: flex; justify-content: center;'>",
            unsafe_allow_html=True,
        )
        st.image(resized_image)
        st.markdown("</div>", unsafe_allow_html=True)
    except FileNotFoundError:
        st.markdown(
            """
            <div style="display: flex; justify-content: center; align-items: center;">
                <div style="background-color: #30D4B3; width: 100px; height: 100px; border-radius: 10px; display: flex; align-items: center; justify-content: center;">
                    <span style="color: white; font-size: 50px;">🏥</span>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# Display title and subtitle
st.markdown(
    """
    <h1 style="text-align: center; color: #30D4B3; font-size: 20px; font-weight: 800; margin-top: 0px;">
        Medical Chatbot
    </h1>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    """
    <p style="text-align: center; font-size: 20px; color: #CCCCCC; margin-top: -10px;">
        Your trusted AI assistant for medical information and guidance
    </p>
    """,
    unsafe_allow_html=True,
)
st.markdown(
    "<hr style='border: 2px solid #30D4B3; border-radius: 5px; margin-top: -5px;'>",
    unsafe_allow_html=True,
)

# Display chat history
for message in st.session_state.messages:
    role_class = "user-message" if message["role"] == "user" else "ai-message"
    st.markdown(f'<div class="{role_class}">{message["content"]}</div>', unsafe_allow_html=True)

# Handle user input submission
def handle_submit():
    if st.session_state.user_input and st.session_state.user_input.strip():
        st.session_state.submitted = True
        st.session_state.current_input = st.session_state.user_input

# Custom CSS for submit button
st.markdown(
    """
    <style>
        div[data-testid="stForm"] button {
            display: flex;
            justify-content: center;
            align-items: center;
            background-color: #007bff;
            color: white;
            border: none;
            padding: 8px 16px;
            border-radius: 5px;
            cursor: pointer;
            font-size: 16px;
            width: 100%;
            text-align: center;
        }
        div[data-testid="stForm"] button:hover {
            background-color: #0056b3;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

# Chat input form
with st.form(key="chat_form", clear_on_submit=True):
    st.text_input("", placeholder="Type your medical question here...", key="user_input")
    submit_button = st.form_submit_button("Send", on_click=handle_submit)

# Clear chat button with unique key
clear_button = st.button("Clear Chat", key="clear_chat_button")

# Process user input
if st.session_state.get("submitted"):
    user_message = st.session_state.current_input
    st.session_state.messages.append({"role": "user", "content": user_message})

    with st.spinner("Thinking..."):
        response = invokeChatbot(user_message) # Replace with invokeChatbot(user_message)

    st.session_state.messages.append({"role": "ai", "content": response})
    save_chat_history(st.session_state.messages)
    st.session_state.submitted = False
    st.rerun()

# Handle chat clearing
if clear_button:
    st.session_state.messages = [{"role": "ai", "content": "Hello! I'm here to assist you with your medical queries. How can I help you today?"}]
    save_chat_history(st.session_state.messages)
    st.rerun()

# Footer notice
st.markdown(
    """
    <div class="footer">
        <p><strong>Important:</strong> This chatbot provides general information only and is not a substitute for professional medical advice.</p>
        <p>Always consult with a qualified healthcare provider for personal medical concerns.</p>
    </div>
    """,
    unsafe_allow_html=True,
)