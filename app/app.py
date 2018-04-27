from flask import Flask, request,jsonify

app = Flask(__name__)
user_list = []
@app.route('/auth/signup', methods=['POST'])
def signup():
    new_user_data = request.get_json()
    new_user = {}
    new_user['username'] = new_user_data['username']
    new_user['password'] = new_user_data['password']
    user_list.append(new_user)
    return jsonify({'Users': user_list}),201

@app.route('/auth/login', methods=['POST'])
def login():
    login_data = request.get_json()
    for user in  user_list:
        if user['username'] == login_data['username'] and user['password'] == login_data['password']:
            return jsonify({"message":"logged in"}),200
        return jsonify({"message": "Either password or username is invallid"}),400
    return jsonify({"message": "not found"})

@app.route('/meals/',methods= ['GET', 'POST'])
def meals():
    if request.method == 'POST':
        return jsonify({"message": "meall added"}),201
    else:
        return jsonify({"message": "All meals"}),200


if __name__ == '__main__':
    app.run(debug=True)
