import re
import ipaddress
from urllib.parse import urlparse


URL_SHORTENERS = {
    "bit.ly",
    "tinyurl.com",
    "t.co",
    "goo.gl",
    "ow.ly",
    "is.gd",
    "buff.ly",
    "cutt.ly",
}


def extract_urls(message):
    """Extract URLs from a message."""

    url_pattern = r"https?://[^\s<>\"]+"

    return re.findall(url_pattern, message)


def is_ip_address(hostname):
    """Check whether the hostname is an IPv4 or IPv6 address."""

    if not hostname:
        return False

    try:
        ipaddress.ip_address(hostname)
        return True

    except ValueError:
        return False


def analyze_url(url):
    """Analyze a single URL and return suspicious indicators."""

    red_flags = []

    parsed = urlparse(url)

    hostname = parsed.hostname

    if not hostname:
        red_flags.append("Invalid or missing hostname")
        return red_flags

    if parsed.scheme.lower() == "http":
        red_flags.append("HTTP instead of HTTPS")

    if is_ip_address(hostname):
        red_flags.append("IP address used instead of domain")

    if hostname.lower() in URL_SHORTENERS:
        red_flags.append("URL shortener detected")

    if parsed.username:
        red_flags.append("Username embedded in URL")

    if len(url) > 150:
        red_flags.append("Unusually long URL")

    if "@" in url:
        red_flags.append("@ character used in URL")

    return red_flags


def analyze_urls(message):
    """Extract and analyze all URLs in a message."""

    urls = extract_urls(message)

    suspicious_urls = []
    red_flags = []

    for url in urls:

        flags = analyze_url(url)

        if flags:
            suspicious_urls.append(url)

            for flag in flags:

                if flag not in red_flags:
                    red_flags.append(flag)

    return {
        "urls": urls,
        "suspicious_urls": suspicious_urls,
        "red_flags": red_flags,
    }