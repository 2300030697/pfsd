from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ask', methods=['POST'])
def ask():
    user_message = request.json['message']
    # Here, you can add your chatbot logic or API call
    bot_response = "This is a placeholder response!"  # Replace with your bot's response
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)
