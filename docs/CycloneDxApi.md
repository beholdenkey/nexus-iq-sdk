# swagger_client.CycloneDxApi

All URIs are relative to _/_

| Method                                                     | HTTP request                                                              | Description |
| ---------------------------------------------------------- | ------------------------------------------------------------------------- | ----------- |
| [**get_by_report_id**](CycloneDxApi.md#get_by_report_id)   | **GET** /api/v2/cycloneDx/{applicationId}/reports/{reportId}              |
| [**get_by_report_id1**](CycloneDxApi.md#get_by_report_id1) | **GET** /api/v2/cycloneDx/{cdxVersion}/{applicationId}/reports/{reportId} |
| [**get_latest**](CycloneDxApi.md#get_latest)               | **GET** /api/v2/cycloneDx/{applicationId}/stages/{stageId}                |
| [**get_latest1**](CycloneDxApi.md#get_latest1)             | **GET** /api/v2/cycloneDx/{cdxVersion}/{applicationId}/stages/{stageId}   |

# **get_by_report_id**

> get_by_report_id(application_id, report_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloneDxApi()
application_id = 'application_id_example' # str |
report_id = 'report_id_example' # str |

try:
    api_instance.get_by_report_id(application_id, report_id)
except ApiException as e:
    print("Exception when calling CycloneDxApi->get_by_report_id: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |
| **report_id**      | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_by_report_id1**

> get_by_report_id1(application_id, report_id, cdx_version)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloneDxApi()
application_id = 'application_id_example' # str |
report_id = 'report_id_example' # str |
cdx_version = 'cdx_version_example' # str |

try:
    api_instance.get_by_report_id1(application_id, report_id, cdx_version)
except ApiException as e:
    print("Exception when calling CycloneDxApi->get_by_report_id1: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |
| **report_id**      | **str** |             |
| **cdx_version**    | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest**

> get_latest(application_id, stage_id)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloneDxApi()
application_id = 'application_id_example' # str |
stage_id = 'stage_id_example' # str |

try:
    api_instance.get_latest(application_id, stage_id)
except ApiException as e:
    print("Exception when calling CycloneDxApi->get_latest: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |
| **stage_id**       | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_latest1**

> get_latest1(application_id, stage_id, cdx_version)

### Example

```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CycloneDxApi()
application_id = 'application_id_example' # str |
stage_id = 'stage_id_example' # str |
cdx_version = 'cdx_version_example' # str |

try:
    api_instance.get_latest1(application_id, stage_id, cdx_version)
except ApiException as e:
    print("Exception when calling CycloneDxApi->get_latest1: %s\n" % e)
```

### Parameters

| Name               | Type    | Description | Notes |
| ------------------ | ------- | ----------- | ----- |
| **application_id** | **str** |             |
| **stage_id**       | **str** |             |
| **cdx_version**    | **str** |             |

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/xml, application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
