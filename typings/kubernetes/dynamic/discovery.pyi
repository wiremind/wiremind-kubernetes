"""
This type stub file was generated by pyright.
"""

import json
from abc import abstractmethod, abstractproperty

DISCOVERY_PREFIX = ...
class Discoverer:
    """
        A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources.

        Subclasses implement the abstract methods with different loading strategies.
    """
    def __init__(self, client, cache_file) -> None:
        ...
    
    def invalidate_cache(self): # -> None:
        ...
    
    @abstractproperty
    def api_groups(self): # -> None:
        ...
    
    @abstractmethod
    def search(self, prefix=..., group=..., api_version=..., kind=..., **kwargs): # -> None:
        ...
    
    @abstractmethod
    def discover(self): # -> None:
        ...
    
    @property
    def version(self): # -> str | Any:
        ...
    
    def default_groups(self, request_resources=...): # -> dict[Any, Any]:
        ...
    
    def parse_api_groups(self, request_resources=..., update=...): # -> str | Any:
        """ Discovers all API groups present in the cluster """
        ...
    
    def get_resources_for_api_version(self, prefix, group, version, preferred): # -> defaultdict[Any, list[Any]]:
        """ returns a dictionary of resources associated with provided (prefix, group, version)"""
        ...
    
    def get(self, **kwargs):
        """ Same as search, but will throw an error if there are multiple or no
            results. If there are multiple results and only one is an exact match
            on api_version, that resource will be returned.
        """
        ...
    


class LazyDiscoverer(Discoverer):
    """ A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources.

        Resources for the cluster are loaded lazily.
    """
    def __init__(self, client, cache_file) -> None:
        ...
    
    def discover(self): # -> None:
        ...
    
    @property
    def api_groups(self): # -> Any:
        ...
    
    def search(self, **kwargs): # -> list[Any]:
        ...
    
    def __iter__(self): # -> Generator[list[Any], Any, None]:
        ...
    


class EagerDiscoverer(Discoverer):
    """ A convenient container for storing discovered API resources. Allows
        easy searching and retrieval of specific resources.

        All resources are discovered for the cluster upon object instantiation.
    """
    def update(self, resources): # -> None:
        ...
    
    def __init__(self, client, cache_file) -> None:
        ...
    
    def discover(self): # -> None:
        ...
    
    @property
    def api_groups(self): # -> Any:
        """ list available api groups """
        ...
    
    def search(self, **kwargs): # -> list[Any]:
        """ Takes keyword arguments and returns matching resources. The search
            will happen in the following order:
                prefix: The api prefix for a resource, ie, /api, /oapi, /apis. Can usually be ignored
                group: The api group of a resource. Will also be extracted from api_version if it is present there
                api_version: The api version of a resource
                kind: The kind of the resource
                arbitrary arguments (see below), in random order

            The arbitrary arguments can be any valid attribute for an Resource object
        """
        ...
    
    def __iter__(self): # -> Generator[Any, Any, None]:
        ...
    


class ResourceGroup:
    """Helper class for Discoverer container"""
    def __init__(self, preferred, resources=...) -> None:
        ...
    
    def to_dict(self): # -> dict[str, Any]:
        ...
    


class CacheEncoder(json.JSONEncoder):
    def default(self, o): # -> Any:
        ...
    


class CacheDecoder(json.JSONDecoder):
    def __init__(self, client, *args, **kwargs) -> None:
        ...
    
    def object_hook(self, obj): # -> Resource | ResourceList | ResourceGroup:
        ...
    


