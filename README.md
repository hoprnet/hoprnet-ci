# Continuous Integration of Hoprnet repository

This repository contains the nodes running in Kubernetes and updated upon every PR successfully merged into `master` or `release/${LAST_STABLE_RELEASE}`

The triggering pipeline of this nodes is located at: https://github.com/hoprnet/hoprnet/blob/master/.github/workflows/merge.yaml under the job step named `Restart deployments`

The Sops master key is stored in Bitwarden under the name `sops`
