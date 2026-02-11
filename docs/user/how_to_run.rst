.. how_to_run


How to Run
-----------

Download Code
>>>>>>>>>>>>>>

This project requires downloading the code to run locally, download via ``git``:

.. code-block:: console

    $ git clone git@github.com:jhao104/proxy_pool.git

Or download a specific ``release`` version:

.. code-block:: console

    https://github.com/jhao104/proxy_pool/releases

Install Dependencies
>>>>>>>>>>>>>>>>>>>>>

Navigate to the project directory and use ``pip`` to install dependencies:

.. code-block:: console

    $ pip install -r requirements.txt


Update Configuration
>>>>>>>>>>>>>>>>>>>>>

The configuration file ``setting.py`` is located in the project's main directory:

.. code-block:: python

    # Configure API service

    HOST = "0.0.0.0"               # IP
    PORT = 5000                    # Listen port

    # Configure database

    DB_CONN = 'redis://@127.0.0.1:8888/0'

    # Configure ProxyFetcher

    PROXY_FETCHER = [
        "freeProxy01",      # These are enabled proxy fetch methods, all fetch methods are in fetcher/proxyFetcher.py
        "freeProxy02",
        # ....
    ]

For more configuration options, please refer to :doc:`/user/how_to_config`

Start Project
>>>>>>>>>>>>>>

If the runtime environment is configured and ready, you can start via ``proxyPool.py``. ``proxyPool.py`` is the project's CLI entry point.
The complete program consists of two parts: ``schedule`` scheduler and ``server`` API service. The scheduler is responsible for fetching and validating proxies, while the API service provides HTTP interface for proxy services.

Start the scheduler and API service separately via command line:

.. code-block:: console

    # Start scheduler
    $ python proxyPool.py schedule

    # Start webApi service
    $ python proxyPool.py server
