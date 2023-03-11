import streamlit as st

def quiz():
    q1, q2, q3, q4 = "","","",""
    st.title("Enable Qui-zy")
    score = 0
    
    st.write("1. What is the purpose of the poem 'Wake up! Wake up!'?")
    q1 = st.radio('Select answer for Question 1: ', ('To encourage people to stay in bed all day', 
                                                    'To remind people to listen to the birds and bees', 
                                                    'To urge people to join in the fun of a beautiful day', 
                                                    'To promote a healthy sleep schedule'))
    st.write("2. What can be heard in the trees in the morning?")
    q2 = st.radio('Select answer for Question 2: ', ('Cats meowing', 
                                                    'Dogs barking', 
                                                    'Birds singing', 
                                                    'Frogs croaking'))
    st.write("3. What should you do after waking up according to the poem?")
    q3 = st.radio('Select answer for Question 3: ', ('Stay in bed', 
                                                    'Brush your teeth', 
                                                    'Watch TV', 
                                                    'Wash and dress'))
    st.write("4. Which animals are mentioned in the poem?")
    q4 = st.radio('Select answer for Question 4: ', ('Dogs, cats, and pigs',
                                                    'Horses, cows, and sheep',
                                                    'Monkeys, tigers, and elephants',
                                                    'Rabbits, squirrels, and mice'))
    response = "Click on Submit after answering the questions"
    st.write(response)

    if(q1 == 'To urge people to join in the fun of a beautiful day'):
        score += 1
    if(q4 == 'Horses, cows, and sheep'):
        score += 1
    if(q3 == 'Wash and dress'):
        score += 1
    if(q2 == 'Birds singing'):
        score += 1

    if(st.button("Submit", key='submit')):
        st.write("Score: ")
        st.write(score)
        st.write("Correct answers: ")
        st.write("1. To urge people to join in the fun of a beautiful day")
        st.write("2. Birds singing")
        st.write("3. Wash and dress")
        st.write("4. Horses, cows, and sheep")
        response = "The selected answers are for the questions are - "+q1+", "+q2+", "+q3+" and "+q4+"."
        st.success(response)