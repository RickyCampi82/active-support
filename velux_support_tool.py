import streamlit as st
import openai

# Configurazione della pagina
st.set_page_config(page_title="Supporto VELUX Intelligente", page_icon="🤖")
st.title("🤖 Tool Intelligente di Supporto VELUX")

st.markdown("Inserisci una domanda dell'operatore e seleziona il tipo di risposta desiderata. Il tool genererà automaticamente un testo in stile VELUX, pronto da leggere al telefono o inviare per email.")

# Inserimento chiave API OpenAI
openai_api_key = st.text_input("🔑 Inserisci la tua API Key OpenAI per generare risposte intelligenti", type="password")

# Input domanda e canale
domanda = st.text_input("💬 Domanda dell'operatore")
canale = st.radio("📞 Tipo di risposta", ["telefono", "email"])

# Prompt di sistema per GPT
def genera_prompt(domanda, canale):
    stile = "risposta sintetica e chiara, da leggere al telefono" if canale == "telefono" else "risposta formale in formato email con apertura, corpo e chiusura"
    return f"""Sei un operatore del supporto clienti VELUX Italia.

Rispondi in italiano a una domanda di un collega che parla con un cliente. Scrivi una {stile}, mantenendo un tono professionale, cortese e preciso.

Segui queste linee guida:
- I prodotti trattati sono VELUX ACTIVE, VELUX App Control, sensori, gateway, compatibilità Wi-Fi, installazione, integrazione con Google Home, Apple HomeKit e simili.
- Non fare affermazioni generiche: sii chiaro e specifico.
- Se la domanda non è coperta, suggerisci di contattare il supporto tecnico ufficiale.

Domanda dell'operatore: {domanda}
"""

# Funzione per invocare GPT
def genera_risposta(domanda, canale, openai_api_key):
    if not openai_api_key:
        return "⚠️ Inserisci una chiave API OpenAI valida per generare una risposta."
    try:
        openai.api_key = openai_api_key
        risposta = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": genera_prompt(domanda, canale)},
                {"role": "user", "content": domanda}
            ],
            temperature=0.5,
            max_tokens=600
        )
        return risposta.choices[0].message.content.strip()
    except Exception as e:
        return f"❌ Errore nella generazione della risposta: {str(e)}"

# Output della risposta
if domanda:
    risposta = genera_risposta(domanda, canale, openai_api_key)
    st.subheader("📝 Risposta suggerita:")
    st.text_area("", risposta, height=200)
    st.code(risposta, language="text")
    st.button("📋 Copia risposta", on_click=st.experimental_set_query_params, args=({"copiato": "ok"},))

