# Terraform Starter Notes

Use Terraform here for infrastructure adjacency, not for every runtime mutation.

Suggested ownership:
- Network-adjacent prerequisites
- DNS records
- External load balancer definitions
- Monitoring or secret backends outside the cluster

Suggested files:
- `versions.tf`
- `providers.tf`
- `variables.tf`
- `main.tf`
- `outputs.tf`
- `environments/<env>/terraform.tfvars`

Rules:
- Separate reusable modules from environment composition.
- Keep secrets out of committed tfvars.
- Pair every environment with a verification command set.
