# Cloud Cost Audit Toolkit

This repository contains a small set of practical tools used during cloud cost audits for AWS and GCP environments.

The goal is not automation at scale, but fast visibility into common sources of wasted spend.

## What this toolkit helps identify

- Idle or underutilized compute resources
- Overprovisioned instances
- Unused disks and snapshots
- Basic cost drivers across services
- Opportunities for rightsizing and cleanup

## Typical use case

These scripts are used as part of a short focused audit to understand where cloud spend is going and where quick savings can be achieved without downtime.

## Structure

aws/
- Scripts for auditing EC2, EBS, and related resources

gcp/
- Scripts for basic cost visibility and unused resource detection

notes/
- Manual audit notes and checklist used during reviews

## Disclaimer

This toolkit provides visibility and signals, not automated changes. All optimizations should be reviewed before applying in production environments.
