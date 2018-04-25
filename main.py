import json
import logging
import os

from flask import Flask, jsonify, request
from libs import json_response
import requests

app = Flask(__name__)

# def json_response(func):
#     def func_wrapper(*args, **kwargs):
#         return jsonify(func(*args, **kwargs))
#     return func_wrapper

@app.route("/")
def hello():
    # Handle POST data
    # Logic
    # Response
    return "Hello World!"

# @app.route("/items")
# # @json_response
# def items_list():
#     return jsonify(["Item 1", "Item 2", "Item 3"])

@app.route("/items")
@json_response()
def items_list():
    return ["Item 1", "Item 2", "Item 3"]

# @json_response
# def other_func(argument4, argument2):
#     return 'blah'

@app.route("/echo", methods=['POST'])
@json_response()
def echo():
    # Return submitted data
    data = request.get_json()

    return data

@app.route("/send_skype_message", methods=['GET', 'POST'])
def send_skype_message():
    # Use API key to send skype message
    conversation_id = '19:da94633601ae4ce09181fb7107489afc@thread.skype'
    endpoint = 'https://0yw7gtq5ol.execute-api.ap-northeast-1.amazonaws.com/production/conversations/%s/messages' % conversation_id
    api_key = 'n4ni77wsMh7O6ST0YEMzP7RChvCCv6pJ8RdH4dzX'
    message = 'MU vo doi'

    # GET /conversation
    # GET /conversation/{id}
    # POST /conversation/{id}/messages
    res = requests.post(
        endpoint,
        headers={'X-Api-Key': api_key},
        data={'message': message}
    )

    return message

@app.route("/load_messages", methods=['GET'])
def load_message():
    return ''

# @app.route("/send_message_v2", methods=['GET', 'POST'])
# def send_skype_message():
#     endpoint = 'https://0yw7gtq5ol.execute-api.ap-northeast-1.amazonaws.com/production/'
#     conversation_id = '19:da94633601ae4ce09181fb7107489afc@thread.skype'
#     api_key = 'n4ni77wsMh7O6ST0YEMzP7RChvCCv6pJ8RdH4dzX'
#     message = 'MU vo doi - chi phoi toan cau'
#
#     res = requests.post(
#         endpoint + conversation_id + '/messages',
#         headers={'X-Api-Key': api_key, 'Content-Type': 'application/json'},
#         data = json.dump({'message': message})
#     )
#
#     return res.text




@app.route("/move_trello_card_to_deployable", methods=['GET', 'POST'])
def move_trello_card_to_deployable():
    endpoint = 'https://api.trello.com/1/'
    card_id = 'lPolRuD7'
    done_list_id = '5add6f546d5899db1df229ef'
    doing_list_id = '5add6f546d5899db1df229ee'
    todo_list_id = '5add6f546d5899db1df229ed'

    key = os.environ.get('TRELLO_API_KEY')
    token = os.environ.get('TRELLO_API_TOKEN')

    url = endpoint + 'cards/' + card_id + '/idList'

    res = requests.put(
        url,
        params={'value': done_list_id,
                'key': key,
                'token': token},
    )

    return app.response_class(
        response=res.text,
        status=200,
        mimetype='application/json'
    )


@app.route('/bitbucket', methods=['POST'])
def bitbucket():
    logging.info(request.get_json())
    # Use API key to send skype message
    conversation_id = '19:da94633601ae4ce09181fb7107489afc@thread.skype'
    endpoint = 'https://0yw7gtq5ol.execute-api.ap-northeast-1.amazonaws.com/production/conversations/%s/messages' % conversation_id
    api_key = 'n4ni77wsMh7O6ST0YEMzP7RChvCCv6pJ8RdH4dzX'
    message = 'MU vo doi'
    data_test = request.get_json()

    res = requests.post(
        endpoint,
        headers={'X-Api-Key': api_key},
        data={'message': data_test['actors']['username']}
    )

    return data_test['actors']['username']

