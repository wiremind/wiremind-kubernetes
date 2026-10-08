from typing import Any

import kubernetes.client

# Generated client methods that send a write request to the API server.
WRITE_METHOD_PREFIXES = ("create_", "delete_", "patch_", "replace_")
# Generated client methods that send a read request to the API server.
READ_METHOD_PREFIXES = ("read_", "list_")


class ClientWithArguments:
    """
    Generated Kubernetes API client that adds arguments to its method calls.

    Add `pretty` to read and write methods, and `dry_run` to write methods.
    The other methods (connect_*, get_*, close) do not accept these arguments.
    """

    client: Any
    dry_run: bool
    pretty: bool
    # Method name prefixes that accept `pretty`.
    pretty_method_prefixes: tuple[str, ...] = READ_METHOD_PREFIXES + WRITE_METHOD_PREFIXES

    def __init__(self, client: Any, dry_run: bool = False, pretty: bool = True):
        self.client = client()  # like kubernetes.client.CoreV1Api
        self.dry_run = dry_run
        self.pretty = pretty

    def get_additional_arguments(self, method_name: str) -> dict[str, str]:
        additional_arguments = {}
        if self.pretty and method_name.startswith(self.pretty_method_prefixes):
            # The generated client types `pretty` as a string and kubernetes>=37 rejects a bool.
            additional_arguments["pretty"] = "true"
        if self.dry_run and method_name.startswith(WRITE_METHOD_PREFIXES):
            # The API accepts dry_run "All" or no dry_run, never a bool.
            additional_arguments["dry_run"] = "All"
        return additional_arguments

    def __getattr__(self, attr: str) -> Any:
        original_attr = getattr(self.client, attr)

        if not callable(original_attr):
            return original_attr

        additional_arguments = self.get_additional_arguments(attr)
        if not additional_arguments:
            return original_attr

        def fn(*args: Any, **kwargs: Any) -> Any:
            kwargs.update(additional_arguments)
            return original_attr(*args, **kwargs)

        return fn


class CoreV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.CoreV1Api, dry_run=dry_run, pretty=pretty)


class AppV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AppsV1Api, dry_run=dry_run, pretty=pretty)


class BatchV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.BatchV1Api, dry_run=dry_run, pretty=pretty)


class AutoscalingV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AutoscalingV1Api, dry_run=dry_run, pretty=pretty)


class AutoscalingV2ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AutoscalingV2Api, dry_run=dry_run, pretty=pretty)


class CustomObjectsApiWithArguments(ClientWithArguments):
    # Custom object methods accept `pretty` on list and create only.
    pretty_method_prefixes = ("list_", "create_")

    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.CustomObjectsApi, dry_run=dry_run, pretty=pretty)


class RbacAuthorizationV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(
            client=kubernetes.client.RbacAuthorizationV1Api,
            dry_run=dry_run,
            pretty=pretty,
        )


class NetworkingV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.NetworkingV1Api, dry_run=dry_run, pretty=pretty)


class StorageV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.StorageV1Api, dry_run=dry_run, pretty=pretty)


class AdmissionregistrationV1ApiWithArguments(ClientWithArguments):
    def __init__(self, *args: Any, dry_run: bool = False, pretty: bool = False, **kwargs: Any) -> None:
        super().__init__(client=kubernetes.client.AdmissionregistrationV1Api, dry_run=dry_run, pretty=pretty)
