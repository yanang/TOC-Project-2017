import sys
from io import BytesIO

import telegram
from flask import Flask, request, send_file

from fsm import TocMachine


API_TOKEN = '318702613:AAGaEL6D6WAz7-ErNiL4e67rLMYY4KrL1uw'
WEBHOOK_URL = 'https://7e4c17c2.ngrok.io/hook'

app = Flask(__name__)
bot = telegram.Bot(token=API_TOKEN)
machine = TocMachine(
    states=[
        'user',
        'pos0',
        'pos1',
        'pos2',
        'pos3',
        'pos4',
        'neg0',
        'none'
    ],
    transitions=[
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'pos0',
            'conditions': 'is_going_to_pos0'
        },
        {
            'trigger': 'advance',
            'source': 'pos0',
            'dest': 'pos1',
            'conditions': 'is_going_to_pos1'
        },
        {
            'trigger': 'advance',
            'source': 'pos1',
            'dest': 'pos2',
            'conditions': 'is_going_to_pos2'
        },
        {
            'trigger': 'advance',
            'source': 'pos1',
            'dest': 'pos3',
            'conditions': 'is_going_to_pos3'
        },
        {
            'trigger': 'advance',
            'source': 'pos1',
            'dest': 'pos4',
            'conditions': 'is_going_to_pos4'
        },
        {
            'trigger': 'advance',
            'source': 'user',
            'dest': 'neg0',
            'conditions': 'is_going_to_neg0'
        },
        {
            'trigger': 'advance',
            'source': 'pos1',
            'dest': 'neg0',
            'conditions': 'is_going_to_neg0_from'
        },
        {
            'trigger': 'advance',
            'source': [
                'user',
                'pos1'
            ],
            'dest': 'none',
            'conditions': 'is_going_to_none'
        },
        {
            'trigger': 'go_back_user',
            'source': [
                'none',
                'pos2',
                'pos3',
                'pos4',
                'neg0'
            ],
            'dest': 'user'
        }
    ],
    initial='user',
    auto_transitions=False,
    show_conditions=True,
)


def _set_webhook():
    status = bot.set_webhook(WEBHOOK_URL)
    if not status:
        print('Webhook setup failed')
        sys.exit(1)
    else:
        print('Your webhook URL has been set to "{}"'.format(WEBHOOK_URL))


@app.route('/hook', methods=['POST'])
def webhook_handler():
    update = telegram.Update.de_json(request.get_json(force=True), bot)
    print(update.message.text)
    machine.advance(update)
    return 'ok'


@app.route('/show-fsm', methods=['GET'])
def show_fsm():
    byte_io = BytesIO()
    machine.graph.draw(byte_io, prog='dot', format='png')
    byte_io.seek(0)
    return send_file(byte_io, attachment_filename='fsm.png', mimetype='image/png')


if __name__ == "__main__":
    _set_webhook()
    app.run()
