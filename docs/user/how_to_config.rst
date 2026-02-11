.. how_to_config

Configuration Reference
------------------------

The configuration file ``setting.py`` is located in the project's main directory. Configuration is mainly divided into four categories: **Service Configuration**, **Database Configuration**, **Fetching Configuration**, and **Validation Configuration**.

Service Configuration
>>>>>>>>>>>>>>>>>>>>>>

* ``HOST``

    IP address the API service listens on. Set to ``127.0.0.1`` for local access, set to ``0.0.0.0`` for remote access.

* ``PORT``

    Port the API service listens on.

Database Configuration
>>>>>>>>>>>>>>>>>>>>>>>

* ``DB_CONN``

    Database URI for storing proxy IPs. Configuration format: ``db_type://[[user]:[pwd]]@ip:port/[db]``.

    Currently supported db_types: ``ssdb``, ``redis``.

    Configuration examples:

.. code-block:: python

    # SSDB IP: 127.0.0.1  Port: 8888
    DB_CONN = 'ssdb://@127.0.0.1:8888'
    # SSDB IP: 127.0.0.1  Port: 8899  Password:  123456
    DB_CONN = 'ssdb://:123456@127.0.0.1:8888'

    # Redis IP: 127.0.0.1  Port: 6379
    DB_CONN = 'redis://@127.0.0.1:6379'
    # Redis IP: 127.0.0.1  Port: 6379  Password:  123456
    DB_CONN = 'redis://:123456@127.0.0.1:6379'
    # Redis IP: 127.0.0.1  Port: 6379  Password:  123456  DB: 15
    DB_CONN = 'redis://:123456@127.0.0.1:6379/15'


* ``TABLE_NAME``

    Name of the data container for storing proxies. Storage structure for ssdb and redis is hash.

Fetching Configuration
>>>>>>>>>>>>>>>>>>>>>>>

* ``PROXY_FETCHER``

    Names of enabled proxy fetching methods. Proxy fetching methods are located in ``fetcher/proxyFetcher.py`` class.

    Since the stability of various proxy sources is hard to predict, when a proxy fetching method becomes invalid, you can comment out its name in this configuration.

    If you add new proxy fetching methods, please also add their method names in this configuration. For details, please refer to :doc:`/dev/extend_fetcher`.

    The scheduler reloads this configuration each time it executes a fetching task, ensuring that the fetching methods run each time are valid.

Validation Configuration
>>>>>>>>>>>>>>>>>>>>>>>>>

* ``HTTP_URL``

    Address used to verify if a proxy is available. Default is ``http://httpbin.org``, can be modified to other addresses based on usage scenario.

* ``HTTPS_URL``

    Address used to verify if a proxy supports HTTPS. Default is ``https://www.qq.com``, can be modified to other addresses based on usage scenario.

* ``VERIFY_TIMEOUT``

    Timeout for proxy verification. Default is ``10`` seconds. When accessing ``HTTP(S)_URL`` via proxy takes longer than ``VERIFY_TIMEOUT``, the proxy is considered unavailable.

* ``MAX_FAIL_COUNT``

    Maximum allowed failure count for proxy verification. Default is ``0``, meaning delete after one failure.

* ``POOL_SIZE_MIN``

    If proxy count is less than `POOL_SIZE_MIN` before the proxy check scheduled task runs, the fetching program will run first.