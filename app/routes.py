from app import app
from flask import request, json
from .jellyseer import handle_jellyseer_notifications

@app.route('/')
@app.route('/notifications/jellyseer', methods=['POST'])
def handle_jellyseer_webhook():
    data = json.loads(request.data)

    handle_jellyseer_notifications(data)


    return data