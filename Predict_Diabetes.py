import json
import requests

def predict_diabetes(BMI, Age, Glucose):
    url = 'http://127.0.0.1:8000/diabetes/v1/predict'

    # Convert inputs to numeric values (float or int)
    try:
        BMI = float(BMI)
        Age = int(Age)
        Glucose = float(Glucose)
    except ValueError:
        print("Error: Please ensure all inputs are numeric.")
        return None

    data = {"BMI": BMI, "Age": Age, "Glucose": Glucose}
    data_json = json.dumps(data)
    headers = {'Content-Type': 'application/json'}    

    response = requests.post(url, data=data_json, headers=headers)

    # Debugging response
    print(f"Response Status Code: {response.status_code}")
    print(f"Request URL: {response.url}")
    
    if response.status_code == 200:
        try:
            result = response.json()
            return result
        except json.JSONDecodeError:
            print("Error: Unable to decode the response as JSON.")
            return None
    else:
        print(f"Error: Received status code {response.status_code}")
        return None

if __name__ == "__main__":
    BMI = input('Enter BMI: ')
    Age = input('Enter Age: ')
    Glucose = input('Enter Glucose: ')
    
    # Predicting diabetes
    predictions = predict_diabetes(BMI, Age, Glucose)
    
    if predictions:
        print("Diabetic" if predictions["prediction"] == 1 else "Not Diabetic")
        print("Confidence: " + str(predictions["confidence"]) + "%")
    else:
        print("No prediction available due to an error.")    