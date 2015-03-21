# EQL Shell #

The **EQL Shell** is a _command line_ script to send [Echo Query Language](http://echoplatform.com/streamserver/docs/features/echo-query-language/) requests to the **StreamServer**. It _always_ uses the **Default Account**, as shown under **Account:** heading on start-up.

```
$ /usr/bin/eql_shell

Echo Query Language Shell (echo.items version '0.73')
Account: (StreamServer Account[Basic] test.echoenabled.com)

Send an EQL text string to Stream Server and display the results.
EQL> url:http://example.com/index.html

Prompts:
SEARCH> "This prompt means execute a search."
COUNT>  "This prompt means execute a count."

Shell Commands
COUNT:  Set to COUNT> mode.
SEARCH: Set to SEARCH> mode.
USERS:  Set to USERS> mode.
QUIT:   Quit the shell.

SEARCH> count
COUNT> url:http://www.example.com/index.html
        COUNT: 3
COUNT>
```

## Items API ##

The **Items API** queries accept an [EQL](http://echoplatform.com/streamserver/docs/features/echo-query-language/) text string. Type either **count** or **search** to toggle the **EQL Shell** prompt to that state.

```
SEARCH> url:http://www.example.com/index.html
{u'children': {u'filter': u'()',
               u'itemsPerPage': u'2',
               u'maxDepth': u'2',
               u'sortOrder': u'reverseChronological'},
 u'entries': [],
 u'hasMoreChildren': u'false',
 u'id': u'http://api.echoenabled.com/v1/search?q=url:http://www.example.com/index.html',
 u'itemsPerPage': u'15',
 u'liveUpdatesTimeout': u'0',
 u'nextSince': u'1339706176.619064',
 u'safeHTML': u'aggressive',
 u'sortOrder': u'reverseChronological',
 u'updated': u'2012-06-14T20:36:16Z'}
```

## Users API ##

The **Users API** can **get** a single user by **identityURL**. Type **users** to toggle the **EQL Shell** prompt to that state.

### Not Found Errors ###

Sometimes, an **identityURL** is _not found_ by the **Users API**. This results in a **logging** error report that the underlying **REST API** found a **HTTP 404**.

```
SEARCH> Users
USERS> http://www.example.com/user/nobody/index.html
ERROR:root:[HTTP 404] users/get API Error
{}
USERS> quit

QUIT

```