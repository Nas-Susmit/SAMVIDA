# Design Document for {{ project_name }}

## Architecture Overview
{{ design.architecture }}

## Database Schema
{{ design.database }}

## API Endpoints
{% for ep in design.api_endpoints %}
- **{{ ep.method }} {{ ep.endpoint }}**: {{ ep.description }}
{% endfor %}

## UI Components
{% for comp in design.ui_components %}
- {{ comp }}
{% endfor %}