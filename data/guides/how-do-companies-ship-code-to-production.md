---
title: "How do Companies Ship Code to Production?"
description: "Explore the process companies use to ship code to production efficiently."
image: "https://assets.bytebytego.com/diagrams/0334-ship-to-prod.png"
createdAt: "2024-03-15"
draft: false
categories:
  - devtools-productivity
tags:
  - software-engineering
  - deployment
---

![](https://assets.bytebytego.com/diagrams/0334-ship-to-prod.png)

The diagram below illustrates the typical workflow.

Step 1: The process starts with a product owner creating user stories based on requirements.

Step 2: The dev team picks up the user stories from the backlog and puts them into a sprint for a two-week dev cycle.

Step 3: The developers commit source code into the code repository Git.

Step 4: A build is triggered in Jenkins. The source code must pass unit tests, code coverage threshold, and gates in SonarQube.

Step 5: Once the build is successful, the build is stored in artifactory. Then the build is deployed into the dev environment.

Step 6: There might be multiple dev teams working on different features. The features need to be tested independently, so they are deployed to QA1 and QA2.

Step 7: The QA team picks up the new QA environments and performs QA testing, regression testing, and performance testing.

Step 8: Once the QA builds pass the QA team’s verification, they are deployed to the UAT environment.

Step 9: If the UAT testing is successful, the builds become release candidates and will be deployed to the production environment on schedule.

Step 10: SRE (Site Reliability Engineering) team is responsible for prod monitoring.
