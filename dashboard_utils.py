import json
from grafanalib.core import Dashboard
from grafanalib._gen import DashboardEncoder

def get_dashboard_json(dashboard, overwrite=False, message="Updated by grafanalib"):
    '''
    Generates JSON from grafanalib Dashboard object

    :param dashboard - Dashboard() created via grafanalib
    '''
    return json.dumps(
        {
            "dashboard": dashboard.to_json_data(),
            "overwrite": overwrite,
            "message": message
        }, sort_keys=True, indent=2, cls=DashboardEncoder)

def upload_to_grafana(json_data, server, api_key, verify=True):
    '''
    Uploads dashboard JSON to Grafana and prints the response

    :param json_data - dashboard json generated by grafanalib
    :param server - grafana server name
    :param api_key - grafana api key with read and write privileges
    '''
    headers = {'Authorization': f"Bearer {api_key}", 'Content-Type': 'application/json'}
    response = requests.post(f"https://{server}/api/dashboards/db", data=json_data, headers=headers, verify=verify)
    print(f"{response.status_code} - {response.content}")

def dashboard_exists(server, api_key, uid):
    '''
    Checks if a dashboard with the given UID exists in Grafana

    :param server - grafana server name
    :param api_key - grafana api key with read and write privileges
    :param uid - dashboard UID
    '''
    headers = {'Authorization': f"Bearer {api_key}"}
    response = requests.get(f"https://{server}/api/dashboards/uid/{uid}", headers=headers)
    return response.status_code == 200