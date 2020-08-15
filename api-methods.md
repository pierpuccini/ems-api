# API Methods

{% api-method method="get" host="http://localhost:5000" path="/api/tensions" %}
{% api-method-summary %}
Get Voltages
{% endapi-method-summary %}

{% api-method-description %}
This endpoint allows you to voltages from all nodes.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Voltages received
{% endapi-method-response-example-description %}

```
[ 'voltage at terminal 1 is 1 p.u.' ]
```
{% endapi-method-response-example %}

{% api-method-response-example httpCode=404 %}
{% api-method-response-example-description %}
Could not connect to powerfactory
{% endapi-method-response-example-description %}

```
{    "message": "pf not defined"}
```
{% endapi-method-response-example %}
{% endapi-method-response %}
{% endapi-method-spec %}
{% endapi-method %}



