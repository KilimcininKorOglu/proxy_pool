.. ext_validator

Proxy Validation
-----------------

Built-in Validation
>>>>>>>>>>>>>>>>>>>>

All proxy validation methods used in the project are defined in `validator.py`_, distinguished by decorators provided in the `ProxyValidator`_ class. A validation method returning ``True`` means
validation passed, returning ``False`` means validation failed.

* Proxy validation methods are divided into three categories: ``preValidator``, ``httpValidator``, ``httpsValidator``:

    * **preValidator**: Pre-validation, called after proxy fetching but before validation. Currently implements `formatValidator`_ to check if proxy IP format is valid;
    * **httpValidator**: Proxy availability validation, passing means the proxy is available. Currently implements `httpTimeOutValidator`_ validation;
    * **httpsValidator**: Validates whether the proxy supports https. Currently implements `httpsTimeOutValidator`_ validation.


.. _validator.py: https://github.com/jhao104/proxy_pool/blob/release-2.3.0/helper/validator.py
.. _ProxyValidator: https://github.com/jhao104/proxy_pool/blob/release-2.3.0/helper/validator.py#L29
.. _formatValidator: https://github.com/jhao104/proxy_pool/blob/release-2.3.0/helper/validator.py#L51
.. _httpTimeOutValidator: https://github.com/jhao104/proxy_pool/blob/release-2.3.0/helper/validator.py#L58
.. _httpsTimeOutValidator: https://github.com/jhao104/proxy_pool/blob/release-2.3.0/helper/validator.py#L71

Multiple methods can be defined for each validation type. Only when **all** methods return ``True`` is the validation considered passed. The execution order is: first execute **httpValidator**, then execute **httpsValidator** after the former passes.
Only proxies that pass `preValidator` will enter availability validation. After `httpValidator` passes, the proxy is considered available and ready to be updated into the proxy pool. After `httpsValidator` passes, the proxy's `https` attribute is updated to `True`.

Extend Validation
>>>>>>>>>>>>>>>>>>

There are examples of custom validation in `validator.py`_. Custom functions need to return True or False, using decorators provided in `ProxyValidator`_ to distinguish validation types. Here are two examples:

* 1. Custom proxy availability validation (``addHttpValidator``):

.. code-block:: python

    @ProxyValidator.addHttpValidator
    def customValidatorExample01(proxy):
        """Custom proxy availability validation function"""
        proxies = {"http": "http://{proxy}".format(proxy=proxy)}
        try:
            r = requests.get("http://www.baidu.com/", headers=HEADER, proxies=proxies, timeout=5)
            return True if r.status_code == 200 and len(r.content) > 200 else False
        except Exception as e:
            return False

* 2. Custom validation for whether proxy supports https (``addHttpsValidator``):

.. code-block:: python

    @ProxyValidator.addHttpsValidator
    def customValidatorExample02(proxy):
        """Custom validation function for https support"""
        proxies = {"https": "https://{proxy}".format(proxy=proxy)}
        try:
            r = requests.get("https://www.baidu.com/", headers=HEADER, proxies=proxies, timeout=5, verify=False)
            return True if r.status_code == 200 and len(r.content) > 200 else False
        except Exception as e:
            return False

Note that when running proxy availability validation, all functions decorated with ``ProxyValidator.addHttpValidator`` will be executed sequentially in definition order. Only when all functions return True will the proxy be considered available. The ``HttpsValidator`` mechanism works the same way.
