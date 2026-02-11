.. how_to_use

How to Use
-----------

There are currently two ways for crawler code to connect to the proxy pool: one is through calling the API interface, and the other is directly reading from the database.

Call API
>>>>>>>>>

After starting ProxyPool's ``server``, the following HTTP interfaces will be provided:

============     ========    ================       ==============
Api               Method      Description            Arg
============     ========    ================       ==============
/                GET         API introduction        None
/get             GET         Return a random proxy   None
/get_all         GET         Return all proxies      None
/get_status      GET         Return proxy count      None
/delete          GET         Delete specified proxy  proxy=host:ip
============     ========    ================       ==============

You can use proxies by wrapping the above API interfaces in your code, example:

.. code-block:: python

   import requests

   def get_proxy():
       return requests.get("http://127.0.0.1:5010/get/").json()

   def delete_proxy(proxy):
       requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

   # your spider code

   def getHtml():
       # ....
       retry_count = 5
       proxy = get_proxy().get("proxy")
       while retry_count > 0:
           try:
               # Access using proxy
               html = requests.get('http://www.example.com', proxies={"http": "http://{}".format(proxy)})
               return html
           except Exception:
               retry_count -= 1
               # Delete proxy from pool
               delete_proxy(proxy)
       return None

In this example, we start a ``server`` on local ``127.0.0.1`` with port ``5010``, use ``/get`` interface to get proxies, and ``/delete`` to delete proxies.

Read Database
>>>>>>>>>>>>>>

Currently two types of databases are supported: ``REDIS`` and ``SSDB``.

* **REDIS** storage structure is ``hash``, hash name is **TABLE_NAME** in configuration

* **SSDB** storage structure is ``hash``, hash name is **TABLE_NAME** in configuration

You can read directly from the database in your code.
