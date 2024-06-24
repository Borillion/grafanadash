import json
from grafanalib.core import Dashboard
from grafanalib._gen import DashboardEncoder

from dashboard_definitions import dashboard
from dashboard_utils import get_dashboard_json

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

def main():
    dashboard_json = get_dashboard_json(dashboard, overwrite=True)
    with open('dashboard.json', 'w') as f:
        f.write(dashboard_json)
    print("Dashboard JSON generated and saved to dashboard.json")

if __name__ == "__main__":
    main()
