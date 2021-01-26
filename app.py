from flask import Flask, request, jsonify, json
from flask_cors import CORS
import requests
import json
from werkzeug.routing import Rule

app = Flask(__name__)

CORS(app)
cors = CORS(app, resources={
    
    r"/*":{
        "origins":"*"
        
        }
    })

@app.route('/')
def hello_world():
    return 'Hello, World!'

uri_qreply = 'https://chat-api.one.th/message/api/v1/push_quickreply'

headers = {
    'Authorization' : 'Bearer Add65f8aea8b8595aa717ec129b1d2dc4fe842b4814574fcc8a4f07e390cc92d2ea5eb8d77cfd45a794acbd219238a556',
    'Content-Type': 'application/json'
    }

payload = {
            "to": "Ufec99da535c25806a92219d2c0ebf86c",
            "bot_id" : "B5c0f69562f9c564cb4faf72b61dfc998",
            "message" : "การตอบกลับอัตโนมัติ",
            "quick_reply" : [{
                            "label" : "ลงทะเบียน1",
                            "type" : "text",
                            "message" : "ฉันต้องการลงทะเบียน",
                            "payload" : { "keyword": "Register", "service": "001" }
    },{
                            "label" : "ลงทะเบียน2",
                            "type" : "text",
                            "message" : "ฉันต้องการลงทะเบียน",
                            "payload" : { "keyword": "Register", "service": "001" }
    }]
}

@app.route('/webhook', methods=['GET','POST'])
def webhook():
            data = request.json
            print(data)
            print("---------------------------------------")
            # r = requests.post(uri_qreply, data=json.dumps(payload), headers=headers)
            # print ("response data from bot ====> ", r)
            return 'success' , 200

         




if __name__ == "__main__":
    #  app.run(debug=True)
     app.run(host="0.0.0.0", port="5050")