---
title: "Infrastructure as Code Landscape Cheatsheet"
description: "A quick reference guide to the Infrastructure as Code landscape."
image: "https://assets.bytebytego.com/diagrams/0063-a-cheatsheet-on-infrastructure-as-code-landscape.png"
createdAt: "2024-02-18"
draft: false
categories:
  - cloud-distributed-systems
tags:
  - "Infrastructure as Code"
  - "DevOps"
---

![](https://assets.bytebytego.com/diagrams/0063-a-cheatsheet-on-infrastructure-as-code-landscape.png)

Scalable infrastructure provisioning provides several benefits related to availability, scalability, repeatability, and cost-effectiveness.

But how do you achieve this?

Provisioning infrastructure using code is the key to scalable infra management.

There are multiple strategies that can help:

*   Containerization is one of the first strategies to make application deployments based on code. Docker is one of the most popular ways to containerize the application.

*   Next, container orchestration becomes a necessity when dealing with multiple containers in an application. This is where container orchestration tools like Kubernetes become important.

*   IaC treats infrastructure provisioning and configuration as code, allowing developers to define the application infrastructure in files that can be versioned, tested, and reused. Popular tools such as Terraform, AWS CloudFormation, and Ansible can be used. Ansible is more of a configuration tool.

*   GitOps leverages a Git workflow combined with CI/CD to automate infrastructure and configuration updates.
