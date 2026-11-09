from urllib.parse import urlparse
import ipaddress


def analyze_url(url):

    parsed_url = urlparse(url)
    hostname = parsed_url.hostname

    results = []

    # Check 1: Identify IP addresses
    try:
        ipaddress.ip_address(hostname)
        uses_ip_address = True
    except (ValueError, TypeError):
        uses_ip_address = False

    # Check 2: Identify HTTPS
    if parsed_url.scheme == "https":
        results.append("This URL uses HTTPS.")
    else:
        results.append(
            "Warning: This URL does not use HTTPS. "
            "Why this matters: Information exchanged with the website "
            "is not protected by HTTPS encryption."
        )

    # Check 3: Identify IP addresses
    if uses_ip_address:
        results.append(
            "Warning: This URL uses an IP address instead of a domain name. "
            "Why this matters: It can be harder to verify who operates "
            "the destination."
        )
    else:
        results.append("This URL uses a domain name.")

    # Check 4: Identify unusually long URLs
    if len(url) > 100:
        results.append(
            "Warning: This URL is unusually long. "
            "Why this matters: Long URLs can make the destination "
            "and link structure harder to inspect."
        )
    else:
        results.append("This URL is within the expected length range.")

    # Check 5: Identify username information in URL
    if parsed_url.username is not None:
        results.append(
            "Warning: This URL contains username information before the hostname. "
            "Why this matters: Text before the @ symbol can make a link "
            "appear to belong to a different website."
        )
    else:
        results.append("No username information detected in the URL.")

    # Check 6: Identify URL shorteners
    shorteners = [
        "bit.ly",
        "tinyurl.com",
        "t.co",
        "is.gd",
        "ow.ly",
        "buff.ly",
        "rebrand.ly",
        "cutt.ly",
        "shorturl.at"
    ]

    if hostname and hostname.lower() in shorteners:
        results.append(
            "Warning: This link uses a URL shortening service. "
            "Its destination may be hidden. "
            "Why this matters: You may not know where the link leads "
            "before opening it."
        )
    else:
        results.append("No recognized URL shortener detected.")

    # Check 7: Identify uncommon domain endings
    suspicious_endings = ["xyz", "top", "click"]

    domain_ending = hostname.lower().split(".")[-1] if hostname else ""

    if domain_ending in suspicious_endings:
        results.append(
            "Warning: This URL uses a domain ending that should be reviewed. "
            "Why this matters: Some suspicious websites use these endings, "
            "but the ending alone does not prove a website is malicious."
        )
    else:
        results.append("No flagged domain ending detected.")

    return results