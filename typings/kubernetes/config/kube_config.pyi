"""
This type stub file was generated by pyright.
"""

EXPIRY_SKEW_PREVENTION_DELAY = ...
KUBE_CONFIG_DEFAULT_LOCATION = ...
ENV_KUBECONFIG_PATH_SEPARATOR = ...
_temp_files = ...
class FileOrData:
    """Utility class to read content of obj[%data_key_name] or file's
     content of obj[%file_key_name] and represent it as file or data.
     Note that the data is preferred. The obj[%file_key_name] will be used iff
     obj['%data_key_name'] is not set or empty. Assumption is file content is
     raw data and data field is base64 string. The assumption can be changed
     with base64_file_content flag. If set to False, the content of the file
     will assumed to be base64 and read as is. The default True value will
     result in base64 encode of the file content after read."""
    def __init__(self, obj, file_key_name, data_key_name=..., file_base_path=..., base64_file_content=..., temp_file_path=...) -> None:
        ...
    
    def as_file(self): # -> str | None:
        """If obj[%data_key_name] exists, return name of a file with base64
        decoded obj[%data_key_name] content otherwise obj[%file_key_name]."""
        ...
    
    def as_data(self): # -> str | None:
        """If obj[%data_key_name] exists, Return obj[%data_key_name] otherwise
        base64 encoded string of obj[%file_key_name] file content."""
        ...
    


class CommandTokenSource:
    def __init__(self, cmd, args, tokenKey, expiryKey) -> None:
        ...
    
    def token(self): # -> A:
        ...
    


class KubeConfigLoader:
    def __init__(self, config_dict, active_context=..., get_google_credentials=..., config_base_path=..., config_persister=..., temp_file_path=...) -> None:
        ...
    
    def set_active_context(self, context_name=...): # -> None:
        ...
    
    def load_and_set(self, client_configuration): # -> None:
        ...
    
    def list_contexts(self): # -> list[dict[Any, Any] | list[Any] | Any]:
        ...
    
    @property
    def current_context(self):
        ...
    


class ConfigNode:
    """Remembers each config key's path and construct a relevant exception
    message in case of missing keys. The assumption is all access keys are
    present in a well-formed kube-config."""
    def __init__(self, name, value, path=...) -> None:
        ...
    
    def __contains__(self, key): # -> bool:
        ...
    
    def __len__(self): # -> int:
        ...
    
    def safe_get(self, key): # -> None:
        ...
    
    def __getitem__(self, key): # -> ConfigNode:
        ...
    
    def get_with_name(self, name, safe=...): # -> ConfigNode | None:
        ...
    


class KubeConfigMerger:
    """Reads and merges configuration from one or more kube-config's.
    The propery `config` can be passed to the KubeConfigLoader as config_dict.

    It uses a path attribute from ConfigNode to store the path to kubeconfig.
    This path is required to load certs from relative paths.

    A method `save_changes` updates changed kubeconfig's (it compares current
    state of dicts with).
    """
    def __init__(self, paths) -> None:
        ...
    
    @property
    def config(self): # -> Any | ConfigNode | None:
        ...
    
    def load_config(self, path): # -> None:
        ...
    
    def save_changes(self): # -> None:
        ...
    
    def save_config(self, path): # -> None:
        ...
    


def list_kube_config_contexts(config_file=...): # -> tuple[list[dict[Any, Any] | list[Any] | Any], Any]:
    ...

def load_kube_config(config_file=..., context=..., client_configuration=..., persist_config=...): # -> None:
    """Loads authentication and cluster information from kube-config file
    and stores them in kubernetes.client.configuration.

    :param config_file: Name of the kube-config file.
    :param context: set the active context. If is set to None, current_context
        from config file will be used.
    :param client_configuration: The kubernetes.client.Configuration to
        set configs to.
    :param persist_config: If True, config file will be updated when changed
        (e.g GCP token refresh).
    """
    ...

def load_kube_config_from_dict(config_dict, context=..., client_configuration=..., persist_config=..., temp_file_path=...): # -> None:
    """Loads authentication and cluster information from config_dict file
    and stores them in kubernetes.client.configuration.

    :param config_dict: Takes the config file as a dict.
    :param context: set the active context. If is set to None, current_context
        from config file will be used.
    :param client_configuration: The kubernetes.client.Configuration to
        set configs to.
    :param persist_config: If True, config file will be updated when changed
        (e.g GCP token refresh).
    :param temp_file_path: store temp files path.
    """
    ...

def new_client_from_config(config_file=..., context=..., persist_config=...): # -> ApiClient:
    """
    Loads configuration the same as load_kube_config but returns an ApiClient
    to be used with any API object. This will allow the caller to concurrently
    talk with multiple clusters.
    """
    ...

def new_client_from_config_dict(config_dict=..., context=..., persist_config=..., temp_file_path=...): # -> ApiClient:
    """
    Loads configuration the same as load_kube_config_from_dict but returns an ApiClient
    to be used with any API object. This will allow the caller to concurrently
    talk with multiple clusters.
    """
    ...

