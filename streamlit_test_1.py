import streamlit as st
hide_menu ="""
<style>
#MainMenu { visibility: hidden;}
</style>
"""
def main():
  st.title("corro")
  st.markdown(hide_menu, unsafe_allow_html=True)
  st.write("Hello Nature")
  st.text_input("Favourite Book name")
