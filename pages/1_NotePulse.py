from google import genai
from google.genai import types
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = genai.Client()

    
st.title('NotePulse')

st.space()

st.markdown("<h2 style = 'text-align: center';>Flash Notes & Summary Generator⚡</h2>", unsafe_allow_html=True)
st.space()
st.markdown("<h4 style = 'text-align: center';>Make notes in a Instant : --</h4>", unsafe_allow_html=True)

input_text = st.text_area('Upto 30,000 characters allowed',placeholder='Paste article, unstructured notes or topics')

if st.button("Generate Notes📝", use_container_width=True):
    if 4 <= len(input_text)<= 30000:
        with st.spinner('**Pulse** processing...'):
            try:
                chat = client.chats.create(
                model = 'gemini-3.5-flash-lite',
                config = types.GenerateContentConfig(
                system_instruction = """You are NotePulse, 
                an advanced educational AI assistant.
                  Convert the provided user text or topic into clear, 
                  structured bullet points, short notes, flashcard key-value pairs, and 
                  formula cheat sheets where applicable. If the input cannot be processed, politely prompt
                    the user to provide valid educational text."""))

                interaction = chat.send_message_stream(input_text)
                                              
                st.subheader('Pulse :')
                with st.container(border = True):

                    st.write_stream(chunk.text for chunk in interaction)
            
            except Exception as e:
                st.error(f"ERROR : {e}")
                
                    
                          
        
                   
        
        
       
    else:
        st.warning('Give text under specified limit')
        


        

            
            

