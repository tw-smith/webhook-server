import requests

def send_ntfy_notification(seer_data: dict):
    base_url =  "https://ntfy.tw-smith.me/"
    requested_by = seer_data.get("request").get("requestedBy_username")
    body = get_ntfy_body(seer_data)
    headers = get_ntfy_headers(seer_data)

    requests.post(base_url + requested_by, body, headers=headers)

def get_ntfy_headers(seer_data: dict) -> dict:
    headers = {}
    subject_prefix = ""

    match seer_data.get("notification_type"):
        case "MEDIA_AVAILABLE":
            subject_prefix = "Media available: "
        case "MEDIA_APPROVED", "MEDIA_AUTO_APPROVED":
            subject_prefix = "Request approved: "
        case "MEDIA_FAILED":
            subject_prefix = "Request failed: "

    match seer_data.get("media").get("media_type"):
        case "movie":
            headers["Tags"] = "film_strip"
        case "tv":
            headers["Tags"] = "tv"

    headers["Title"] = subject_prefix + seer_data.get("subject")

    return headers

def get_ntfy_body(seer_data: dict) -> dict:

    body = seer_data.get("message")

    return body