import streamlit as st
import json
from google import genai 
from google.genai import types
from dotenv import load_dotenv

load_dotenv()
client = genai.Client()

if "quiz_output" not in st.session_state:
    st.session_state.quiz_output = None

def quiz(quiz_output:dict[str], key_preffix : str = "q"):
    for i in range(len(quiz_output['questions'])):
        st.subheader(f'Question {i+1} :--')
        option = st.radio(quiz_output['questions'][i],quiz_output['options'][i], index=None, key= f"{key_preffix}_{i}")

        if option == None:
            st.info('please select a option')
        elif option == quiz_output['answers'][i]:
            st.success(f'You are correct answer is : {quiz_output["answers"][i]}')
            st.success(quiz_output['explanation'][i])
        else:
            st.error(f'Sorry wrong answer, correct answer is : {quiz_output["answers"][i]}')
            st.error(quiz_output['explanation'][i])

def Ai(input_text : str, questions: int):
    if 4 <= len(input_text) <= 30000:
                with st.spinner('Quizo is working...'):
                    try:
                        chat = client.chats.create(
                            model='gemini-3.5-flash-lite',
                            config= types.GenerateContentConfig(
                                response_mime_type= "application/json",
                                system_instruction= 'you are a quiz maker , when user will add topic or text,' \
                                f' you will have to give them {questions} questions,' \
                                'in format like like this ' \
                                'a json dictionary in format {questions : [q1,q2,....,qn],options : [[o1,o2,o3,o4],[],......,[]],answers:[a1,a2,....,an],explanation : [e1,e2,....,en]}' \
                                'if user gives text that is not related to quiz and we can not make quiz out of it ,you will inform him to give right text politely' \
                                'questions should be good and if he says to give easy,hard, mix, you can then customise according to user'
                            ,)
                        )
                        interaction = chat.send_message(input_text)
                        st.session_state.quiz_output = json.loads(interaction.text)

                    except Exception as e:
                        st.error(f"Error :{e}")
    else:
        st.warning('Give text under specified limit')


    



st.title('Quizo_𝐴𝑖')
st.space()
st.markdown("<h2 style = 'text-align: center';> Yo buddy🤓, welcome to Quizo </h2>", unsafe_allow_html=True)
st.space()
st.markdown("<h3 style = 'text-align: center';> Try out some Quiz practice? </h2>", unsafe_allow_html=True)
input_text = st.text_area('Maximum 30,000 characters limit',placeholder='This way, buddy...')

col1, col2, col3 = st.columns(3)



with col1:
    if st.button('10 Question', use_container_width=True):
        Ai(input_text,10)

with col2:
    if st.button('20 Question',use_container_width=True):
        Ai(input_text,20)

with col3:
    if st.button('30 Question',use_container_width=True):
        Ai(input_text,30)

                            

with st.container(border=True):
        if st.session_state.quiz_output:
            st.write('---')
            quiz(st.session_state.quiz_output)