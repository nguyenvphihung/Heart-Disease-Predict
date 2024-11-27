# Heart Disease Prediction Web Application

This is a web application that predicts the probability of a user having heart disease using a pre-trained RandomForest model. The application also recommends a nutrition plan based on the prediction result and includes a real-time chat feature that allows users to communicate with doctors.

## Features
- **Heart Disease Prediction**: Users can input health-related data, and the application will predict the probability of heart disease.
- **Nutrition Recommendation**: Based on the probability of heart disease, the application provides a nutrition recommendation to help users manage their health.
- **Real-time Doctor Chat**: Users can communicate with doctors via a real-time chat interface powered by SocketIO.

## Project Structure
The main files and directories in this project are:
- `app.py`: The main Flask application that handles requests, predictions, and real-time chat.
- `model.pkl`: The pre-trained RandomForest model used to predict heart disease.
- `templates/`: Contains the HTML templates used in the application.
  - `index.html`: The main page where users input their data and receive predictions.
  - `doctor.html`: The page where users can chat with doctors.
- `static/`: Contains static files (CSS, JavaScript) used in the application.
- `requirements.txt`: Lists the Python dependencies required for the project.

## Setup Instructions

### Prerequisites
- Python 3.x
- Flask
- Flask-SocketIO
- Pickle (for loading the pre-trained model)

### Step-by-Step Guide

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nguyenvphihung/Heart-Disease-Prediction.git

Dưới đây là phần hướng dẫn sử dụng mà bạn có thể thêm vào file `README.md`:  

---

## Usage Instructions  

### 1. Run the Application  
After setting up the project by following the setup instructions:  
- Navigate to the project directory.  
- Start the Flask application by running:  
  ```bash  
  python app.py  
  ```  
- Open a web browser and go to: `http://127.0.0.1:5000`  

### 2. Use the Features  

#### Heart Disease Prediction  
1. On the main page (`index.html`), enter the required health data in the input fields.  
2. Click the "Predict" button to get the probability of having heart disease.  

#### Nutrition Recommendation  
- Based on the prediction results, the application will provide dietary suggestions to help manage your health.  

#### Real-time Doctor Chat  
1. Navigate to the "Chat with a Doctor" page (`doctor.html`).  
2. Use the real-time chat interface to communicate directly with a doctor for further assistance.  

