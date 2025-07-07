import requests
from config.env import API_URL

def predict_premium(input_data: dict) -> dict:
    try:
        response = requests.post(f"{API_URL}/api/predict", json=input_data)
        result = response.json()

        if response.status_code == 200:
            return {"success": True, "data": result}
        else:
            return {"success": False, "error": f"API Error: {response.status_code}", "details": result}
    except requests.exceptions.ConnectionError:
        return {"success": False, "error": "❌ Could not connect to the FastAPI server."}