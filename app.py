from flask import Flask, request, render_template
import pickle
from flask_socketio import SocketIO, emit


app = Flask(__name__)
model = pickle.load(open('C:/Users/Admin/Documents/RandomForest-Prediction-Web-Application-master/model.pkl', 'rb'))
socketio = SocketIO(app)

def recommend_nutrition(probability):
    if probability > 70:
        return "Recommended diet: Reduce salt, reduce saturated fat, increase the intake of fruits and vegetables. Avoid fast food and sugar."
    elif 30 < probability <= 70:
        return  "Recommended diet: Reduce salt and fat intake, eat more fish, whole grains, and green vegetables."
    else:
        return "Recommended diet: Maintain a balanced diet, limit foods high in sugar and salt."

@app.route('/doctor')
def doctor_page():
    return render_template('doctor.html')

@socketio.on('user_message')
def handle_user_message(msg):
    print('User message: ' + msg)
    emit('new_question', msg, broadcast=True)

@socketio.on('doctor_response')
def handle_doctor_response(response):
    print('Doctor response: ' + response)
    emit('response', response, broadcast=True)

@app.route('/')
def Render():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    A = [float(x) for x in request.form.values()]
    
    model_probability = model.predict_proba([A])
    probability = model_probability[0][1] * 100
    prediction = "Probability of this user having Heart Disease is %0.2f%%" % probability
    nutrition_recommendation = recommend_nutrition(probability)

    return render_template('index.html', result=prediction, nutrition=nutrition_recommendation)



if __name__ == "__main__":
    socketio.run(app, debug=True)
