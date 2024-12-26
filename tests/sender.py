import requests
import json

def send_payload(url, payload):
    headers = {'Content-Type': 'application/json'}
    response = requests.post(url, json=payload, headers=headers)
    # return response.status_code, response.json()
    
    return response.status_code, response.text

def load_json_file(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

# Example usage
if __name__ == "__main__":
    url = "http://13.49.221.50:8080/payload"
    file_path = "C:\\Users\\Moran\\repos\\home-exam\\tests\\example.json"
    payload = load_json_file(file_path)
    payload_str=json.dumps(payload)
    status_code, response = send_payload(url, payload)
    print(f"Status Code: {status_code}")
    print(f"Response: {response}")