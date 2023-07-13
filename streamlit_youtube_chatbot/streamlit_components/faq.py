import streamlit as st


def faq():
    st.markdown(
        """
# FAQ
## Wie funktioniert der Gründungs-Bot?
Der Gründungs-Bot funktioniert, indem er zunächst das Transkript der YouTube-Videoserie "Existenzgründung Schritt für Schritt: Von der passenden Rechtsform bis zum Jahresabschluss" indiziert. Das Transkript wird in kleinere Teile zerlegt und in einem Vektorindex gespeichert, der semantische Suche und Abruf von relevantem Kontext ermöglicht. Dieser Prozess stellt sicher, dass die bereitgestellten Empfehlungen zur Unternehmensgründung präzise und aktuell sind.

## Sind die Gründungsempfehlungen 100% genau?
Obwohl ich den Anforderungen entsprechend konfiguriert wurde, um nur die Informationen wiederzugeben, die in der YouTube-Videoserie erklärt wurden, ist dies nur eine erste Implementierung (Minimum Viable Product, MVP). Für solche Produkte sind umfangreichere Tests erforderlich, um sicherzustellen, dass sie wie erwartet funktionieren. Daher kann ich keine 100%-ige Genauigkeit garantieren, dass der Bot immer vollständig genaue Ergebnisse liefert. Es wird empfohlen, alle bereitgestellten Informationen und Empfehlungen auf ihre Richtigkeit zu überprüfen.
"""
    )
