import streamlit as st

st.write("Тест по География и История")
st.write("Моля, отговорете на следните 5 въпроса:")

score = 0

st.write("1. Коя е столицата на България?")
q1 = st.text_input("Въведете град:", key="q1")

st.write("2. През коя година е основана българската държава?")
q2 = st.text_input("Въведете година:", key="q2")

st.write("3. Кой е най-високият връх в България?")
q3 = st.text_input("Въведете връх:", key="q3")

st.write("4. Кой е известен като Апостола на свободата?")
q4 = st.text_input("Въведете име:", key="q4")

st.write("5. Колко континента има на Земята?")
q5 = st.number_input("Въведете число:", min_value=0, step=1, key="q5")

if st.button("Провери резултата"):
    if q1.strip().lower() == "софия":
        score = score + 1
    
    if q2.strip() == "681":
        score = score + 1
        
    if q3.strip().lower() == "мусала":
        score = score + 1
        
    if q4.strip().lower() == "васил левски":
        score = score + 1
        
    if q5 == 7:
        score = score + 1

    if score == 5:
        st.write("Отличен! Резултат: 5 от 5.")
    else:
        st.write("Вашият резултат е: " + str(score) + " от 5. Опитайте отново.")
