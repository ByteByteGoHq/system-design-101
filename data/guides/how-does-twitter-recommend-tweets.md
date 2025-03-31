---
title: How does Twitter recommend “For You” Timeline in 1.5 seconds?
description: Twitter's "For You" timeline recommendation system explained.
image: 'https://assets.bytebytego.com/diagrams/0121-twitter-serving-pipeline.jpeg'
createdAt: '2024-02-22'
draft: false
categories:
  - real-world-case-studies
tags:
  - System Design
  - Recommendation Systems
---

![](https://assets.bytebytego.com/diagrams/0121-twitter-serving-pipeline.jpeg)

We spent a few days analyzing it.

The diagram above shows the detailed pipeline based on the open-sourced algorithm.

The process involves 5 stages:

*   **Candidate Sourcing** ~ start with 500 million Tweets
*   **Global Filtering** ~ down to 1500 candidates
*   **Scoring & Ranking** ~ 48M parameter neural network, Twitter Blue boost
*   **Filtering** ~ to achieve author and content diversity
*   **Mixing** ~ with Ads recommendation and Who to Follow

The post was jointly created by ByteByteGo and [Mem](https://www.linkedin.com/company/memdotai/). Special thanks [Scott Mackie](https://www.linkedin.com/in/ACoAABLDe9kBSK7DsORQHK2G1srZCmM1isaUun8), founding engineer at Mem, for putting this together.

Mem is building the world’s first knowledge assistant. In next week’s ByteByteGo guest newsletter, Mem will be sharing lessons they’ve learned from their extensive work with large language models and building AI-native infrastructure.
