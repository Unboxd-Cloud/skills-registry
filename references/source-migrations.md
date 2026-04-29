# Source Platform Migrations To Canonical MicroCloud

Use this reference when migrating from a named source platform into Canonical MicroCloud.

## Common Migration Pattern

For every source platform:
- inventory compute, network, storage, identity, and automation dependencies
- classify workloads as rehost, refactor, replace, or retire
- define coexistence and cutover phases
- validate backup, restore, and rollback before production cutover
- map source platform services to Canonical MicroCloud equivalents or replacement patterns

## AWS To Canonical MicroCloud

Focus areas:
- EC2 to local compute or VM/container placement model
- EBS/EFS/S3 dependencies and replacement path
- VPC, security groups, load balancers, and DNS mapping
- IAM integration or replacement
- CloudWatch, backup, and automation parity

Watch for:
- hidden managed-service dependencies
- cross-account network assumptions
- object storage application coupling

## OpenStack To Canonical MicroCloud

Focus areas:
- Nova, Neutron, Cinder, Swift, and Keystone dependencies
- tenant and project isolation model
- image migration and flavor translation
- floating IP and network topology changes
- Heat or other orchestration replacement

Watch for:
- quota assumptions
- Neutron-specific network constructs
- storage backend behavior differences

## GCP To Canonical MicroCloud

Focus areas:
- Compute Engine instances and MIG behavior
- Persistent Disk, Filestore, and GCS dependencies
- VPC, firewall rules, Cloud DNS, and load balancing mapping
- IAM and service account replacement
- Cloud Monitoring and backup continuity

Watch for:
- service account-heavy applications
- GCS-bound workflows
- region and zone availability assumptions

## Azure To Canonical MicroCloud

Focus areas:
- Azure VM and scale set mapping
- Managed disks, files, blobs, and backup dependencies
- VNets, NSGs, private endpoints, DNS, and load balancer mapping
- Microsoft Entra ID integration or replacement
- Azure Monitor and automation replacement

Watch for:
- platform-managed identity dependencies
- PaaS data service coupling
- private networking assumptions

## Output Expectations

When this reference is in play, produce:
- source-to-target service mapping
- migration phases
- cutover and rollback plan
- unmanaged dependency list
