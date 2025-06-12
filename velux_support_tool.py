
# Web App Velux Support Tool (Streamlit)
import streamlit as st

# Database semplificato FAQ
faq_db = [
    {
        "keywords": ["quanti sensori", "numero sensori", "aggiungere sensori"],
        "categoria": "installazione",
        "telefono": "Può associare fino a 10 sensori per ogni gateway VELUX ACTIVE.",
        "email": (
            "Gentile Cliente,\n\n"
            "La informiamo che è possibile associare fino a 10 sensori per ciascun gateway VELUX ACTIVE."
            " In caso di necessità di copertura per ambienti aggiuntivi, è sufficiente installare un secondo gateway.\n\n"
            "Cordiali saluti,\nTeam VELUX"
        )
    },
    {
        "keywords": ["wifi", "rete", "connessione"],
        "categoria": "compatibilità",
        "telefono": "VELUX ACTIVE supporta reti Wi-Fi a 2.4 GHz, non è compatibile con 5 GHz.",
        "email": (
            "Gentile Cliente,\n\n"
            "La informiamo che VELUX ACTIVE è compatibile esclusivamente con reti Wi-Fi a 2.4 GHz."
            " Le reti a 5 GHz non sono supportate.\n\n"
            "Cordiali saluti,\nTeam VELUX"
        )
    }
]

def trova_risposta(domanda, canale="telefono"):
    domanda_lower = domanda.lower()
    for faq in faq_db:
        if any(kw in domanda_lower for kw in faq["keywords"]):
            return faq[canale]
    return (
        "Mi dispiace, non ho trovato una risposta automatica a questa domanda. Contatta il supporto tecnico o consulta la guida ufficiale."
        if canale == "telefono"
        else (
            "Gentile Cliente,\n\nnon abbiamo trovato una risposta automatica alla sua richiesta. "
            "La invitiamo a contattare il supporto tecnico VELUX per ulteriori dettagli.\n\nCordiali saluti,\nTeam VELUX"
        )
    )

# Interfaccia Streamlit
st.set_page_config(page_title="Supporto VELUX", page_icon="🔧")
st.title("🛠️ Tool di Supporto VELUX")

st.markdown("Inserisci una domanda dell'operatore e seleziona il tipo di risposta desiderata.")

domanda = st.text_input("Domanda dell'operatore")
canale = st.radio("Tipo di risposta", ["telefono", "email"])

if domanda:
    risposta = trova_risposta(domanda, canale)
    st.subheader("Risposta suggerita:")
    st.text_area("", risposta, height=200)
    st.code(risposta, language="text")
    st.button("📋 Copia risposta", on_click=st.experimental_set_query_params, args=({"copiato": "ok"},))
