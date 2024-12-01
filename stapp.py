import requests
import json
import streamlit as st

url = "http://localhost:11434/api/generate"

headers = {
    'Content-Type': 'application/json'
}

history = []

def generate_response(prompt):
    history.append(prompt)
    final_prompt = "\n".join(history)

    data = {
        "model": "codeguru",  # Ensure this is the correct model name
        "prompt": final_prompt,
        "stream": False
    }

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        data = response.json()
        actual_response = data.get('response', 'No response found')
        return actual_response
    else:
        return f"Error: {response.status_code}, {response.text}"

# Streamlit UI
st.title("CodeGuru By-👑 Milind_Patil 👑")
prompt = st.text_area("Enter your prompt:", placeholder="Type your prompt here...")

if st.button("Generate Response"):
    if prompt:
        response = generate_response(prompt)
        st.write("### Response:")
        st.write(response)
    else:
        st.warning("Please enter a prompt!")
