---
title: 'Netflix Tech Stack - CI/CD Pipeline'
description: "Netflix's CI/CD pipeline: from planning to incident reporting."
image: 'https://assets.bytebytego.com/diagrams/0287-netflix-ci-cd.png'
createdAt: '2024-03-02'
draft: false
categories:
  - real-world-case-studies
  - devops-cicd
tags:
  - CI/CD
  - Streaming
---

![](https://assets.bytebytego.com/diagrams/0287-netflix-ci-cd.png)

*   **Planning:** Netflix Engineering uses JIRA for planning and Confluence for documentation.

*   **Coding:** Java is the primary programming language for the backend service, while other languages are used for different use cases.

*   **Build:** Gradle is mainly used for building, and Gradle plugins are built to support various use cases.

*   **Packaging:** Package and dependencies are packed into an Amazon Machine Image (AMI) for release.

*   **Testing:** Testing emphasizes the production culture's focus on building chaos tools.

*   **Deployment:** Netflix uses its self-built Spinnaker for canary rollout deployment.

*   **Monitoring:** The monitoring metrics are centralized in Atlas, and Kayenta is used to detect anomalies.

*   **Incident report:** Incidents are dispatched according to priority, and PagerDuty is used for incident handling.
