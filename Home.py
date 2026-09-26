import streamlit as st


st.markdown("<h1 style = 'text-align: center'>🤖 HOME 🤖</h1>",unsafe_allow_html=True)

st.space()

st.markdown("<h2 style = 'text-align: center'>Hey 👋,  Welcome!!!</h2>",unsafe_allow_html=True)

st.space()

st.markdown("<h3 style = 'text-align: center'>Our software consists of two Ai Brothers :-</h3>",unsafe_allow_html=True)

col1,col2 = st.columns(2)

with col1:
    if st.button("**Bulleto Ai📝**",use_container_width=True):
        st.switch_page("pages/Bulleto.py")

with col2:
    if st.button("**Quizo Ai🧠**", use_container_width=True):
        st.switch_page("pages/Quizo.py")

st.space()

st.subheader("**Bulleto Ai :**")
st.write("Bulleto is a smart tool that instantly generates short notes from your topic or chunki notes," \
" flashcards, and revision formulas.As every student knows, dealing with massive chunks of unstructured study material can be overwhelming." \
" To save you valuable time, we created Bulleto. " \
"Powered by the latest **Gemini 3.5 Flash-Lite model**, " \
"Bulleto delivers high-precision study aids with lightning-fast execution.")

st.space()
st.subheader("**Quizo Ai :**")

st.write( "As name suggests," \
" Quizo is a question-generating nerd—and Bulleto’s little brother!." \
"He is your ultimate study companion for active recall and revision," \
" creating custom questions directly from your topics and notes. " \
"Don't let the nerd title fool you;"\
"Quizo is incredibly efficient."\
"Powered by the same **Gemini 3.5 Flash-Lite model**, he delivers lightning-fast performance so you never have to worry about speed.")

