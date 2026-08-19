from src.analyzer import analyze_message, generate_explanation
from src.scoring import calculate_risk_score, get_risk_level
from src.url_analyzer import analyze_urls


message = """
URGENT!

Your account has been suspended due to suspicious activity.

Verify your account immediately using your security code.

Your payment failed. Update your credit card information
within 24 hours to restore access.

Verify your account:
http://192.168.1.20/login

Or visit:
https://bit.ly/abc123
"""


results = analyze_message(message)

url_results = analyze_urls(message)

score = calculate_risk_score(results, url_results)

risk_level = get_risk_level(score)

explanations = generate_explanation(results, url_results)


print("\n=== PHISHING AWARENESS ANALYZER ===\n")

print("Keyword analysis:")
print(results)

print("\nURL analysis:")
print(url_results)

print("\nRisk Score:", score)
print("Risk Level:", risk_level)

print("\nWhy is this message suspicious?")

for explanation in explanations:
    print("-", explanation)
    