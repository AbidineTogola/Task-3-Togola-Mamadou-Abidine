from src.scoring import calculate_risk_score, get_risk_level


def test_risk_score():
    results = {
        "urgency": ["urgent", "immediately"],
        "credentials": ["verify your account"],
        "threats": ["suspicious activity"],
        "payment": ["payment failed"],
    }

    score = calculate_risk_score(results)

    assert score == 9


def test_url_risk_score():
    results = {
        "urgency": [],
        "credentials": [],
        "threats": [],
        "payment": [],
    }

    url_results = {
        "urls": ["http://192.168.1.20/login"],
        "suspicious_urls": ["http://192.168.1.20/login"],
        "red_flags": [
            "HTTP instead of HTTPS",
            "IP address used instead of domain",
        ],
    }

    score = calculate_risk_score(results, url_results)

    assert score == 4


def test_risk_level():
    assert get_risk_level(0) == "Low"
    assert get_risk_level(4) == "Low"

    assert get_risk_level(5) == "Medium"
    assert get_risk_level(9) == "Medium"

    assert get_risk_level(10) == "High"
    assert get_risk_level(19) == "High"

    assert get_risk_level(20) == "Critical"
    assert get_risk_level(22) == "Critical"