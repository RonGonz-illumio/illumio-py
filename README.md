# illumio-py  

[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg?color=orange)](https://opensource.org/licenses/Apache-2.0)
[![Latest Release](https://img.shields.io/github/v/release/dsommerville-illumio/illumio-py?label=Latest%20Release)](https://github.com/dsommerville-illumio/illumio-py/releases/latest)

## Release Notes  

See the [CHANGELOG](CHANGELOG.rst).  

## Overview  

Illumio Policy Compute Engine REST client for python 3. Exposes PCE API endpoints as functions through a simple interface.  

Compatible with Illumio Core PCE version 21.2+.  

The main entrypoint for the client is the `PolicyComputeEngine` class:  

```python
>>> from illumio import PolicyComputeEngine
>>> pce = PolicyComputeEngine('my.pce.com', port='8443', org_id='12')
>>> pce.set_credentials('<API_KEY>', '<API_SECRET>')
>>> workloads = pce.get_workloads(
...     params={
...         'managed': True,
...         'enforcement_mode': 'visibility_only'
...     }
... )
>>> workloads
[
    Workload(href='/orgs/12/workloads/c754a713-2bde-4427-af1f-bff145be509b', ...),
    ...
]
```

For more information on the Illumio APIs, see the [REST API guide](https://docs.illumio.com/core/21.5/Content/LandingPages/Guides/rest-api.htm) and the [API reference](https://docs.illumio.com/core/21.5/API-Reference/index.html) for your version of Illumio Core.  

## Installation  

> The `illumio` library is not yet available on pypi.  

The wheel and source distributables for the latest release can be found [here](/releases/latest).  

To build and install from source  

```sh
$ git clone git@github.com:dsommerville-illumio/illumio-py.git
$ cd illumio-py
$ make
```

## Support  

The `illumio` package is released and distributed as open source software subject to the included [LICENSE](LICENSE). Illumio has no obligation or responsibility related to the package with respect to support, maintenance, availability, security or otherwise. Please read the entire [LICENSE](LICENSE) for additional information regarding the permissions and limitations. Support is offered on a best-effort basis through the [Illumio app integrations team](mailto:app-integrations@illumio.com) and project contributors.

## Contributing  

See [CONTRIBUTING](.github/CONTRIBUTING.md) for details.  
