# swagger_client.TelemetryApi

All URIs are relative to _/_

| Method                                                                 | HTTP request               | Description |
| ---------------------------------------------------------------------- | -------------------------- | ----------- |
| [**post_external_telemetry**](TelemetryApi.md#post_external_telemetry) | **POST** /api/v2/telemetry |

# **post_external_telemetry**

> post_external_telemetry(body=body, user_agent=user_agent)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.TelemetryApi()
body = NULL # dict(str, str) |  (optional)
user_agent = 'user_agent_example' # str |  (optional)

try:
    api_instance.post_external_telemetry(body=body, user_agent=user_agent)
except ApiException as e:
    print("Exception when calling TelemetryApi->post_external_telemetry: %s\n" % e)
```

### Parameters

| Name           | Type                          | Description | Notes      |
| -------------- | ----------------------------- | ----------- | ---------- |
| **body**       | [**dict(str, str)**](dict.md) |             | [optional] |
| **user_agent** | **str**                       |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: _/_

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
