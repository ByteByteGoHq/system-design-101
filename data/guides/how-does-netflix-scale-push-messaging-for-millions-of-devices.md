---
title: 'How Netflix Scales Push Messaging'
description: 'Explore how Netflix scales push messaging for millions of devices.'
image: 'https://assets.bytebytego.com/diagrams/0291-netflix-pn.png'
createdAt: '2024-02-28'
draft: false
categories:
  - real-world-case-studies
tags:
  - System Design
  - Push Notifications
---

This post draws from an article published on Netflix’s engineering blog. Here’s my understanding of how the online streaming giant’s system works.

![](https://assets.bytebytego.com/diagrams/0291-netflix-pn.png)

**Requirements & Scale**

*   220 million users
*   Near real-time
*   Backend systems need to send notifications to various clients
*   Supported clients: iOS, Android, smart TVs, Roku, Amazon FireStick, web browser

**The Life of a Push Notification**

1.  Push notification events are triggered by the clock, user actions, or by systems.
2.  Events are sent to the event management engine.
3.  The event management engine listens to specific events and forward events to different queues. The queues are populated by priority-based event forwarding rules.
4.  The “event priority-based processing cluster” processes events and generates push notifications data for devices.
5.  A Cassandra database is used to store the notification data.
6.  A push notification is sent to outbound messaging systems.
7.  For Android, FCM is used to send push notifications. For Apple devices, APNs are used. For web, TV, and other streaming devices, Netflix’s homegrown solution called ‘Zuul Push’ is used.
