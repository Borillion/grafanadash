from os import getenv
from dashboard_definitions import dashboard
from dashboard_utils import get_dashboard_json, upload_to_grafana, dashboard_exists

def main():
    # Define the dashboard UID (this should be unique and consistent)
    dashboard_uid = 'minimal-dashboard'

    # Fetch Grafana API credentials from environment variables
    grafana_api_key = getenv("GRAFANA_API_KEY")
    grafana_server = getenv("GRAFANA_SERVER")

    # Step 1: Generate the dashboard JSON
    dashboard_json = get_dashboard_json(dashboard, overwrite=True)

    # Save the JSON to a file
    with open('dashboard.json', 'w') as f:
        f.write(dashboard_json)
    print("Dashboard JSON generated and saved to dashboard.json")

    # Print the JSON content
    print("Dashboard JSON content:")
    print(dashboard_json)

    if grafana_api_key and grafana_server:
        # Step 2: Check if the dashboard exists
        if dashboard_exists(grafana_server, grafana_api_key, dashboard_uid):
            print("Dashboard exists. Updating the existing dashboard.")
        else:
            print("Dashboard does not exist. Creating a new dashboard.")

        # Step 3: Upload the dashboard to Grafana
        upload_to_grafana(dashboard_json, grafana_server, grafana_api_key)
    else:
        print("Grafana API key or server not provided. Skipping upload.")

if __name__ == "__main__":
    main()
