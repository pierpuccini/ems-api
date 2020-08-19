# API Methods

{% api-method method="get" host="http://localhost:5000" path="/api/load-flow/0/terminals/all" %}
{% api-method-summary %}
Get terminal info
{% endapi-method-summary %}

{% api-method-description %}
This endpoint allows you to voltages from all nodes.
{% endapi-method-description %}

{% api-method-spec %}
{% api-method-request %}
{% api-method-path-parameters %}
{% api-method-parameter name="project" type="integer" required=true %}
This is project you wish to activate in order shown in DigSilent
{% endapi-method-parameter %}
{% endapi-method-path-parameters %}
{% endapi-method-request %}

{% api-method-response %}
{% api-method-response-example httpCode=200 %}
{% api-method-response-example-description %}
Terminal info recieved
{% endapi-method-response-example-description %}

```javascript
{
    "terminals": {
        "Bus_0012": {
            "reactive_gen": {
                "value": 0.0,
                "unit": "Mvar"
            },
            "active_flow": {
                "value": 7.7102326679141315,
                "unit": "MW"
            },
            "magnitude": {
                "value": 1.05522051228861,
                "unit": "p.u."
            },
            "angle": {
                "value": -15.077414289317803,
                "unit": "deg"
            },
            "active_gen": {
                "value": 0.0,
                "unit": "MW"
            },
            "reactive_out": {
                "value": 2.343011708584044,
                "unit": "Mvar"
            },
            "active_out": {
                "value": 7.7102326679141315,
                "unit": "MW"
            },
            "line": {
                "value": 34.822276905524134,
                "unit": "kV"
            },
            "reactive_flow": {
                "value": 2.343011708584044,
                "unit": "Mvar"
            }
        },
        "Bus_0014": {
        ...
        },
        ...
    }
}
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



