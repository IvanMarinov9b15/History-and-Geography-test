import streamlit as st

st.write("Тест по География и История")
st.write("Моля, въведете вашите отговори в полетата по-долу.")

score = 0

st.write("1. Коя е столицата на България?")
q1 = st.text_input("Вашият отговор за въпрос 1:", key="q1")

st.write("2. През коя година е основана българската държава?")
q2 = st.text_input("Вашият отговор за въпрос 2:", key="q2")

st.write("3. Кой е най-високият връх в България?")
q3 = st.text_input("Вашият отговор за въпрос 3:", key="q3")

st.write("4. Кой е известен като Апостола на свободата?")
q4 = st.text_input("Вашият отговор за въпрос 4:", key="q4")

st.write("5. Колко континента има на Земята?")
q5 = st.text_input("Вашият отговор за въпрос 5:", key="q5")

if st.button("Провери резултата"):
    if q1.strip().lower() == "софия":
        score = score + 1
    
    if q2.strip() == "681":
        score = score + 1
        
    if q3.strip().lower() == "мусала":
        score = score + 1
        
    if q4.strip().lower() == "васил левски":
        score = score + 1
        
    if q5.strip() == "7":
        score = score + 1

    if score == 5:
        st.write("Резултат: 5/5. Всички отговори са верни.")
    else:
        st.write("Резултат: " + str(score) + "/5. Опитайте отново за по-добър резултат.")
    elif score >= 3:
        st.info(f"Резултат: {score}/5. Добър опит.")
    else:
        st.error(f"Резултат: {score}/5. Опитайте отново.")
