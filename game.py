import random 
import streamlit as st

st.sidebar.subheader("**Built by Saurabh**")

st.header("Welcome to the Game of Rock, Paper & Scissors")

option=st.selectbox("Choose Your One Option :",["Rock","Paper","Scissors"])
st.write('**You Selected :**',option)

btn=st.button("Submit")

if btn:
    def get_choices():
        player_choice = option
        options = ["Rock", "Paper", "Scissors"]
        computer_choice = random.choice(options)
        choices = {"player": player_choice, "computer": computer_choice}
        return choices

    def check_win(player, computer):
        st.write(f"**Computer Selected :** {computer}")
        if player == computer:
            return "It's a Tie!"
        elif player == "Rock":
            if computer == "Scissors":
                return "Rock smashes Scissors! You Win!"
            else:
                return "Paper covers Rock! You Lose."
        elif player == "Paper":
            if computer == "Rock":
                return "Paper covers Rock! You Win!"
            else:
                return "Scissors cuts Paper! You Lose."
        elif player == "Scissors":
            if computer == "Paper":
                return "Scissors cuts Paper! You Win!"
            else:
                return "Rock smashes Scissors! You Lose."
        
    choices = get_choices()
    result = check_win(choices["player"], choices["computer"])
    
    st.subheader(result)
    st.balloons()
    st.success("Thanks for Playing...")

 
    

