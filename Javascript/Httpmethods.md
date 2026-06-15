## **Common HTTP Status Codes**
| **Status Code** | **Meaning** |
|---------------|-------------|
| **1xx Informational** | Request received, continuing process |
| `100 Continue` | Server received request headers, client should proceed |
| `101 Switching Protocols` | Server switching protocols as requested |
| **2xx Success** | Request successfully received, understood, and accepted |
| `200 OK` | Standard success response |
| `201 Created` | Resource successfully created |
| `202 Accepted` | Request accepted but not yet processed |
| `204 No Content` | Request successful but no response body |
| **3xx Redirection** | Further action needed |
| `301 Moved Permanently` | Resource moved to a new URL |
| `302 Found` | Temporary redirection |
| `304 Not Modified` | Cached resource still valid |
| **4xx Client Errors** | Client made an error |
| `400 Bad Request` | Invalid request syntax |
| `401 Unauthorized` | Authentication required |
| `403 Forbidden` | Access denied |
| `404 Not Found` | Resource not found |
| `409 Conflict` | Resource conflict |
| `429 Too Many Requests` | Rate limit exceeded |
| **5xx Server Errors** | Server failed to fulfill request |
| `500 Internal Server Error` | Unexpected server error |
| `502 Bad Gateway` | Invalid response from upstream server |
| `503 Service Unavailable` | Server overloaded or under maintenance |
| `504 Gateway Timeout` | Upstream server did not respond |
