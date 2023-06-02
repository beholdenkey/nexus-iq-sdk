# swagger_client.ReportsApi

All URIs are relative to _/_

| Method                                                                                     | HTTP request                                                 | Description |
| ------------------------------------------------------------------------------------------ | ------------------------------------------------------------ | ----------- |
| [**get_all1**](ReportsApi.md#get_all1)                                                     | **GET** /api/v2/reports/applications                         |
| [**get_by_application_id**](ReportsApi.md#get_by_application_id)                           | **GET** /api/v2/reports/applications/{applicationId}         |
| [**get_components_in_quarantine**](ReportsApi.md#get_components_in_quarantine)             | **GET** /api/v2/reports/components/quarantined               |
| [**get_components_with_waivers**](ReportsApi.md#get_components_with_waivers)               | **GET** /api/v2/reports/components/waivers                   |
| [**get_metrics**](ReportsApi.md#get_metrics)                                               | **POST** /api/v2/reports/metrics                             |
| [**get_report_history_for_application**](ReportsApi.md#get_report_history_for_application) | **GET** /api/v2/reports/applications/{applicationId}/history |
| [**get_stale_waivers**](ReportsApi.md#get_stale_waivers)                                   | **GET** /api/v2/reports/waivers/stale                        |

# **get_all1**

> list[ApiApplicationReportDTOV2] get_all1()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()

try:
    api_response = api_instance.get_all1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_all1: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**list[ApiApplicationReportDTOV2]**](ApiApplicationReportDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_application_id**

> list[ApiApplicationReportDTOV2] get_by_application_id(application_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
application_id = 'application_id_example' # str |

try:
    api_response = api_instance.get_by_application_id(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_by_application_id: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |

### Return type

[**list[ApiApplicationReportDTOV2]**](ApiApplicationReportDTOV2.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components_in_quarantine**

> ApiComponentsInQuarantineDTO get_components_in_quarantine()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()

try:
    api_response = api_instance.get_components_in_quarantine()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_components_in_quarantine: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiComponentsInQuarantineDTO**](ApiComponentsInQuarantineDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_components_with_waivers**

> ApiComponentWaiversDTO get_components_with_waivers(format=format)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
format = 'format_example' # str |  (optional)

try:
    api_response = api_instance.get_components_with_waivers(format=format)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_components_with_waivers: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes      |
| ---------- | ------- | ----------- | ---------- |
| **format** | **str** |             | [optional] |

### Return type

[**ApiComponentWaiversDTO**](ApiComponentWaiversDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_metrics**

> get_metrics(body=body)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
body = swagger_client.ApiMetricsReportingQueryDTOV2() # ApiMetricsReportingQueryDTOV2 |  (optional)

try:
    api_instance.get_metrics(body=body)
except ApiException as e:
    print("Exception when calling ReportsApi->get_metrics: %s\n" % e)
```

### Parameters

| Name     | Type                                                                  | Description | Notes      |
| -------- | --------------------------------------------------------------------- | ----------- | ---------- |
| **body** | [**ApiMetricsReportingQueryDTOV2**](ApiMetricsReportingQueryDTOV2.md) |             | [optional] |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_report_history_for_application**

> ApiReportHistoryDTO get_report_history_for_application(application_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()
application_id = 'application_id_example' # str |

try:
    api_response = api_instance.get_report_history_for_application(application_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_report_history_for_application: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |

### Return type

[**ApiReportHistoryDTO**](ApiReportHistoryDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_stale_waivers**

> ApiStaleWaiversResponseDTO get_stale_waivers()

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ReportsApi()

try:
    api_response = api_instance.get_stale_waivers()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ReportsApi->get_stale_waivers: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiStaleWaiversResponseDTO**](ApiStaleWaiversResponseDTO.md)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
