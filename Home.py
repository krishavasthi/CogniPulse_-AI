import streamlit as st




st.markdown("""<h1 style = "text-align: center ;">CogniPulse AI</h1>""",unsafe_allow_html=True)

st.space()

st.markdown("<h2 style = 'text-align: center'>Hey 👋,  Welcome!!!</h2>",unsafe_allow_html=True)

st.space()

st.markdown("<h3 style = 'text-align: center'>CogniPulse AI operates on Two Core Engines :-</h3>",unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    if st.button("**NotePulse📝**",use_container_width=True):
        st.switch_page("pages/1_NotePulse.py")

with col2:
    if st.button("**CogniQuiz🧠**", use_container_width=True):
        st.switch_page("pages/CogniQuiz.py")

st.space()

st.subheader("**NotePulse :**")
st.write("NotePulse is a smart synthesis engine that instantly generates short notes," \
" flashcards, and revision formulas from your topics or course material. " \
"To save you valuable study time, NotePulse converts unstructured text into concise revision aids." \
" Powered by the latest **Gemini 3.5 Flash-Lite model**, it delivers high-precision outputs with lightning-fast execution.")

st.space()
st.subheader("**CogniQuiz :**")

st.write( "CogniQuiz is an automated creative question generator designed for active recall and self-assessment." \
" It creates custom quizzes directly from your notes to test your understanding before exams. " \
"Powered by the same **Gemini 3.5 Flash-Lite model**, " \
"CogniQuiz delivers structured assessments instantly.")

