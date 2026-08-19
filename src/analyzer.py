from .rules import (
    URGENCY_KEYWORDS_EN,
    URGENCY_KEYWORDS_FR,
    CREDENTIAL_KEYWORDS_EN,
    CREDENTIAL_KEYWORDS_FR,
    THREAT_KEYWORDS_EN,
    THREAT_KEYWORDS_FR,
    PAYMENT_KEYWORDS_EN,
    PAYMENT_KEYWORDS_FR,
)


def analyze_message(message):
    message = message.lower()

    results = {
        "urgency": [],
        "credentials": [],
        "threats": [],
        "payment": [],
    }

    keywords = URGENCY_KEYWORDS_EN + URGENCY_KEYWORDS_FR

    for keyword in dict.fromkeys(keywords):
        if keyword in message:
            results["urgency"].append(keyword)

    keywords = CREDENTIAL_KEYWORDS_EN + CREDENTIAL_KEYWORDS_FR

    for keyword in dict.fromkeys(keywords):
        if keyword in message:
            results["credentials"].append(keyword)

    keywords = THREAT_KEYWORDS_EN + THREAT_KEYWORDS_FR

    for keyword in dict.fromkeys(keywords):
        if keyword in message:
            results["threats"].append(keyword)

    keywords = PAYMENT_KEYWORDS_EN + PAYMENT_KEYWORDS_FR

    for keyword in dict.fromkeys(keywords):
        if keyword in message:
            results["payment"].append(keyword)

    return results


def generate_explanation(results, url_results):
    reasons = []

    if results["urgency"]:
        reasons.append(
            "The message uses urgency to pressure the recipient into acting quickly."
        )

    if results["credentials"]:
        reasons.append(
            "The message contains credential or security-related requests."
        )

    if results["threats"]:
        reasons.append(
            "The message contains threats or consequences designed to create fear."
        )

    if results["payment"]:
        reasons.append(
            "The message contains payment or financial-related indicators."
        )

    if url_results["suspicious_urls"]:
        reasons.append(
            "The message contains URLs with suspicious characteristics."
        )

    if not reasons:
        reasons.append(
            "No major phishing indicators were detected."
        )

    return reasons

