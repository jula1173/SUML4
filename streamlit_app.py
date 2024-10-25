import streamlit as st
import pandas as pd
import time
import os
from transformers import pipeline


st.title("Aplikacja NLP - Analiza Wydźwięku i Tłumaczenie Tekstu")


st.header("Wprowadzenie")
st.write("Witaj w aplikacji do analizy wydźwięku tekstu oraz tłumaczenia! Używamy narzędzi NLP, by pomagać w analizie treści i tłumaczeniu.")
st.write("To narzędzie może analizować wydźwięk emocjonalny tekstu w języku angielskim lub tłumaczyć tekst z języka angielskiego na niemiecki.")


st.success('Aplikacja uruchomiona pomyślnie! Wybierz opcję, aby kontynuować.')
st.balloons()  


option = st.selectbox(
    "Wybierz opcję:",
    [
        "Wydźwięk emocjonalny tekstu (eng)",
        "Tłumaczenie z angielskiego na niemiecki",
    ],
)

if option == "Wydźwięk emocjonalny tekstu (eng)":
    st.subheader("Analiza Wydźwięku Emocjonalnego Tekstu")
    text = st.text_area(label="Wpisz tekst po angielsku:")
    if text:
        with st.spinner("Analizuję wydźwięk..."):
            classifier = pipeline("sentiment-analysis")
            answer = classifier(text)
            st.success("Analiza zakończona!")
            st.write("Wynik analizy:", answer)

elif option == "Tłumaczenie z angielskiego na niemiecki":
    st.subheader("Tłumaczenie Tekstu z Angielskiego na Niemiecki")
    text = st.text_area(label="Wpisz tekst po angielsku:")
    if text:
        with st.spinner("Tłumaczę..."):
            # Użycie modelu Helsinki-NLP do tłumaczenia
            translator = pipeline("translation", model="Helsinki-NLP/opus-mt-en-de")
            translation = translator(text)
            st.success("Tłumaczenie zakończone!")
            st.write("Przetłumaczony tekst:", translation)


# Instrukcja użytkowania
st.header("Instrukcja")
st.write("1. Wybierz opcję: analiza wydźwięku lub tłumaczenie.")
st.write("2. Wpisz tekst w języku angielskim.")
st.write("3. Odczytaj wynik analizy lub tłumaczenia poniżej pola tekstowego.")


st.write("Projekt wykonany przez s24595")


st.subheader('Zadanie do wykonania')
st.write('Wykorzystaj Huggin Face do stworzenia swojej własnej aplikacji tłumaczącej tekst z języka angielskiego na język niemiecki. Zmodyfikuj powyższy kod dodając do niego kolejną opcję, tj. tłumaczenie tekstu. Informacje potrzebne do zmodyfikowania kodu znajdziesz na stronie Huggin Face - https://huggingface.co/docs/transformers/index')
st.write('🐞 Dodaj właściwy tytuł do swojej aplikacji, może jakieś grafiki?')
st.write('🐞 Dodaj krótką instrukcję i napisz do czego służy aplikacja')
st.write('🐞 Wpłyń na user experience, dodaj informacje o ładowaniu, sukcesie, błędzie, itd.')
st.write('🐞 Na końcu umieść swój numer indeksu')
st.write('🐞 Stwórz nowe repozytorium na GitHub, dodaj do niego swoją aplikację, plik z wymaganiami (requirements.txt)')
st.write('🐞 Udostępnij stworzoną przez siebie aplikację (https://share.streamlit.io) a link prześlij do prowadzącego')