This folder contains simple Python scripts used to audit AWS resources during cost reviews.

Current scripts focus on visibility only and do not make any changes.

ec2_instance_audit.py
- Lists EC2 instances
- Shows instance age and state
- Helps identify long running or forgotten compute resources

cost_guardrails.tf
- Example Terraform configuration showing basic cost guardrails
- Demonstrates limiting instance types and enforcing cost tags
