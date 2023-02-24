from flask import Flask, jsonify, request

from list_organization import list_organization

app = Flask(__name__)
# curl http://192.168.1.142:5555/give_organization
#curl http://266c-46-0-228-206.ngrok.io/give_organization
#curl http://127.0.0.1:5000/
#curl http://127.0.0.1:5000/give_organization
#curl http://127.0.0.1:5000/api/profile/get

#curl http://192.168.56.1:5555/api/profile/get


class SimpleIterator:
    def __init__(self, limit):
        self.limit = limit
        self.counter = 0

    def __next__(self):        
        if self.counter < self.limit:
            self.counter += 1      
            return self.counter             
        else:
            self.counter = 0
            return self.counter
     

@app.route("/give_organization")
def take_organization():
    return jsonify({"org_name":list_organization[next(s_iter1)]})



@app.route("/")
def hello():
    return jsonify({"Welcome" : "Hello, this is Flusk-stub"})

@app.route("/api/profile/get", methods=["POST"])
def api_profile_get():

    l = {
        "SYSTEM_PROFILE" : [
        {
            "SYSTEM" : "NOTES",
            "USE_CASE" : "UC 01 Просмотр записки",
            "JMETER_TAG" : "UC01",
            "INTENSIVITY" : 100,
        },
        {
            "SYSTEM" : "NOTES",
            "USE_CASE" : "UC 02 Удаление случайной записки",
            "JMETER_TAG" : "UC02",
            "INTENSIVITY" : 20,
        },
        {
            "SYSTEM" : "NOTES",
            "USE_CASE" : "UC 03 Изменение случайной записки",
            "JMETER_TAG" : "UC03",
            "INTENSIVITY" : 20,
        },
        {
            "SYSTEM" : "NOTES",
            "USE_CASE" : "UC 04 Создание новой записки",
            "JMETER_TAG" : "UC04",
            "INTENSIVITY" : 20,
        },
        {
            "SYSTEM" : "NOTES",
            "USE_CASE" : "UC 05 Проверка в Django admin",
            "JMETER_TAG" : "UC05",
            "INTENSIVITY" : 20,
        },

        ]
    }


    request_data = request.get_json()


    app_name = request_data["app"].upper()

    if app_name == "NOTES":
        return jsonify(l)





if __name__ == "__main__":
    
    list_organization = list_organization
    s_iter1 = SimpleIterator(len(list_organization)-1)
    app.run(host="192.168.1.142", port=5555, debug=False)
    # app.run(host="127.0.0.1", port=5555, debug=False)