from google import genai
from google.genai import types
from dotenv import load_dotenv
import streamlit as st

load_dotenv()

client = genai.Client()

    
st.title('Bulleto_𝐴𝑖')

st.space()

st.markdown("<h2 style = 'text-align: center';>Hi, Welcome to Bulleto Ai !! </h2>", unsafe_allow_html=True)
st.space()
st.markdown("<h4 style = 'text-align: center';>Place your study material here :</h4>", unsafe_allow_html=True)

input_text = st.text_area('Maximum 30,000 characters allowed',placeholder='Here buddy!!!')

if st.button("Make Notes 📝"):
    if 4 <= len(input_text)<= 30000:
        with st.spinner('Ai processing...'):
            try:
                chat = client.chats.create(
                model = 'gemini-3.5-flash-lite',
                config = types.GenerateContentConfig(
                system_instruction = 'you are a bullet points maker and flashcard, short notes maker or formulas if any.' \
                                'when user will give you text or just a topic name , you have to covert it into bullet points, short notes,flash cards.' \
                                'if user gives a text that can not be made into bullet points or short notes or flash cards,'
                                ' you will say that to user that is it is not possible and put correct text'))

                interaction = chat.send_message_stream(input_text)
                                              
                st.subheader('Bulleto :')
                with st.container(border = True):

                    st.write_stream(chunk.text for chunk in interaction)
            
            except Exception as e:
                st.error(f"ERROR : {e}")
                
                    
                          
        
                   
        
        
       
    else:
        st.warning('Give text under specified limit')
        


        

            
            

