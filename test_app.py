"""
Test suite for the Soul Foods Sales Visualiser Dash app.

Uses the standard Dash testing framework (dash.testing) which spins up the
real app in a browser via Selenium. Run with:

    pytest test_app.py

These tests verify that the three key parts of the dashboard render:
    1. the header,
    2. the visualisation (graph), and
    3. the region picker.
"""

from dash.testing.application_runners import import_app


def test_header_is_present(dash_duo):
    """The dashboard header should render with the expected title text."""
    app = import_app("app")
    dash_duo.start_server(app)

    # Wait for the H1 header element to appear in the DOM.
    header = dash_duo.wait_for_element("h1", timeout=10)

    assert header is not None
    assert header.text == "Soul Foods Sales Visualiser"


def test_visualisation_is_present(dash_duo):
    """The sales line chart (dcc.Graph) should render on the page."""
    app = import_app("app")
    dash_duo.start_server(app)

    # The dcc.Graph has id="sales-graph"; wait for it to be drawn.
    graph = dash_duo.wait_for_element("#sales-graph", timeout=10)

    assert graph is not None


def test_region_picker_is_present(dash_duo):
    """The region radio-button picker (dcc.RadioItems) should render."""
    app = import_app("app")
    dash_duo.start_server(app)

    # The dcc.RadioItems has id="region-filter".
    region_picker = dash_duo.wait_for_element("#region-filter", timeout=10)

    assert region_picker is not None
