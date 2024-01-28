<p>
  <a href="https://blog.bytebytego.com/?utm_source=site"><img src="../images/banner.jpg" /> </a>
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

# System Design 101

시각 자료와 간단한 용어를 사용하여 복잡한 시스템을 설명합니다. 

시스템 디자인 면접을 준비 중이거나 단순히 시스템이 표면 아래에서 어떻게 작동하는지 이해하고 싶으신 분이라면 이 리포지토리가 도움이 되길 바랍니다.

# Table of Contents

<!-- TOC toc.levels=2 -->

- [Communication protocols](#communication-protocols)
  - [REST API vs. GraphQL](#rest-api-vs-graphql)
  - [gRPC는 어떻게 작동하나요?](#grpc는-어떻게-작동하나요)
  - [webhook이란 무엇인가요?](#what-is-a-webhook)
  - [API 성능을 개선하는 방법은 무엇인가요?](#api-성능을-개선하는-방법은-무엇인가요)
  - [HTTP 1.0 -\> HTTP 1.1 -\> HTTP 2.0 -\> HTTP 3.0 (QUIC)](#http-10---http-11---http-20---http-30-quic)
  - [SOAP vs REST vs GraphQL vs RPC](#soap-vs-rest-vs-graphql-vs-rpc)
  - [Code First vs. API First](#code-first-vs-api-first)
  - [HTTP status codes](#http-status-codes)
  - [API gateway는 무엇을 하나요?](#what-does-api-gateway-do)
  - [효과적이고 안전한 API를 설계하려면 어떻게 해야 할까요?](#how-do-we-design-effective-and-safe-apis)
  - [TCP/IP encapsulation](#tcpip-encapsulation)
  - [왜 Nginx를 "reverse" 프록시라고 부르나요?](#왜-nginx를-reverse-프록시라고-부르나요)
  - [일반적인 로드 밸런싱 알고리즘은 무엇인가요?](#일반적인-로드-밸런싱-알고리즘은-무엇인가요)
  - [URL, URI, URN - 차이를 알고 있나요?](#url-uri-urn---차이를-알고-있나요)
- [CI/CD](#cicd)
  - [쉬운 용어로 설명하는 CI/CD 파이프라인](#쉬운-용어로-설명하는-cicd-파이프라인)
  - [넷플릭스 기술스택 (CI/CD Pipeline)](#넷플릭스-기술스택-cicd-pipeline)
- [아키텍처 패턴](#아키텍처-패턴)
  - [MVC, MVP, MVVM, MVVM-C, VIPER](#mvc-mvp-mvvm-mvvm-c-and-viper)
  - [18 Key Design Patterns Every Developer Should Know](#18-key-design-patterns-every-developer-should-know)
- [Database](#database)
  - [클라우드 서비스의 다양한 데이터베이스에 관한 치트시트](#클라우드-서비스의-다양한-데이터베이스에-관한-치트시트)
  - [데이터베이스를 강화하는 8가지 데이터 구조](#데이터베이스를-강화하는-8가지-데이터-구조)
  - [데이터베이스에서 SQL 문은 어떻게 실행되나요?](#데이터베이스에서-SQL-문은-어떻게-실행되나요)
  - [CAP 정리](#cap-정리)
  - [메모리 및 스토리지의 종류](#메모리-및-스토리지의-종류)
  - [SQL 쿼리 시각화](#SQL-쿼리-시각화)
  - [SQL 언어](#sql-언어)
- [캐시](#캐시)
  - [데이터는 어디에나 캐시됩니다](#데이터는-어디에나-캐시됩니다)
  - [Redis는 왜 빠른가요?](#redis는-왜-빠른가요)
  - [Redis는 어떻게 사용하나요?](#redis는-어떻게-사용하나요)
  - [주요 캐싱 전략](#주요-캐싱-전략)
- [마이크로서비스 아키텍처](#마이크로서비스-아키텍처)
  - [일반적인 마이크로서비스 아키텍처는 어떤 모습일까요?](#일반적인-마이크로서비스-아키텍처는-어떤-모습일까요)
  - [마이크로서비스 모범 사례](#마이크로서비스-모범사례)
  - [마이크로서비스에 일반적으로 사용하는 기술 스택은 무엇인가요?](#마이크로서비스에-일반적으로-사용하는-기술-스택은-무엇인가요)
  - [카프카가 빠른 이유](#카프카가-빠른-이유)
- [결제 시스템](#결제-시스템)
  - [결제 시스템을 배우는 방법은 무엇인가요?](#how-to-learn-payment-systems)
  - [신용카드를 "은행에서 가장 수익성이 높은 상품"이라고 부르는 이유는 무엇인가요? 비자/마스터카드는 어떻게 수익을 창출하나요?](#why-is-the-credit-card-called-the-most-profitable-product-in-banks-how-does-visamastercard-make-money)
  - [How does VISA work when we swipe a credit card at a merchant’s shop?](#how-does-visa-work-when-we-swipe-a-credit-card-at-a-merchants-shop)
  - [세계의 결제 시스템 시리즈(1부): 인도의 통합 결제 인터페이스(UPI)](#payment-systems-around-the-world-series-part-1-unified-payments-interface-upi-in-india)
- [DevOps](#devops)
  - [DevOps vs. SRE vs. Platform Engineering. 무엇이 다른가요?](#devops-vs-sre-vs-platform-engineering-what-is-the-difference)
  - [k8s(Kubernetes)란 무엇인가요?](#what-is-k8s-kubernetes)
  - [Docker vs. Kubernetes. 어떤것을 사용해야 하나요?](#docker-vs-kubernetes-which-one-should-we-use)
  - [Docker는 어떻게 작동하나요?](#how-does-docker-work)
- [GIT](#git)
  - [Git Commands 작동 방식](#how-git-commands-work)
  - [Git은 어떻게 작동하나요?](#how-does-git-work)
  - [Git merge vs. Git rebase](#git-merge-vs-git-rebase)
- [클라우드 서비스](#cloud-services)
  - [다양한 클라우드 서비스에 대한 유용한 치트시트(2023년판)](#a-nice-cheat-sheet-of-different-cloud-services-2023-edition)
  - [cloud native란 무엇인가요?](#what-is-cloud-native)
- [Developer productivity tools](#developer-productivity-tools)
  - [JSON 파일 시각화](#visualize-json-files)
  - [코드를 아키텍처 다이어그램으로 자동 변환](#automatically-turn-code-into-architecture-diagrams)
- [리눅스](#linux)
  - [리눅스 파일 시스템 설명](#linux-file-system-explained)
  - [가장 많이 사용되는 18가지 리눅스 명령어 알아보기](#18-most-used-linux-commands-you-should-know)
- [보안](#security)
  - [HTTPS는 어떻게 작동하나요?](#how-does-https-work)
  - [간단한 용어로 설명하는 Oauth 2.0](#oauth-20-explained-with-simple-terms)
  - [인증 메커니즘의 4가지 주요 형태](#top-4-forms-of-authentication-mechanisms)
  - [Session, cookie, JWT, token, SSO, OAuth 2.0 - 그게 뭔가요?](#session-cookie-jwt-token-sso-and-oauth-20---what-are-they)
  - [데이터베이스에 비밀번호를 안전하게 저장하는 방법과 비밀번호를 확인하는 방법은 무엇인가요?](#how-to-store-passwords-safely-in-the-database-and-how-to-validate-a-password)
  - [10세 어린이에게 JSON Web Token(JWT) 설명하기](#explaining-json-web-token-jwt-to-a-10-year-old-kid)
  - [Google authenticator(또는 다른 유형의 2 factor authenticator)는 어떻게 작동하나요?](#how-does-google-authenticator-or-other-types-of-2-factor-authenticators-work)
- [실제 사례 연구](#real-world-case-studies)
  - [넷플릭스 기술 스택](#netflixs-tech-stack)
  - [트위터 아키텍처 2022](#twitter-architecture-2022)
  - [지난 15년간 에어비앤비 마이크로서비스 아키텍처의 진화 과정](#evolution-of-airbnbs-microservice-architecture-over-the-past-15-years)
  - [모노레포 vs. 마이크로레포](#monorepo-vs-microrepo)
  - [스택 오버플로 웹사이트를 어떻게 디자인할 건가요?](#how-will-you-design-the-stack-overflow-website)
  - [아마존 프라임 비디오 모니터링이 서버리스에서 모놀리식으로 전환된 이유는 무엇인가요? 어떻게 90%의 비용을 절감할 수 있을까요?](#why-did-amazon-prime-video-monitoring-move-from-serverless-to-monolithic-how-can-it-save-90-cost)
  - [디즈니 핫스타는 어떻게 토너먼트 기간 동안 50억 개의 이모티콘을 획득할 수 있었나요?](#how-does-disney-hotstar-capture-5-billion-emojis-during-a-tournament)
  - [Discord가 수조 개의 메시지를 저장하는 방법](#how-discord-stores-trillions-of-messages)
  - [동영상 라이브 스트리밍은 YouTube, TikTok 라이브, Twitch에서 어떻게 작동하나요?](#how-do-video-live-streamings-work-on-youtube-tiktok-live-or-twitch)

<!-- /TOC -->

## Communication protocols

아키텍처 스타일은 애플리케이션 프로그래밍 인터페이스(API)의 여러 구성 요소가 서로 상호 작용하는 방식을 정의합니다. 결과적으로 API를 설계하고 구축하는 표준 접근 방식을 제공함으로써 효율성, 안정성, 다른 시스템과의 쉬운 통합을 보장합니다. 다음은 가장 많이 사용되는 스타일입니다.

<p>
  <img src="../images/api-architecture-styles.png" style="width: 640px">
</p>

- SOAP: 

  성숙하고, 포괄적이고, XML 기반 
  
  엔터프라이즈 애플리케이션에 가장 적합 

- RESTful: 

  인기있고, 구현하기 쉽고, HTTP methods 

  웹 서비스에 이상적 

- GraphQL: 

  쿼리 언어, 특정 데이터 요청 

  네트워크 오버헤드 감소, 빠른 응답 

- gRPC: 

  Modern, high-performance, Protocol Buffers 

  마이크로 서비스 아키텍처에 적합 

- WebSocket: 

  실시간, 양방향, 지속적인 연결 

  지연 시간이 짧은 데이터에 적합 

- Webhook: 

  이벤트 기반, HTTP 콜백, 비동기식 

  이벤트가 발생하면 시스템에 알림 


### REST API vs. GraphQL

API 설계에 있어서 REST와 GraphQL은 고유의 장단점이 있습니다.

아래 다이어그램은 REST와 GraphQL을 간략하게 비교한 것입니다.

<p>
  <img src="../images/graphQL.jpg">
</p>

REST

- CRUD 작업에 GET, POST, PUT, DELETE와 같은 표준 HTTP 메서드를 사용합니다.
- 서로 다른 서비스/애플리케이션 간에 간단하고 균일한 인터페이스가 필요할 때 효과적입니다.
- 캐싱 전략은 구현이 간단합니다.
- 단점으로 별도의 엔드포인트에서 관련 데이터를 수집하기 위해 여러 번의 왕복이 필요할 수 있습니다.

GraphQL

- 클라이언트가 필요한 데이터를 정확하게 쿼리할 수 있는 단일 엔드포인트를 제공합니다.
- 클라이언트가 중첩 쿼리에 필요한 정확한 필드를 지정하면 서버는 해당 필드만 포함한 최적화된 페이로드를 반환합니다.
- 데이터 수정을 위한 뮤테이션과 실시간 알림을 위한 구독을 지원합니다.
- 여러 소스의 데이터를 응집하는데 적합하며 빠르게 진화하는 프런트엔드 요구사항에 잘 맞습니다.
- 하지만 복잡성을 클라이언트 측으로 전가하며, 제대로 보호하지 않으면 악의적인 쿼리를 허용할 수 있습니다.
- 캐싱 전략은 REST보다 더 복잡할 수 있습니다.

애플리케이션과 개발팀의 구체적인 요구사항에 따라 REST와 GraphQL 중 적합한 것을 선택해야 합니다. GraphQL은 복잡하거나 자주 변경되는 프런트엔드 요구사항에 적합하며, REST는 단순하고 일관된 계약이 선호되는 애플리케이션에 적합합니다.

두 API 방식 모두 은총알은 아닙니다. 올바른 스타일을 선택하려면 요구 사항과 장단점을 신중하게 평가하는 것이 중요합니다. REST와 GraphQL은 모두 데이터를 노출하고 최신 애플리케이션을 구동하는 데 유효한 옵션입니다.


### gRPC는 어떻게 작동하나요?

RPC(Remote Procedure Call)는 마이크로서비스 아키텍처에서 서비스가 서로 다른 서버에 배포될 때 원격 서비스 간의 통신을 가능하게 하기 때문에 "**remote**"라고 불립니다. 사용자 입장에서는 로컬 함수 호출처럼 작동합니다.

아래 다이어그램은 **gRPC**의 전체 데이터 플로우를 보여줍니다.

<p>
  <img src="../images/grpc.jpg">
</p>

1단계: 클라이언트에서 REST 호출을 수행합니다. request body는 일반적으로 JSON 포맷입니다.

2-4단계: 주문 서비스(gRPC 클라이언트)가 REST 호출을 수신하여 변환한 후 결제 서비스에 RPC 호출을 합니다. gRPC는 **client stub**을 바이너리로 인코딩하여 로우레벨 전송 계층으로 보냅니다.

5단계: gRPC가 HTTP2를 통해 패킷을 전송합니다. 바이너리 인코딩과 네트워크 최적화로 인해 gRPC는 JSON보다 5배 빠르다고 합니다.

6-8단계: 결제 서비스(gRPC 서버)가 네트워크에서 패킷을 수신하고, 이를 디코딩한 후 서버 애플리케이션을 호출합니다.

9-11단계: 서버 애플리케이션에서 결과를 반환하고 인코딩하여 전송 계층으로 전송합니다.

12-14단계: 주문 서비스가 패킷을 수신하여 디코딩한 후 결과를 클라이언트 애플리케이션에 보냅니다.

### What is a webhook?

아래 다이어그램은 폴링과 웹훅을 비교한 것입니다. 

<p>
  <img src="../images/webhook.jpeg" style="width: 680px" />
</p>

전자상거래 웹사이트를 운영한다고 가정해 보겠습니다. 클라이언트가 API 게이트웨이를 통해 주문 서비스로 주문을 보내면, 주문 서비스는 결제 트랜잭션을 위해 결제 서비스로 이동합니다. 그러면 결제 서비스는 외부 결제 서비스 공급업체(PSP)와 통신하여 트랜잭션을 완료합니다. 

외부 PSP와의 통신을 처리하는 방법에는 두 가지가 있습니다.

**1. 숏 폴링 Short polling** 

결제 요청을 PSP에 전송한 후 결제 서비스에서 PSP에 결제 상태를 계속 묻습니다. 몇 번의 라운드가 끝나면 PSP는 마침내 상태를 반환합니다. 

숏 폴링에는 두 가지 단점이 있습니다.
- 상태를 지속적으로 폴링하려면 결제 서비스의 리소스가 필요합니다. 
- 외부 서비스가 결제 서비스와 직접 통신하므로 보안 취약점이 발생할 수 있습니다.

**2. 웹훅 Webhook** 

외부 서비스에 웹훅을 등록할 수 있습니다. 즉, 요청에 대한 업데이트가 있을 때 특정 URL로 다시 호출하라는 의미입니다. PSP가 처리를 완료하면 HTTP 요청을 호출하여 결제 상태를 업데이트합니다.

이러한 방식으로 프로그래밍 패러다임이 바뀌고 결제 서비스는 더 이상 결제 상태를 폴링하기 위해 리소스를 낭비할 필요가 없습니다.

PSP가 다시 응답하지 않으면 어떻게 하나요? 매시간 결제 상태를 확인하도록 하우스키핑 작업을 설정할 수 있습니다.

웹훅은 서버가 클라이언트에 HTTP 요청을 보내기 때문에 리버스 API 또는 푸시 API라고도 불립니다. 웹훅을 사용할 때는 다음 세 가지 사항에 주의해야 합니다.

1. 외부 서비스가 호출할 수 있는 적절한 API를 설계해야 합니다.
2. 보안을 위해 API 게이트웨이에 적절한 규칙을 설정해야 합니다.
3. 외부 서비스에 올바른 URL을 등록해야 합니다.

### API 성능을 개선하는 방법은 무엇인가요?

아래 다이어그램은 API 성능을 개선하는 5가지 일반적인 방법을 보여줍니다.

<p>
  <img src="../images/api-performance.jpg">
</p>

Pagination

이는 결과의 크기가 클 때 일반적으로 사용하는 최적화 방법입니다. 서비스 응답성을 개선하기 위해 결과를 클라이언트로 다시 스트리밍합니다.

Asynchronous Logging

동기식 로깅은 모든 호출에 대해 디스크를 처리하므로 시스템 속도가 느려질 수 있습니다. 비동기 로깅은 로그를 잠금 없는 버퍼로 먼저 전송한 후 즉시 반환합니다. 로그는 주기적으로 디스크에 플러시됩니다. 따라서 I/O 오버헤드가 크게 줄어듭니다.

Caching

자주 액세스하는 데이터를 캐시에 저장할 수 있습니다. 클라이언트는 데이터베이스를 직접 방문하는 대신 캐시를 먼저 쿼리할 수 있습니다. 캐시에 미스가 있는 경우 클라이언트는 데이터베이스에서 쿼리할 수 있습니다. Redis와 같은 캐시는 데이터를 메모리에 저장하므로 데이터 액세스가 데이터베이스보다 훨씬 빠릅니다.

Payload Compression

요청과 응답은 gzip 등을 사용하여 압축할 수 있으므로 전송되는 데이터 크기가 훨씬 작아집니다. 이렇게 하면 업로드와 다운로드 속도가 빨라집니다.

Connection Pool

리소스에 액세스할 때 데이터베이스에서 데이터를 로드해야 하는 경우가 종종 있습니다. 닫혀 있는 데이터베이스 커넥션을 열면 상당한 오버헤드가 추가됩니다. 따라서 오픈 커넥션 풀을 통해 데이터베이스에 연결해야 합니다. 커넥션 풀은 커넥션 라이프사이클을 관리하는 역할을 합니다.

### HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)

각 세대의 HTTP는 어떤 문제를 해결하나요?

아래 다이어그램은 주요 특징을 보여줍니다.

<p>
  <img src="../images/http3.jpg" />
</p>

- HTTP 1.0은 1996년에 완성되어 완전히 문서화되었습니다. 동일한 서버에 대한 모든 요청에는 별도의 TCP 연결이 필요합니다.

- HTTP 1.1은 1997년에 발표되었습니다. TCP 커넥션은 재사용(persistent connection)을 위해 열어둘 수 있지만, HOL(head-of-line) 차단 문제를 해결하지는 못합니다.

  HOL 차단 - 브라우저에서 허용하는 병렬 요청의 수를 모두 사용하면 후속 요청은 이전 요청이 완료될 때까지 기다려야 합니다.

- HTTP 2.0은 2015년에 발표되었습니다. 이는 요청 다중화를 통해 HOL 문제를 해결하여 응용 계층에서 HOL 차단을 제거하지만, 전송(TCP) 계층에는 여전히 HOL이 존재합니다.

  다이어그램에서 볼 수 있듯이 HTTP 2.0은 동일한 TCP 커넥션에 서로 다른 HTTP 교환을 다중화할 수 있는 추상화 개념인 HTTP "steam"을 도입했습니다. 각 스트림을 순서대로 전송할 필요는 없습니다.

- HTTP 3.0 초안은 2020년에 발표되었습니다. HTTP 2.0의 후속 버전으로 제안되었습니다. 기본 트랜스포트 프로토콜로 TCP 대신 QUIC을 사용하므로 전송 계층에서 HOL 차단이 제거됩니다. 

QUIC은 UDP를 기반으로 합니다. 이는 전송 계층에서 스트림을 퍼스트 클래스 시티즌으로 소개합니다. QUIC 스트림은 동일한 QUIC 커넥션을 공유하므로 새 스트림을 생성하기 위해 추가적인 핸드셰이크나 슬로우 스타트가 필요하지 않으며, 대부분의 경우 한 스트림에 영향을 미치는 패킷 손실이 다른 스트림에 영향을 미치지 않도록 독립적으로 전달됩니다.

### SOAP vs REST vs GraphQL vs RPC

아래 다이어그램은 API 타임라인과 API 스타일을 비교한 것입니다.

시간이 지남에 따라 다양한 API 아키텍처 스타일이 출시됩니다. 각 스타일에는 데이터 교환을 표준화하는 고유한 패턴이 있습니다. 

다이어그램에서 각 스타일의 사용 사례를 확인할 수 있습니다.

<p>
  <img src="../images/SOAP vs REST vs GraphQL vs RPC.jpeg" />
</p>


### Code First vs. API First 

아래 다이어그램은 코드 퍼스트 개발과 API 퍼스트 개발의 차이점을 보여줍니다. API 퍼스트 설계를 고려해야 하는 이유는 무엇인가요?

<p>
  <img src="../images/api_first.jpg" style="width: 680px" />
</p>


- 마이크로서비스는 시스템 복잡성을 증가시키며, 시스템의 다양한 기능을 담당하는 별도의 서비스를 제공합니다. 이러한 아키텍처는 업무의 디커플링과 분리를 용이하게 하지만 서비스 간의 다양한 커뮤니케이션을 처리해야 합니다.

코드를 작성하기 전에 시스템의 복잡성을 고려하고 서비스의 범위를 신중하게 정의하는 것이 좋습니다.

- 기능조직은 동일한 언어로 의사소통해야 하며, 목적조직은 자체 컴포넌트와 서비스에만 책임이 있습니다. API 설계를 통해 조직이 동일한 언어로 의사소통하는 것이 좋습니다.

코드를 작성하기 전에 요청과 응답을 모의로 작성하여 API 설계를 검증할 수 있습니다.

- 소프트웨어 품질과 개발자 생산성이 향상됩니다. 프로젝트가 시작될 때 대부분의 불확실성을 제거했기 때문에 전반적인 개발 프로세스가 더 원활해지고 소프트웨어 품질이 크게 향상됩니다.

개발자는 갑작스러운 변경 사항을 논의하는 대신 기능 개발에 집중할 수 있기 때문에 이 프로세스에 만족합니다.

프로젝트 라이프사이클이 끝날 무렵에 서프라이즈가 발생할 가능성이 줄어듭니다.

API를 먼저 설계했기 때문에 코드가 개발되는 동안 테스트를 설계할 수 있습니다. 어떤 면에서는 API 퍼스트 개발 방식을 사용할 때 TDD(Test Driven Design)를 적용한다고 볼 수 있습니다.

### HTTP status codes

<p>
  <img src="../images/http-status-code.jpg" style="width: 540px" />
</p>


HTTP의 응답 코드는 5가지 카테고리로 나누어집니다.

Informational (100-199)  
Success (200-299)  
Redirection (300-399)  
Client Error (400-499)  
Server Error (500-599)  

### What does API gateway do? 

아래 다이어그램은 자세한 내용을 보여줍니다.

<p>
  <img src="../images/api_gateway.jpg" style="width: 520px" />
</p>

1단계 - 클라이언트가 API 게이트웨이에 HTTP 요청을 보냅니다.

2단계 - API 게이트웨이가 HTTP 요청의 어트리뷰트를 파싱하고 유효성을 검사합니다.

3단계 - API 게이트웨이가 allow-list/deny-list 검사를 수행합니다.

4단계 - API 게이트웨이가 인증과 인가를 위해 ID 공급자와 통신합니다.

5단계 - 요청에 레이트 리미트 규칙을 적용합니다. 한도를 초과하면 요청을 거부합니다.

6,7단계 - 요청이 기본 검사를 통과했으므로 이제 API 게이트웨이가 path 매칭을 통해 라우팅할 관련 서비스를 찾습니다.

8단계 - API 게이트웨이가 요청을 적절한 프로토콜로 변환하여 백엔드 마이크로서비스로 전송합니다.

9-12단계: API 게이트웨이는 오류를 적절하게 처리하고, 복구하는 데 시간이 오래 걸리는 오류가 발생하는 경우 장애를 처리합니다.(circuit break) 또한 로깅과 모니터링을 위해 ELK(Elastic-Logstash-Kibana) 스택을 활용할 수 있습니다. 때때로 API 게이트웨이에 데이터를 캐시하기도 합니다.

### How do we design effective and safe APIs?

아래 다이어그램은 쇼핑 카트 예시와 함께 일반적인 API 설계를 보여줍니다. 

<p>
  <img src="../images/safe-apis.jpg" />
</p>


API 설계는 단순한 URL path 설계가 아니라는 점에 유의하세요. 대부분의 경우 적절한 리소스 이름, 식별자, path 패턴을 선택해야 합니다. 적절한 HTTP 헤더 필드를 설계하거나 API 게이트웨이 내에서 효과적인 rate limit 규칙을 설계하는 것도 마찬가지로 중요합니다.

### TCP/IP encapsulation 

데이터는 네트워크를 통해 어떻게 전송되나요? OSI 모델에 많은 계층이 필요한 이유는 무엇인가요?

아래 다이어그램은 네트워크를 통해 데이터를 전송할 때 어떻게 캡슐화되고 캡슐화가 해제되는지 보여줍니다.

<p>
  <img src="../images/osi model.jpeg" />
</p>

1단계: 디바이스 A가 네트워크상의 HTTP 프로토콜을 통해 장치 B로 데이터를 전송할 때, 먼저 응용 계층에서 HTTP 헤더가 추가됩니다.

2단계: 그런 다음 TCP 혹은 UDP 헤더가 데이터에 추가됩니다. 이 헤더는 전송 계층에서 TCP 세그먼트로 캡슐화됩니다. 헤더에는 소스 포트, 데스티네이션 포트, 시퀀스 넘버가 포함됩니다.

3단계: 그런 다음 세그먼트는 네트워크 계층에서 IP 헤더로 캡슐화됩니다. IP 헤더에는 소스/데스티네이션 IP 주소가 포함됩니다.

4단계: 데이터 링크 계층에서 IP 데이터그램에 소스/데스티네이션 MAC 주소와 함께 MAC 헤더가 추가됩니다.

5단계: 캡슐화된 프레임이 물리 계층으로 전송되고 네트워크를 통해 2진수 비트로 전송됩니다.

6-10단계: 디바이스 B가 네트워크에서 비트를 수신하면 캡슐화 프로세스의 역처리인 캡슐화 해제 프로세스를 수행합니다. 헤더가 한 층씩 제거되고 결국 디바이스 B가 데이터를 읽을 수 있게 됩니다.

네트워크 모델에 계층이 필요한 이유는 각 계층이 고유한 책임에 집중하기 때문입니다. 각 계층은 처리 지침을 헤더에 의존할 수 있으며 마지막 계층의 데이터의 의미를 알 필요가 없습니다.

### 왜 Nginx를 "reverse" 프록시라고 부르나요?

아래 다이어그램은 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐩𝐫𝐨𝐱𝐲 와 𝐫𝐞𝐯𝐞𝐫𝐬𝐞 𝐩𝐫𝐨𝐱𝐲 의 차이점을 보여줍니다.

<p>
  <img src="../images/Forward Proxy v.s. Reverse Proxy2x.jpg" style="width: 720px" />
</p>

포워드 프록시는 사용자 디바이스와 인터넷 사이에 있는 서버입니다.

포워드 프록시는 일반적으로 다음 용도로 사용됩니다.

1. 클라이언트 보호
2. 브라우징 제약 우회하기
3. 특정 콘텐츠에 대한 액세스 차단

리버스 프록시는 클라이언트의 요청을 수락하여 웹 서버로 요청을 전달한 후 프록시 서버가 요청을 처리한 것처럼 결과를 클라이언트에 반환하는 서버입니다.

리버스 프록시는 다음과 같은 경우에 유용합니다.

1. 서버 보호
2. 로드 밸런싱
3. 정적 콘텐츠 캐싱
4. SSL 통신 암호화 및 복호화

### 일반적인 로드 밸런싱 알고리즘은 무엇인가요?

아래 다이어그램은 6가지 일반적인 알고리즘을 보여줍니다.

<p>
  <img src="../images/lb-algorithms.jpg" />
</p>

- 정적 알고리즘

1. Round robin

    클라이언트 요청은 순차적으로 다른 서비스 인스턴스로 전송됩니다. 서비스는 일반적으로 스테이트리스(과거 처리 내용을 기억하지 않는 서비스)여야 합니다. 

3. Sticky round-robin

    이는 라운드 로빈 알고리즘을 개선한 것입니다. 앨리스의 첫 번째 요청이 서비스 A로 전달되면 다음 요청도 서비스 A로 전달됩니다. 

4. Weighted round-robin

    관리자는 각 서비스에 대한 가중치를 지정할 수 있습니다. 가중치가 높은 서비스는 다른 서비스보다 더 많은 요청을 처리합니다.

6. Hash

    이 알고리즘은 들어오는 요청의 IP 또는 URL에 해시 함수를 적용합니다. 요청은 해시 함수 결과에 따라 관련 인스턴스로 라우팅됩니다.

- 동적 알고리즘

5. Least connections

    동시 연결이 가장 적은 서비스 인스턴스로 새 요청이 전송됩니다. 

7. Least response time

    새 요청은 응답 시간이 가장 빠른 서비스 인스턴스로 전송됩니다.

### URL, URI, URN - 차이를-알고-있나요? 

아래 다이어그램은 URL, URI, URN의 비교를 보여줍니다.

<p>
  <img src="../images/url-uri-urn.jpg" />
</p>

- URI 

URI은 Uniform Resource Identifier의 약자입니다. 웹에서 논리적 또는 물리적 리소스를 식별합니다. URL과 URN은 URI의 하위 유형입니다. URL은 리소스를 찾고 URN은 리소스의 이름을 지정합니다.

URI는 다음과 같은 부분으로 구성되어 있습니다. 
scheme:[//authority]path[?query][#fragment] 

- URL 

URL은 Uniform Resource Locator의 약자로, HTTP의 핵심 개념입니다. 웹에서 고유한 리소스의 주소입니다. FTP와 JDBC와 같은 다른 프로토콜과 함께 사용할 수 있습니다. 

- URN 

URN은 Uniform Resource Name의 약자로, urn 스키마를 사용합니다. URN은 리소스를 찾는 데 사용할 수 없습니다. 다이어그램에 제시된 간단한 예는 네임스페이스와 네임스페이스 특정 문자열로 구성되어 있습니다.

이 주제에 대해 더 자세히 알아보려면 다음을 추천합니다. [W3C’s clarification](https://www.w3.org/TR/uri-clarification/).

## CI/CD

### 쉬운 용어로 설명하는 CI/CD 파이프라인

<p>
  <img src="../images/ci-cd-pipeline.jpg" style="width: 680px" />
</p>

섹션 1 - CI/CD가 포함된 소프트웨어 개발 수명 주기

소프트웨어 개발 수명 주기(SDLC)는 개발, 테스트, 배포, 유지 관리 등 몇 가지 주요 단계로 구성됩니다. CI/CD는 이러한 단계를 자동화하고 통합하여 더 빠르고 안정적인 릴리스를 가능하게 합니다.

코드가 git 리포지토리에 푸시되면 자동화된 빌드 및 테스트 프로세스가 시작됩니다. 코드의 유효성을 검사하기 위해 엔드투엔드(e2e) 테스트 케이스가 실행됩니다. 테스트를 통과하면 코드를 스테이징/프로덕션 환경에 자동으로 배포할 수 있습니다. 이슈가 발견되면 코드는 버그 수정을 위해 개발 단계로 다시 보내집니다. 이러한 자동화는 개발자에게 신속한 피드백을 제공하고 프로덕션 환경에서 발생하는 버그 위험을 줄여줍니다.

섹션 2 - CI와 CD의 차이점

Continuous Integration(CI)은 빌드, 테스트, 병합 프로세스를 자동화합니다. 코드가 커밋될 때마다 테스트를 실행하여 통합 이슈를 조기에 발견합니다. 이를 통해 코드 커밋을 자주 하고 피드백을 빠르게 받을 수 있습니다.

Continuous Delivery(CD)는 인프라 변경, 배포와 같은 릴리스 프로세스를 자동화합니다. 자동화된 워크플로를 통해 언제든지 소프트웨어를 안정적으로 릴리스할 수 있습니다. 또한 CD는 프로덕션 배포 전에 필요한 메뉴얼 테스트와 승인 단계를 자동화할 수도 있습니다.

섹션 3 - CI/CD 파이프라인

일반적인 CI/CD 파이프라인은 다음과 같이 연결된 여러 단계로 구성됩니다.
- 개발자가 코드 변경 사항을 소스 컨트롤에 커밋합니다.
- CI 서버가 변경 사항을 감지하고 빌드를 트리거합니다.
- 코드가 컴파일되고 테스트됩니다(단위 테스트, 통합 테스트).
- 테스트 결과를 개발자에게 보고됩니다.
- 성공하면 아티팩트가 스테이징 환경에 배포됩니다.
- 릴리스 전에 스테이징 환경에서 추가 테스트를 수행할 수 있습니다.
- CD 시스템이 승인한 변경 사항을 프로덕션에 배포합니다.

### 넷플릭스 기술스택 (CI/CD Pipeline)

<p>
  <img src="../images/netflix-ci-cd.jpg" style="width: 720px" />
</p>

플래닝: 넷플릭스 엔지니어링은 플래닝에는 JIRA를, 문서화에는 Confluence를 사용합니다.

코딩: Java는 백엔드 서비스를 위한 기본 프로그래밍 언어이며, 다른 언어는 유즈케이스에 따라 사용됩니다.  

빌드: Gradle은 주로 빌드에 사용되며, Gradle 플러그인은 다양한 유스케이스를 지원하기 위해 만들어졌습니다.

패키징: 패키지 및 의존성은 릴리스를 위해 아마존 머신 이미지(AMI)에 패키징됩니다. 

테스팅: Testing emphasizes the production culture's focus on building chaos tools.  

배포: 넷플릭스는 카나리 롤아웃 배포에 자체 구축한 Spinnaker를 사용합니다.

모니터링: 모니터링 지표는 Atlas에서 중앙 집중식으로 관리되며, 이상 징후를 감지하는 데 Kayenta가 사용됩니다. 

인시던트 리포트: 우선순위에 따라 인시던트가 발송되며, 사고 처리를 위해 PagerDuty가 사용됩니다. 

## 아키텍처 패턴

### MVC, MVP, MVVM, MVVM-C, VIPER
이러한 아키텍처 패턴은 iOS, Android 플랫폼에서 앱 개발 시 가장 일반적으로 사용하는 패턴입니다. 개발자들은 이전 패턴의 한계를 극복하기 위해 이러한 패턴을 도입했습니다. 그렇다면 어떻게 다를까요?

<p>
  <img src="../images/client arch patterns.png" style="width: 720px" />
</p>

- 가장 오래된 패턴인 MVC는 거의 50년 전으로 거슬러 올라갑니다.
- 모든 패턴에는 콘텐츠를 표시하고 사용자 입력을 수신하는 'view'(V)가 있습니다. 
- 대부분의 패턴에는 비즈니스 데이터를 관리하기 위한 'model'(M)이 포함됩니다.
- "Controller", " presenter", "view-model"은 뷰와 모델(VIPER 패턴의 "entity") 사이를 매개하는 변환기입니다.

### 18 Key Design Patterns Every Developer Should Know

패턴은 일반적인 설계 문제에 대한 재사용 가능한 솔루션으로, 보다 원활하고 효율적인 개발 프로세스를 가능하게 합니다. 패턴은 더 나은 소프트웨어 구조를 구축하기 위한 청사진 역할을 합니다. 다음은 가장 많이 사용되는 패턴 중 일부입니다.

<p>
  <img src="../images/18-oo-patterns.png" />
</p>

- Abstract Factory: Family Creator - Makes groups of related items. 
- Builder: Lego Master - Builds objects step by step, keeping creation and appearance separate. 
- Prototype: Clone Maker - Creates copies of fully prepared examples. 
- Singleton: One and Only - A special class with just one instance. 
- Adapter: Universal Plug - Connects things with different interfaces. 
- Bridge: Function Connector - Links how an object works to what it does. 
- Composite: Tree Builder - Forms tree-like structures of simple and complex parts. 
- Decorator: Customizer - Adds features to objects without changing their core. 
- Facade: One-Stop-Shop - Represents a whole system with a single, simplified interface. 
- Flyweight: Space Saver - Shares small, reusable items efficiently. 
- Proxy: Stand-In Actor - Represents another object, controlling access or actions. 
- Chain of Responsibility: Request Relay - Passes a request through a chain of objects until handled. 
- Command: Task Wrapper - Turns a request into an object, ready for action. 
- Iterator: Collection Explorer - Accesses elements in a collection one by one. 
- Mediator: Communication Hub - Simplifies interactions between different classes. 
- Memento: Time Capsule - Captures and restores an object's state. 
- Observer: News Broadcaster - Notifies classes about changes in other objects. 
- Visitor: Skillful Guest - Adds new operations to a class without altering it.

## Database

### 클라우드 서비스의 다양한 데이터베이스에 관한 치트시트

<p>
  <img src="../images/cloud-dbs2.png" />
</p>

프로젝트에 적합한 데이터베이스를 선택하는 것은 복잡한 작업입니다. 각기 다른 유즈케이스에 적합한 데이터베이스 옵션이 많으면 의사 결정에 대한 피로도가 빠르게 높아질 수 있습니다. 

이 치트시트가 프로젝트의 요구사항에 맞는 올바른 서비스를 찾아내고 잠재적인 함정을 피하는 데 도움이 되기를 바랍니다. 

참고: Google은 데이터베이스 유즈케이스에 대한 문서가 제한되어 있습니다. 사용 가능한 자료를 최대한 검토하고 최선의 옵션을 제시했지만, 일부 항목은 더 정확한 정보가 필요할 수 있습니다. 

### 데이터베이스를 강화하는 8가지 데이터 구조

정답은 유즈케이스에 따라 달라집니다. 데이터는 메모리나 디스크에 인덱스될 수 있습니다. 마찬가지로 데이터 포맷도 넘버, 스트링, 지리적 좌표 등 다양합니다. 시스템이 쓰기 중심일 수도 있고 읽기 중심일 수도 있습니다. 이러한 모든 요소는 데이터베이스 인덱스 포맷 선택에 영향을 미칩니다. 

<p>
  <img src="../images/8-ds-db.jpg" />
</p>

다음은 데이터 인덱싱에 가장 많이 사용되는 몇 가지 데이터 구조입니다.

- Skiplist: 일반적인 인메모리 인덱스 타입으로, Redis에서 사용.
- Hash index: "Map" 데이터 구조(또는 "Collection")의 매우 일반적인 구현.
- SSTable: 디스크에 이뮤터블 'Map' 구현
- LSM tree: Skiplist + SSTable. 높은 쓰기 처리량. 
- B-tree: 디스크 기반 솔루션. 일관된 읽기/쓰기 성능.
- Inverted index: 도큐먼트 인덱싱에 사용. 루씬에서 사용.
- Suffix tree: 스트링 패턴 검색. 
- R-tree: 가장 가까운 이웃 찾기와 같은 다차원 검색. 

### 데이터베이스에서 SQL 문은 어떻게 실행되나요?

아래 다이어그램은 그 과정을 보여줍니다. 데이터베이스마다 아키텍처가 다르지만 이 다이어그램은 몇 가지 일반적인 설계를 보여줍니다.

<p>
  <img src="../images/sql execution order in db.jpeg" style="width: 580px" />
</p>


1단계 - SQL 문은 전송 계층 프로토콜(예: TCP)을 통해 데이터베이스로 전송됩니다.

2단계 - SQL 문은 command parser로 전송되어 구문 및 의미 분석을 거친 후 쿼리 트리가 생성됩니다.

3단계 - 쿼리 트리가 optimizer로 전송됩니다. optimizer가 실행 계획을 생성합니다.

4단계 - 실행 계획이 executor에게 전송됩니다. executor는 익스큐션에서 데이터를 검색합니다.

5단계 - Access methods는 실행에 필요한 데이터 페칭 로직을 제공하여 스토리지 엔진에서 데이터를 검색합니다. 

6단계 - Access methods는 SQL 문의 읽기 전용 여부를 결정합니다. 쿼리가 읽기 전용인 경우(SELECT 문), 쿼리는 추가 처리를 위해 buffer manager에게 전달됩니다. buffer manager는 캐시 또는 데이터 파일에서 데이터를 찾습니다.

7단계 - UPDATE 혹은 INSERT 문인 경우, 추가 처리를 위해 transaction manager에게 전달합니다.

8단계 - 트랜잭션이 진행되는 동안 데이터는 잠겨 있습니다. 이는 lock manager에 의해 보장됩니다. 또한 트랜잭션의 ACID 프로퍼티도 보장합니다. 

###  CAP 정리

CAP 정리는 컴퓨터 과학에서 가장 유명한 용어 중 하나이지만 개발자마다 이해하는 바가 다를 수 있습니다. 이 용어가 무엇이며 왜 혼란스러울 수 있는지 살펴보겠습니다. 

<p>
  <img src="../images/cap theorem.jpeg" />
</p>

CAP 정리에 따르면 분산 시스템은 이 세 가지 보장 중 두 가지 이상을 동시에 제공할 수 없습니다.

**Consistency**: 일관성이란 모든 클라이언트가 어느 노드에 연결하든 동일한 데이터를 동시에 볼 수 있다는 의미입니다.

**Availability**: 가용성이란 일부 노드가 다운되더라도 데이터를 요청하는 모든 클라이언트가 응답을 받는다는 의미입니다.

**Partition Tolerance**: 파티션은 두 노드 간의 통신 단절을 나타냅니다. 파티션 똘레랑스는 시스템이 네트워크 파티션에도 불구하고 계속 작동할 수 있는 능력을 의미합니다.

"셋 중 둘" 공식은 유용할 수 있지만 **이러한 단순화는 오해의 소지가 있습니다**.

1. 데이터베이스를 선택하는 것은 쉽지 않습니다. CAP 정리만으로 선택을 정당화하는 것은 충분하지 않습니다. 예를 들어, 회사에서 단순히 AP 시스템이라는 이유만으로 채팅 애플리케이션을 위해 Cassandra를 선택하지는 않습니다. 채팅 메시지를 저장하는 데 있어 Cassandra를 바람직한 옵션으로 만드는 좋은 특성 목록이 있습니다. 더 깊이 파고들 필요가 있습니다.

2. "CAP는 디자인 공간의 극히 일부분, 즉 파티션이 있을 때 완벽한 가용성과 일관성을 보장하는 경우는 드뭅니다." 논문에서 인용: CAP Twelve Years Later: How the "Rules" Have Changed.

3. 이 정리는 약 100%의 가용성과 일관성을 의미합니다. 보다 현실적인 논의는 네트워크 파티션이 없을 때 지연 시간과 일관성 간의 절충안입니다. 자세한 내용은 PACELC 정리를 참조하세요.

**Is the CAP theorem actually useful?**

절충안을 논의할 수 있다는 점에서 여전히 유용하다고 생각하지만, 이는 일부분일 뿐입니다. 올바른 데이터베이스를 선택하려면 더 깊이 파고들어야 합니다.

### 메모리 및 스토리지의 종류

<p>
  <img src="../images/Types_of_Memory_and_Storage.jpeg" style="width: 420px" />
</p>


### SQL 쿼리 시각화

<p>
  <img src="../images/sql-execution-order.jpg" style="width: 580px" />
</p>

SQL 문은 데이터베이스 시스템에서 다음과 같은 여러 단계로 실행됩니다. 

- SQL문 파싱과 유효성 검사 
- SQL을 관계대수(relational algebra) 같은 내부 표현으로 변환 
- 내부 표현을 최적화하고 인덱스 정보를 활용하는 실행 계획 생성 
- 계획 실행 및 결과 반환

SQL 실행은 매우 복잡하며 다음과 같은 많은 고려 사항을 포함합니다. 

- 인덱스 및 캐시 사용 
- 테이블 조인 순서 
- 동시성 제어 
- 트랜잭션 관리

### SQL 언어 

1986년, SQL(Structured Query Language)이 표준이 되었습니다. 그 후 40년 동안 관계형 데이터베이스 관리 시스템에서 가장 많이 사용되는 언어가 되었습니다. 최신 표준(ANSI SQL 2016)을 읽는 데는 많은 시간이 소요될 수 있습니다. 어떻게 배울 수 있을까요? 

<p>
  <img src="../images/how-to-learn-sql.jpg" />
</p>

SQL 언어에는 5가지 구성 요소가 있습니다. 

- DDL: data definition language. 예: CREATE, ALTER, DROP 
- DQL: data query language. 예: SELECT 
- DML: data manipulation language. 예: INSERT, UPDATE, DELETE 
- DCL: data control language. 예: GRANT, REVOKE 
- TCL: transaction control language. 예: COMMIT, ROLLBACK 

백엔드 엔지니어의 경우 대부분을 알아야 할 수도 있습니다. 데이터 분석가라면 DQL을 잘 이해해야 할 수도 있습니다. 자신에게 가장 관련성이 높은 주제를 선택하세요. 

## 캐시

### 데이터는 어디에나 캐시됩니다

이 다이어그램은 일반적인 아키텍처에서 데이터를 캐시하는 위치를 보여줍니다.

<p>
  <img src="../images/where do we cache data.jpeg" style="width: 720px" />
</p>


플로우를 따라 **multiple layers** 가 있습니다.

1. Client apps: HTTP 응답은 브라우저에 의해 캐시될 수 있습니다. HTTP를 통해 처음으로 데이터를 요청하면 HTTP 헤더에 만료 정책과 함께 반환되며, 데이터를 다시 요청하면 클라이언트 앱이 먼저 브라우저 캐시에서 데이터를 검색하려고 시도합니다.
2. CDN: CDN은 정적 웹 리소스를 캐시합니다. 클라이언트는 근처의 CDN 노드에서 데이터를 검색할 수 있습니다.
3. Load Balancer: 로드 밸런서는 리소스도 캐시할 수 있습니다.
4. Messaging infra: Message brokers가 먼저 디스크에 메시지를 저장한 다음, consumers는 자신의 속도에 맞춰 메시지를 검색합니다. 리텐션 폴리시에 따라 데이터는 일정 기간 동안 카프카 클러스터에 캐시됩니다.
5. Services: 서비스에는 여러개의 캐시 계층이 있습니다. CPU 캐시에 데이터가 없으면 메모리 캐시에서 검색을 시도합니다. 때로는 서비스가 디스크에 데이터를 저장하는 세컨드 레벨 캐시가 있는 경우도 있습니다.
6. Distributed Cache: Redis와 같은 분산 캐시는 여러 서비스에 대한 키-값 쌍을 메모리에 보관합니다. 데이터베이스보다 훨씬 뛰어난 읽기/쓰기 성능을 제공합니다.
7. Full-text Search: 도큐먼트 검색이나 로그 검색을 위해 Elastic Search와 같은 풀 텍스트 검색을 사용해야 할 때가 있습니다. 데이터 사본도 검색 엔진에서 인덱스됩니다.
8. Database: 데이터베이스 내에서도 다양한 레벨의 캐시가 있습니다.
- WAL(Write-ahead Log): 데이터는 B 트리 인덱스를 구축하기 전에 먼저 WAL에 기록됩니다.
- Bufferpool: 쿼리 결과를 캐시하기 위해 할당된 메모리 영역입니다.
- Materialized View: 쿼리 결과를 미리 계산하고 데이터베이스 테이블에 저장하여 쿼리 성능을 향상시킵니다.
- Transaction log: 모든 트랜잭션과 데이터베이스 업데이트 기록합니다.
- Replication Log: 데이터베이스 클러스터의 복제 상태를 기록하는 데 사용됩니다.

### Redis는 왜 빠른가요? 

아래 다이어그램과 같이 3가지 주요 이유가 있습니다.

<p>
  <img src="../images/why_redis_fast.jpeg" />
</p>


1. Redis is a RAM-based data store. RAM access is at least 1000 times faster than random disk access.
2. Redis leverages IO multiplexing and single-threaded execution loop for execution efficiency.
3. Redis leverages several efficient lower-level data structures.

Question: Another popular in-memory store is Memcached. Do you know the differences between Redis and Memcached?

You might have noticed the style of this diagram is different from my previous posts. Please let me know which one you prefer.

### Redis는 어떻게 사용하나요?

<p>
  <img src="../images/top-redis-use-cases.jpg" style="width: 520px" />
</p>


There is more to Redis than just caching. 

Redis can be used in a variety of scenarios as shown in the diagram. 

- Session 

  We can use Redis to share user session data among different services. 

- Cache 

  We can use Redis to cache objects or pages, especially for hotspot data. 

- Distributed lock 

  We can use a Redis string to acquire locks among distributed services. 

- Counter 

  We can count how many likes or how many reads for articles. 

- Rate limiter 

  We can apply a rate limiter for certain user IPs. 

- Global ID generator 

  We can use Redis Int for global ID. 

- Shopping cart 

  We can use Redis Hash to represent key-value pairs in a shopping cart. 

- Calculate user retention 

  We can use Bitmap to represent the user login daily and calculate user retention. 

- Message queue 

  We can use List for a message queue. 

- Ranking 

  We can use ZSet to sort the articles. 

### 주요 캐싱 전략

Designing large-scale systems usually requires careful consideration of caching. 
Below are five caching strategies that are frequently utilized. 

<p>
  <img src="../images/top_caching_strategy.jpeg" style="width: 680px" />
</p>



## 마이크로서비스 아키텍처

### 일반적인 마이크로서비스 아키텍처는 어떤 모습일까요? 

<p>
  <img src="../images/typical-microservice-arch.jpg" style="width: 520px" />
</p>


The diagram below shows a typical microservice architecture. 

- Load Balancer: This distributes incoming traffic across multiple backend services. 
- CDN (Content Delivery Network): CDN is a group of geographically distributed servers that hold static content for faster delivery. The clients look for content in CDN first, then progress  to backend services.
- API Gateway: This handles incoming requests and routes them to the relevant services. It talks to the identity provider and service discovery.
- Identity Provider: This handles authentication and authorization for users. 
- Service Registry & Discovery: Microservice registration and discovery happen in this component, and the API gateway looks for relevant services in this component to talk to. 
- Management: This component is responsible for monitoring the services.
- Microservices: Microservices are designed and deployed in different domains. Each domain has its own database. The API gateway talks to the microservices via REST API or other protocols, and the microservices within the same domain talk to each other using RPC (Remote Procedure Call).

Benefits of microservices:

- They can be quickly designed, deployed, and horizontally scaled.
- Each domain can be independently maintained by a dedicated team.
- Business requirements can be customized in each domain and better supported, as a result.

### 마이크로서비스 모범사례

A picture is worth a thousand words: 9 best practices for developing microservices.

<p>
  <img src="../images/microservice-best-practices.jpeg" />
</p>

 
When we develop microservices, we need to follow the following best practices: 

1. Use separate data storage for each microservice 
2. Keep code at a similar level of maturity 
3. Separate build for each microservice 
4. Assign each microservice with a single responsibility 
5. Deploy into containers 
6. Design stateless services 
7. Adopt domain-driven design
8. Design micro frontend 
9. Orchestrating microservices 

### 마이크로서비스에 일반적으로 사용하는 기술 스택은 무엇인가요

Below you will find a diagram showing the microservice tech stack, both for the development phase and for production.

<p>
  <img src="../images/microservice-tech.jpeg" />
</p>


▶️ 𝐏𝐫𝐞-𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧

- Define API - This establishes a contract between frontend and backend. We can use Postman or OpenAPI for this.
- Development - Node.js or react is popular for frontend development, and java/python/go for backend development. Also, we need to change the configurations in the API gateway according to API definitions.
- Continuous Integration - JUnit and Jenkins for automated testing. The code is packaged into a Docker image and deployed as microservices.

▶️ 𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧

- NGinx is a common choice for load balancers. Cloudflare provides CDN (Content Delivery Network). 
- API Gateway - We can use spring boot for the gateway, and use Eureka/Zookeeper for service discovery.
- The microservices are deployed on clouds. We have options among AWS, Microsoft Azure, or Google GCP.
Cache and Full-text Search - Redis is a common choice for caching key-value pairs. Elasticsearch is used for full-text search.
- Communications - For services to talk to each other, we can use messaging infra Kafka or RPC.
- Persistence - We can use MySQL or PostgreSQL for a relational database, and Amazon S3 for object store. We can also use Cassandra for the wide-column store if necessary.
- Management & Monitoring - To manage so many microservices, the common Ops tools include Prometheus, Elastic Stack, and Kubernetes.

### 카프카가 빠른 이유

There are many design decisions that contributed to Kafka’s performance. In this post, we’ll focus on two. We think these two carried the most weight.

<p>
  <img src="../images/why_is_kafka_fast.jpeg" />
</p>

1. The first one is Kafka’s reliance on Sequential I/O.
2. The second design choice that gives Kafka its performance advantage is its focus on efficiency: zero copy principle.
 
The diagram illustrates how the data is transmitted between producer and consumer, and what zero-copy means.
 
- Step 1.1 - 1.3: Producer writes data to the disk 
- Step 2: Consumer reads data without zero-copy

2.1 The data is loaded from disk to OS cache

2.2 The data is copied from OS cache to Kafka application

2.3 Kafka application copies the data into the socket buffer 

2.4 The data is copied from socket buffer to network card

2.5 The network card sends data out to the consumer

 
- Step 3: Consumer reads data with zero-copy

3.1: The data is loaded from disk to OS cache
3.2 OS cache directly copies the data to the network card via sendfile() command
3.3 The network card sends data out to the consumer
 
Zero copy is a shortcut to save the multiple data copies between application context and kernel context.

## 결제 시스템

### How to learn payment systems?

<p>
  <img src="../images/learn-payments.jpg" />
</p>

###  Why is the credit card called “the most profitable product in banks”? How does VISA/Mastercard make money? 

The diagram below shows the economics of the credit card payment flow.

<p>
  <img src="../images/how does visa makes money.jpg" style="width: 640px" />
</p>

1.&nbsp;&nbsp;The cardholder pays a merchant $100 to buy a product.

2.&nbsp;The merchant benefits from the use of the credit card with higher sales volume and needs to compensate the issuer and the card network for providing the payment service. The acquiring bank sets a fee with the merchant, called the “merchant discount fee.”

3 - 4. The acquiring bank keeps $0.25 as the acquiring markup, and $1.75 is paid to the issuing bank as the interchange fee. The merchant discount fee should cover the interchange fee. 

  The interchange fee is set by the card network because it is less efficient for each issuing bank to negotiate fees with each merchant.

5.&nbsp;&nbsp;The card network sets up the network assessments and fees with each bank, which pays the card network for its services every month. For example, VISA charges a 0.11% assessment, plus a $0.0195 usage fee, for every swipe.

6.&nbsp;&nbsp;The cardholder pays the issuing bank for its services.

Why should the issuing bank be compensated?

- The issuer pays the merchant even if the cardholder fails to pay the issuer. 
- The issuer pays the merchant before the cardholder pays the issuer.
- The issuer has other operating costs, including managing customer accounts, providing statements, fraud detection, risk management, clearing & settlement, etc. 

### How does VISA work when we swipe a credit card at a merchant’s shop?

<p>
  <img src="../images/visa_payment.jpeg" />
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
  <img src="../images/how-does-upi-work.png"  style="width: 600px" />
</p>


## DevOps

###  DevOps vs. SRE vs. Platform Engineering. What is the difference?

The concepts of DevOps, SRE, and Platform Engineering have emerged at different times and have been developed by various individuals and organizations. 

<p>
  <img src="../images/devops-sre-platform.jpg" />
</p>

DevOps as a concept was introduced in 2009 by Patrick Debois and Andrew Shafer at the Agile conference. They sought to bridge the gap between software development and operations by promoting a collaborative culture and shared responsibility for the entire software development lifecycle. 

SRE, or Site Reliability Engineering, was pioneered by Google in the early 2000s to address operational challenges in managing large-scale, complex systems. Google developed SRE practices and tools, such as the Borg cluster management system and the Monarch monitoring system, to improve the reliability and efficiency of their services. 

Platform Engineering is a more recent concept, building on the foundation of SRE engineering. The precise origins of Platform Engineering are less clear, but it is generally understood to be an extension of the DevOps and SRE practices, with a focus on delivering a comprehensive platform for product development that supports the entire business perspective. 

It's worth noting that while these concepts emerged at different times. They are all related to the broader trend of improving collaboration, automation, and efficiency in software development and operations. 

### What is k8s (Kubernetes)?

K8s is a container orchestration system. It is used for container deployment and management. Its design is greatly impacted by Google’s internal system Borg.

<p>
  <img src="../images/k8s.jpeg" style="width: 680px" />
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

### Docker vs. Kubernetes. Which one should we use? 

<p>
  <img src="../images/docker-vs-k8s.jpg" style="width: 680px" />
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

### How does Docker work? 

The diagram below shows the architecture of Docker and how it works when we run “docker build”, “docker pull” 
and “docker run”. 

<p>
  <img src="../images/docker.jpg" style="width: 680px" />
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

### How Git Commands work

To begin with, it's essential to identify where our code is stored. The common assumption is that there are only two locations - one on a remote server like Github and the other on our local machine. However, this isn't entirely accurate. Git maintains three local storages on our machine, which means that our code can be found in four places: 

<p>
  <img src="../images/git-commands.png" style="width: 600px" />
</p>


- Working directory: where we edit files 
- Staging area: a temporary location where files are kept for the next commit 
- Local repository: contains the code that has been committed 
- Remote repository: the remote server that stores the code 

Most Git commands primarily move files between these four locations. 

### How does Git Work?

The diagram below shows the Git workflow. 

<p>
  <img src="../images/git-workflow.jpeg" style="width: 520px" />
</p>


Git is a distributed version control system. 

Every developer maintains a local copy of the main repository and edits and commits to the local copy. 

The commit is very fast because the operation doesn’t interact with the remote repository. 

If the remote repository crashes, the files can be recovered from the local repositories. 

### Git merge vs. Git rebase

What are the differences?

<p>
  <img src="../images/git-merge-git-rebase.jpeg" style="width: 680px" />
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

## Cloud Services

### A nice cheat sheet of different cloud services (2023 edition)

<p>
  <img src="../images/cloud-compare.jpg" />
</p>


### What is cloud native?

Below is a diagram showing the evolution of architecture and processes since the 1980s. 

<p>
  <img src="../images/cloud-native.jpeg" style="width: 640px" />
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

## Developer productivity tools

### Visualize JSON files

Nested JSON files are hard to read.

**JsonCrack** generates graph diagrams from JSON files and makes them easy to read.

Additionally, the generated diagrams can be downloaded as images.

<p>
  <img src="../images/json-cracker.jpeg" />
</p>


### Automatically turn code into architecture diagrams

<p>
  <img src="../images/diagrams_as_code.jpeg" style="width: 640px" />
</p>


What does it do?

- Draw the cloud system architecture in Python code.
- Diagrams can also be rendered directly inside the Jupyter Notebooks.
- No design tools are needed. 
- Supports the following providers: AWS, Azure, GCP, Kubernetes, Alibaba Cloud, Oracle Cloud, etc. 
 
[Github repo](https://github.com/mingrammer/diagrams)

## Linux

### Linux file system explained

<p>
  <img src="../images/linux-file-systems.jpg" style="width: 680px" />
</p>

The Linux file system used to resemble an unorganized town where individuals constructed their houses wherever they pleased. However, in 1994, the Filesystem Hierarchy Standard (FHS) was introduced to bring order to the Linux file system.

By implementing a standard like the FHS, software can ensure a consistent layout across various Linux distributions. Nonetheless, not all Linux distributions strictly adhere to this standard. They often incorporate their own unique elements or cater to specific requirements.
To become proficient in this standard, you can begin by exploring. Utilize commands such as "cd" for navigation and "ls" for listing directory contents. Imagine the file system as a tree, starting from the root (/). With time, it will become second nature to you, transforming you into a skilled Linux administrator.

### 18 Most-used Linux Commands You Should Know 

Linux commands are instructions for interacting with the operating system. They help manage files, directories, system processes, and many other aspects of the system. You need to become familiar with these commands in order to navigate and maintain Linux-based systems efficiently and effectively. 

This diagram below shows popular Linux commands: 

<p>
  <img src="../images/18 Most-Used Linux Commands You Should Know-01.jpeg" style="width: 680px" />
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

## Security

### How does HTTPS work?

Hypertext Transfer Protocol Secure (HTTPS) is an extension of the Hypertext Transfer Protocol (HTTP.) HTTPS transmits encrypted data using Transport Layer Security (TLS.) If the data is hijacked online, all the hijacker gets is binary code. 

<p>
  <img src="../images/https.jpg" />
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
  <img src="../images/oAuth2.jpg" />
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
  <img src="../images/top4-most-used-auth.jpg" />
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
  <img src="../images/session.jpeg" />
</p>

From simple to complex, here is my understanding of user identity management:

- WWW-Authenticate is the most basic method. You are asked for the username and password by the browser. As a result of the inability to control the login life cycle, it is seldom used today.

- A finer control over the login life cycle is session-cookie. The server maintains session storage, and the browser keeps the ID of the session. A cookie usually only works with browsers and is not mobile app friendly.

- To address the compatibility issue, the token can be used. The client sends the token to the server, and the server validates the token. The downside is that the token needs to be encrypted and decrypted, which may be time-consuming.

- JWT is a standard way of representing tokens. This information can be verified and trusted because it is digitally signed. Since JWT contains the signature, there is no need to save session information on the server side.

- By using SSO (single sign-on), you can sign on only once and log in to multiple websites. It uses CAS (central authentication service) to maintain cross-site information.

- By using OAuth 2.0, you can authorize one website to access your information on another website.

### How to store passwords safely in the database and how to validate a password? 

<p>
  <img src="../images/salt.jpg" style="width: 720px" />
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

**How to validate a password?**

To validate a password, it can go through the following process:

1. A client enters the password.
1. The system fetches the corresponding salt from the database.
1. The system appends the salt to the password and hashes it. Let’s call the hashed value H1.
1. The system compares H1 and H2, where H2 is the hash stored in the database. If they are the same, the password is valid. 

### Explaining JSON Web Token (JWT) to a 10 year old Kid

<p>
  <img src="../images/jwt.jpg" />
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
  <img src="../images/google_authenticate.jpeg" />
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


##  Real World Case Studies

### Netflix's Tech Stack

This post is based on research from many Netflix engineering blogs and open-source projects. If you come across any inaccuracies, please feel free to inform us.

<p>
  <img src="../images/netflix tech stack.png" style="width: 680px" />
</p>

**Mobile and web**: Netflix has adopted Swift and Kotlin to build native mobile apps. For its web application, it uses React.

**Frontend/server communication**: Netflix uses GraphQL.

**Backend services**: Netflix relies on ZUUL, Eureka, the Spring Boot framework, and other technologies.

**Databases**: Netflix utilizes EV cache, Cassandra, CockroachDB, and other databases.

**Messaging/streaming**: Netflix employs Apache Kafka and Fink for messaging and streaming purposes.

**Video storage**: Netflix uses S3 and Open Connect for video storage.

**Data processing**: Netflix utilizes Flink and Spark for data processing, which is then visualized using Tableau. Redshift is used for processing structured data warehouse information.

**CI/CD**: Netflix employs various tools such as JIRA, Confluence, PagerDuty, Jenkins, Gradle, Chaos Monkey, Spinnaker, Atlas, and more for CI/CD processes.

### Twitter Architecture 2022

Yes, this is the real Twitter architecture. It is posted by Elon Musk and redrawn by us for better readability. 

<p>
  <img src="../images/twitter-arch.jpeg" />
</p>


### Evolution of Airbnb’s microservice architecture over the past 15 years

Airbnb’s microservice architecture went through 3 main stages. 

<p>
  <img src="../images/airbnb_arch.jpeg" />
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
  <img src="../images/monorepo-microrepo.jpg" />
</p>


Monorepo isn't new; Linux and Windows were both created using Monorepo. To improve scalability and build speed, Google developed its internal dedicated toolchain to scale it faster and strict coding quality standards to keep it consistent. 

Amazon and Netflix are major ambassadors of the Microservice philosophy. This approach naturally separates the service code into separate repositories. It scales faster but can lead to governance pain points later on. 

Within Monorepo, each service is a folder, and every folder has a BUILD config and OWNERS permission control. Every service member is responsible for their own folder. 

On the other hand, in Microrepo, each service is responsible for its repository, with the build config and permissions typically set for the entire repository. 

In Monorepo, dependencies are shared across the entire codebase regardless of your business, so when there's a version upgrade, every codebase upgrades their version. 

In Microrepo, dependencies are controlled within each repository. Businesses choose when to upgrade their versions based on their own schedules. 

Monorepo has a standard for check-ins. Google's code review process is famously known for setting a high bar, ensuring a coherent quality standard for Monorepo, regardless of the business. 

Microrepo can either set its own standard or adopt a shared standard by incorporating the best practices. It can scale faster for business, but the code quality might be a bit different. 
Google engineers built Bazel, and Meta built Buck. There are other open-source tools available, including Nx, Lerna, and others. 

Over the years, Microrepo has had more supported tools, including Maven and Gradle for Java, NPM for NodeJS, and CMake for C/C++, among others. 

### How will you design the Stack Overflow website? 

If your answer is on-premise servers and monolith (on the bottom of the following image), you would likely fail the interview, but that's how it is built in reality!

<p>
  <img src="../images/stackoverflow.jpg" />
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
  <img src="../images/serverless-to-monolithic.jpeg" />
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
  <img src="../images/hotstar_emojis.jpeg" style="width: 720px" />
</p>


1. Clients send emojis through standard HTTP requests. You can think of Golang Service as a typical Web Server. Golang is chosen because it supports concurrency well. Threads in Golang are lightweight.

2. Since the write volume is very high, Kafka (message queue) is used as a buffer.

3. Emoji data are aggregated by a streaming processing service called Spark. It aggregates data every 2 seconds, which is configurable. There is a trade-off to be made based on the interval. A shorter interval means emojis are delivered to other clients faster but it also means more computing resources are needed.

4. Aggregated data is written to another Kafka. 

5. The PubSub consumers pull aggregated emoji data from Kafka. 

6. Emojis are delivered to other clients in real-time through the PubSub infrastructure. The PubSub infrastructure is interesting. Hotstar considered the following protocols: Socketio, NATS, MQTT, and gRPC, and settled with MQTT.
 
A similar design is adopted by LinkedIn which streams a million likes/sec.

### How Discord Stores Trillions Of Messages 

The diagram below shows the evolution of message storage at Discord: 

<p>
  <img src="../images/discord-store-messages.jpg" />
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
  <img src="../images/live_streaming_updated.jpg" style="width: 640px" />
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
