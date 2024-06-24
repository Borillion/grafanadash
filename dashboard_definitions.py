from grafanalib.core import Dashboard, TimeSeries, Target, GridPos

dashboard = Dashboard(
    title="Minimal Dashboard",
    timezone="browser",
    panels=[
        TimeSeries(
            title="Simple Time Series",
            dataSource='default',  # Replace with your data source name or UID
            targets=[
                Target(
                    expr='up',  # Example expression for Prometheus
                ),
            ],
        ),
    ],
).auto_panel_ids()
