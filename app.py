import streamlit as st
import requests
import json

# Set page configuration
st.set_page_config(
    page_title="AI Psychologist",
    page_icon="🧠",
    layout="wide"
)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

def query_llama(prompt):
    """Send a query to the Ollama API."""
    try:
        system_prompt = """You are an empathetic and professional psychologist with years of experience in counseling. 
        Your role is to provide supportive, thoughtful responses while maintaining professional boundaries. 
        Focus on active listening, asking relevant questions, and offering constructive insights.
        However, always make it clear that you are an AI and recommend seeking professional help for serious concerns."""
        
        full_prompt = f"{system_prompt}\n\nClient: {prompt}\nPsychologist:"
        
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "llama3.2",
                "prompt": full_prompt,
                "stream": False
            }
        )
        response.raise_for_status()
        return response.json()["response"]
    except requests.exceptions.RequestException as e:
        st.error(f"Error communicating with Ollama: {str(e)}")
        return None

# Streamlit UI
st.title("🧠 AI Psychology Assistant")
st.write("A supportive space for psychological discussions and guidance")

# Display chat history
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("What would you like to discuss?"):
    # Display user message
    with st.chat_message("user"):
        st.markdown(prompt)
    st.session_state.messages.append({"role": "user", "content": prompt})

    # Get and display assistant response
    with st.chat_message("assistant"):
        response = query_llama(prompt)
        if response:
            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

# Add sidebar with information
with st.sidebar:
    st.title("About")
    st.markdown("""
    This AI Psychology Assistant uses the Llama 2 model through Ollama to provide supportive conversations and psychological insights.
    
    **Important Notice:**
    - This is an AI assistant and not a replacement for professional mental health care
    - For serious concerns, please seek help from licensed mental health professionals
    - In case of emergency, contact your local emergency services
    
    **Technical Requirements:**
    - Ollama must be installed and running
    - Llama 2 model must be pulled (`ollama pull llama2`)
    """)
