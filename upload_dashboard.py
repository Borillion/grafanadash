import json
import requests
from os import getenv
from dashboard_definitions import dashboard
from dashboard_utils import get_dashboard_json

def upload_to_grafana(json_data, server, api_key, verify=True):
    headers = {'Authorization': f"Bearer {api_key}", 'Content-Type': 'application/json'}
    response = requests.post(f"https://{server}/api/dashboards/db", data=json_data, headers=headers, verify=verify)
    print(f"{response.status_code} - {response.content}")

def main():
    grafana_api_key = getenv("GRAFANA_API_KEY")
    grafana_server = getenv("GRAFANA_SERVER")

    with open('dashboard.json', 'r') as f:
        dashboard_json = f.read()

    if grafana_api_key and grafana_server:
        upload_to_grafana(dashboard_json, grafana_server, grafana_api_key)
    else:
        print("Grafana API key or server not provided. Skipping upload.")

if __name__ == "__main__":
    main()
