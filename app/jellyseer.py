from .ntfy import send_ntfy_notification


def handle_jellyseer_notifications(data: dict):
    send_ntfy_notification(data)

