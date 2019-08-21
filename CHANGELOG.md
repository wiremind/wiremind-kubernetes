# wiremind-kubernetes

## 1.1.7 (2019-08-21)
### Fixes
- remove hardcoded `load_oid_token`, upgrade to kubernetes 10.x.x.

## 1.1.6 (2019-08-01)
### Changes
- scale-down: sleep 1 second instead of 2.

## 1.1.5 (2019-05-14)
### Changes
- `run_command`: allow to return output.

## 1.1.3 (2019-05-14)
### Changes
- stop-pods: wait only 2 seconds before checking, change logger output levels.

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
