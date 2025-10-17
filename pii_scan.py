"""PII Scan"""

import re
import logging
import spacy
import requests
from presidio_analyzer import AnalyzerEngine, RecognizerRegistry, RecognizerResult, PatternRecognizer, Pattern
from presidio_analyzer.predefined_recognizers import (
    ItDriverLicenseRecognizer,
    ItVatCodeRecognizer,
    ItFiscalCodeRecognizer,
    ItIdentityCardRecognizer,
    ItPassportRecognizer,
    EsNieRecognizer,
    EsNifRecognizer,
    PlPeselRecognizer,
    FiPersonalIdentityCodeRecognizer,
    AbaRoutingRecognizer,
    AuAbnRecognizer,
    AuAcnRecognizer,
    AuMedicareRecognizer,
    AuTfnRecognizer,
    InAadhaarRecognizer,
    InPanRecognizer,
    InPassportRecognizer,
    InVehicleRegistrationRecognizer,
    InVoterRecognizer,
    UkNinoRecognizer
)
from presidio_anonymizer import AnonymizerEngine

# -----------------------------
# Load spaCy model
# -----------------------------
try:
    nlp = spacy.load("en_core_web_lg")
except OSError:
    from spacy.cli import download
    download("en_core_web_lg")
    nlp = spacy.load("en_core_web_lg")

# -----------------------------
# Logging
# -----------------------------
logging.basicConfig(level=logging.CRITICAL)

# -----------------------------
# Presidio Analyzer and Registry
# -----------------------------
registry = RecognizerRegistry()
registry.load_predefined_recognizers()

# Add additional English recognizers
english_recognizers = [
    ItDriverLicenseRecognizer,
    ItVatCodeRecognizer,
    ItFiscalCodeRecognizer,
    ItIdentityCardRecognizer,
    ItPassportRecognizer,
    EsNieRecognizer,
    EsNifRecognizer,
    PlPeselRecognizer,
    FiPersonalIdentityCodeRecognizer,
    AbaRoutingRecognizer,
    AuAbnRecognizer,
    AuAcnRecognizer,
    AuMedicareRecognizer,
    AuTfnRecognizer,
    InAadhaarRecognizer,
    InPanRecognizer,
    InPassportRecognizer,
    InVehicleRegistrationRecognizer,
    InVoterRecognizer,
    UkNinoRecognizer
]

for rec in english_recognizers:
    registry.add_recognizer(rec(supported_language='en'))

# Create the analyzer and anonymizer engines
analyzer = AnalyzerEngine()
anonymizer = AnonymizerEngine()

# -----------------------------
# Custom MEDICAL_LICENSE recognizer
# -----------------------------
from presidio_analyzer import PatternRecognizer, Pattern

# Only add if it doesn’t already exist
if not any(getattr(r, "supported_entity", None) == "MEDICAL_LICENSE" for r in analyzer.registry.recognizers):
    license_pattern = Pattern(
        name="MEDICAL_LICENSE",
        regex=r"MD\d{6}",  # matches MD followed by 6 digits
        score=0.85
    )
    license_recognizer = PatternRecognizer(
        supported_entity="MEDICAL_LICENSE",
        patterns=[license_pattern]
    )
    analyzer.registry.add_recognizer(license_recognizer)


# -----------------------------
# Functions
# -----------------------------
def show_aggie_pride() -> str:
    """Return Aggie Pride string"""
    return "Aggie Pride - Worldwide"


def analyze_text(text: str, entity_list: list, show_supported=False) -> list[RecognizerResult]:
    """
    Analyze the text using the specified entity list
    """
    if show_supported:
        return analyzer.get_supported_entities()

    results = analyzer.analyze(
        text=text,
        entities=entity_list,
        language='en'
        # Removed return_decision_process=True to avoid hanging
    )
    return results


def anonymize_text(text: str, entity_list: list) -> str:
    """
    Anonymize the text using the entity list
    """
    results = analyze_text(text, entity_list)
    anonymized_text = anonymizer.anonymize(text=text, analyzer_results=results)
    return anonymized_text.text


def anonymize_data(data: list) -> None:
    """
    Print anonymized data line by line
    """
    for i, item in enumerate(data):
        if item:
            if item.startswith('#'):
                print(item)
            else:
                print(f'ID:{i}:Original  : {item}')
                print(f'ID:{i}:Anonymized: {anonymize_text(item, [])}')


def read_data() -> list:
    """
    Reads data from a secure file using a secret key stored in .env
    """
    with open('.env', encoding='utf-8') as f:
        for line in f.readlines():
            m = re.search(r'SECRET="(\w+)"', line)
            if m:
                secret = m.group(1)
                break
        else:
            raise RuntimeError("SECRET not found in .env file")

    url = f'https://drive.google.com/uc?export=download&id=1Madj8otKjwwOO353nL_{secret}'
    response = requests.get(url, timeout=10)
    return response.text.split('\n')


# -----------------------------
# Main
# -----------------------------
if __name__ == '__main__':
    print(show_aggie_pride())
