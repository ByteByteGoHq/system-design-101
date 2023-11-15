<p>
  <a href="https://blog.bytebytego.com/?utm_source=site"><img src="../../images/banner.jpg" /> </a>
</p>

<p align="center">
  【
  <a href="https://www.youtube.com/channel/UCZgt6AzoyjslHTC9dz0UoTw">
    👨🏻‍💻 YouTube
  </a> | 
  <a href="https://blog.bytebytego.com/?utm_source=site">
    📮 Newsletter
  </a> 】
</p>

<a href="https://trendshift.io/repositories/3709" target="_blank"><img src="https://trendshift.io/api/badge/repositories/3709" alt="ByteByteGoHq%2Fsystem-design-101 | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>

# 系统设计 101（System Design 101）

使用图片和简单术语来解释复杂系统。

无论你是在准备系统设计面试，还是单纯想了解系统的底层工作原理，我们都希望这个存储库可以帮助你得偿所愿。

# 目录

<!-- TOC toc.levels=2 -->

- [系统设计 101（System Design 101）](#系统设计-101system-design-101)
- [目录](#目录)
  - [通信协议](#通信协议)
    - [REST API vs. GraphQL](#rest-api-vs-graphql)
    - [gRPC 是如何工作的？](#grpc-是如何工作的)
    - [什么是 webhook？](#什么是-webhook)
    - [如何改善 API 性能？](#如何改善-api-性能)
    - [HTTP 1.0 -\> HTTP 1.1 -\> HTTP 2.0 -\> HTTP 3.0 (QUIC)](#http-10---http-11---http-20---http-30-quic)
    - [SOAP vs REST vs GraphQL vs RPC](#soap-vs-rest-vs-graphql-vs-rpc)
    - [代码优先（Code First） vs. API 优先（API First）](#代码优先code-first-vs-api-优先api-first)
    - [HTTP 状态码](#http-状态码)
    - [API 网关有什么作用？](#api-网关有什么作用)
    - [我们要如何设计高效安全的 API？](#我们要如何设计高效安全的-api)
    - [TCP/IP 封装](#tcpip-封装)
    - [为什么 Nginx 被称为“反向”代理？](#为什么-nginx-被称为反向代理)
    - [常见的负载均衡算法是什么？](#常见的负载均衡算法是什么)
    - [URL，URI，URN - 你知道它们之间的差别吗？](#urluriurn---你知道它们之间的差别吗)
  - [CI/CD](#cicd)
    - [简单解释 CI/CD 管道](#简单解释-cicd-管道)
    - [Netflix 技术栈（CI/CD 管道）](#netflix-技术栈cicd-管道)
  - [设计模式](#设计模式)
    - [MVC, MVP, MVVM, MVVM-C, and VIPER](#mvc-mvp-mvvm-mvvm-c-and-viper)
    - [每一位开发者都必须知道的 18 个关键设计模式](#每一位开发者都必须知道的-18-个关键设计模式)
  - [数据库](#数据库)
    - [关于云服务中不同类型的数据库的一个很好的备忘单](#关于云服务中不同类型的数据库的一个很好的备忘单)
    - [为数据库提供支持的八种数据结构](#为数据库提供支持的八种数据结构)
    - [一条 SQL 语句是如何在数据库中执行的？](#一条-sql-语句是如何在数据库中执行的)
    - [CAP 理论](#cap-理论)
    - [内存和存储类型](#内存和存储类型)
    - [可视化 SQL 查询](#可视化-sql-查询)
    - [SQL 语言](#sql-语言)
  - [缓存](#缓存)
    - [随处缓存数据](#随处缓存数据)
    - [为什么 Redis 那么快？](#为什么-redis-那么快)
    - [Redis 的使用场景](#redis-的使用场景)
    - [最佳缓存策略](#最佳缓存策略)
  - [微服务架构](#微服务架构)
    - [典型的微服务架构长啥样？](#典型的微服务架构长啥样)
    - [微服务最佳实践](#微服务最佳实践)
    - [微服务通常使用哪些技术栈？](#微服务通常使用哪些技术栈)
    - [为什么 Kafka 快？](#为什么-kafka-快)
  - [支付系统](#支付系统)
    - [如何学习支付系统？](#如何学习支付系统)
    - [信用卡为何被称为“银行最赚钱的产品”？VISA/万事达卡是如何赚钱的？](#信用卡为何被称为银行最赚钱的产品visa万事达卡是如何赚钱的)
    - [当我们在商家处刷卡时，VISA 是如何运作的？](#当我们在商家处刷卡时visa-是如何运作的)
    - [Payment Systems Around The World Series (Part 1): Unified Payments Interface (UPI) in India](#payment-systems-around-the-world-series-part-1-unified-payments-interface-upi-in-india)
  - [DevOps](#devops)
    - [DevOps vs. SRE vs. Platform Engineering. What is the difference?](#devops-vs-sre-vs-platform-engineering-what-is-the-difference)
    - [k8s (Kubernetes)是什么？](#k8s-kubernetes是什么)
    - [Docker vs. Kubernetes。我们应该用哪一个？](#docker-vs-kubernetes我们应该用哪一个)
    - [Docker 的工作原理](#docker-的工作原理)
  - [GIT](#git)
    - [Git 命令是如何工作的？](#git-命令是如何工作的)
    - [Git 的工作原理](#git-的工作原理)
    - [Git merge vs. Git rebase](#git-merge-vs-git-rebase)
  - [云服务](#云服务)
    - [A nice cheat sheet of different cloud services (2023 edition)](#a-nice-cheat-sheet-of-different-cloud-services-2023-edition)
    - [What is cloud native?](#what-is-cloud-native)
  - [开发者生产力工具](#开发者生产力工具)
    - [可视化 JSON 文件](#可视化-json-文件)
    - [自动将代码转换为架构图](#自动将代码转换为架构图)
  - [Linux](#linux)
    - [Linux 文件系统解析](#linux-文件系统解析)
    - [你应该知道的 18 个最常用的 Linux 命令](#你应该知道的-18-个最常用的-linux-命令)
  - [安全](#安全)
    - [HTTPS 是如何工作的？](#https-是如何工作的)
    - [Oauth 2.0 Explained With Simple Terms.](#oauth-20-explained-with-simple-terms)
    - [Top 4 Forms of Authentication Mechanisms](#top-4-forms-of-authentication-mechanisms)
    - [Session, cookie, JWT, token, SSO, and OAuth 2.0 - what are they?](#session-cookie-jwt-token-sso-and-oauth-20---what-are-they)
    - [如何将密码安全地存储到数据库中，以及如何验证密码？](#如何将密码安全地存储到数据库中以及如何验证密码)
    - [Explaining JSON Web Token (JWT) to a 10 year old Kid](#explaining-json-web-token-jwt-to-a-10-year-old-kid)
    - [How does Google Authenticator (or other types of 2-factor authenticators) work?](#how-does-google-authenticator-or-other-types-of-2-factor-authenticators-work)
  - [现实世界中的案例学习](#现实世界中的案例学习)
    - [Netflix 的技术栈](#netflix-的技术栈)
    - [Twitter 架构 2022](#twitter-架构-2022)
    - [过去 15 年 Airbnb 微服务架构的演进之路](#过去-15-年-airbnb-微服务架构的演进之路)
    - [Monorepo vs. Microrepo.](#monorepo-vs-microrepo)
    - [如果是你，你要如何设计 Stack Overflow 网站？](#如果是你你要如何设计-stack-overflow-网站)
    - [Why did Amazon Prime Video monitoring move from serverless to monolithic? How can it save 90% cost?](#why-did-amazon-prime-video-monitoring-move-from-serverless-to-monolithic-how-can-it-save-90-cost)
    - [How does Disney Hotstar capture 5 Billion Emojis during a tournament?](#how-does-disney-hotstar-capture-5-billion-emojis-during-a-tournament)
    - [Discord 是怎样存储 Trillions Of Messages](#discord-是怎样存储-trillions-of-messages)
    - [How do video live streamings work on YouTube, TikTok live, or Twitch?](#how-do-video-live-streamings-work-on-youtube-tiktok-live-or-twitch)
  - [License](#license)

<!-- /TOC -->

## 通信协议

架构风格定义了应用编程接口（application programming interface，API）的不同组件之间是如何相互交互的。结果就是，通过提供设计和构建 API 的标准方法，它们一起保证了效率、可靠性以及与其他系统集成的便捷性。以下是最常用的风格：

<p>
  <img src="../../images/api-architecture-styles.png" style="width: 640px">
</p>

- SOAP：

  成熟、全面、基于 XML
  
  最适合企业应用
  
- RESTful：

  流行、易于实现的 HTTP 方法
  
  网络服务的理想之选

- GraphQL：

  查询语言、请求特定数据

  减少网络开销，更快的响应速度

- gRPC：

  现代、高性能协议缓冲

  适合微服务架构
  
- WebSocket：

  实时、双向、持久连接
  
  非常适合低延迟数据交换

- Webhook：

  事件驱动、HTTP 回调、异步

  事件发生时通知系统
  

### REST API vs. GraphQL

当涉及到 API 设计的时候，REST 和 GraphQL 分别都有其优劣。

下图显示了 REST 和 GraphQL 之间的简单比较。


<p>
  <img src="../../images/graphQL.jpg">
</p>

REST

- 使用标准的 HTTP 方法，例如 GET、POST、DELETE， 来进行 CRUD 操作
- 当你需要在独立服务或者应用之间的简单统一接口时，工作良好
- 缓存策略的实现很直接
- 缺点是可能需要多次往返，才能从不同的端点组装相关数据。

GraphQL

- 为客户端提供单一端点，从而实现所需数据的精确查询。
- 客户端在嵌套查询中指定所需的确切字段，而服务端返回仅包含这些字段的优化负载。
- 支持数据修改和实时通知订阅
- 非常适合来自多个来源的数据的聚合，并可以很好地满足快速变化的前端需求。
- 但是，它将复杂性转移到了前端，并且如果没有适当保护，则可能会允许滥用查询。
- 缓存策略可能比 REST 更复杂。

REST 和 GraphQL之间哪一个是最佳选择取决于应用和开发团队之间的特定需求。GraphQL 非常适合复杂或频繁变化的前端需求，而 REST 则适合那些更倾向于简单和一致的应用程序。

这两种 API 方法都不是灵丹妙药。仔细评估要求和权衡对于选择正确的 API 方法非常重要。REST 和 GraphQL 都是公开数据和支持现代应用程序的有效选项。

### gRPC 是如何工作的？

RPC（远程过程调用，Remote Procedure Call）之所以被称为“**远程**”是因为在微服务架构下，服务被部署到不同服务器时，它允许远程服务之间进行通信。从用户的角度来说，使用它就像使用本地函数调用一样。

下图说明了 **gRPC** 的整个数据流。

<p>
  <img src="../../images/grpc.jpg">
</p>

步骤 1：客户端发起一个 REST 调用。请求体通常是 JSON 格式。

步骤 2 - 4：订单服务（gRPC 客户端）收到 REST 调用后，对其进行转换，然后向支付服务发起一个 RPC 请求。gRPC 将**客户端存根（client stub）**编码为二进制格式，然后将其发送到低层的传输层。

步骤 5：使用 HTTP2，gRPC 向网络发送数据包。由于二进制编码和网络优化，gRPC 据说比 JSON 快 5 倍。

步骤 6 - 8：支付服务（gRPC 服务器）收到来自网络的数据包后，对其进行解码，然后调用服务器应用。

步骤 9 - 11：服务器应用返回调用结果，将其编码后发送到传输层。

步骤 12 - 14：订单服务接收数据包后解码，然后将结果发送给客户端应用。

### 什么是 webhook？

下图显示了轮询（polling）和 Webhook 之间的比较。

<p>
  <img src="../../images/webhook.jpeg" style="width: 680px" />
</p>

假设我们运行着一个电子商务网站。客户端通过 API 网关发送订单到订单服务，订单服务转到支付服务请求支付交易。支付服务接着与外部的支付服务提供商（payment service provider，PSP）交互以完成交易。

有两种处理与外部 PSP 通信的方法。

**1. 短轮询** 

在发送支付请求到 PSP 后，支付服务不断向 PSP 询问支付状态。几轮后，PSP 终于返回状态。

短轮询有两个缺点：
* 持续轮询状态需要消耗支付服务的资源。
* 外部服务与支付服务直接通信，从而产生安全漏洞。

**2. Webhook** 

我们可以向外部服务注册一个 webhook。这意味着：当你有请求更新的时候，通过某个 URL 对我进行回调。当 PSP 完成处理后，它会调用 HTTP 请求来更新支付状态。

这样就改变了编程范式，并且支付服务不再需要浪费资源来轮询支付状态。

那如果 PSP 用不回调怎么办？我们可以设置一个内部任务，每小时检查付款状态。

Webhook 通常被称为反向 API 或者推送 API，因为服务器向客户端发送 HTTP 请求。使用 webhook 时，我们需要注意三件事：

1. 我们需要为外部服务调用设计一个合适的 API。
2. 出于安全考虑，我们需要在 API 网关中设置适当的规则。
3. 我们需要在外部服务中注册正确的 URL。

### 如何改善 API 性能？

下图显示了改善 API 性能的五种常见技巧。

<p>
  <img src="../../images/api-performance.jpg">
</p>

分页（Pagination）

当结果很大的时候，常用此种优化方式。结果会流回客户端以提高服务响应能力。

异步日志记录（Asynchronous Logging）

同步日志记录每次调用时都会与磁盘进行交互，这会降低系统速度。异步日志记录首先将日志发送到无锁缓冲区并立即返回。日志将会被定期刷新到磁盘。这显著减少了 I/O 开销。

缓存（Caching）

我们可以将经常访问的数据缓存到缓冲区中。客户端可以先查询缓存，而不是直接访问数据库。如果缓存未命中，客户端可以查询数据库。像 Redis 这样的缓存将数据存储在内存中，因此和数据库相比，数据访问要快得多。

有效负载压缩（Payload Compression）

可以使用 gzip 等工具压缩请求和响应，这样，传输的数据大小会小得多。这可以加速上传和下载速度。

连接池（Connection Pool）

访问资源时，我们通常需要从数据库中加载数据。打开正关闭的数据库连接会增加大量开销。因此，我们应该通过一个包含打开的连接的连接池来连接数据库。连接池负责管理连接的生命周期。

### HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)

每一代 HTTP 都解决了些什么问题呢？

下图说明了每一代 HTTP 的主要特性。

<p>
  <img src="../../images/http3.jpg" />
</p>

- HTTP 1.0 在 1996 年才最终被确定下来并完整记录。对于同一服务器的每个请求都需要建立独立的 TCP 连接。

- HTTP 1.1 在 1997 年发布。TCP 连接可以保持打开状态以供重用（持久连接），但它并没有解决 HOL（head-of-line，队头）阻塞问题。

  HOL 阻塞 —— 当浏览器允许的并发请求数用完时，后续请求需要等待前面的请求完成。

- HTTP 2.0 在 2015 年发布。通过请求复用解决了 HOL 问题，在应用层消除了 HOL 阻塞，但在传输层（TCP）仍然存在 HOL。

  如图所示，HTTP 2.0 引入了 HTTP “流”：一种抽象，允许将不同的 HTTP 交换复用到同一个 TCP 连接上。每个流不需要按序发送。

- HTTP 3.0 第一稿于 2020 年发布。它是 HTTP 2.0 的拟议后继者。它使用 QUIC 替代 TCP 作为底层传输协议，从而消除了传输层的 HOL 阻塞。

QUIC 基于 UDP。它将流作为传输层的一等公民引入。QUIC 流共享相同的 QUIC 连接，因此创建新流不需要额外的握手和慢启动，但 QUIC 流是独立传送的，因此在大多数情况下，影响一个流的数据包丢失不会影响其他流。

### SOAP vs REST vs GraphQL vs RPC

下图显示了 API 时间轴和 API 风格比较。

随着时间的推移，发布了不同的 API 架构风格。它们每一个都有自己的标准化数据交换模式。

你可以在图中查看每种风格的用例。


<p>
  <img src="../../images/SOAP vs REST vs GraphQL vs RPC.jpeg" />
</p>


### 代码优先（Code First） vs. API 优先（API First）

下图显示了代码优先开发和 API 优先开发之间的区别。为什么我们要考虑 API 优先的设计呢？

<p>
  <img src="../../images/api_first.jpg" style="width: 680px" />
</p>


- 微服务增加了系统复杂性，我们划分服务，以提供系统的不同功能。虽然这种架构有利于解耦和分离，但是，我们还需要处理服务之间的各种通信。

在编写代码并仔细定义服务边界之前，最好先考虑下系统的复杂性。

- 不同的功能团队需要使用相同的语言，而专门的功能团队只负责自己的组件和服务。建议组织通过 API 设计使用相同的语言。

在写代码前，我们就可以模拟请求和响应来验证 API 设计。

- 提高软件质量和开发人员生产力。由于我们在项目启动时已经解决了大部分不确定因素，因此，整体开发过程会更加顺利，软件质量也会得到了很大的提高。

开发人员也会对这个过程感到满意，因为他们可以专注于功能开发，而不用协商突然的变化。

在项目生命周期结束时出现意外的可能性会降低。

因为我们先设计了API，所以可以在开发代码的同时设计测试。在某种程度上，使用API​​优先开发的同时也可以有 TDD（测试驱动设计）。

### HTTP 状态码

<p>
  <img src="../../images/http-status-code.jpg" style="width: 540px" />
</p>

HTTP 响应码分为五类：

- 信息性（Informational） (100-199) 
- 成功（Success） (200-299) 
- 重定向（Redirection） (300-399) 
- 客户端错误 (400-499) 
- 服务端错误 (500-599) 

### API 网关有什么作用？

下图显示了其细节。

<p>
  <img src="../../images/api_gateway.jpg" style="width: 520px" />
</p>

步骤 1 - 客户端发送 HTTP 请求给 API 网关。

步骤 2 - API 网关解析和验证 HTTP 请求的属性。 

步骤 3 - API 网关进行允许列表/拒绝列表检查。

步骤 4 - API 网关和身份提供商交互，进行身份​​验证和授权。

步骤 5 - 对请求应用速率规则，如果超过限制，请求将被拒绝。

步骤 6 和 7 - 现在，请求通过了基本检查，API 网关通过路径匹配找到要路由到的相关服务。

步骤 8 - API 网关将请求转换为合适对协议，然后将其发送给后端微服务。

步骤 9-12: API 网关可以正确处理错误，并且在错误需要较长时间才能恢复（熔断）对时候处理故障。它还可以利用 ELK (Elastic-Logstash-Kibana) 堆栈进行日志记录和监控。有时，我们还会在 API 网关中缓存数据。

### 我们要如何设计高效安全的 API？

下图用购物车的例子，显示了典型的 API 设计。

<p>
  <img src="../../images/safe-apis.jpg" />
</p>

注意，API 设计不仅仅是 URL 路径设计。大多数情况下，我们需要选择合适的资源名称、标识符和路径模式。设计合适的 HTTP 头部字段或者设计高效的 API 网关的限速规则同样重要。

### TCP/IP 封装 

数据是如何通过网络发送的？为什么在 OSI 模型中，我们需要那么多层？

<p>
  <img src="../../images/osi model.jpeg" />
</p>

上图显示了数据通过网络传输时如何被封装和解封装的。

步骤 1：当设备 A 通过 HTTP 协议经过网络向设备 B 发送数据时，它首先在应用层添加一个 HTTP 头。

步骤 2：然后一个 TCP 或者 UDP 标头被添加到数据中。在传输层将其封装成 TCP 报文段。标头包含源端口、目标端口和序列号。

步骤 3：接着在网络层增加 IP 标头，对这些报文段进行封装。IP 标头包含源/目标 IP 地址。

步骤 4：IP 在数据链路层，向数据报添加 MAC 标头，其中包含源/目标 MAC 地址。

步骤 5：封装后的数据帧被发送到物理层，然后以二进制位的形式通过网络发送。

步骤 6-10：当设备 B 从网络上接收到这些二进制位数据时，执行解封装过程（封装过程的反向过程）。逐层去除数据头部，最后，设备 B 得以读取数据。

网络模型中之所以需要层的概念，是因为每一层都专注于自己的职责。每层都可以依赖标头来处理指令，而不需要知道最后一层数据的含义。

### 为什么 Nginx 被称为“反向”代理？

下图显示了正向代理（𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐩𝐫𝐨𝐱𝐲）和反向代理（𝐫𝐞𝐯𝐞𝐫𝐬𝐞 𝐩𝐫𝐨𝐱𝐲）之间的区别。

<p>
  <img src="../../images/Forward Proxy v.s. Reverse Proxy2x.jpg" style="width: 720px" />
</p>

正向代理指的是位于用户设备和网络之间的服务器。

正向代理通常用于：

1. 保护客户端
2. 规避浏览限制
3. 阻止访问某些内容

反向代理指的是一个这样的服务器，它接收来自客户端的请求，将其转发给网络服务器，然后将结果返回给客户端，就好像代理服务器已经处理了请求一样。

反向代理适用于：

1. 保护服务端
2. 负载均衡
3. 缓存静态内容
4. 加密和解密 SSL 通信

### 常见的负载均衡算法是什么？

下图显示了六种常见的算法。

<p>
  <img src="../../images/lb-algorithms.jpg" />
</p>

- 静态算法

1. 轮询

    客户端请求按顺序发送到不同服务实例。这些服务通常要求是无状态的。
    
2. 粘性轮询

    轮询算法的改进版。如果 Alice 的第一个请求被发送给服务 A，那么她后续的请求也会被发送到服务 A。

3. 加权轮询

    管理员可以指定每个服务的权重。权重较高的服务比权重较低的其他服务处理更多请求。
    
4. 哈希值

    算法对传入请求的 IP 或者 URL 应用哈希函数。基于哈希函数的返回值将请求路由到相应实例。
    
- 动态算法

1. 最少连接数

    新请求将被发送到并发连接数最少的服务实例。

2. 最短响应时间

    新请求将被发送到响应最快的服务实例。

### URL，URI，URN - 你知道它们之间的差别吗？

下图显示了 URL、URI 和 URN 的比较。

<p>
  <img src="../../images/url-uri-urn.jpg" />
</p>

- URI 

URI 表示统一资源标识符（Uniform Resource Identifier）。它标识网络上的逻辑或物理资源。URL 和 URN 是 URI 的子类型。URL定位资源，而 URN 命名资源。

URI 由以下部分组成：
scheme:[//authority]path[?query][#fragment] 

- URL 

URL 表示统一资源定位符（Uniform Resource Locator），是 HTTP 的关键概念。它是网络上唯一资源的地址。它可以与 FTP 和 JDBC 等其他协议一起使用。

- URN 

URN 表示统一资源名称（Uniform Resource Name）。它使用 urn 方案。不能用 URN 来定位资源。图中给出了一个简单示例，它由命名空间和特定于命名空间的字符串组成。

如果您想了解有关该主题的更多详细信息，我建议您查看 [W3C 的说明](https://www.w3.org/TR/uri-clarification/)。

## CI/CD

### 简单解释 CI/CD 管道

<p>
  <img src="../../images/ci-cd-pipeline.jpg" style="width: 680px" />
</p>

第 1 节 - SDLC 和 CI/CD

软件开发生命周期（software development life cycle，SDLC）由几个关键阶段组成：开发、测试、部署和维护。CI/CD 自动化并集成这些阶段，以实现更快、更可靠的发布。

当代码被推送到 git 存储库时，它会触发自动构建和测试过程。端到端 (e2e) 测试用例被运行以验证代码。如果测试通过，代码可以自动部署到预发布（staging）/生产（production）环境。如果发现问题，代码将被发送回开发以修复错误。这种自动化为开发人员提供了快速反馈，并降低了生产中出现错误的风险。

第 2 节 - CI 和 CD 的区别

持续集成 (Continuous Integration，CI) 自动执行构建、测试和合并过程。只要提交代码，它就会运行测试以尽早检测集成问题。它鼓励频繁的代码提交和快速反馈。

持续交付 (Continuous Delivery，CD) 可自动执行基础架构更改和部署等发布流程。它确保可以通过自动化工作流程随时可靠地发布软件。CD 还可以自动执行生产部署之前所需的手动测试和批准步骤。

第 3 节 - CI/CD 管道

典型的 CI/CD 管道有几个相连的阶段：
- 开发者提交代码更改到源代码管理
- CI 服务器检测变更，然后触发构建
- 对代码进行编译测试（单元测试，集成测试）
- 将测试结果报告给开发者
- 一旦成功，就会将其部署到预发布环境
- 发布前，可能会在预发布环境上进行进一步测试
- CD 系统将批准的变更发布到生产环境

### Netflix 技术栈（CI/CD 管道）

<p>
  <img src="../../images/netflix-ci-cd.jpg" style="width: 720px" />
</p>

规划：Netflix 工程使用 JIRA 进行规划，使用 Confluence 进行文档编制。

编码：Java 是后端服务的主要编程语言，而其他语言则用于不同的场景。

构建：Gradle 主要用于构建，构建不同的 Gradle 插件以支持不同的使用场景。

打包：包和依赖项打包到 Amazon 系统映像 (AMI) 中以供发布。

测试：测试强调生产文化对构建混乱工具的关注。

部署：Netflix 使用自建的 Spinnaker 进行金丝雀部署（canary rollout deployment）
> 更多关于“金丝雀部署”，可以查看[这里](https://glossary.cncf.io/zh-cn/canary-deployment/)

监控：监控指标集中在 Atlas 中，使用 Kayenta 来检测异常情况。

事件（incident）报告：事件按照优先级调度，使用 PagerDuty 进行事件处理。


## 设计模式

### MVC, MVP, MVVM, MVVM-C, and VIPER

这些架构模式是应用程序开发（无论是是在 iOS 还是 Android 平台上）中最常用的模式。开发人员引入它们是为了克服早期模式的局限性。那么，它们有何不同？

<p>
  <img src="../../images/client arch patterns.png" style="width: 720px" />
</p>

- MVC，最古老的模式，最早可追溯到近 50 年前
- 每一种模式都有一个“视图”（view, V），负责显示内容和接收用户输入
- 大部分的模式都包括一个“模型（model，M）”，用来管理业务数据
- “控制器（Controller）”、“控制器（Presenter）”和“视图模型（View-Model）”是在视图和模型（VIPER 模式中的“实体”）

### 每一位开发者都必须知道的 18 个关键设计模式

模式是针对常见设计问题的可重用解决方案，以实现更顺畅高效的开发过程。它们是构建更好的软件结构的蓝图。下面是一些最流行的模式：

<p>
  <img src="../../images/18-oo-patterns.png" />
</p>

- 抽象工厂（Abstract Factory）模式：家庭创造者 —— 制作相关项的组合。
- 建造者（Builder）模式：乐高大师 —— 逐步构建对象，分离创建和外观。
- 原型（Prototype）模式：克隆制造者 —— 创建完备实例的副本。
- 单例（Singleton）模式：唯一实例 —— 一个只有一个实例的特殊类。 
- 适配器（Adapter）模式：通用插头 —— 连接具有不同接口的东西。
- 桥接（Bridge）模式：功能连接器 —— 将对象的工作方式连接到其功能。
- 组合（Composite）模式：树形构建器 —— 形成简单和负责部分的树形结构。
- 装饰器（Decorator）模式：定制器 —— 给对象添加功能而无需改变其内核。
- 外观（Facade）模式：一站式商店 ——通过单一简化接口来代表整个系统。
- 享元（Flyweight）模式：节约空间小能手 —— 高效共享小型可重用项。
- 代理（Proxy）模式：替身演员 —— 代表另一个对象，控制访问或者操作。
- 责任链（Chain of Responsibility）模式：请求中继 —— 将请求通过一系列对象传递，直至被处理。
- 命令（Command）模式：任务包装器 —— 将请求转化为一个准备就绪的对象。
- 迭代器（Iterator）模式：集合探索者 —— 逐个访问集合中的元素。
- 中介者（Mediator）模式：通信中心 —— 简化不同类之间的交互。
- 备忘录（Memento）模式：时间胶囊 —— 捕获并恢复对象状态。
- 观察者（Observer）模式：新闻广播员 —— 通知类其他对象的变化。
- 访问者（Visitor）模式：熟练的访客 —— 为类增加新操作而不对其进行更改。

## 数据库

### 关于云服务中不同类型的数据库的一个很好的备忘单

<p>
  <img src="../../images/cloud-dbs2.png" />
</p>

为你的项目选择正确的数据是一项复杂的任务。许多数据库选项都适合不同的场景，这很快就会导致决策疲劳。

我们希望这份备忘单能够提供高级指导，以帮你找到符合项目需求的正确服务，并避免潜在陷阱。

注意：Google 关于其数据库用例的文档有限。尽管我们尽力查看可用的内容并得出最佳选择，但某些条目可能需要更加准确。

### 为数据库提供支持的八种数据结构

根据使用场景不同，答案也不同。数据可以在内存或磁盘上建立索引。同样，数据格式也各不相同，例如数字、字符串、地理坐标等。系统可能是写入密集型的，也可能是读取密集型的。所有这些因素都会影响您对数据库索引格式的选择。

<p>
  <img src="../../images/8-ds-db.jpg" />
</p>

下面是一些用于索引数据的最流行的数据结构：

- 跳跃表（Skiplist）：常见的内存索引类型。在 Redis 中使用 
- 哈希索引（Hash index）：“Map” 数据结构（或者“Collection”）的一个非常见的实现
- SSTable：不可变的磁盘 “Map” 实现 
- LSM 树：Skiplist + SSTable。高写入吞吐量
- B 树（B-tree）：基于磁盘的方案。一致读写性能
- 倒排索引（Inverted index）：用于文档索引。在 Lucene 中使用
- 后缀树（Suffix tree）：用于字符串模式搜索
- R 树（R-tree）多维搜索，例如寻找最近邻

### 一条 SQL 语句是如何在数据库中执行的？

下图显示了 SQL 语句的执行过程。注意，不同数据库的架构不一样，下图演示的是一些常见设计。

<p>
  <img src="../../images/sql execution order in db.jpeg" style="width: 580px" />
</p>


步骤 1 - 通过传输层协议（例如，TCP）将 SQL 语句发送到数据库。

步骤 2 - 发送 SQL 语句到命令解析器，然后命令解析器对其进行语法和语义分析，生成查询树。

步骤 3 - 发送查询树到优化器。优化器创建执行计划。

步骤 4 - 发送执行计划到执行器。执行器根据执行检索数据。

步骤 5 - 访问方法提供执行所需的数据获取逻辑，从存储引擎检索数据。

步骤 6 - 访问方法决定 SQL 语句是否只读。如果是只读查询（SELECT 语句），就会将其传到缓冲区管理器以进行进一步处理。缓冲区管理器在缓存或者数据文件中查询数据。

步骤 7 - 如果是 UPDATE 或者 INSERT 语句，则将其传到事务管理器进行进一步处理。

步骤 8 - 事务期间，数据处于锁定模式。这由锁管理器保证。它还确保事务的 ACID 属性。

###  CAP 理论

CAP 理论是计算机科学中最著名的术语之一，但我打赌，不同的开发者对其有不同的理解。让我们来看看它是什么，以及为什么它会令人困惑。

<p>
  <img src="../../images/cap theorem.jpeg" />
</p>

CAP 理论指出，分布式系统不能同时提供这三个保证中的两个以上的保证。

**一致性（Consistency）**：一致性意味着，不管客户端连接到哪个节点，它们都同时看到相同的数据。

**可用性（Availability）**：可用性意味着，即使某些节点发生了故障，任何客户端请求都能得到响应。

**分区容错性（Partition Tolerance）**：分区表示两个节点之间的通信发生了中断。分区容错性意味着，尽管存在网络分区，系统仍能继续运行。

“三分之二”表述可能有用，**但这种简化可能会产生误导**。

1. 选择合适的数据库并不容易。仅仅根据 CAP 定理来证明我们的选择并不够。例如，公司不会只因为 Cassandra 是一个 AP 系统就选择它作为聊天应用。Cassandra 具有一系列不错的特性，使其成为存储聊天消息的理想选择。我们需要更深入地挖掘。

2. “CAP 仅限制了一小部分的设计空间：在存在分区的情况下实现完美的可用性和一致性是很少见的”。引自论文：十二年后的 CAP：“规则”是如何改变的（CAP Twelve Years Later: How the “Rules” Have Changed）。

3. 该理论是关于百分百可用性和一致性的。更现实的讨论是在没有网络分区的情况下，延迟和一致性之间的权衡。详情请参阅 PACELC 定理。

**CAP 理论真的有用吗？**

我认为它依然有用，因为它让我们能够进行一系列权衡讨论，但这只是故事的一部分。在选择正确的数据库时，我们需要更深入挖掘。

### 内存和存储类型

<p>
  <img src="../../images/Types_of_Memory_and_Storage.jpeg" style="width: 420px" />
</p>


### 可视化 SQL 查询

<p>
  <img src="../../images/sql-execution-order.jpg" style="width: 580px" />
</p>

SQL 语句由数据系统执行，包含以下几个执行步骤：

- 解析 SQL 语句并检查其有效性
- 将 SQL 语句转化为内部表达形式，例如，关系代数
- 优化内部表达形式，并创建利用索引信息的执行计划
- 执行计划并返回结果 

SQL 的执行是非常复杂的，涉及很多考虑因素，例如：

- 索引和缓存的使用
- 表连接的顺序
- 并发控制
- 事务管理

### SQL 语言 

1986 年，SQL (Structured Query Language，结构化查询语言) 成为标准。在接下来的 40 年间，它成为了关系数据库管理系统的主导语言。阅读最新标准（ANSI SQL 2016）可能会耗费你大量的时间。那么，我要怎样才能学习它呢？

<p>
  <img src="../../images/how-to-learn-sql.jpg" />
</p>

SQL 语言有五个组件：

- DDL：数据定义语言，例如 CREATE、ALTER、DROP 
- DQL：数据查询语言，，例如 SELECT 
- DML：数据操作语言，例如 INSERT、UPDATE、DELETE 
- DCL：数据控制语言，例如 GRANT、REVOKE 
- TCL：事务控制语言，例如 COMMIT、ROLLBACK 

对于一个后端工程师来说，你可能需要了解上面大多数组件。而作为一名数据分析师，你可能需要很好地了解 DQL。根据需求，选择与自己关系最大的主题吧。


## 缓存

### 随处缓存数据

下图说明了在典型架构中，我们缓存数据的位置。

<p>
  <img src="../../images/where do we cache data.jpeg" style="width: 720px" />
</p>

在这个架构中，有**多个层**。

1. 客户端应用：HTTP 响应可以由浏览器进行缓存。我们第一次通过 HTTP 请求数据，数据返回时在 HTTP 标头中包含过期策略；当我们再次请求数据时，客户端应用会先尝试从浏览器缓存中检索数据。
2. CDN：CDN 缓存静态网络资源。客户端可以就近从 CDN 节点检索数据。
3. 负载均衡器：负载均衡器也可以缓存资源。
4. 消息传递基础设施（Messaging infra）：消息代理首先将消息存储在磁盘上，然后消费者按需检索消息。根据保留策略（retention policy），数据会在 Kafka 集群中缓存一段时间。
5. 服务：服务存在多层缓存。如果数据没有缓存在 CPU 缓存中，那么服务会尝试从内存中检索数据。有时，服务会有二级缓存，来将数据存储到磁盘中。
6. 分布式缓存：像 Redis 这样的分布式缓存在内存中保存多个服务的键值对。和数据库相比，它能提供更好的读/写性能。
7. 全文搜索：有时，我们需要使用像 Elastic Search 这样的全文搜索来对文档或日志进行搜索。因此，搜索引擎中也会对数据副本进行索引。
8. 数据库：即使在数据库中，我们也有不同级别的缓存：
- WAL(Write-ahead Log)：在构建 B 树索引前，先将数据写入 WAL
- Bufferpool：一块内存区域，分配于缓存查询结果
- 物化视图（Materialized View）：预计算查询结果并将其存储在数据库表中，以获得更好的查询性能
- 事务日志：记录所有事务和数据库更新
- 复制日志：用于记录数据库集群中的复制状态

### 为什么 Redis 那么快？

主要有三个原因，如下图所示。

<p>
  <img src="../../images/why_redis_fast.jpeg" />
</p>


1. Redis 是一个基于 RAM 的数据存储。RAM 访问至少比随机磁盘访问快 1000 倍。
2. Redis 利用 IO 多路复用和单线程执行循环来提高执行效率。
3. Redis 利用多种高效的底层数据结构。

问题：另一种流行的内存存储是 Memcached。你知道Redis和Memcached的区别吗？

> 译者注：答案可以参考 [redis和memcached的区别和使用场景](https://cloud.tencent.com/developer/article/1692015)

您可能已经注意到该图的风格与我之前的帖子不同。请告诉我您更喜欢哪一个。

### Redis 的使用场景

<p>
  <img src="../../images/top-redis-use-cases.jpg" style="width: 520px" />
</p>

Redis 不仅仅是缓存。

Redis 可用于多种场景，如图所示。

- 会话（Session） 

  我们可以使用 Redis 在不同服务之间共享用户会话数据。

- 缓存（Cache） 

  我们可以使用 Redis 来缓存对象或页面，尤其是热点数据。

- 分布式锁 

  我们可以使用 Redis 字符串来获取分布式服务之间的锁。

- 计数器（Counter） 

  我们可以用它来统计文章的点赞数或阅读量。 

- 速率限制器（Rate limiter） 

  我们可以对某些用户 IP 应用速率限制器。

- 全局 ID 生成器（Global ID generator） 

  我们可以使用 Redis Int 作为全局 ID。 

- 购物车（Shopping cart） 

  我们可以使用 Redis Hash 来表示购物车中的键值对。

- 计算用户留存率 

  我们可以使用 Bitmap 来表示用户每天的登录情况并计算用户留存情况。

- 消息队列 

  我们可以使用 List 作为消息队列。 

- 排行（Ranking） 

  我们可以使用 ZSet 对文章进行排序。 

### 最佳缓存策略

设计大型系统通常需要仔细地考虑缓存。下面是五种常用的缓存策略。

<p>
  <img src="../../images/top_caching_strategy.jpeg" style="width: 680px" />
</p>



## 微服务架构

### 典型的微服务架构长啥样？

<p>
  <img src="../../images/typical-microservice-arch.jpg" style="width: 520px" />
</p>

上图显示了一个典型的微服务架构。

- 负载均衡器（Load Balancer）：它将传入的流量分发到多个后端服务。
- CDN (Content Delivery Network，内容分发网络)：CDN 是一组地理分布的服务器，用于保存静态内容以实现更快的传输。客户端首先在 CDN 查找内容，然后再进行后端服务。
- API 网关（API Gateway）：它处理进来的请求并将其路由到相关服务。它与身份提供者和服务发现进行通信。
- 身份提供者（Identity Provider）：负责处理用户的身份验证和授权。
- 服务注册和发现（Service Registry & Discovery）：该组件负责微服务注册和发现，此外，API 网关从此组件查找相关服务进行通信。
- 管理（Management）：该组件负责监控服务。
- 微服务：根据域不同来设计和部署微服务。每个域都有其自身的数据库。API 网关通过 REST API 或者其他协议与微服务进行通信，同一个域中的微服务使用 RPC （远程过程调用）相互通信。

微服务的优点：

- 可以对其进行快速设计、部署和水平扩展。
- 每个域都可以由专门的团队独立维护。
- 可以在每个域对业务需求进行定制，从而获得更好的支持。
  
### 微服务最佳实践

一图胜千言：开发微服务的 9 个最佳实践。

<p>
  <img src="../../images/microservice-best-practices.jpeg" />
</p>

开发微服务时，我们需要遵循以下最佳实践：

1. 为每个微服务使用单独的数据存储
2. 保持代码处于相似的成熟度 
3. 单独构建每个微服务 
4. 为每个微服务分配单一职责 
5. 部署到容器中 
6. 设计无状态服务 
7. 采用领域驱动设计
8. 设计微前端 
9. 编排微服务 

### 微服务通常使用哪些技术栈？

下面，你将看到一张显示微服务技术栈的图标，同时涉及开发阶段和生产阶段。

<p>
  <img src="../../images/microservice-tech.jpeg" />
</p>


▶️ 预生产（𝐏𝐫𝐞-𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧）

- 定义 API - 这为前后端之间建立契约。为此，我们可以使用 Postman 或者 OpenAPI。
- 开发 - Node.js 或 react 在前端开发中很是流行，而 java/python/go 则是后端开发的流行之选。此外，我们需要根据 API 定义更改 API 网关的配置。
- 持续集成 - JUnit 和 Jenkins 用于自动化测试。打包代码到 Docker 镜像并部署为微服务。

▶️ 生产（𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧）

- NGinx 是负载均衡的常见选择。Cloudflare 则提供 CDN (Content Delivery Network)功能。
- API 网关 - 我们可以使用 spring boot 作为网关，并 Eureka/Zookeeper 进行服务发现。
- 在云上部署微服务。可以选择 AWS、Microsoft Azure 或者 Google GCP。缓存和全文搜索 —— 通常选择 Redis 来缓存键值对。使用 Elasticsearch 进行全文搜索。
- 通信 - 为了使服务之间能够相互通信，我们可以使用 Kafka 或者 RPC。
- 持久化 - 可以使用 MySQL 或者 PostgreSQL 作为关系数据库，使用 Amazon S3 作为对象存储。如有必要，我们还可以使用 Cassandra 进行宽列存储。
- 管理和监控 - 为了管理如此多的微服务，常见的运维攻击包括 Prometheus、Elastic Stack 和 Kubernetes。

### 为什么 Kafka 快？

有许多设计决策为 Kafka 的性能做出了贡献。在这里，我们将关注其中两个设计决策。我们认为这两者最有分量。

<p>
  <img src="../../images/why_is_kafka_fast.jpeg" />
</p>

1. 第一个是 Kafka 对顺序 I/O 的依赖。
2. 赋予 Kafka 性能优势的第二个设计决策是它对于效率的关注：零拷贝原则（zero copy principle）。
 
上图说明了数据是如何在生产者和消费者之间传输的，以及零拷贝的含义。
 
- 步骤 1.1 - 1.3：生产者将数据写到磁盘中 
- 步骤 2：消费者无需零拷贝即可读取数据。

  * 2.1 从磁盘中将数据加载到操作系统缓存
  
  * 2.2 从操作系统缓存拷贝数据到 Kafka 应用

  * 2.3 Kafka 应用拷贝数据到 socket 缓存 

  * 2.4 从 socket 缓存拷贝数据到网卡
  
  * 2.5 网卡发送数据给消费者

 
- 步骤 3：消费者以零拷贝方式读取数据

  * 3.1 从磁盘加载数据到操作系统缓存
  * 3.2 操作系统缓存通过 sendfile() 命令，直接将数据拷贝到网卡
  * 3.3 网卡发送数据给消费者
 
零拷贝（Zero copy）是一种在应用程序上下文和内核上下文之间保存多个数据副本的快捷方式。

## 支付系统

### 如何学习支付系统？

<p>
  <img src="../../images/learn-payments.jpg" />
</p>

###  信用卡为何被称为“银行最赚钱的产品”？VISA/万事达卡是如何赚钱的？

下图显示了信用卡支付流程背后的经济学。
 
<p>
  <img src="../../images/how does visa makes money.jpg" style="width: 640px" />
</p>

1. 持卡人向商家支付 100 美元以购买产品。

2. 商家从使用量较高的信用卡中获益，并且需要为发卡机构和卡网络提供的支付服务进行补偿。收单银行向商家收取一定费用，称为“商家折扣费”。

3 - 4. 收单银行保留 0.25 美元作为收单加价，并向发卡行支付 1.75 美元作为互换费。商户折扣费应该覆盖互换费用。 

  互换费用由卡网络设定，因为每个商户与每个发卡行就费用进行谈判效率较低。

1. 卡网络与各银行建立网络评估和费用，银行每月支付卡网络服务费。例如，VISA 对每次刷卡收取 0.11% 的评估费，另加 0.0195 美元的使用费。

2. 持卡人向发卡行支付其服务费。

发卡行为何需要获得补偿呢？

- 即使持卡人未能向发卡行支付款项，发卡行仍需支付商家。
- 发卡行在持卡人向其支付之前就已支付商家。
- 发卡行有其他运营成本，包括管理客户账户、提供对账单、欺诈检测、风险管理、清算等。

### 当我们在商家处刷卡时，VISA 是如何运作的？

<p>
  <img src="../../images/visa_payment.jpeg" />
</p>


VISA, Mastercard, and American Express act as card networks for the clearing and settling of funds. The card acquiring bank and the card issuing bank can be – and often are – different. If banks were to settle transactions one by one without an intermediary, each bank would have to settle the transactions with all the other banks. This is quite inefficient.   
 
The diagram below shows VISA’s role in the credit card payment process. There are two flows involved. Authorization flow happens when the customer swipes the credit card. Capture and settlement flow happens when the merchant wants to get the money at the end of the day.
 
- Authorization Flow

Step 0: The card issuing bank issues credit cards to its customers. 
 
Step 1: The cardholder wants to buy a product and swipes the credit card at the Point of Sale (POS) terminal in the merchant’s shop.
 
Step 2: The POS terminal sends the transaction to the acquiring bank, which has provided the POS terminal.
 
Steps 3 and 4: The acquiring bank sends the transaction to the card network, also called the card scheme. The card network sends the transaction to the issuing bank for approval.
 
Steps 4.1, 4.2 and 4.3: The issuing bank freezes the money if the transaction is approved. The approval or rejection is sent back to the acquirer, as well as the POS terminal. 
 
- Capture and Settlement Flow

Steps 1 and 2: The merchant wants to collect the money at the end of the day, so they hit ”capture” on the POS terminal. The transactions are sent to the acquirer in batch. The acquirer sends the batch file with transactions to the card network.
 
Step 3: The card network performs clearing for the transactions collected from different acquirers, and sends the clearing files to different issuing banks.
 
Step 4: The issuing banks confirm the correctness of the clearing files, and transfer money to the relevant acquiring banks.
 
Step 5: The acquiring bank then transfers money to the merchant’s bank. 
 
Step 4: The card network clears up the transactions from different acquiring banks. Clearing is a process in which mutual offset transactions are netted, so the number of total transactions is reduced.
 
In the process, the card network takes on the burden of talking to each bank and receives service fees in return.

### Payment Systems Around The World Series (Part 1): Unified Payments Interface (UPI) in India


What’s UPI? UPI is an instant real-time payment system developed by the National Payments Corporation of India.

It accounts for 60% of digital retail transactions in India today.

UPI = payment markup language + standard for interoperable payments


<p>
  <img src="../../images/how-does-upi-work.png"  style="width: 600px" />
</p>


## DevOps

###  DevOps vs. SRE vs. Platform Engineering. What is the difference?

The concepts of DevOps, SRE, and Platform Engineering have emerged at different times and have been developed by various individuals and organizations. 

<p>
  <img src="../../images/devops-sre-platform.jpg" />
</p>

DevOps as a concept was introduced in 2009 by Patrick Debois and Andrew Shafer at the Agile conference. They sought to bridge the gap between software development and operations by promoting a collaborative culture and shared responsibility for the entire software development lifecycle. 

SRE, or Site Reliability Engineering, was pioneered by Google in the early 2000s to address operational challenges in managing large-scale, complex systems. Google developed SRE practices and tools, such as the Borg cluster management system and the Monarch monitoring system, to improve the reliability and efficiency of their services. 

Platform Engineering is a more recent concept, building on the foundation of SRE engineering. The precise origins of Platform Engineering are less clear, but it is generally understood to be an extension of the DevOps and SRE practices, with a focus on delivering a comprehensive platform for product development that supports the entire business perspective. 

It's worth noting that while these concepts emerged at different times. They are all related to the broader trend of improving collaboration, automation, and efficiency in software development and operations. 

### k8s (Kubernetes)是什么？

K8s is a container orchestration system. It is used for container deployment and management. Its design is greatly impacted by Google’s internal system Borg.

<p>
  <img src="../../images/k8s.jpeg" style="width: 680px" />
</p>

A k8s cluster consists of a set of worker machines, called nodes, that run containerized applications. Every cluster has at least one worker node.

The worker node(s) host the Pods that are the components of the application workload. The control plane manages the worker nodes and the Pods in the cluster. In production environments, the control plane usually runs across multiple computers, and a cluster usually runs multiple nodes, providing fault tolerance and high availability.

- Control Plane Components

1. API Server

    The API server talks to all the components in the k8s cluster. All the operations on pods are executed by talking to the API server.

2. Scheduler

    The scheduler watches pod workloads and assigns loads on newly created pods.

3. Controller Manager

    The controller manager runs the controllers, including Node Controller, Job Controller, EndpointSlice Controller, and ServiceAccount Controller.

4. Etcd
    
    etcd is a key-value store used as Kubernetes' backing store for all cluster data.

- Nodes

1. Pods

    A pod is a group of containers and is the smallest unit that k8s administers. Pods have a single IP address applied to every container within the pod.

2. Kubelet

    An agent that runs on each node in the cluster. It ensures containers are running in a Pod.

3. Kube Proxy

    Kube-proxy is a network proxy that runs on each node in your cluster. It routes traffic coming into a node from the service. It forwards requests for work to the correct containers.

### Docker vs. Kubernetes。我们应该用哪一个？

<p>
  <img src="../../images/docker-vs-k8s.jpg" style="width: 680px" />
</p>


What is Docker ? 

Docker is an open-source platform that allows you to package, distribute, and run applications in isolated containers. It focuses on containerization, providing lightweight environments that encapsulate applications and their dependencies. 

What is Kubernetes ? 

Kubernetes, often referred to as K8s, is an open-source container orchestration platform. It provides a framework for automating the deployment, scaling, and management of containerized applications across a cluster of nodes. 

How are both different from each other ? 

Docker: Docker operates at the individual container level on a single operating system host. 

You must manually manage each host and setting up networks, security policies, and storage for multiple related containers can be complex. 

Kubernetes: Kubernetes operates at the cluster level. It manages multiple containerized applications across multiple hosts, providing automation for tasks like load balancing, scaling, and ensuring the desired state of applications. 

In short, Docker focuses on containerization and running containers on individual hosts, while Kubernetes specializes in managing and orchestrating containers at scale across a cluster of hosts. 

### Docker 的工作原理

The diagram below shows the architecture of Docker and how it works when we run “docker build”, “docker pull” 
and “docker run”. 

<p>
  <img src="../../images/docker.jpg" style="width: 680px" />
</p>

There are 3 components in Docker architecture: 

- Docker client 
    
    The docker client talks to the Docker daemon. 

- Docker host 

    The Docker daemon listens for Docker API requests and manages Docker objects such as images, containers, networks, and volumes. 

- Docker registry 

    A Docker registry stores Docker images. Docker Hub is a public registry that anyone can use. 

Let’s take the “docker run” command as an example. 

  1. Docker pulls the image from the registry. 
  1. Docker creates a new container. 
  1. Docker allocates a read-write filesystem to the container. 
  1. Docker creates a network interface to connect the container to the default network. 
  1. Docker starts the container.

## GIT

### Git 命令是如何工作的？

To begin with, it's essential to identify where our code is stored. The common assumption is that there are only two locations - one on a remote server like Github and the other on our local machine. However, this isn't entirely accurate. Git maintains three local storages on our machine, which means that our code can be found in four places: 

<p>
  <img src="../../images/git-commands.png" style="width: 600px" />
</p>


- Working directory: where we edit files 
- Staging area: a temporary location where files are kept for the next commit 
- Local repository: contains the code that has been committed 
- Remote repository: the remote server that stores the code 

Most Git commands primarily move files between these four locations. 

### Git 的工作原理

The diagram below shows the Git workflow. 

<p>
  <img src="../../images/git-workflow.jpeg" style="width: 520px" />
</p>


Git is a distributed version control system. 

Every developer maintains a local copy of the main repository and edits and commits to the local copy. 

The commit is very fast because the operation doesn’t interact with the remote repository. 

If the remote repository crashes, the files can be recovered from the local repositories. 

### Git merge vs. Git rebase

What are the differences?

<p>
  <img src="../../images/git-merge-git-rebase.jpeg" style="width: 680px" />
</p>


When we **merge changes** from one Git branch to another, we can use ‘git merge’ or ‘git rebase’. The diagram below shows how the two commands work.

**Git merge**

This creates a new commit G’ in the main branch. G’ ties the histories of both main and feature branches.

Git merge is **non-destructive**. Neither the main nor the feature branch is changed.

**Git rebase**

Git rebase moves the feature branch histories to the head of the main branch. It creates new commits E’, F’, and G’ for each commit in the feature branch.

The benefit of rebase is that it has a linear **commit history**.

Rebase can be dangerous if “the golden rule of git rebase” is not followed.

**The Golden Rule of Git Rebase**

Never use it on public branches!

## 云服务

### A nice cheat sheet of different cloud services (2023 edition)

<p>
  <img src="../../images/cloud-compare.jpg" />
</p>


### What is cloud native?

Below is a diagram showing the evolution of architecture and processes since the 1980s. 

<p>
  <img src="../../images/cloud-native.jpeg" style="width: 640px" />
</p>

Organizations can build and run scalable applications on public, private, and hybrid clouds using cloud native technologies. 

This means the applications are designed to leverage cloud features, so they are resilient to load and easy to scale. 

Cloud native includes 4 aspects: 

1. Development process 

    This has progressed from waterfall to agile to DevOps. 

2. Application Architecture 

    The architecture has gone from monolithic to microservices. Each service is designed to be small, adaptive to the limited resources in cloud containers. 

3. Deployment & packaging 

    The applications used to be deployed on physical servers. Then around 2000, the applications that were not sensitive to latency were usually deployed on virtual servers. With cloud native applications, they are packaged into docker images and deployed in containers. 

4. Application infrastructure 

    The applications are massively deployed on cloud infrastructure instead of self-hosted servers. 

## 开发者生产力工具

### 可视化 JSON 文件

Nested JSON files are hard to read.

**JsonCrack** generates graph diagrams from JSON files and makes them easy to read.

Additionally, the generated diagrams can be downloaded as images.

<p>
  <img src="../../images/json-cracker.jpeg" />
</p>


### 自动将代码转换为架构图

<p>
  <img src="../../images/diagrams_as_code.jpeg" style="width: 640px" />
</p>


What does it do?

- Draw the cloud system architecture in Python code.
- Diagrams can also be rendered directly inside the Jupyter Notebooks.
- No design tools are needed. 
- Supports the following providers: AWS, Azure, GCP, Kubernetes, Alibaba Cloud, Oracle Cloud, etc. 
 
[Github repo](https://github.com/mingrammer/diagrams)

## Linux

### Linux 文件系统解析

<p>
  <img src="../../images/linux-file-systems.jpg" style="width: 680px" />
</p>

The Linux file system used to resemble an unorganized town where individuals constructed their houses wherever they pleased. However, in 1994, the Filesystem Hierarchy Standard (FHS) was introduced to bring order to the Linux file system.

By implementing a standard like the FHS, software can ensure a consistent layout across various Linux distributions. Nonetheless, not all Linux distributions strictly adhere to this standard. They often incorporate their own unique elements or cater to specific requirements.
To become proficient in this standard, you can begin by exploring. Utilize commands such as "cd" for navigation and "ls" for listing directory contents. Imagine the file system as a tree, starting from the root (/). With time, it will become second nature to you, transforming you into a skilled Linux administrator.

### 你应该知道的 18 个最常用的 Linux 命令

Linux commands are instructions for interacting with the operating system. They help manage files, directories, system processes, and many other aspects of the system. You need to become familiar with these commands in order to navigate and maintain Linux-based systems efficiently and effectively. 

This diagram below shows popular Linux commands: 

<p>
  <img src="../../images/18 Most-Used Linux Commands You Should Know-01.jpeg" style="width: 680px" />
</p>


- ls - List files and directories 
- cd - Change the current directory 
- mkdir - Create a new directory 
- rm - Remove files or directories 
- cp - Copy files or directories 
- mv - Move or rename files or directories 
- chmod - Change file or directory permissions 
- grep - Search for a pattern in files 
- find - Search for files and directories 
- tar - manipulate tarball archive files 
- vi - Edit files using text editors 
- cat - display the content of files 
- top - Display processes and resource usage 
- ps - Display processes information 
- kill - Terminate a process by sending a signal 
- du - Estimate file space usage 
- ifconfig - Configure network interfaces  
- ping - Test network connectivity between hosts 

## 安全

### HTTPS 是如何工作的？

Hypertext Transfer Protocol Secure (HTTPS) is an extension of the Hypertext Transfer Protocol (HTTP.) HTTPS transmits encrypted data using Transport Layer Security (TLS.) If the data is hijacked online, all the hijacker gets is binary code. 

<p>
  <img src="../../images/https.jpg" />
</p>


How is the data encrypted and decrypted?

Step 1 - The client (browser) and the server establish a TCP connection.

Step 2 - The client sends a “client hello” to the server. The message contains a set of necessary encryption algorithms (cipher suites) and the latest TLS version it can support. The server responds with a “server hello” so the browser knows whether it can support the algorithms and TLS version.

The server then sends the SSL certificate to the client. The certificate contains the public key, host name, expiry dates, etc. The client validates the certificate. 

Step 3 - After validating the SSL certificate, the client generates a session key and encrypts it using the public key. The server receives the encrypted session key and decrypts it with the private key. 

Step 4 - Now that both the client and the server hold the same session key (symmetric encryption), the encrypted data is transmitted in a secure bi-directional channel.

Why does HTTPS switch to symmetric encryption during data transmission? There are two main reasons:

1. Security: The asymmetric encryption goes only one way. This means that if the server tries to send the encrypted data back to the client, anyone can decrypt the data using the public key.

2. Server resources: The asymmetric encryption adds quite a lot of mathematical overhead. It is not suitable for data transmissions in long sessions.

### Oauth 2.0 Explained With Simple Terms. 

OAuth 2.0 is a powerful and secure framework that allows different applications to securely interact with each other on behalf of users without sharing sensitive credentials. 

<p>
  <img src="../../images/oAuth2.jpg" />
</p>

The entities involved in OAuth are the User, the Server, and the Identity Provider (IDP). 

What Can an OAuth Token Do? 

When you use OAuth, you get an OAuth token that represents your identity and permissions. This token can do a few important things: 

Single Sign-On (SSO): With an OAuth token, you can log into multiple services or apps using just one login, making life easier and safer. 

Authorization Across Systems: The OAuth token allows you to share your authorization or access rights across various systems, so you don't have to log in separately everywhere. 

Accessing User Profile: Apps with an OAuth token can access certain parts of your user profile that you allow, but they won't see everything. 

Remember, OAuth 2.0 is all about keeping you and your data safe while making your online experiences seamless and hassle-free across different applications and services.

### Top 4 Forms of Authentication Mechanisms 

<p>
  <img src="../../images/top4-most-used-auth.jpg" />
</p>

1. SSH Keys: 
   
    Cryptographic keys are used to access remote systems and servers securely 

1. OAuth Tokens: 

    Tokens that provide limited access to user data on third-party applications 

1. SSL Certificates: 
  
    Digital certificates ensure secure and encrypted communication between servers and clients 

1. Credentials: 

    User authentication information is used to verify and grant access to various systems and services

### Session, cookie, JWT, token, SSO, and OAuth 2.0 - what are they?

These terms are all related to user identity management. When you log into a website, you declare who you are (identification). Your identity is verified (authentication), and you are granted the necessary permissions (authorization). Many solutions have been proposed in the past, and the list keeps growing.

<p>
  <img src="../../images/session.jpeg" />
</p>

From simple to complex, here is my understanding of user identity management:

- WWW-Authenticate is the most basic method. You are asked for the username and password by the browser. As a result of the inability to control the login life cycle, it is seldom used today.

- A finer control over the login life cycle is session-cookie. The server maintains session storage, and the browser keeps the ID of the session. A cookie usually only works with browsers and is not mobile app friendly.

- To address the compatibility issue, the token can be used. The client sends the token to the server, and the server validates the token. The downside is that the token needs to be encrypted and decrypted, which may be time-consuming.

- JWT is a standard way of representing tokens. This information can be verified and trusted because it is digitally signed. Since JWT contains the signature, there is no need to save session information on the server side.

- By using SSO (single sign-on), you can sign on only once and log in to multiple websites. It uses CAS (central authentication service) to maintain cross-site information.

- By using OAuth 2.0, you can authorize one website to access your information on another website.

### 如何将密码安全地存储到数据库中，以及如何验证密码？

<p>
  <img src="../../images/salt.jpg" style="width: 720px" />
</p>

 
**Things NOT to do**

- Storing passwords in plain text is not a good idea because anyone with internal access can see them.

- Storing password hashes directly is not sufficient because it is pruned to precomputation attacks, such as rainbow tables. 

- To mitigate precomputation attacks, we salt the passwords. 

**What is salt?**

According to OWASP guidelines, “a salt is a unique, randomly generated string that is added to each password as part of the hashing process”.
 
**How to store a password and salt?**

1. the hash result is unique to each password.
1. The password can be stored in the database using the following format: hash(password + salt).

**如何验证密码？**

To validate a password, it can go through the following process:

1. A client enters the password.
2. The system fetches the corresponding salt from the database.
3. The system appends the salt to the password and hashes it. Let’s call the hashed value H1.
4. The system compares H1 and H2, where H2 is the hash stored in the database. If they are the same, the password is valid. 

### Explaining JSON Web Token (JWT) to a 10 year old Kid

<p>
  <img src="../../images/jwt.jpg" />
</p>

Imagine you have a special box called a JWT. Inside this box, there are three parts: a header, a payload, and a signature.

The header is like the label on the outside of the box. It tells us what type of box it is and how it's secured. It's usually written in a format called JSON, which is just a way to organize information using curly braces { } and colons : .

The payload is like the actual message or information you want to send. It could be your name, age, or any other data you want to share. It's also written in JSON format, so it's easy to understand and work with.
Now, the signature is what makes the JWT secure. It's like a special seal that only the sender knows how to create. The signature is created using a secret code, kind of like a password. This signature ensures that nobody can tamper with the contents of the JWT without the sender knowing about it.

When you want to send the JWT to a server, you put the header, payload, and signature inside the box. Then you send it over to the server. The server can easily read the header and payload to understand who you are and what you want to do.

### How does Google Authenticator (or other types of 2-factor authenticators) work?

Google Authenticator is commonly used for logging into our accounts when 2-factor authentication is enabled. How does it guarantee security?
 
Google Authenticator is a software-based authenticator that implements a two-step verification service. The diagram below provides detail. 

<p>
  <img src="../../images/google_authenticate.jpeg" />
</p>


There are two stages involved:

- Stage 1 - The user enables Google two-step verification.
- Stage 2 - The user uses the authenticator for logging in, etc.

Let’s look at these stages.
 
**Stage 1**

Steps 1 and 2: Bob opens the web page to enable two-step verification. The front end requests a secret key. The authentication service generates the secret key for Bob and stores it in the database.
 
Step 3: The authentication service returns a URI to the front end. The URI is composed of a key issuer, username, and secret key. The URI is displayed in the form of a QR code on the web page.
 
Step 4: Bob then uses Google Authenticator to scan the generated QR code. The secret key is stored in the authenticator.

**Stage 2**
Steps 1 and 2: Bob wants to log into a website with Google two-step verification. For this, he needs the password. Every 30 seconds, Google Authenticator generates a 6-digit password using TOTP (Time-based One Time Password) algorithm. Bob uses the password to enter the website.
 
Steps 3 and 4: The frontend sends the password Bob enters to the backend for authentication. The authentication service reads the secret key from the database and generates a 6-digit password using the same TOTP algorithm as the client.
 
Step 5: The authentication service compares the two passwords generated by the client and the server, and returns the comparison result to the frontend. Bob can proceed with the login process only if the two passwords match.
 
Is this authentication mechanism safe? 

- Can the secret key be obtained by others? 

    We need to make sure the secret key is transmitted using HTTPS. The authenticator client and the database store the secret key, and we need to make sure the secret keys are encrypted.

- Can the 6-digit password be guessed by hackers?
    
    No. The password has 6 digits, so the generated password has 1 million potential combinations. Plus, the password changes every 30 seconds. If hackers want to guess the password in 30 seconds, they need to enter 30,000 combinations per second.


##  现实世界中的案例学习

### Netflix 的技术栈

This post is based on research from many Netflix engineering blogs and open-source projects. If you come across any inaccuracies, please feel free to inform us.

<p>
  <img src="../../images/netflix tech stack.png" style="width: 680px" />
</p>

**Mobile and web**: Netflix has adopted Swift and Kotlin to build native mobile apps. For its web application, it uses React.

**Frontend/server communication**: Netflix uses GraphQL.

**Backend services**: Netflix relies on ZUUL, Eureka, the Spring Boot framework, and other technologies.

**Databases**: Netflix utilizes EV cache, Cassandra, CockroachDB, and other databases.

**Messaging/streaming**: Netflix employs Apache Kafka and Fink for messaging and streaming purposes.

**Video storage**: Netflix uses S3 and Open Connect for video storage.

**Data processing**: Netflix utilizes Flink and Spark for data processing, which is then visualized using Tableau. Redshift is used for processing structured data warehouse information.

**CI/CD**: Netflix employs various tools such as JIRA, Confluence, PagerDuty, Jenkins, Gradle, Chaos Monkey, Spinnaker, Atlas, and more for CI/CD processes.

### Twitter 架构 2022

Yes, this is the real Twitter architecture. It is posted by Elon Musk and redrawn by us for better readability. 

<p>
  <img src="../../images/twitter-arch.jpeg" />
</p>


### 过去 15 年 Airbnb 微服务架构的演进之路

Airbnb’s microservice architecture went through 3 main stages. 

<p>
  <img src="../../images/airbnb_arch.jpeg" />
</p>


Monolith (2008 - 2017)

Airbnb began as a simple marketplace for hosts and guests. This is built in a Ruby on Rails application - the monolith. 

What’s the challenge?

- Confusing team ownership + unowned code
- Slow deployment 

Microservices (2017 - 2020)

Microservice aims to solve those challenges. In the microservice architecture, key services include:

- Data fetching service
- Business logic data service
- Write workflow service
- UI aggregation service
- Each service had one owning team

What’s the challenge?

Hundreds of services and dependencies were difficult for humans to manage.

Micro + macroservices (2020 - present)

This is what Airbnb is working on now. The micro and macroservice hybrid model focuses on the unification of APIs.

### Monorepo vs. Microrepo. 

Which is the best? Why do different companies choose different options? 

<p>
  <img src="../../images/monorepo-microrepo.jpg" />
</p>


Monorepo isn't new; Linux and Windows were both created using Monorepo. To improve scalability and build speed, Google developed its internal dedicated toolchain to scale it faster and strict coding quality standards to keep it consistent. 

Amazon and Netflix are major ambassadors of the Microservice philosophy. This approach naturally separates the service code into separate repositories. It scales faster but can lead to governance pain points later on. 

Within Monorepo, each service is a folder, and every folder has a BUILD config and OWNERS permission control. Every service member is responsible for their own folder. 

On the other hand, in Microrepo, each service is responsible for its repository, with the build config and permissions typically set for the entire repository. 

In Monorepo, dependencies are shared across the entire codebase regardless of your business, so when there's a version upgrade, every codebase upgrades their version. 

In Microrepo, dependencies are controlled within each repository. Businesses choose when to upgrade their versions based on their own schedules. 

Monorepo has a standard for check-ins. Google's code review process is famously known for setting a high bar, ensuring a coherent quality standard for Monorepo, regardless of the business. 

Microrepo can either set its own standard or adopt a shared standard by incorporating the best practices. It can scale faster for business, but the code quality might be a bit different. 
Google engineers built Bazel, and Meta built Buck. There are other open-source tools available, including Nix, Lerna, and others. 

Over the years, Microrepo has had more supported tools, including Maven and Gradle for Java, NPM for NodeJS, and CMake for C/C++, among others. 

### 如果是你，你要如何设计 Stack Overflow 网站？

If your answer is on-premise servers and monolith (on the bottom of the following image), you would likely fail the interview, but that's how it is built in reality!

<p>
  <img src="../../images/stackoverflow.jpg" />
</p>


**What people think it should look like**

The interviewer is probably expecting something like the top portion of the picture.

- Microservice is used to decompose the system into small components.
- Each service has its own database. Use cache heavily.
- The service is sharded.
- The services talk to each other asynchronously through message queues.
- The service is implemented using Event Sourcing with CQRS.
- Showing off knowledge in distributed systems such as eventual consistency, CAP theorem, etc.

**What it actually is**

Stack Overflow serves all the traffic with only 9 on-premise web servers, and it’s on monolith! It has its own servers and does not run on the cloud.

This is contrary to all our popular beliefs these days. 

### Why did Amazon Prime Video monitoring move from serverless to monolithic? How can it save 90% cost?

The diagram below shows the architecture comparison before and after the migration. 

<p>
  <img src="../../images/serverless-to-monolithic.jpeg" />
</p>


What is Amazon Prime Video Monitoring Service? 

Prime Video service needs to monitor the quality of thousands of live streams. The monitoring tool automatically analyzes the streams in real time and identifies quality issues like block corruption, video freeze, and sync problems. This is an important process for customer satisfaction. 

There are 3 steps: media converter, defect detector, and real-time notification. 

- What is the problem with the old architecture? 

  The old architecture was based on Amazon Lambda, which was good for building services quickly. However, it was not cost-effective when running the architecture at a high scale. The two most expensive operations are: 

1. The orchestration workflow - AWS step functions charge users by state transitions and the orchestration performs multiple state transitions every second. 

2. Data passing between distributed components - the intermediate data is stored in Amazon S3 so that the next stage can download. The download can be costly when the volume is high. 

- Monolithic architecture saves 90% cost 

  A monolithic architecture is designed to address the cost issues. There are still 3 components, but the media converter and defect detector are deployed in the same process, saving the cost of passing data over the network. Surprisingly, this approach to deployment architecture change led to 90% cost savings! 

This is an interesting and unique case study because microservices have become a go-to and fashionable choice in the tech industry. It's good to see that we are having more discussions about evolving the architecture and having more honest discussions about its pros and cons. Decomposing components into distributed microservices comes with a cost. 

- What did Amazon leaders say about this? 
  
  Amazon CTO Werner Vogels: “Building **evolvable software systems** is a strategy, not a religion. And revisiting your architecture with an open mind is a must.” 

Ex Amazon VP Sustainability Adrian Cockcroft: “The Prime Video team had followed a path I call **Serverless First**…I don’t advocate **Serverless Only**”. 

### How does Disney Hotstar capture 5 Billion Emojis during a tournament?

<p>
  <img src="../../images/hotstar_emojis.jpeg" style="width: 720px" />
</p>


1. Clients send emojis through standard HTTP requests. You can think of Golang Service as a typical Web Server. Golang is chosen because it supports concurrency well. Threads in Golang are lightweight.

2. Since the write volume is very high, Kafka (message queue) is used as a buffer.

3. Emoji data are aggregated by a streaming processing service called Spark. It aggregates data every 2 seconds, which is configurable. There is a trade-off to be made based on the interval. A shorter interval means emojis are delivered to other clients faster but it also means more computing resources are needed.

4. Aggregated data is written to another Kafka. 

5. The PubSub consumers pull aggregated emoji data from Kafka. 

6. Emojis are delivered to other clients in real-time through the PubSub infrastructure. The PubSub infrastructure is interesting. Hotstar considered the following protocols: Socketio, NATS, MQTT, and gRPC, and settled with MQTT.
 
A similar design is adopted by LinkedIn which streams a million likes/sec.

### Discord 是怎样存储 Trillions Of Messages 

The diagram below shows the evolution of message storage at Discord: 

<p>
  <img src="../../images/discord-store-messages.jpg" />
</p>


MongoDB ➡️ Cassandra ➡️ ScyllaDB 

In 2015, the first version of Discord was built on top of a single MongoDB replica. Around Nov 2015, MongoDB stored 100 million messages and the RAM couldn’t hold the data and index any longer. The latency became unpredictable. Message storage needs to be moved to another database. Cassandra was chosen. 

In 2017, Discord had 12 Cassandra nodes and stored billions of messages. 

At the beginning of 2022, it had 177 nodes with trillions of messages. At this point, latency was unpredictable, and maintenance operations became too expensive to run. 

There are several reasons for the issue: 

- Cassandra uses the LSM tree for the internal data structure. The reads are more expensive than the writes. There can be many concurrent reads on a server with hundreds of users, resulting in hotspots. 
- Maintaining clusters, such as compacting SSTables, impacts performance. 
- Garbage collection pauses would cause significant latency spikes 

ScyllaDB is Cassandra compatible database written in C++. Discord redesigned its architecture to have a monolithic API, a data service written in Rust, and ScyllaDB-based storage. 

The p99 read latency in ScyllaDB is 15ms compared to 40-125ms in Cassandra. The p99 write latency is 5ms compared to 5-70ms in Cassandra. 

### How do video live streamings work on YouTube, TikTok live, or Twitch?
 
Live streaming differs from regular streaming because the video content is sent via the internet in real-time, usually with a latency of just a few seconds.
 
The diagram below explains what happens behind the scenes to make this possible.

<p>
  <img src="../../images/live_streaming_updated.jpg" style="width: 640px" />
</p>

 
Step 1: The raw video data is captured by a microphone and camera. The data is sent to the server side.
 
Step 2: The video data is compressed and encoded. For example, the compressing algorithm separates the background and other video elements. After compression, the video is encoded to standards such as H.264. The size of the video data is much smaller after this step.
 
Step 3: The encoded data is divided into smaller segments, usually seconds in length, so it takes much less time to download or stream.
 
Step 4: The segmented data is sent to the streaming server. The streaming server needs to support different devices and network conditions. This is called ‘Adaptive Bitrate Streaming.’ This means we need to produce multiple files at different bitrates in steps 2 and 3.
 
Step 5: The live streaming data is pushed to edge servers supported by CDN (Content Delivery Network.) Millions of viewers can watch the video from an edge server nearby. CDN significantly lowers data transmission latency. 
 
Step 6: The viewers’ devices decode and decompress the video data and play the video in a video player.
 
Steps 7 and 8: If the video needs to be stored for replay, the encoded data is sent to a storage server, and viewers can request a replay from it later.
 
Standard protocols for live streaming include:

- RTMP (Real-Time Messaging Protocol): This was originally developed by Macromedia to transmit data between a Flash player and a server. Now it is used for streaming video data over the internet. Note that video conferencing applications like Skype use RTC (Real-Time Communication) protocol for lower latency.
- HLS (HTTP Live Streaming): It requires the H.264 or H.265 encoding. Apple devices accept only HLS format.
- DASH (Dynamic Adaptive Streaming over HTTP): DASH does not support Apple devices.
- Both HLS and DASH support adaptive bitrate streaming.

## License

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></a></p>
