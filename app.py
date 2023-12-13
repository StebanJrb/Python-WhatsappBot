from flask import Flask, request 
import sett
import services

app = Flask(__name__)

@app.route('/Welcome', methods={'GET'})
def Welcome():
    return 'Vertice Universal Bot on Flask'

@app.route('/webhook', methods={'GET'})
def verify_token():
    try:
        token = request.args.get('hub.verify_token')
        challenge =request.args.get('hub.challenge')

        if token == sett.token and challenge != None:
            return challenge
        else:
            return '..:: Incorrect token',403
    except Exception as e:
        return e,403
     
@app.route('/webhook', methods= {'POST'})
def recieve_messages():
    try:
        body = request.get_json()
        entry = body['entry'][0]
        changes = entry['changes'][0]
        value = changes['value']
        message = value['messages'][0]
        number = message['from']
        messageId = message['id']
        contacts = value['contacts'][0]
        name = contacts['profile']['name']
        text = services.get_whatsapp_message(message)
        services.chat_administrator(text, number, messageId, name)
        return '..:: Sended',200
    except Exception as e:
        return '..:: Didnt sended: '+ str(e) ,403

if __name__ == '__main__':
    app.run()
