from app import app
from dash.testing.application_runners import import_app

# 1. Test that the header is present
def test_header_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("h1", timeout=10)
    header_text = dash_duo.find_element("h1").text
    assert header_text == "Soul Foods Sales Visualiser"

# 2. Test that the visualisation (graph) is present
def test_visualization_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#sales-line-chart", timeout=10)
    assert dash_duo.find_element("#sales-line-chart")

# 3. Test that the region picker is present
def test_region_picker_exists(dash_duo):
    dash_duo.start_server(app)
    dash_duo.wait_for_element("#region_selector", timeout=10)
    assert dash_duo.find_element("#region_selector")