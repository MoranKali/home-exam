import requests
import json

def send_payload(url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    return response.status_code, response.json()

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Example usage
if __name__ == "__main__":
    url = "http://13.61.5.154:8080//payload"
    file_path = "C:\\Users\\Moran\\repos\\home-exam\\tests\\example_no_token.json"
    payload = load_json_file(file_path)
    status_code, response = send_payload(url, payload)
    print(f"Status Code: {status_code}")
    print(f"Response: {response}")