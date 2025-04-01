---
title: "What is Kubernetes (k8s)?"
description: "Learn about Kubernetes, a container orchestration system for deployment."
image: "https://assets.bytebytego.com/diagrams/0245-k8s.png"
createdAt: "2024-03-14"
draft: false
categories:
  - devops-cicd
tags:
  - "Kubernetes"
  - "Containers"
---

[![k8s](https://assets.bytebytego.com/diagrams/0245-k8s.png)](https://assets.bytebytego.com/diagrams/0245-k8s.png)

k8s is a container orchestration system. It is used for container deployment and management. Its design is greatly impacted by Google’s internal system Borg.

A k8s cluster consists of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node. \[1]

The worker node(s) host the Pods that are the components of the application workload. The control plane manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers and a cluster usually runs multiple nodes, providing fault tolerance and high availability. \[1]

## Control Plane Components

*   **API Server**

    The API server talks to all the components in the k8s cluster. All the operations on pods are executed by talking to the API server.

*   **Scheduler**

    The scheduler watches the workloads on pods and assigns loads on newly created pods.

*   **Controller Manager**

    The controller manager runs the controllers, including Node Controller, Job Controller, EndpointSlice Controller, and ServiceAccount Controller.

*   **etcd**

    etcd is a key-value store used as Kubernetes' backing store for all cluster data.

## Nodes

*   **Pods**

    A pod is a group of containers and is the smallest unit that k8s administers. Pods have a single IP address applied to every container within the pod.

*   **Kubelet**

    An agent that runs on each node in the cluster. It ensures containers are running in a Pod. \[1]

*   **Kube Proxy**

    kube-proxy is a network proxy that runs on each node in your cluster. It routes traffic coming into a node from the service. It forwards requests for work to the correct containers.
