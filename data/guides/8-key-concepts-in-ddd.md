---
title: "8 Key Concepts in Domain-Driven Design"
description: "Explore 8 key concepts in Domain-Driven Design for better software."
image: "https://assets.bytebytego.com/diagrams/0011-8-key-concepts-in-ddd.png"
createdAt: "2024-03-06"
draft: false
categories:
  - software-architecture
tags:
  - DDD
  - Software Design
---

![](https://assets.bytebytego.com/diagrams/0011-8-key-concepts-in-ddd.png)

Domain-driven design advocates driving the design of software through domain modeling.

Unified language is one of the key concepts of domain-driven design. A domain model is a bridge across the business domains.

## Domain Driven Design

Domain-driven design advocates driving the design of software through domain modeling.

Unified language is one of the key concepts of domain-driven design. A domain model is a bridge across the business domains.

## Business Entities

The use of models can assist in expressing business concepts and knowledge and in guiding further development of software, such as databases, APIs, etc.

## Model Boundaries

Loose boundaries among sets of domain models are used to model business correlations.

## Aggregation

An Aggregate is a cluster of related objects (entities and value objects) that are treated as a single unit for the purpose of data changes.

## Entities vs. Value Objects

In addition to aggregate roots and entities, there are some models that look like disposable, they don't have their own ID to identify them, but are more as part of some entity that expresses a collection of several fields.

## Operational Modeling

In domain-driven design, in order to manipulate these models, there are a number of objects that act as "operators".

## Layering the architecture

In order to better organize the various objects in a project, we need to simplify the complexity of complex projects by layering them like a computer network.

## Build the domain model

Many methods have been invented to extract domain models from business knowledge.
