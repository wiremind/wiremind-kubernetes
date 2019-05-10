# wiremind-kubernetes

## 1.1.2 (2019-05-10)
### Changes
- Move a few logs to debug.

## 1.1.1 (2019-05-10)
### Changes
- improve `run_command` to log live output.

## 1.0.1 (2019-04-09)
### Changes
- KubernetesDeploymentManager: use `release_name` for real.

## 1.0.0 (2019-04-09)
### Breaking changes
- Improve `_run_command` helper, rename it to `run_command`.
### Changes
- Use logger everywhere.
- Add `kubernetes_exec` helper function.

## 0.4.1 (2019-04-05)
### Changes
- Loading kube configuration: autodetect if run from a pod.
