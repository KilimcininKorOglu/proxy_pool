.. ext_fetcher

Extend Proxy Sources
---------------------

The project includes several free proxy sources by default, but free sources have limited quality, so running directly may result in poor proxy quality. Therefore, a method for users to customize and extend proxy fetching is provided.

If you want to add a new proxy fetching method, the process is as follows:

1. First, add a custom static method for fetching proxies in the `ProxyFetcher`_ class. The method needs to return proxy strings in ``host:ip`` format using generator (yield), for example:

.. code-block:: python

    class ProxyFetcher(object):
    # ....
    # Custom proxy source fetching method
    @staticmethod
    def freeProxyCustom01():  # Just make sure the name doesn't duplicate existing ones
        # Get proxies from some website, API, or database
        # Assume you already have a proxy list
        proxies = ["x.x.x.x:3128", "x.x.x.x:80"]
        for proxy in proxies:
            yield proxy
        # Ensure each proxy is returned in correct host:ip format

2. After adding the method, modify the ``PROXY_FETCHER`` item in the configuration file `setting.py`_, adding the name of the custom method you just added:

.. code-block:: python

    PROXY_FETCHER = [
        # ....
        "freeProxyCustom01"  # Make sure the name matches your added method name
    ]

.. _ProxyFetcher: https://github.com/jhao104/proxy_pool/blob/1a3666283806a22ef287fba1a8efab7b94e94bac/fetcher/proxyFetcher.py#L20
.. _setting.py: https://github.com/jhao104/proxy_pool/blob/1a3666283806a22ef287fba1a8efab7b94e94bac/setting.py#L47