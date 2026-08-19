def calculate_risk_score(results, url_results=None):
    score = 0

    score += len(results["urgency"]) * 1
    score += len(results["credentials"]) * 2
    score += len(results["threats"]) * 3
    score += len(results["payment"]) * 2

    if url_results:
        score += calculate_url_score(url_results)

    return score


def calculate_url_score(url_results):
    score = 0

    for flag in url_results["red_flags"]:

        if flag == "HTTP instead of HTTPS":
            score += 1

        elif flag == "IP address used instead of domain":
            score += 3

        elif flag == "URL shortener detected":
            score += 2

        elif flag == "Username embedded in URL":
            score += 3

        elif flag == "@ character used in URL":
            score += 3

        elif flag == "Unusually long URL":
            score += 1

        elif flag == "Invalid or missing hostname":
            score += 3

    return score


def get_risk_level(score):

    if score <= 4:
        return "Low"

    elif score <= 9:
        return "Medium"

    elif score <= 19:
        return "High"

    else:
        return "Critical"