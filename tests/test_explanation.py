from src.analyzer import generate_explanation


def test_phishing_explanation():
    results = {
        "urgency": ["urgent"],
        "credentials": ["verify your account"],
        "threats": ["suspicious activity"],
        "payment": ["credit card"],
    }

    url_results = {
        "urls": ["http://192.168.1.20/login"],
        "suspicious_urls": ["http://192.168.1.20/login"],
        "red_flags": ["HTTP instead of HTTPS"],
    }

    explanations = generate_explanation(results, url_results)

    assert len(explanations) == 5


def test_no_phishing_indicators():
    results = {
        "urgency": [],
        "credentials": [],
        "threats": [],
        "payment": [],
    }

    url_results = {
        "urls": [],
        "suspicious_urls": [],
        "red_flags": [],
    }

    explanations = generate_explanation(results, url_results)

    assert explanations == [
        "No major phishing indicators were detected."
    ]
