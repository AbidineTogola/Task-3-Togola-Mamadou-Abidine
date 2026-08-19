from src.url_analyzer import analyze_urls


def test_http_url():
    message = "Visit http://example.com/login"

    result = analyze_urls(message)

    assert "http://example.com/login" in result["urls"]
    assert "HTTP instead of HTTPS" in result["red_flags"]


def test_ip_url():
    message = "Visit http://192.168.1.20/login"

    result = analyze_urls(message)

    assert "IP address used instead of domain" in result["red_flags"]


def test_shortened_url():
    message = "Click https://bit.ly/abc123"

    result = analyze_urls(message)

    assert "URL shortener detected" in result["red_flags"]


def test_no_url():
    message = "Hello, see you tomorrow."

    result = analyze_urls(message)

    assert result["urls"] == []
    assert result["suspicious_urls"] == []
    assert result["red_flags"] == []
