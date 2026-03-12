# User Stories for {{ project_name }}

{% for story in stories %}
- **{{ story.id }}**: As a **{{ story.role }}**, I want to **{{ story.action }}** so that **{{ story.benefit }}** (Priority: {{ story.priority }})
{% endfor %}