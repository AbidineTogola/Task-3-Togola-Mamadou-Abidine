from src.analyzer import analyze_message


def test_urgency_detection():
    message = "URGENT! Act now!"

    result = analyze_message(message)

    assert "urgent" in result["urgency"]
    assert "act now" in result["urgency"]


def test_credential_detection():
    message = "Verify your account and enter your security code."

    result = analyze_message(message)

    assert "verify your account" in result["credentials"]
    assert "security code" in result["credentials"]


def test_threat_detection():
    message = "Your account is blocked because of suspicious activity."

    result = analyze_message(message)

    assert "suspicious activity" in result["threats"]


def test_payment_detection():
    message = "Your payment failed. Update your credit card."

    result = analyze_message(message)

    assert "payment failed" in result["payment"]
    assert "credit card" in result["payment"]


def test_legitimate_message():
    message = "Hello, the meeting is scheduled for tomorrow at 10 AM."

    result = analyze_message(message)

    assert result["urgency"] == []
    assert result["credentials"] == []
    assert result["threats"] == []
    assert result["payment"] == []
    