# Echo StreamServer API #

This is a Python client for the Echo StreamServer REST API. There are a few APIs, actually. See the [Echo Documentation](http://echoplatform.com/streamserver/docs/rest-api/) for details.

  * feeds - Feeds API
  * items - Items API
  * kvs   - Key-Value Store API
  * users - User API

Most API methods raise the echo.StreamServerError exception.
This indicates a server-side error, or malformed request.

# Details #

Each **Echo API** is a separate _module_ or _package_ to **import**. Every **API** has both a _function_ interface and a **client** _object_ interface. The _function_ interface uses a **default** account shared by everyone.