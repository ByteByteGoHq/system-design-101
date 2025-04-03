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

Karmaşık sistemleri görsellerle ve basit terimlerle açıklıyoruz.

İster bir System Design mülakatına hazırlanıyor olun, ister sistemlerin yüzeyin altında nasıl çalıştığını anlamak istiyor olun, bu repository'nin size yardımcı olacağını umuyoruz.

# İçindekiler

<!-- TOC toc.levels=2 -->

- [İletişim protokolleri](#communication-protocols)
  - [REST API vs. GraphQL](#rest-api-vs-graphql)
  - [gRPC nasıl çalışır?](#how-does-grpc-work)
  - [Webhook nedir?](#what-is-a-webhook)
  - [API performansı nasıl iyileştirilir?](#how-to-improve-api-performance)
  - [HTTP 1.0 -\> HTTP 1.1 -\> HTTP 2.0 -\> HTTP 3.0 (QUIC)](#http-10---http-11---http-20---http-30-quic)
  - [SOAP vs REST vs GraphQL vs RPC](#soap-vs-rest-vs-graphql-vs-rpc)
  - [Code First vs. API First](#code-first-vs-api-first)
  - [HTTP durum kodları](#http-status-codes)
  - [API gateway ne yapar?](#what-does-api-gateway-do)
  - [Etkili ve güvenli API'ler nasıl tasarlanır?](#how-do-we-design-effective-and-safe-apis)
  - [TCP/IP kapsülleme](#tcpip-encapsulation)
  - [Nginx neden "reverse" proxy olarak adlandırılır?](#why-is-nginx-called-a-reverse-proxy)
  - [Yaygın load-balancing algoritmaları nelerdir?](#what-are-the-common-load-balancing-algorithms)
  - [URL, URI, URN - Farklarını biliyor musunuz?](#url-uri-urn---do-you-know-the-differences)
- [CI/CD](#cicd)
  - [CI/CD Pipeline Basit Terimlerle Açıklaması](#cicd-pipeline-explained-in-simple-terms)
  - [Netflix Tech Stack (CI/CD Pipeline)](#netflix-tech-stack-cicd-pipeline)
- [Mimari desenler](#architecture-patterns)
  - [MVC, MVP, MVVM, MVVM-C ve VIPER](#mvc-mvp-mvvm-mvvm-c-and-viper)
  - [Her Geliştiricinin Bilmesi Gereken 18 Temel Tasarım Deseni](#18-key-design-patterns-every-developer-should-know)
- [Veritabanı](#database)
  - [Cloud servislerindeki farklı veritabanları için güzel bir kopya kağıdı](#a-nice-cheat-sheet-of-different-databases-in-cloud-services)
  - [Veritabanlarınızı Güçlendiren 8 Veri Yapısı](#8-data-structures-that-power-your-databases)
  - [SQL sorgusu veritabanında nasıl çalıştırılır?](#how-is-an-sql-statement-executed-in-the-database)
  - [CAP teoremi](#cap-theorem)
  - [Bellek ve Depolama Türleri](#types-of-memory-and-storage)
  - [SQL sorgusunu görselleştirme](#visualizing-a-sql-query)
  - [SQL dili](#sql-language)
- [Cache](#cache)
  - [Veri her yerde önbelleğe alınır](#data-is-cached-everywhere)
  - [Redis neden bu kadar hızlı?](#why-is-redis-so-fast)
  - [Redis nasıl kullanılabilir?](#how-can-redis-be-used)
  - [En iyi önbellek stratejileri](#top-caching-strategies)
- [Microservice mimarisi](#microservice-architecture)
  - [Tipik bir microservice mimarisi nasıl görünür?](#what-does-a-typical-microservice-architecture-look-like)
  - [Microservice En İyi Uygulamalar](#microservice-best-practices)
  - [Microservice'ler için yaygın olarak hangi teknoloji yığını kullanılır?](#what-tech-stack-is-commonly-used-for-microservices)
  - [Kafka neden hızlı?](#why-is-kafka-fast)
- [Ödeme sistemleri](#payment-systems)
  - [Ödeme sistemleri nasıl öğrenilir?](#how-to-learn-payment-systems)
  - [Kredi kartı neden "bankaların en karlı ürünü" olarak adlandırılıyor? VISA/Mastercard nasıl para kazanıyor?](#why-is-the-credit-card-called-the-most-profitable-product-in-banks-how-does-visamastercard-make-money)
  - [Bir mağazada kredi kartı kullandığımızda VISA nasıl çalışır?](#how-does-visa-work-when-we-swipe-a-credit-card-at-a-merchants-shop)
  - [Dünya Çapında Ödeme Sistemleri Serisi (Bölüm 1): Hindistan'da Unified Payments Interface (UPI)](#payment-systems-around-the-world-series-part-1-unified-payments-interface-upi-in-india)
- [DevOps](#devops)
  - [DevOps vs. SRE vs. Platform Engineering. Fark nedir?](#devops-vs-sre-vs-platform-engineering-what-is-the-difference)
  - [k8s (Kubernetes) nedir?](#what-is-k8s-kubernetes)
  - [Docker vs. Kubernetes. Hangisini kullanmalıyız?](#docker-vs-kubernetes-which-one-should-we-use)
  - [Docker nasıl çalışır?](#how-does-docker-work)
- [GIT](#git)
  - [Git Komutları nasıl çalışır?](#how-git-commands-work)
  - [Git Nasıl Çalışır?](#how-does-git-work)
  - [Git merge vs. Git rebase](#git-merge-vs-git-rebase)
- [Cloud Servisleri](#cloud-services)
  - [Farklı cloud servisleri için güzel bir kopya kağıdı (2023 sürümü)](#a-nice-cheat-sheet-of-different-cloud-services-2023-edition)
  - [Cloud native nedir?](#what-is-cloud-native)
- [Geliştirici üretkenlik araçları](#developer-productivity-tools)
  - [JSON dosyalarını görselleştirme](#visualize-json-files)
  - [Kodu otomatik olarak mimari diyagramlara dönüştürme](#automatically-turn-code-into-architecture-diagrams)
- [Linux](#linux)
  - [Linux dosya sistemi açıklaması](#linux-file-system-explained)
  - [Bilmeniz Gereken En Çok Kullanılan 18 Linux Komutu](#18-most-used-linux-commands-you-should-know)
- [Güvenlik](#security)
  - [HTTPS nasıl çalışır?](#how-does-https-work)
  - [Oauth 2.0 Basit Terimlerle Açıklaması](#oauth-20-explained-with-simple-terms)
  - [Kimlik Doğrulamanın 4 Temel Formu](#top-4-forms-of-authentication-mechanisms)
  - [Session, cookie, JWT, token, SSO ve OAuth 2.0 - bunlar nedir?](#session-cookie-jwt-token-sso-and-oauth-20---what-are-they)
  - [Şifreler veritabanında nasıl güvenli saklanır ve şifre nasıl doğrulanır?](#how-to-store-passwords-safely-in-the-database-and-how-to-validate-a-password)
  - [JSON Web Token'ı (JWT) 10 yaşındaki bir çocuğa açıklamak](#explaining-json-web-token-jwt-to-a-10-year-old-kid)
  - [Google Authenticator (veya diğer 2 faktörlü doğrulayıcılar) nasıl çalışır?](#how-does-google-authenticator-or-other-types-of-2-factor-authenticators-work)
- [Gerçek Dünya Vaka Çalışmaları](#real-world-case-studies)
  - [Netflix'in Teknoloji Yığını](#netflixs-tech-stack)
  - [Twitter Mimarisi 2022](#twitter-architecture-2022)
  - [Airbnb'nin microservice mimarisinin son 15 yıldaki evrimi](#evolution-of-airbnbs-microservice-architecture-over-the-past-15-years)
  - [Monorepo vs. Microrepo](#monorepo-vs-microrepo)
  - [Stack Overflow websitesi nasıl tasarlanır?](#how-will-you-design-the-stack-overflow-website)
  - [Amazon Prime Video izleme neden serverless'tan monolitik'e geçti? %90 maliyet nasıl tasarruf edilebilir?](#why-did-amazon-prime-video-monitoring-move-from-serverless-to-monolithic-how-can-it-save-90-cost)
  - [Disney Hotstar bir turnuva sırasında 5 Milyar Emojiyi nasıl yakalıyor?](#how-does-disney-hotstar-capture-5-billion-emojis-during-a-tournament)
  - [Discord Trilyonlarca Mesajı Nasıl Depoluyor?](#how-discord-stores-trillions-of-messages)
  - [YouTube, TikTok live veya Twitch'te video canlı yayınları nasıl çalışır?](#how-do-video-live-streamings-work-on-youtube-tiktok-live-or-twitch)

<!-- /TOC -->

## İletişim protokolleri

Architecture style'lar, bir application programming interface (API)'nin farklı bileşenlerinin birbirleriyle nasıl etkileşime girdiğini tanımlar. Sonuç olarak, API'lerin tasarımı ve oluşturulması için standart bir yaklaşım sağlayarak verimlilik, güvenilirlik ve diğer sistemlerle entegrasyon kolaylığını sağlarlar. İşte en çok kullanılan style'lar:

<p>
  <img src="../images/api-architecture-styles.png" style="width: 640px">
</p>

- SOAP:

  Olgun, kapsamlı, XML-tabanlı

  Kurumsal uygulamalar için en uygun

- RESTful:

  Popüler, kolay uygulanabilir, HTTP metodları

  Web servisleri için ideal

- GraphQL:

  Query dili, özel veri istekleri

  Network yükünü azaltır, daha hızlı yanıtlar

- gRPC:

  Modern, yüksek performanslı, Protocol Buffers

  Microservices mimarileri için uygun

- WebSocket:

  Gerçek zamanlı, çift yönlü, kalıcı bağlantılar

  Düşük gecikmeli veri alışverişi için mükemmel

- Webhook:

  Event-driven, HTTP callbacks, asenkron

  Olaylar gerçekleştiğinde sistemleri bilgilendirir


### REST API vs. GraphQL

API tasarımı söz konusu olduğunda, REST ve GraphQL'in kendilerine özgü güçlü ve zayıf yönleri vardır.

Aşağıdaki diyagram REST ve GraphQL arasındaki hızlı bir karşılaştırmayı göstermektedir.

<p>
  <img src="../images/graphQL.jpg">
</p>

REST

- CRUD işlemleri için GET, POST, PUT, DELETE gibi standart HTTP metodlarını kullanır.
- Ayrı servisler/uygulamalar arasında basit, uniform arayüzlere ihtiyaç duyulduğunda iyi çalışır.
- Caching stratejileri uygulaması kolaydır.
- Dezavantajı, farklı endpointlerden ilişkili verileri toplamak için birden fazla roundtrip gerektirebilir.

GraphQL

- Clientların tam olarak ihtiyaç duydukları verileri sorgulamaları için tek bir endpoint sağlar.
- Clientlar nested querylerde gerekli alanları belirtir ve server sadece bu alanları içeren optimize edilmiş payloadlar döner.
- Veri değiştirmek için Mutations ve gerçek zamanlı bildirimler için Subscriptions destekler.
- Birden fazla kaynaktan veri toplamada başarılıdır ve hızla değişen frontend gereksinimleriyle iyi çalışır.
- Ancak, karmaşıklığı client tarafına kaydırır ve düzgün korunmazsa kötüye kullanılabilir querylere izin verebilir.
- Caching stratejileri REST'e göre daha karmaşık olabilir.

REST ve GraphQL arasındaki en iyi seçim, uygulamanın ve geliştirme ekibinin özel gereksinimlerine bağlıdır. GraphQL karmaşık veya sık değişen frontend ihtiyaçları için uygunken, REST basit ve tutarlı contractların tercih edildiği uygulamalar için uygundur.

Hiçbir API yaklaşımı mükemmel çözüm değildir. Doğru stili seçmek için gereksinimleri ve trade-offları dikkatle değerlendirmek önemlidir. Hem REST hem de GraphQL, veri sunmak ve modern uygulamaları güçlendirmek için geçerli seçeneklerdir.


### gRPC nasıl çalışır?

RPC (Remote Procedure Call), microservice mimarisinde servisler farklı sunuculara dağıtıldığında uzak servisler arasındaki iletişimi sağladığı için "**remote**" olarak adlandırılır. Kullanıcı açısından, yerel bir fonksiyon çağrısı gibi davranır.

Aşağıdaki diyagram **gRPC** için genel veri akışını göstermektedir.

<p>
  <img src="../images/grpc.jpg">
</p>

Adım 1: Client'tan bir REST çağrısı yapılır. Request body genellikle JSON formatındadır.

Adım 2 - 4: Order service (gRPC client) REST çağrısını alır, dönüştürür ve payment service'e bir RPC çağrısı yapar. gRPC **client stub**'ı binary formata encode eder ve low-level transport layer'a gönderir.

Adım 5: gRPC paketleri HTTP2 üzerinden network'e gönderir. Binary encoding ve network optimizasyonları sayesinde gRPC'nin JSON'dan 5 kat daha hızlı olduğu söylenir.

Adım 6 - 8: Payment service (gRPC server) paketleri network'ten alır, decode eder ve server uygulamasını çağırır.

Adım 9 - 11: Sonuç server uygulamasından döner, encode edilir ve transport layer'a gönderilir.

Adım 12 - 14: Order service paketleri alır, decode eder ve sonucu client uygulamasına gönderir.

### Webhook nedir?

Aşağıdaki diyagram polling ve Webhook arasındaki karşılaştırmayı göstermektedir.

<p>
  <img src="../images/webhook.jpeg" style="width: 680px" />
</p>

Bir eCommerce websitesi işlettiğimizi varsayalım. Client'lar API gateway üzerinden order service'e siparişler gönderir, bu siparişler ödeme işlemleri için payment service'e gider. Payment service daha sonra işlemleri tamamlamak için external payment service provider (PSP) ile iletişime geçer.

External PSP ile iletişimi yönetmenin iki yolu vardır.

**1. Short polling**

PSP'ye ödeme isteği gönderdikten sonra, payment service sürekli olarak PSP'den ödeme durumunu sorar. Birkaç tur sonra, PSP sonunda durumu döner.

Short polling'in iki dezavantajı vardır:
* Durumun sürekli sorgulanması payment service'ten kaynak gerektirir.
* External service doğrudan payment service ile iletişim kurarak güvenlik açıkları oluşturur.

**2. Webhook**

External service'e bir webhook kaydedebiliriz. Bu şu anlama gelir: istek hakkında güncellemeleriniz olduğunda belirli bir URL'den beni geri arayın. PSP işlemi tamamladığında, ödeme durumunu güncellemek için HTTP isteği çağıracaktır.

Bu şekilde, programlama paradigması değişir ve payment service artık ödeme durumunu sorgulamak için kaynak harcamak zorunda kalmaz.

PSP hiç geri aramazsa ne olur? Her saat ödeme durumunu kontrol etmek için bir housekeeping job ayarlayabiliriz.

Webhook'lar genellikle reverse API'ler veya push API'ler olarak adlandırılır çünkü server client'a HTTP istekleri gönderir. Webhook kullanırken 3 şeye dikkat etmemiz gerekir:

1. External service'in çağıracağı uygun bir API tasarlamamız gerekir.
2. Güvenlik nedeniyle API gateway'de uygun kurallar ayarlamamız gerekir.
3. External service'te doğru URL'yi kaydetmemiz gerekir.

### API performansını nasıl iyileştiririz?

Aşağıdaki diyagram API performansını iyileştirmek için 5 yaygın işlemi gösterir.

<p>
  <img src="../images/api-performance.jpg">
</p>

Pagination

Bu, sonuçların boyutu büyük olduğunda yaygın bir iyileştirmedir. Sonuçlar client'a streaming olarak geri döndürülür, böylece servis yanıtını iyileştirir.

Asynchronous Logging

Synchronous logging her çağrı için disk ile iletişime geçer ve sistemi yavaşlatabilir. Asynchronous logging logları önce lock-free buffer'a gönderir ve hemen geri döner. Loglar periyodik olarak diske yazılır. Bu I/O yükünü önemli ölçüde azaltır.

Caching

Sık erişilen verileri cache'e depolayabiliriz. Client doğrudan database'e gitmek yerine önce cache'i sorgulayabilir. Cache miss olursa, client database'i sorgulayabilir. Redis gibi cache'ler verileri memory'de depolar, bu nedenle veri erişimi database'den çok daha hızlıdır.

Payload Compression

Request ve response'lar gzip vb. kullanılarak sıkıştırılabilir, böylece iletilen veri boyutu çok daha küçük olur. Bu upload ve download hızını artırır.

Connection Pool

Kaynaklara erişirken genellikle database'den veri yüklememiz gerekir. Database connection'larını açıp kapatmak önemli bir yük ekler. Bu nedenle database'e açık connection'ların bir pool'u üzerinden bağlanmalıyız. Connection pool, connection yaşam döngüsünü yönetmekten sorumludur.

### HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)

Her nesil HTTP'nin çözdüğü sorunlar nelerdir?

Aşağıdaki diyagram HTTP'nin ana özelliklerini gösterir.

<p>
  <img src="../images/http3.jpg" />
</p>

- HTTP 1.0 1996'da tamamlandı ve tamamen belgelendi. Aynı sunucuya yapılan her istek ayrı bir TCP bağlantısı gerektirir.

- HTTP 1.1 1997'de yayınlandı. Bir TCP bağlantısı yeniden kullanım için açık bırakılabilir (persistent connection), ancak HOL (head-of-line) blocking sorununu çözmez.

  HOL blocking - tarayıcıda izin verilen paralel istek sayısı dolduğunda, sonraki isteklerin öncekiler tamamlanana kadar beklemesi gerekir.

- HTTP 2.0 2015'te yayınlandı. Request multiplexing ile HOL sorununu ele alır, bu da application katmanındaki HOL blocking'i ortadan kaldırır, ancak HOL hala transport (TCP) katmanında mevcuttur.

  Diyagramda görebileceğiniz gibi, HTTP 2.0 HTTP "streams" kavramını tanıttı: farklı HTTP değişimlerinin aynı TCP bağlantısı üzerinde multiplexing yapılmasına izin veren bir soyutlama. Her stream'in sırayla gönderilmesi gerekmez.

- HTTP 3.0'ın ilk taslağı 2020'de yayınlandı. HTTP 2.0'ın önerilen halefidir. Altta yatan transport protokolü olarak TCP yerine QUIC kullanır, böylece transport katmanındaki HOL blocking'i ortadan kaldırır.

QUIC, UDP tabanlıdır. Transport katmanında stream'leri birinci sınıf vatandaş olarak tanıtır. QUIC stream'leri aynı QUIC bağlantısını paylaşır, bu nedenle yenilerini oluşturmak için ek handshake ve slow start gerekmez, ancak QUIC stream'leri bağımsız olarak iletilir, böylece çoğu durumda bir stream'i etkileyen paket kaybı diğerlerini etkilemez.

### SOAP vs REST vs GraphQL vs RPC

Aşağıdaki diyagram API timeline ve API stilleri karşılaştırmasını gösterir.

Zamanla farklı API mimari stilleri yayınlanır. Her biri kendi standart veri değişim desenlerine sahiptir.

Her stilin kullanım durumlarını diyagramda görebilirsiniz.

<p>
  <img src="../images/SOAP vs REST vs GraphQL vs RPC.jpeg" />
</p>


### Code First vs. API First

Aşağıdaki diyagram, kod ilk geliştirme ile API ilk tasarım arasındaki farkları gösterir. Neden API ilk tasarımı düşünmeliyiz?

<p>
  <img src="../images/api_first.jpg" style="width: 680px" />
</p>


- Mikroservisler sistemin karmaşıklığını artırır ve sistemdeki farklı işlevleri sunmak için ayrı servislerimiz var. Bu mimari, ayrımcılık ve görev ayrımını kolaylaştırır, ancak servisler arasındaki farklı iletişimleri ele almak zorundayız. 

Sistemin karmaşıklığını düşünmeden kod yazmak ve hizmetlerin sınırlarını dikkatlice tanımlamak daha iyi bir yöntemdir.

- Ayrı işlevsel takımlar aynı dil konuşmalı ve sadece kendi bileşenleri ve hizmetleri için sorumludur. Organizasyonun API tasarımı aracılığıyla aynı dil konuşması önerilir.

API tasarımını doğrulamak için kod yazmadan önce mock request ve response'lar oluşturabiliriz.

- Yazılım kalitesini ve geliştirici verimliliğini artırır. Proje başladığında belirsizliklerin çoğunu giderdiğimiz için, genel geliştirme süreci daha sorunsuz ilerler ve yazılım kalitesi büyük ölçüde artar.

Geliştiriciler ani değişiklikler konusunda pazarlık yapmak yerine fonksiyonel geliştirmeye odaklanabildikleri için süreçten memnundur.

Proje yaşam döngüsünün sonuna doğru sürprizlerle karşılaşma olasılığı azalır.

API'yi önce tasarladığımız için, kod geliştirilirken testler de tasarlanabilir. Bir anlamda, API first development kullanırken TDD (Test Driven Design) de yapmış oluyoruz.

### HTTP status codes

<p>
  <img src="../images/http-status-code.jpg" style="width: 540px" />
</p>


HTTP response kodları beş kategoriye ayrılır:

Informational (100-199)
Success (200-299) 
Redirection (300-399)
Client Error (400-499)
Server Error (500-599)

### API gateway ne yapar?

Aşağıdaki diyagram API gateway'in detaylarını gösterir.

<p>
  <img src="../images/api_gateway.jpg" style="width: 520px" />
</p>

1. Client bir HTTP isteği API gateway'e gönderir.

2. API gateway HTTP isteğindeki nitelikleri çözer ve doğrular.

3. API gateway izin listesi/reddetme listesi kontrollerini yapar.

4. API gateway kimlik sağlayıcısına kimlik doğrulaması ve yetkilendirme yapar.

5. Hız sınırlama kuralları isteğe uygulanır. Eğer sınırı aşıyorsa, istek reddedilir.

6-7. - İstek temel kontrolleri geçtikten sonra, API gateway path eşleştirmesi yaparak yönlendirilecek ilgili servisi bulur.

8. - API gateway isteği uygun protokole dönüştürür ve backend microservice'lere gönderir.

9-12. -  API gateway hataları düzgün şekilde yönetebilir ve hatanın düzelmesi uzun sürerse (circuit break) arızaları ele alır. Ayrıca logging ve monitoring için ELK (Elastic-Logstash-Kibana) stack kullanabilir. Bazen API gateway'de data cache'leriz.

### Nasıl tasarımızı etkili ve güvenli API'lar?

Aşağıdaki diyagram, bir alışveriş sepeti örneğiyle tipik API tasarımlarını gösterir.

<p>
  <img src="../images/safe-apis.jpg" />
</p>


API tasarımı URL yol tasarımından çok daha fazlasıdır. Çoğunlukla, uygun kaynak adları, tanımlayıcılar ve yol desenlerini seçmek gerekir. HTTP başlık alanlarının veya API gateway'de etkili hız sınırlama kurallarını tasarlamak için aynı önemdedir.

### TCP/IP kapsülleme

Veriler nasıl gönderilir? Neden OSI modelinde çok sayıda katman gerekir?

Aşağıdaki diyagram, verilerin ağ üzerinden nasıl kapsüllendiğini ve kapsülleme sürecinin tersini gösterir.

<p>
  <img src="../images/osi model.jpeg" />
</p>

1. Device A, HTTP protokolü üzerinden ağ üzerinden Device B'ye veri gönderirken, ilk olarak uygulama katmanında HTTP başlığı eklenir.

2. Ardından, veriye TCP veya UDP başlığı eklenir. Bu, taşıma katmanında TCP segmentlerine kapsüllenir. Başlık, kaynak port, hedef port ve sıra numarasını içerir.

3. Sonra, veriye IP başlığı eklenir. IP başlığı, kaynak ve hedef IP adreslerini içerir.

4. Sonra, veriye MAC başlığı eklenir. Bu, veri bağlantı katmanında kapsüllenir. Başlık, kaynak ve hedef MAC adreslerini içerir.

5. Kapsüllenen çerçeveler fiziksel katmana gönderilir ve ağ üzerinde ikili bitler olarak gönderilir.

6-10. - Device B ağdan bitleri aldığında, kapsülleme sürecinin tersini yapar. Başlıklar bir tabaka bir tabaka kaldırılır ve sonunda Device B verileri okuyabilir.

Ağ modelinde katmanlar gereklidir çünkü her katman kendi sorumluluklarına odaklanır. Her katman, son katmanın verilerinin anlamını bilmek zorunda değildir.

### Neden Nginx "reverse" proxy olarak adlandırılır?

Aşağıdaki diyagram, ileri ve ters proxy arasındaki farkları gösterir.

<p>
  <img src="../images/Forward Proxy v.s. Reverse Proxy2x.jpg" style="width: 720px" />
</p>

Forward proxy, kullanıcı cihazları ile internet arasında bulunan bir sunucudur.

Forward proxy genellikle şunlar için kullanılır:

1. İstemcileri korumak
2. Gezinme kısıtlamalarını aşmak  
3. Belirli içeriklere erişimi engellemek

Reverse proxy, istemciden gelen istekleri kabul eden, web sunucularına ileten ve sanki proxy sunucusu işlemi gerçekleştirmiş gibi sonuçları istemciye döndüren bir sunucudur.

Reverse proxy şunlar için iyidir:

1. Sunucuları korumak
2. Load balancing
3. Statik içerikleri cache'leme
4. SSL iletişimlerini şifreleme ve şifre çözme

### Yaygın load-balancing algoritmaları nelerdir?

Aşağıdaki diyagram 6 yaygın algoritmayı gösterir.

<p>
  <img src="../images/lb-algorithms.jpg" />
</p>

- Statik Algoritmalar

1. Round robin

    İstemci istekleri sıralı bir düzende farklı servis örneklerine gönderilir. Servislerin genellikle durumsuz olması gerekir.

3. Sticky round-robin

    Bu, round-robin algoritmasının geliştirilmiş halidir. Eğer Alice'in ilk isteği servis A'ya giderse, sonraki istekleri de servis A'ya gider.

4. Weighted round-robin

    Admin her servis için ağırlık belirleyebilir. Daha yüksek ağırlığa sahip olanlar diğerlerinden daha fazla istek işler.

6. Hash

    Bu algoritma, gelen isteklerin IP'sine veya URL'sine bir hash fonksiyonu uygular. İstekler hash fonksiyonu sonucuna göre ilgili örneklere yönlendirilir.

- Dinamik Algoritmalar

5. Least connections

    Yeni bir istek, en az eşzamanlı bağlantıya sahip servis örneğine gönderilir.

7. Least response time

    Yeni bir istek, en hızlı yanıt süresine sahip servis örneğine gönderilir.

### URL, URI, URN - Aralarındaki farkları biliyor musunuz?

Aşağıdaki diyagram URL, URI ve URN karşılaştırmasını gösterir.

<p>
  <img src="../images/url-uri-urn.jpg" />
</p>

- URI

URI (Uniform Resource Identifier), web üzerindeki mantıksal veya fiziksel bir kaynağı tanımlayan bir belirteçtir. URL ve URN, URI'nin alt tipleridir. URL bir kaynağın konumunu belirtirken, URN bir kaynağı isimlendirmek için kullanılır.

Bir URI aşağıdaki parçalardan oluşur:
scheme:[//authority]path[?query][#fragment]

- URL

URL (Uniform Resource Locator), HTTP'nin temel kavramıdır. Web üzerindeki benzersiz bir kaynağın adresidir. FTP ve JDBC gibi diğer protokollerle de kullanılabilir.

- URN

URN (Uniform Resource Name), urn şemasını kullanır. URN'ler bir kaynağın konumunu belirlemek için kullanılamaz. Diyagramda verilen basit örnek, bir namespace ve namespace'e özgü bir dizeden oluşur.

Konu hakkında daha detaylı bilgi için [W3C'nin açıklamasını](https://www.w3.org/TR/uri-clarification/) incelemenizi öneririm.

## CI/CD

### CI/CD Pipeline Basit Terimlerle Açıklaması

<p>
  <img src="../images/ci-cd-pipeline.jpg" style="width: 680px" />
</p>

Bölüm 1 - CI/CD ile SDLC

Software development life cycle (SDLC) birkaç önemli aşamadan oluşur: geliştirme, test, deployment ve bakım. CI/CD bu aşamaları otomatikleştirir ve entegre eder, böylece daha hızlı ve güvenilir sürümler yapılabilir.

Kod bir git repository'sine push edildiğinde, otomatik bir build ve test süreci tetiklenir. Kodu doğrulamak için end-to-end (e2e) test senaryoları çalıştırılır. Testler başarılı olursa, kod otomatik olarak staging/production ortamına deploy edilebilir. Sorun bulunursa, kod hata düzeltmesi için geliştirme aşamasına geri gönderilir. Bu otomasyon geliştiricilere hızlı geri bildirim sağlar ve production ortamındaki hata riskini azaltır.

Bölüm 2 - CI ve CD Arasındaki Fark

Continuous Integration (CI) build, test ve merge süreçlerini otomatikleştirir. Entegrasyon sorunlarını erken tespit etmek için kod commit edildiğinde testleri çalıştırır. Bu, sık kod commit'lerini ve hızlı geri bildirimi teşvik eder.

Continuous Delivery (CD) infrastructure değişiklikleri ve deployment gibi release süreçlerini otomatikleştirir. Otomatik iş akışları sayesinde yazılımın her zaman güvenilir bir şekilde release edilebilmesini sağlar. CD ayrıca production deployment öncesinde gereken manuel test ve onay adımlarını da otomatikleştirebilir.

Bölüm 3 - CI/CD Pipeline

Tipik bir CI/CD pipeline'ı birbiriyle bağlantılı birkaç aşamadan oluşur:
- Geliştirici kod değişikliklerini source control'e commit eder
- CI server değişiklikleri algılar ve build'i tetikler
- Kod derlenir ve test edilir (unit, integration testleri)
- Test sonuçları geliştiriciye raporlanır
- Başarılı olursa, artifact'lar staging ortamlarına deploy edilir
- Release öncesi staging'de daha fazla test yapılabilir
- CD sistemi onaylanan değişiklikleri production'a deploy eder

### Netflix Tech Stack (CI/CD Pipeline)

<p>
  <img src="../images/netflix-ci-cd.jpg" style="width: 720px" />
</p>

Planning: Netflix Engineering planlama için JIRA ve dokümantasyon için Confluence kullanır.

Coding: Backend servisi için ana programlama dili Java'dır, farklı kullanım durumları için başka diller de kullanılır.

Build: Build için ağırlıklı olarak Gradle kullanılır ve çeşitli kullanım durumlarını desteklemek için Gradle eklentileri oluşturulur.

Packaging: Paket ve bağımlılıklar release için bir Amazon Machine Image (AMI) içine paketlenir.

Testing: Test, production kültürünün chaos araçları oluşturmaya odaklanmasını vurgular.

Deployment: Netflix, canary rollout deployment için kendi geliştirdiği Spinnaker'ı kullanır.

Monitoring: İzleme metrikleri Atlas'ta merkezileştirilir ve anomali tespiti için Kayenta kullanılır.

Incident report: Olaylar önceliğe göre dağıtılır ve olay yönetimi için PagerDuty kullanılır.

## Architecture patterns

### MVC, MVP, MVVM, MVVM-C ve VIPER
Bu mimari desenler, iOS veya Android platformlarında uygulama geliştirmede en yaygın kullanılan desenlerdir. Geliştiriciler bunları önceki desenlerin sınırlamalarının üstesinden gelmek için tanıttı. Peki nasıl farklılaşıyorlar?

<p>
  <img src="../images/client arch patterns.png" style="width: 720px" />
</p>

- MVC, en eski desen, neredeyse 50 yıl öncesine dayanır
- Her desenin içeriği görüntülemek ve kullanıcı girdisini almaktan sorumlu bir "view" (V) bileşeni vardır
- Çoğu desen iş verilerini yönetmek için bir "model" (M) içerir
- "Controller", "presenter" ve "view-model", view ile model arasında (VIPER deseninde "entity") aracılık yapan çevirmenlerdir

### Her Geliştiricinin Bilmesi Gereken 18 Temel Design Pattern

Pattern'lar yaygın tasarım problemlerine yeniden kullanılabilir çözümlerdir ve daha düzgün, daha verimli bir geliştirme sürecine yol açar. Daha iyi yazılım yapıları oluşturmak için blueprint görevi görürler. Bunlar en popüler pattern'lardan bazılarıdır:

<p>
  <img src="../images/18-oo-patterns.png" />
</p>

- Abstract Factory: Aile Yaratıcısı - İlişkili öğe grupları oluşturur.
- Builder: Lego Ustası - Nesneleri adım adım oluşturur, yaratım ve görünümü ayrı tutar.
- Prototype: Klon Yapıcı - Tam hazırlanmış örneklerin kopyalarını oluşturur.
- Singleton: Tek ve Yalnız - Sadece bir örneği olan özel bir sınıf.
- Adapter: Evrensel Fiş - Farklı arayüzlere sahip şeyleri bağlar.
- Bridge: Fonksiyon Bağlayıcı - Bir nesnenin nasıl çalıştığını ne yaptığına bağlar.
- Composite: Ağaç Oluşturucu - Basit ve karmaşık parçalardan ağaç benzeri yapılar oluşturur.
- Decorator: Özelleştirici - Çekirdeği değiştirmeden nesnelere özellikler ekler.
- Facade: Tek Durak - Tüm sistemi tek, basitleştirilmiş bir arayüzle temsil eder.
- Flyweight: Alan Tasarrufçusu - Küçük, yeniden kullanılabilir öğeleri verimli şekilde paylaşır.
- Proxy: Vekil Oyuncu - Başka bir nesneyi temsil eder, erişimi veya eylemleri kontrol eder.
- Chain of Responsibility: İstek Röle - Bir isteği işlenene kadar nesneler zinciri boyunca iletir.
- Command: Görev Sarmalayıcı - Bir isteği eyleme hazır bir nesneye dönüştürür.
- Iterator: Koleksiyon Gezgini - Bir koleksiyondaki öğelere tek tek erişir.
- Mediator: İletişim Merkezi - Farklı sınıflar arasındaki etkileşimleri basitleştirir.
- Memento: Zaman Kapsülü - Bir nesnenin durumunu yakalar ve geri yükler.
- Observer: Haber Yayıncısı - Sınıfları diğer nesnelerdeki değişiklikler hakkında bilgilendirir.
- Visitor: Yetenekli Misafir - Değiştirmeden bir sınıfa yeni işlemler ekler.

## Veritabanı

### Cloud servislerindeki farklı veritabanları için güzel bir özet tablo

<p>
  <img src="../images/cloud-dbs2.png" />
</p>

Projeniz için doğru veritabanını seçmek karmaşık bir görevdir. Her biri farklı kullanım durumlarına uygun birçok veritabanı seçeneği, hızlıca karar verme yorgunluğuna yol açabilir.

Bu özet tablonun, projenizin ihtiyaçlarına uygun doğru servisi belirlemek ve olası tuzaklardan kaçınmak için üst düzey bir yön sağlamasını umuyoruz.

Not: Google'ın veritabanı kullanım durumları için sınırlı dokümantasyonu var. Mevcut olanları inceleyip en iyi seçeneğe ulaşmak için elimizden geleni yapsak da, bazı girişlerin daha doğru olması gerekebilir.

### Veritabanlarınıza Güç Veren 8 Veri Yapısı

Cevap kullanım durumunuza göre değişecektir. Veriler bellekte veya diskte indekslenebilir. Benzer şekilde, veri formatları sayılar, stringler, coğrafi koordinatlar vb. gibi değişir. Sistem yazma ağırlıklı veya okuma ağırlıklı olabilir. Tüm bu faktörler veritabanı indeks formatı seçiminizi etkiler.

<p>
  <img src="../images/8-ds-db.jpg" />
</p>

Veri indeksleme için kullanılan en popüler veri yapılarından bazıları şunlardır:

- Skiplist: yaygın bir bellek içi indeks türü. Redis'te kullanılır
- Hash index: "Map" veri yapısının (veya "Collection") çok yaygın bir uygulaması
- SSTable: değiştirilemez disk üzerinde "Map" uygulaması
- LSM tree: Skiplist + SSTable. Yüksek yazma performansı
- B-tree: disk tabanlı çözüm. Tutarlı okuma/yazma performansı
- Inverted index: doküman indeksleme için kullanılır. Lucene'de kullanılır
- Suffix tree: string pattern araması için
- R-tree: en yakın komşuyu bulmak gibi çok boyutlu arama için

### SQL ifadesi veritabanında nasıl çalıştırılır?

Aşağıdaki diyagram süreci göstermektedir. Farklı veritabanlarının mimarileri farklı olsa da, diyagram bazı ortak tasarımları göstermektedir.

<p>
  <img src="../images/sql execution order in db.jpeg" style="width: 580px" />
</p>

Adım 1 - SQL ifadesi veritabanına bir transport layer protokolü (örn. TCP) üzerinden gönderilir.

Adım 2 - SQL ifadesi komut ayrıştırıcıya gönderilir, sözdizimsel ve anlamsal analiz yapılır ve bir sorgu ağacı oluşturulur.

Adım 3 - Sorgu ağacı optimize ediciye gönderilir. Optimize edici bir yürütme planı oluşturur.

Adım 4 - Yürütme planı yürütücüye gönderilir. Yürütücü yürütmeden veri alır.

Adım 5 - Erişim yöntemleri, yürütme için gerekli veri getirme mantığını sağlar, storage engine'den veri alır.

Adım 6 - Erişim yöntemleri SQL ifadesinin salt okunur olup olmadığına karar verir. Eğer sorgu salt okunur ise (SELECT ifadesi), daha fazla işlem için buffer manager'a iletilir. Buffer manager verileri cache'te veya veri dosyalarında arar.

Adım 7 - Eğer ifade UPDATE veya INSERT ise, daha fazla işlem için transaction manager'a iletilir.

Adım 8 - Transaction sırasında, veriler lock modundadır. Bu lock manager tarafından garanti edilir. Ayrıca transaction'ın ACID özelliklerini sağlar.

### CAP teoremi

CAP teoremi bilgisayar bilimindeki en ünlü terimlerden biridir, ancak farklı geliştiricilerin farklı anlayışları olduğuna bahse girerim. Ne olduğunu ve neden kafa karıştırıcı olabileceğini inceleyelim.

<p>
  <img src="../images/cap theorem.jpeg" />
</p>

CAP teoremi, bir dağıtık sistemin bu üç garantiden aynı anda ikisinden fazlasını sağlayamayacağını belirtir.

**Consistency**: tutarlılık, tüm istemcilerin hangi node'a bağlandıklarından bağımsız olarak aynı anda aynı verileri görmesi anlamına gelir.

**Availability**: kullanılabilirlik, bazı node'lar devre dışı olsa bile veri isteyen herhangi bir istemcinin yanıt alması anlamına gelir.

**Partition Tolerance**: partition, iki node arasındaki iletişim kopukluğunu gösterir. Partition tolerance, sistemin network partition'larına rağmen çalışmaya devam etmesi anlamına gelir.

"3'ten 2'si" formülasyonu yararlı olabilir, **ancak bu basitleştirme yanıltıcı olabilir**.

1. Veritabanı seçmek kolay değildir. Seçimimizi sadece CAP teoremine dayanarak gerekçelendirmek yeterli değildir. Örneğin, şirketler sohbet uygulamaları için Cassandra'yı sadece AP sistem olduğu için seçmezler. Cassandra'yı sohbet mesajlarını depolamak için tercih edilir bir seçenek yapan iyi özelliklerin bir listesi vardır. Daha derine inmemiz gerekir.

2. "CAP sadece tasarım alanının çok küçük bir kısmını yasaklar: nadir görülen partition'ların varlığında mükemmel kullanılabilirlik ve tutarlılık". CAP Twelve Years Later: How the "Rules" Have Changed makalesinden alıntı.

3. Teorem %100 kullanılabilirlik ve tutarlılık hakkındadır. Daha gerçekçi bir tartışma, network partition olmadığında gecikme ve tutarlılık arasındaki trade-off'lar olacaktır. Daha fazla detay için PACELC teoremine bakın.

**CAP teoremi gerçekten yararlı mı?**

Zihnimizi bir dizi trade-off tartışmasına açtığı için hala yararlı olduğunu düşünüyorum, ancak bu hikayenin sadece bir parçası. Doğru veritabanını seçerken daha derine inmemiz gerekiyor.

### Bellek ve Depolama Türleri

<p>
  <img src="../images/Types_of_Memory_and_Storage.jpeg" style="width: 420px" />
</p>

### SQL sorgusunu görselleştirme

<p>
  <img src="../images/sql-execution-order.jpg" style="width: 580px" />
</p>

SQL ifadeleri veritabanı sistemi tarafından birkaç adımda yürütülür:

- SQL ifadesini ayrıştırma ve geçerliliğini kontrol etme
- SQL'i ilişkisel cebir gibi dahili bir gösterime dönüştürme
- Dahili gösterimi optimize etme ve indeks bilgisini kullanan bir yürütme planı oluşturma
- Planı yürütme ve sonuçları döndürme

SQL'in yürütülmesi oldukça karmaşıktır ve şunlar gibi birçok hususu içerir:

- İndeks ve cache kullanımı
- Tablo join'lerinin sırası
- Eşzamanlılık kontrolü
- Transaction yönetimi

### SQL dili

1986'da SQL (Structured Query Language) bir standart haline geldi. Sonraki 40 yıl boyunca, ilişkisel veritabanı yönetim sistemleri için dominant dil haline geldi. En son standardı (ANSI SQL 2016) okumak zaman alıcı olabilir. Nasıl öğrenebilirim?

<p>
  <img src="../images/how-to-learn-sql.jpg" />
</p>

SQL dilinin 5 bileşeni vardır:

- DDL: veri tanımlama dili, CREATE, ALTER, DROP gibi
- DQL: veri sorgulama dili, SELECT gibi
- DML: veri manipülasyon dili, INSERT, UPDATE, DELETE gibi
- DCL: veri kontrol dili, GRANT, REVOKE gibi
- TCL: transaction kontrol dili, COMMIT, ROLLBACK gibi

Bir backend mühendisi olarak, çoğunu bilmeniz gerekebilir. Bir veri analisti olarak, DQL'i iyi anlamanız gerekebilir. Size en uygun konuları seçin.

## Cache

### Veri her yerde cache'lenir

Bu diyagram tipik bir mimaride verileri nerede cache'lediğimizi gösteriyor.

<p>
  <img src="../images/where do we cache data.jpeg" style="width: 720px" />
</p>

Akış boyunca **birden çok katman** vardır.

1. Client uygulamaları: HTTP yanıtları browser tarafından cache'lenebilir. İlk kez HTTP üzerinden veri istediğimizde, HTTP header'ında bir süre sonu politikasıyla birlikte döner; tekrar veri istediğimizde, client uygulama önce browser cache'inden veriyi almaya çalışır.
2. CDN: CDN statik web kaynaklarını cache'ler. İstemciler yakındaki bir CDN node'undan veri alabilir.
3. Load Balancer: Load Balancer da kaynakları cache'leyebilir.
4. Messaging altyapısı: Message broker'lar mesajları önce diske kaydeder, sonra consumer'lar kendi hızlarında alır. Retention politikasına bağlı olarak, veriler belirli bir süre Kafka cluster'larında cache'lenir.
5. Servisler: Bir serviste birden çok cache katmanı vardır. Veri CPU cache'inde değilse, servis veriyi bellekten almaya çalışır. Bazen servisin veriyi diskte depolamak için ikinci seviye cache'i vardır.
6. Distributed Cache: Redis gibi distributed cache'ler çoklu servisler için key-value çiftlerini bellekte tutar. Veritabanından çok daha iyi okuma/yazma performansı sağlar.
7. Full-text Search: Bazen doküman araması veya log araması için Elastic Search gibi full-text search'leri kullanmamız gerekir. Verinin bir kopyası search engine'de de indekslenir.
8. Veritabanı: Veritabanında bile farklı seviyelerde cache'lerimiz var:
- WAL(Write-ahead Log): B tree indeksi oluşturmadan önce veriler WAL'a yazılır
- Bufferpool: Sorgu sonuçlarını cache'lemek için ayrılmış bellek alanı
- Materialized View: Daha iyi sorgu performansı için sorgu sonuçlarını önceden hesaplar ve veritabanı tablolarında saklar
- Transaction log: tüm transaction'ları ve veritabanı güncellemelerini kaydeder
- Replication Log: bir veritabanı cluster'ında replikasyon durumunu kaydetmek için kullanılır

### Redis neden hızlı?

Aşağıdaki diyagramda gösterildiği gibi 3 ana neden var.

<p>
  <img src="../images/why_redis_fast.jpeg" />
</p>

1. Redis RAM tabanlı bir veri deposudur. RAM erişimi rastgele disk erişiminden en az 1000 kat daha hızlıdır.
2. Redis, yürütme verimliliği için IO multiplexing ve single-threaded execution loop kullanır.
3. Redis birkaç verimli düşük seviyeli veri yapısı kullanır.

Soru: Bir diğer popüler in-memory store Memcached'dir. Redis ve Memcached arasındaki farkları biliyor musunuz?

Bu diyagramın stilinin önceki paylaşımlarımdan farklı olduğunu fark etmiş olabilirsiniz. Hangisini tercih ettiğinizi lütfen bana bildirin.

### Redis nasıl kullanılabilir?

<p>
  <img src="../images/top-redis-use-cases.jpg" style="width: 520px" />
</p>

Redis'in sadece cache'lemeden daha fazlası var.

Redis diyagramda gösterildiği gibi çeşitli senaryolarda kullanılabilir.

- Session

  Redis'i farklı servisler arasında kullanıcı session verilerini paylaşmak için kullanabiliriz.

- Cache

  Redis'i özellikle hotspot veriler için nesneleri veya sayfaları cache'lemek için kullanabiliriz.

- Distributed lock

  Distributed servisler arasında lock almak için Redis string kullanabiliriz.

- Counter

  Makaleler için kaç beğeni veya kaç okuma olduğunu sayabiliriz.

- Rate limiter

  Belirli kullanıcı IP'leri için rate limiter uygulayabiliriz.

- Global ID generator

  Global ID için Redis Int kullanabiliriz.

- Shopping cart

  Alışveriş sepetindeki key-value çiftlerini temsil etmek için Redis Hash kullanabiliriz.

- Calculate user retention

  Kullanıcı günlük girişini temsil etmek ve user retention'ı hesaplamak için Bitmap kullanabiliriz.

- Message queue

  Message queue için List kullanabiliriz.

- Ranking

  Makaleleri sıralamak için ZSet kullanabiliriz.

### En iyi cache stratejileri

Büyük ölçekli sistemleri tasarlamak genellikle cache'lemenin dikkatli bir şekilde değerlendirilmesini gerektirir.
Aşağıda sıkça kullanılan beş cache stratejisi bulunmaktadır.

<p>
  <img src="../images/top_caching_strategy.jpeg" style="width: 680px" />
</p>

## Microservice mimarisi

### Tipik bir microservice mimarisi neye benzer?

<p>
  <img src="../images/typical-microservice-arch.jpg" style="width: 520px" />
</p>

Aşağıdaki diyagram tipik bir microservice mimarisini göstermektedir.

- Load Balancer: Gelen trafiği birden çok backend servisi arasında dağıtır.
- CDN (Content Delivery Network): CDN, daha hızlı teslimat için coğrafi olarak dağıtılmış sunuculardan oluşan bir gruptur. İstemciler önce CDN'de içerik arar, sonra backend servislere ilerler.
- API Gateway: Gelen istekleri işler ve ilgili servislere yönlendirir. Identity provider ve service discovery ile iletişim kurar.
- Identity Provider: Kullanıcılar için authentication ve authorization işlemlerini yönetir.
- Service Registry & Discovery: Microservice kaydı ve keşfi bu bileşende gerçekleşir ve API gateway iletişim kurmak için ilgili servisleri bu bileşende arar.
- Management: Bu bileşen servislerin izlenmesinden sorumludur.
- Microservices: Microservice'ler farklı domainlerde tasarlanır ve deploy edilir. Her domain'in kendi veritabanı vardır. API gateway microservice'lerle REST API veya diğer protokoller üzerinden iletişim kurar ve aynı domain içindeki microservice'ler birbirleriyle RPC (Remote Procedure Call) kullanarak iletişim kurar.

Microservice'lerin faydaları:

- Hızlıca tasarlanabilir, deploy edilebilir ve yatay olarak ölçeklenebilir.
- Her domain bağımsız olarak özel bir ekip tarafından yönetilebilir.
- İş gereksinimleri her domain'de özelleştirilebilir ve sonuç olarak daha iyi desteklenebilir.

### Microservice Best Practices

Bir resim bin kelimeye bedeldir: microservice geliştirmek için 9 best practice.

<p>
  <img src="../images/microservice-best-practices.jpeg" />
</p>

Microservice'ler geliştirirken aşağıdaki best practice'leri takip etmeliyiz:

1. Her microservice için ayrı veri depolama kullan
2. Kodu benzer olgunluk seviyesinde tut
3. Her microservice için ayrı build kullan
4. Her microservice'e tek bir sorumluluk ata
5. Container'lara deploy et
6. Stateless servisler tasarla
7. Domain-driven design benimse
8. Micro frontend tasarla
9. Microservice'leri orchestrate et

### Microservice'ler için yaygın olarak hangi tech stack kullanılır?

Aşağıda geliştirme aşaması ve production için microservice tech stack'ini gösteren bir diyagram bulacaksınız.

<p>
  <img src="../images/microservice-tech.jpeg" />
</p>

▶️ Pre-Production

- API Tanımlama - Frontend ve backend arasında bir sözleşme oluşturur. Bunun için Postman veya OpenAPI kullanabiliriz.
- Development - Frontend geliştirme için Node.js veya react popülerdir, backend geliştirme için java/python/go. Ayrıca API tanımlarına göre API gateway'deki konfigürasyonları değiştirmemiz gerekir.
- Continuous Integration - Otomatik test için JUnit ve Jenkins. Kod bir Docker image'ına paketlenir ve microservice olarak deploy edilir.

▶️ Production

- Load balancer'lar için NGinx yaygın bir seçimdir. Cloudflare CDN (Content Delivery Network) sağlar.
- API Gateway - Gateway için spring boot kullanabiliriz ve service discovery için Eureka/Zookeeper kullanabiliriz.
- Microservice'ler cloud'larda deploy edilir. AWS, Microsoft Azure veya Google GCP arasında seçeneklerimiz var.
Cache ve Full-text Search - Key-value çiftlerini cache'lemek için Redis yaygın bir seçimdir. Full-text search için Elasticsearch kullanılır.
- İletişim - Servislerin birbiriyle konuşması için messaging altyapısı Kafka veya RPC kullanabiliriz.
- Persistence - İlişkisel veritabanı için MySQL veya PostgreSQL, object store için Amazon S3 kullanabiliriz. Gerekirse wide-column store için Cassandra da kullanabiliriz.
- Management & Monitoring - Bu kadar çok microservice'i yönetmek için yaygın Ops araçları Prometheus, Elastic Stack ve Kubernetes'i içerir.

### Kafka neden hızlı

Kafka'nın performansına katkıda bulunan birçok tasarım kararı var. Bu yazıda, ikisine odaklanacağız. Bu ikisinin en büyük etkiye sahip olduğunu düşünüyoruz.

<p>
  <img src="../images/why_is_kafka_fast.jpeg" />
</p>

1. İlki Kafka'nın Sequential I/O'ya dayanmasıdır.
2. Kafka'ya performans avantajı sağlayan ikinci tasarım seçimi, verimliliğe odaklanmasıdır: zero copy prensibi.

Diyagram, verinin producer ve consumer arasında nasıl iletildiğini ve zero-copy'nin ne anlama geldiğini göstermektedir.

- Adım 1.1 - 1.3: Producer veriyi diske yazar
- Adım 2: Consumer zero-copy olmadan veri okur

2.1 Veri diskten OS cache'e yüklenir

2.2 Veri OS cache'den Kafka uygulamasına kopyalanır

2.3 Kafka uygulaması veriyi socket buffer'a kopyalar

2.4 Veri socket buffer'dan network card'a kopyalanır

2.5 Network card veriyi consumer'a gönderir

- Adım 3: Consumer zero-copy ile veri okur

3.1: Veri diskten OS cache'e yüklenir
3.2 OS cache sendfile() komutu ile veriyi doğrudan network card'a kopyalar
3.3 Network card veriyi consumer'a gönderir

Zero copy, uygulama bağlamı ve kernel bağlamı arasındaki çoklu veri kopyalamalarını kısaltmak için bir kısayoldur.
## Ödeme sistemleri

### Ödeme sistemleri nasıl öğrenilir?

<p>
  <img src="../images/learn-payments.jpg" />
</p>

### Kredi kartı neden "bankaların en karlı ürünü" olarak adlandırılır? VISA/Mastercard nasıl para kazanır?

Aşağıdaki diyagram kredi kartı ödeme akışının ekonomisini göstermektedir.

<p>
  <img src="../images/how does visa makes money.jpg" style="width: 640px" />
</p>

1.&nbsp;&nbsp;Kart sahibi bir ürün almak için satıcıya 100$ öder.

2.&nbsp;Satıcı, kredi kartı kullanımından daha yüksek satış hacmi ile fayda sağlar ve ödeme hizmetini sağladığı için ihraççıyı ve kart ağını tazmin etmesi gerekir. Acquirer bank, satıcı ile "merchant discount fee" olarak adlandırılan bir ücret belirler.

3 - 4. Acquirer bank acquiring markup olarak 0.25$ tutar ve 1.75$ ihraççı bankaya interchange fee olarak ödenir. Merchant discount fee, interchange fee'yi karşılamalıdır.

  Interchange fee kart ağı tarafından belirlenir çünkü her ihraççı bankanın her satıcı ile ücret müzakere etmesi daha verimsizdir.

5.&nbsp;&nbsp;Kart ağı, her banka ile network assessments ve ücretleri belirler, bankalar her ay kart ağına hizmetleri için ödeme yapar. Örneğin VISA, her işlem için %0.11 assessment ve 0.0195$ kullanım ücreti alır.

6.&nbsp;&nbsp;Kart sahibi hizmetleri için ihraççı bankaya ödeme yapar.

İhraççı banka neden tazmin edilmelidir?

- İhraççı, kart sahibi ihraççıya ödeme yapmasa bile satıcıya ödeme yapar.
- İhraççı, kart sahibi ihraççıya ödemeden önce satıcıya ödeme yapar.
- İhraççının müşteri hesaplarını yönetme, ekstreleri sağlama, dolandırıcılık tespiti, risk yönetimi, clearing & settlement gibi diğer operasyonel maliyetleri vardır.

### Bir satıcının dükkanında kredi kartı kullandığımızda VISA nasıl çalışır?

<p>
  <img src="../images/visa_payment.jpeg" />
</p>

VISA, Mastercard ve American Express fonların clearing ve settlement işlemleri için kart ağları olarak görev yapar. Card acquiring bank ve card issuing bank farklı olabilir - ve genellikle farklıdır. Eğer bankalar bir aracı olmadan işlemleri tek tek settle etmek zorunda kalsalardı, her banka diğer tüm bankalarla işlemleri settle etmek zorunda kalırdı. Bu oldukça verimsizdir.

Aşağıdaki diyagram kredi kartı ödeme sürecinde VISA'nın rolünü göstermektedir. İki akış söz konusudur. Authorization flow müşteri kredi kartını kullandığında gerçekleşir. Capture ve settlement flow satıcı günün sonunda parayı almak istediğinde gerçekleşir.

- Authorization Flow

Adım 0: Card issuing bank müşterilerine kredi kartları verir.

Adım 1: Kart sahibi bir ürün almak ister ve satıcının dükkanındaki Point of Sale (POS) terminalinde kredi kartını kullanır.

Adım 2: POS terminali işlemi, POS terminalini sağlayan acquiring bank'a gönderir.

Adım 3 ve 4: Acquiring bank işlemi kart ağına gönderir, kart ağı da onay için issuing bank'a gönderir.

Adım 4.1, 4.2 ve 4.3: İşlem onaylanırsa issuing bank parayı dondurur. Onay veya red cevabı acquirer'a ve POS terminaline gönderilir.

- Capture ve Settlement Flow

Adım 1 ve 2: Satıcı günün sonunda parayı toplamak ister, bu yüzden POS terminalinde "capture"a basar. İşlemler toplu olarak acquirer'a gönderilir. Acquirer işlem dosyasını kart ağına gönderir.

Adım 3: Kart ağı farklı acquirer'lardan toplanan işlemler için clearing yapar ve clearing dosyalarını farklı issuing bank'lara gönderir.

Adım 4: İssuing bank'lar clearing dosyalarının doğruluğunu onaylar ve ilgili acquiring bank'lara para transferi yapar.

Adım 5: Acquiring bank daha sonra parayı satıcının bankasına transfer eder.

Adım 4: Kart ağı farklı acquiring bank'lardan gelen işlemleri netleştirir. Clearing, karşılıklı işlemlerin netleştirildiği ve toplam işlem sayısının azaltıldığı bir süreçtir.

Bu süreçte kart ağı her banka ile konuşma yükünü üstlenir ve karşılığında servis ücreti alır.

### Dünya Genelinde Ödeme Sistemleri Serisi (Bölüm 1): Hindistan'da Unified Payments Interface (UPI)

UPI nedir? UPI, National Payments Corporation of India tarafından geliştirilen anlık gerçek zamanlı bir ödeme sistemidir.

Bugün Hindistan'daki dijital perakende işlemlerinin %60'ını oluşturmaktadır.

UPI = payment markup language + birlikte çalışabilir ödemeler için standart

<p>
  <img src="../images/how-does-upi-work.png"  style="width: 600px" />
</p>

## DevOps

### DevOps vs. SRE vs. Platform Engineering. Farkları nedir?

DevOps, SRE ve Platform Engineering kavramları farklı zamanlarda ortaya çıkmış ve çeşitli kişi ve organizasyonlar tarafından geliştirilmiştir.

<p>
  <img src="../images/devops-sre-platform.jpg" />
</p>

DevOps kavramı 2009'da Patrick Debois ve Andrew Shafer tarafından Agile konferansında tanıtıldı. Yazılım geliştirme ve operasyonlar arasındaki boşluğu, işbirlikçi bir kültürü ve tüm yazılım geliştirme yaşam döngüsü için paylaşılan sorumluluğu teşvik ederek kapatmayı amaçladılar.

SRE, yani Site Reliability Engineering, 2000'lerin başında Google tarafından büyük ölçekli, karmaşık sistemleri yönetmedeki operasyonel zorlukları ele almak için öncülük edildi. Google, hizmetlerinin güvenilirliğini ve verimliliğini artırmak için Borg cluster management system ve Monarch monitoring system gibi SRE uygulamaları ve araçları geliştirdi.

Platform Engineering daha yeni bir kavramdır ve SRE engineering temelini esas alır. Platform Engineering'in kesin kökenleri daha az belirgindir, ancak genel olarak DevOps ve SRE uygulamalarının bir uzantısı olarak anlaşılır ve tüm iş perspektifini destekleyen kapsamlı bir ürün geliştirme platformu sunmaya odaklanır.

Bu kavramların farklı zamanlarda ortaya çıktığını belirtmek önemlidir. Hepsi yazılım geliştirme ve operasyonlarda işbirliği, otomasyon ve verimliliği iyileştirme genel eğilimiyle ilgilidir.

### K8s (Kubernetes) nedir?

K8s bir container orchestration sistemidir. Container deployment ve yönetimi için kullanılır. Tasarımı Google'ın iç sistemi Borg'dan büyük ölçüde etkilenmiştir.

<p>
  <img src="../images/k8s.jpeg" style="width: 680px" />
</p>

Bir k8s cluster'ı, node olarak adlandırılan ve container'lı uygulamaları çalıştıran bir dizi worker machine'den oluşur. Her cluster'ın en az bir worker node'u vardır.

Worker node'lar, uygulama iş yükünün bileşenleri olan Pod'ları barındırır. Control plane, worker node'ları ve cluster'daki Pod'ları yönetir. Production ortamlarında, control plane genellikle birden fazla bilgisayarda çalışır ve bir cluster genellikle birden fazla node çalıştırır, fault tolerance ve high availability sağlar.

- Control Plane Bileşenleri

1. API Server

    API server k8s cluster'ındaki tüm bileşenlerle konuşur. Pod'lar üzerindeki tüm operasyonlar API server ile konuşularak yürütülür.

2. Scheduler

    Scheduler pod iş yüklerini izler ve yeni oluşturulan pod'lara yük atar.

3. Controller Manager

    Controller manager, Node Controller, Job Controller, EndpointSlice Controller ve ServiceAccount Controller dahil olmak üzere controller'ları çalıştırır.

4. Etcd
    
    etcd, tüm cluster verisi için Kubernetes'in backing store'u olarak kullanılan bir key-value store'dur.

- Node'lar

1. Pod'lar

    Bir pod, container'ların bir grubudur ve k8s'nin yönettiği en küçük birimdir. Pod'lar pod içindeki her container'a uygulanan tek bir IP adresine sahiptir.

2. Kubelet

    Cluster'daki her node'da çalışan bir agent'tır. Pod'daki container'ların çalıştığından emin olur.

3. Kube Proxy

    Kube-proxy, cluster'ınızdaki her node'da çalışan bir network proxy'dir. Node'a service'den gelen trafiği yönlendirir. İş isteklerini doğru container'lara iletir.

### Docker vs. Kubernetes. Hangisini kullanmalıyız?

<p>
  <img src="../images/docker-vs-k8s.jpg" style="width: 680px" />
</p>

Docker nedir?

Docker, uygulamaları izole container'larda paketlemenize, dağıtmanıza ve çalıştırmanıza olanak tanıyan açık kaynaklı bir platformdur. Uygulamaları ve bağımlılıklarını kapsülleyen hafif ortamlar sağlayan container'laştırmaya odaklanır.

Kubernetes nedir?

Kubernetes, genellikle K8s olarak anılır, açık kaynaklı bir container orchestration platformudur. Container'lı uygulamaların bir node cluster'ı genelinde deployment, scaling ve yönetimini otomatikleştirmek için bir framework sağlar.

İkisi birbirinden nasıl farklıdır?

Docker: Docker tek bir işletim sistemi host'unda bireysel container seviyesinde çalışır.

Her host'u manuel olarak yönetmeniz gerekir ve birden fazla ilişkili container için network'ler, güvenlik politikaları ve storage kurulumu karmaşık olabilir.

Kubernetes: Kubernetes cluster seviyesinde çalışır. Birden fazla host genelinde birden fazla container'lı uygulamayı yönetir, load balancing, scaling ve uygulamaların istenen durumunu sağlama gibi görevler için otomasyon sağlar.

Kısacası, Docker container'laştırmaya ve container'ları bireysel host'larda çalıştırmaya odaklanırken, Kubernetes bir host cluster'ı genelinde container'ları ölçekli olarak yönetme ve orchestration konusunda uzmanlaşmıştır.

### Docker nasıl çalışır?

Aşağıdaki diyagram Docker'ın mimarisini ve "docker build", "docker pull" ve "docker run" çalıştırdığımızda nasıl çalıştığını gösterir.

<p>
  <img src="../images/docker.jpg" style="width: 680px" />
</p>

Docker mimarisinde 3 bileşen vardır:

- Docker client
    
    Docker client Docker daemon ile konuşur.

- Docker host

    Docker daemon Docker API isteklerini dinler ve image'lar, container'lar, network'ler ve volume'lar gibi Docker nesnelerini yönetir.

- Docker registry

    Bir Docker registry Docker image'larını depolar. Docker Hub herkesin kullanabileceği public bir registry'dir.

"docker run" komutunu örnek olarak alalım.

  1. Docker registry'den image'ı çeker.
  1. Docker yeni bir container oluşturur.
  1. Docker container'a bir read-write filesystem tahsis eder.
  1. Docker container'ı varsayılan network'e bağlamak için bir network interface oluşturur.
  1. Docker container'ı başlatır.

## GIT

### Git Komutları nasıl çalışır

Öncelikle, kodumuzun nerede depolandığını belirlemek önemlidir. Yaygın varsayım sadece iki konum olduğudur - biri Github gibi uzak bir sunucuda ve diğeri yerel makinemizde. Ancak bu tamamen doğru değildir. Git makinemizde üç yerel depolama alanı tutar, bu da kodumuzun dört yerde bulunabileceği anlamına gelir:

<p>
  <img src="../images/git-commands.png" style="width: 600px" />
</p>

- Working directory: dosyaları düzenlediğimiz yer
- Staging area: dosyaların bir sonraki commit için geçici olarak tutulduğu yer
- Local repository: commit edilmiş kodun bulunduğu yer
- Remote repository: kodu depolayan uzak sunucu

Çoğu Git komutu öncelikle dosyaları bu dört konum arasında taşır.

### Git Nasıl Çalışır?

Aşağıdaki diyagram Git workflow'unu gösterir.

<p>
  <img src="../images/git-workflow.jpeg" style="width: 520px" />
</p>

Git dağıtık bir versiyon kontrol sistemidir.

Her geliştirici ana repository'nin yerel bir kopyasını tutar ve yerel kopyada düzenleme ve commit yapar.

Commit çok hızlıdır çünkü işlem remote repository ile etkileşime girmez.

Remote repository çökerse, dosyalar yerel repository'lerden kurtarılabilir.

### Git merge vs. Git rebase

Farklar nelerdir?

<p>
  <img src="../images/git-merge-git-rebase.jpeg" style="width: 680px" />
</p>

Bir Git branch'inden diğerine değişiklikleri **merge ettiğimizde**, 'git merge' veya 'git rebase' kullanabiliriz. Aşağıdaki diyagram iki komutun nasıl çalıştığını gösterir.

**Git merge**

Bu, main branch'de yeni bir G' commit'i oluşturur. G' hem main hem de feature branch'lerinin geçmişlerini birbirine bağlar.

Git merge **yıkıcı değildir**. Ne main ne de feature branch değiştirilir.

**Git rebase**

Git rebase feature branch geçmişlerini main branch'in head'ine taşır. Feature branch'deki her commit için yeni E', F' ve G' commit'leri oluşturur.

Rebase'in faydası **doğrusal bir commit geçmişine** sahip olmasıdır.

"git rebase'in altın kuralı"na uyulmazsa rebase tehlikeli olabilir.

**Git Rebase'in Altın Kuralı**

Asla public branch'lerde kullanmayın!

## Cloud Services

### Farklı bulut hizmetleri için güzel bir kısayol kağıdı (2023 versiyonu)

<p>
  <img src="../images/cloud-compare.jpg" />
</p>


### Cloud native nedir?

Aşağıdaki diyagram, 1980'lerden beri mimari ve süreçlerdeki evrimi gösterir.

<p>
  <img src="../images/cloud-native.jpeg" style="width: 640px" />
</p>

Organizasyonlar cloud native teknolojilerini kullanarak public, private ve hybrid cloud'larda ölçeklenebilir uygulamalar geliştirebilir ve çalıştırabilir.

Bu, uygulamaların cloud özelliklerinden yararlanacak şekilde tasarlandığı, böylece yüke karşı dayanıklı ve kolayca ölçeklendirilebilir olduğu anlamına gelir.

Cloud native 4 yönü içerir:

1. Geliştirme süreci

    Bu waterfall'dan agile'a ve DevOps'a ilerlemiştir.

2. Uygulama Mimarisi

    Mimari monolitik'ten microservices'e geçmiştir. Her servis cloud container'larındaki sınırlı kaynaklara uyum sağlayacak şekilde küçük tasarlanmıştır.

3. Deployment ve paketleme

    Uygulamalar önceleri fiziksel sunucularda deploy edilirdi. 2000'li yıllar civarında, gecikmeye duyarlı olmayan uygulamalar genellikle sanal sunucularda deploy edilirdi. Cloud native uygulamalarla birlikte, docker image'larına paketlenip container'larda deploy ediliyorlar.

4. Uygulama altyapısı

    Uygulamalar kendi sunucuları yerine cloud altyapısında yoğun şekilde deploy ediliyor.

## Developer productivity tools

### JSON dosyalarını görselleştirme

İç içe JSON dosyalarını okumak zordur.

**JsonCrack** JSON dosyalarından grafik diyagramları oluşturur ve bunları kolay okunur hale getirir.

Ek olarak, oluşturulan diyagramlar resim olarak indirilebilir.

<p>
  <img src="../images/json-cracker.jpeg" />
</p>


### Kodu otomatik olarak mimari diyagramlara dönüştürme

<p>
  <img src="../images/diagrams_as_code.jpeg" style="width: 640px" />
</p>


Ne yapar?

- Cloud sistem mimarisini Python koduyla çizer.
- Diyagramlar Jupyter Notebook'lar içinde doğrudan render edilebilir.
- Tasarım araçlarına ihtiyaç yoktur.
- Şu sağlayıcıları destekler: AWS, Azure, GCP, Kubernetes, Alibaba Cloud, Oracle Cloud, vb.

[Github repo](https://github.com/mingrammer/diagrams)

## Linux

### Linux dosya sistemi açıklaması

<p>
  <img src="../images/linux-file-systems.jpg" style="width: 680px" />
</p>

Linux dosya sistemi eskiden insanların evlerini istedikleri yere inşa ettikleri düzensiz bir kasabaya benziyordu. Ancak 1994'te Linux dosya sistemine düzen getirmek için Filesystem Hierarchy Standard (FHS) tanıtıldı.

FHS gibi bir standardı uygulayarak, yazılımlar çeşitli Linux dağıtımlarında tutarlı bir düzen sağlayabilir. Bununla birlikte, tüm Linux dağıtımları bu standarda sıkı sıkıya bağlı kalmaz. Genellikle kendi benzersiz öğelerini eklerler veya belirli gereksinimlere göre uyarlarlar.
Bu standardda uzmanlaşmak için keşfederek başlayabilirsiniz. Gezinmek için "cd" ve dizin içeriklerini listelemek için "ls" gibi komutları kullanın. Dosya sistemini kökten (/) başlayan bir ağaç olarak düşünün. Zamanla, bu size doğal gelecek ve sizi yetenekli bir Linux yöneticisine dönüştürecektir.

### Bilmeniz Gereken 18 En Çok Kullanılan Linux Komutu

Linux komutları işletim sistemiyle etkileşim kurmak için kullanılan talimatlardır. Dosyaları, dizinleri, sistem süreçlerini ve sistemin diğer birçok yönünü yönetmeye yardımcı olurlar. Linux tabanlı sistemlerde verimli ve etkili bir şekilde gezinmek ve bakımını yapmak için bu komutlara aşina olmanız gerekir.

Aşağıdaki diyagram popüler Linux komutlarını gösterir:

<p>
  <img src="../images/18 Most-Used Linux Commands You Should Know-01.jpeg" style="width: 680px" />
</p>


- ls - Dosya ve dizinleri listele
- cd - Mevcut dizini değiştir
- mkdir - Yeni dizin oluştur
- rm - Dosya veya dizinleri sil
- cp - Dosya veya dizinleri kopyala
- mv - Dosya veya dizinleri taşı veya yeniden adlandır
- chmod - Dosya veya dizin izinlerini değiştir
- grep - Dosyalarda desen ara
- find - Dosya ve dizinleri ara
- tar - Tarball arşiv dosyalarını işle
- vi - Metin editörü ile dosyaları düzenle
- cat - Dosya içeriğini görüntüle
- top - Süreçleri ve kaynak kullanımını görüntüle
- ps - Süreç bilgilerini görüntüle
- kill - Bir süreci sinyal göndererek sonlandır
- du - Dosya alan kullanımını tahmin et
- ifconfig - Ağ arayüzlerini yapılandır
- ping - Ana bilgisayarlar arasında ağ bağlantısını test et

## Security

### HTTPS nasıl çalışır?

Hypertext Transfer Protocol Secure (HTTPS), Hypertext Transfer Protocol'ün (HTTP) bir uzantısıdır. HTTPS, Transport Layer Security (TLS) kullanarak şifrelenmiş veri iletir. Veriler internette ele geçirilirse, saldırgan sadece binary kod elde eder.

<p>
  <img src="../images/https.jpg" />
</p>


Veriler nasıl şifrelenir ve çözülür?

Adım 1 - Client (tarayıcı) ve server TCP bağlantısı kurar.

Adım 2 - Client server'a "client hello" gönderir. Mesaj bir dizi gerekli şifreleme algoritması (cipher suites) ve destekleyebildiği en son TLS versiyonunu içerir. Server "server hello" ile yanıt verir, böylece tarayıcı algoritmaları ve TLS versiyonunu destekleyip destekleyemeyeceğini bilir.

Ardından server SSL sertifikasını client'a gönderir. Sertifika public key, host name, son kullanma tarihleri vb. içerir. Client sertifikayı doğrular.

Adım 3 - SSL sertifikasını doğruladıktan sonra, client bir oturum anahtarı oluşturur ve bunu public key kullanarak şifreler. Server şifrelenmiş oturum anahtarını alır ve private key ile çözer.

Adım 4 - Artık hem client hem de server aynı oturum anahtarına sahip olduğundan (simetrik şifreleme), şifrelenmiş veriler güvenli çift yönlü bir kanalda iletilir.

HTTPS neden veri iletimi sırasında simetrik şifrelemeye geçer? İki ana neden vardır:

1. Güvenlik: Asimetrik şifreleme sadece tek yönlü çalışır. Bu, server şifrelenmiş verileri client'a geri göndermeye çalışırsa, herkesin public key kullanarak verileri çözebileceği anlamına gelir.

2. Server kaynakları: Asimetrik şifreleme oldukça fazla matematiksel yük ekler. Uzun oturumlarda veri iletimi için uygun değildir.

### OAuth 2.0 Basit Terimlerle Açıklandı

OAuth 2.0, farklı uygulamaların hassas kimlik bilgilerini paylaşmadan kullanıcılar adına güvenli bir şekilde etkileşime girmesine olanak tanıyan güçlü ve güvenli bir framework'tür.

<p>
  <img src="../images/oAuth2.jpg" />
</p>

OAuth'daki varlıklar Kullanıcı, Server ve Identity Provider (IDP)'dır.

Bir OAuth Token Ne Yapabilir?

OAuth kullandığınızda, kimliğinizi ve izinlerinizi temsil eden bir OAuth token alırsınız. Bu token birkaç önemli şey yapabilir:

Single Sign-On (SSO): OAuth token ile tek bir giriş kullanarak birden fazla servise veya uygulamaya giriş yapabilirsiniz, bu da hayatı daha kolay ve güvenli hale getirir.

Sistemler Arası Yetkilendirme: OAuth token, yetkilendirme veya erişim haklarınızı çeşitli sistemler arasında paylaşmanıza olanak tanır, böylece her yerde ayrı ayrı giriş yapmanız gerekmez.

Kullanıcı Profiline Erişim: OAuth token'a sahip uygulamalar, izin verdiğiniz kullanıcı profilinizin belirli bölümlerine erişebilir, ancak her şeyi göremezler.

OAuth 2.0'ın tamamı, sizi ve verilerinizi güvende tutarken çevrimiçi deneyimlerinizi farklı uygulamalar ve servisler arasında sorunsuz ve zahmetsiz hale getirmekle ilgilidir.

### En Çok Kullanılan 4 Kimlik Doğrulama Mekanizması

<p>
  <img src="../images/top4-most-used-auth.jpg" />
</p>

1. SSH Keys:

    Uzak sistemlere ve sunuculara güvenli erişim için kriptografik anahtarlar kullanılır

1. OAuth Tokens:

    Üçüncü taraf uygulamalarda kullanıcı verilerine sınırlı erişim sağlayan token'lar

1. SSL Certificates:

    Sunucular ve client'lar arasında güvenli ve şifrelenmiş iletişimi sağlayan dijital sertifikalar

1. Credentials:

    Çeşitli sistemlere ve servislere erişimi doğrulamak ve vermek için kullanılan kullanıcı kimlik doğrulama bilgileri

### Session, cookie, JWT, token, SSO ve OAuth 2.0 - bunlar nedir?

Bu terimler hepsi kullanıcı kimlik yönetimiyle ilgilidir. Bir web sitesine giriş yaptığınızda, kim olduğunuzu beyan edersiniz (identification). Kimliğiniz doğrulanır (authentication) ve size gerekli izinler verilir (authorization). Geçmişte birçok çözüm önerildi ve liste büyümeye devam ediyor.

<p>
  <img src="../images/session.jpeg" />
</p>

Basitten karmaşığa, kullanıcı kimlik yönetimi hakkındaki anlayışım:

- WWW-Authenticate en temel yöntemdir. Tarayıcı tarafından kullanıcı adı ve şifre istenir. Giriş yaşam döngüsünü kontrol edememe nedeniyle, günümüzde nadiren kullanılır.

- Giriş yaşam döngüsü üzerinde daha iyi kontrol session-cookie'dir. Server session depolamasını sürdürür ve tarayıcı session'ın ID'sini tutar. Cookie genellikle sadece tarayıcılarla çalışır ve mobil uygulama dostu değildir.

- Uyumluluk sorununu çözmek için token kullanılabilir. Client token'ı server'a gönderir ve server token'ı doğrular. Dezavantajı, token'ın şifrelenmesi ve çözülmesi gerektiğinden zaman alıcı olabilir.

- JWT token'ları temsil etmenin standart bir yoludur. Bu bilgiler dijital olarak imzalandığı için doğrulanabilir ve güvenilirdir. JWT imzayı içerdiğinden, server tarafında session bilgisini kaydetmeye gerek yoktur.

- SSO (single sign-on) kullanarak, sadece bir kez giriş yapabilir ve birden fazla web sitesine giriş yapabilirsiniz. Siteler arası bilgileri sürdürmek için CAS (central authentication service) kullanır.

- OAuth 2.0 kullanarak, bir web sitesine diğer bir web sitesindeki bilgilerinize erişim izni verebilirsiniz.

### Şifreler veritabanında nasıl güvenli bir şekilde saklanır ve şifre nasıl doğrulanır?

<p>
  <img src="../images/salt.jpg" style="width: 720px" />
</p>


**YAPILMAMASI gerekenler**

- Şifreleri düz metin olarak saklamak iyi bir fikir değildir çünkü dahili erişimi olan herkes bunları görebilir.

- Şifre hash'lerini doğrudan saklamak yeterli değildir çünkü rainbow table'lar gibi ön hesaplama saldırılarına açıktır.

- Ön hesaplama saldırılarını azaltmak için, şifrelere salt eklenir.

**Salt nedir?**

OWASP yönergelerine göre, "salt, hash işleminin bir parçası olarak her şifreye eklenen benzersiz, rastgele oluşturulmuş bir dizedir".

**Şifre ve salt nasıl saklanır?**

1. hash sonucu her şifre için benzersizdir.
1. Şifre veritabanında şu formatta saklanabilir: hash(password + salt).

**Şifre nasıl doğrulanır?**

Bir şifreyi doğrulamak için şu süreçten geçebilir:

1. Bir client şifreyi girer.
1. Sistem veritabanından ilgili salt'ı alır.
1. Sistem salt'ı şifreye ekler ve hash'ler. Buna H1 diyelim.
1. Sistem H1 ve H2'yi karşılaştırır, H2 veritabanında saklanan hash'tir. Aynıysa, şifre geçerlidir.

### JSON Web Token'ı (JWT) 10 yaşındaki bir çocuğa açıklamak

<p>
  <img src="../images/jwt.jpg" />
</p>

JWT adında özel bir kutunuz olduğunu hayal edin. Bu kutunun içinde üç bölüm vardır: header, payload ve signature.

Header kutunun dışındaki etiket gibidir. Bize ne tür bir kutu olduğunu ve nasıl güvende tutulduğunu söyler. Genellikle JSON adı verilen bir formatta yazılır, bu sadece bilgileri süslü parantezler { } ve iki noktalar : kullanarak düzenlemenin bir yoludur.

Payload göndermek istediğiniz asıl mesaj veya bilgi gibidir. İsminiz, yaşınız veya paylaşmak istediğiniz diğer veriler olabilir. Bu da JSON formatında yazılır, böylece anlaşılması ve çalışması kolaydır.
Şimdi, signature JWT'yi güvenli yapan şeydir. Sadece gönderenin nasıl oluşturacağını bildiği özel bir mühür gibidir. Signature gizli bir kod kullanılarak oluşturulur, şifre gibi. Bu signature, gönderenin haberi olmadan kimsenin JWT içeriğini değiştiremeyeceğini garanti eder.

JWT'yi bir server'a göndermek istediğinizde, header, payload ve signature'ı kutunun içine koyarsınız. Sonra server'a gönderirsiniz. Server header ve payload'ı kolayca okuyarak kim olduğunuzu ve ne yapmak istediğinizi anlayabilir.

### Google Authenticator (veya diğer 2 faktörlü kimlik doğrulayıcılar) nasıl çalışır?

Google Authenticator, 2 faktörlü kimlik doğrulama etkinleştirildiğinde hesaplarımıza giriş yapmak için yaygın olarak kullanılır. Güvenliği nasıl garanti eder?

Google Authenticator, iki adımlı doğrulama hizmeti uygulayan yazılım tabanlı bir kimlik doğrulayıcıdır. Aşağıdaki diyagram detay sağlar.

<p>
  <img src="../images/google_authenticate.jpeg" />
</p>


İki aşama vardır:

- Aşama 1 - Kullanıcı Google iki adımlı doğrulamayı etkinleştirir.
- Aşama 2 - Kullanıcı giriş yapmak vb. için kimlik doğrulayıcıyı kullanır.

Bu aşamalara bakalım.

**Aşama 1**

Adım 1 ve 2: Bob iki adımlı doğrulamayı etkinleştirmek için web sayfasını açar. Frontend bir gizli anahtar ister. Authentication service Bob için gizli anahtarı oluşturur ve veritabanında saklar.

Adım 3: Authentication service frontend'e bir URI döndürür. URI bir key issuer, kullanıcı adı ve gizli anahtardan oluşur. URI web sayfasında QR kodu şeklinde görüntülenir.

Adım 4: Bob daha sonra Google Authenticator'ı kullanarak oluşturulan QR kodunu tarar. Gizli anahtar authenticator'da saklanır.

**Aşama 2**
Adım 1 ve 2: Bob Google iki adımlı doğrulama ile bir web sitesine giriş yapmak istiyor. Bunun için şifreye ihtiyacı var. Google Authenticator her 30 saniyede bir TOTP (Time-based One Time Password) algoritması kullanarak 6 haneli bir şifre oluşturur. Bob web sitesine girmek için şifreyi kullanır.

Adım 3 ve 4: Frontend Bob'un girdiği şifreyi doğrulama için backend'e gönderir. Authentication service veritabanından gizli anahtarı okur ve client ile aynı TOTP algoritmasını kullanarak 6 haneli bir şifre oluşturur.

Adım 5: Authentication service client ve server tarafından oluşturulan iki şifreyi karşılaştırır ve karşılaştırma sonucunu frontend'e döndürür. Bob ancak iki şifre eşleşirse giriş işlemine devam edebilir.

Bu kimlik doğrulama mekanizması güvenli mi?

- Gizli anahtar başkaları tarafından elde edilebilir mi?

    Gizli anahtarın HTTPS kullanılarak iletildiğinden emin olmamız gerekir. Authenticator client ve veritabanı gizli anahtarı saklar ve gizli anahtarların şifrelendiğinden emin olmamız gerekir.

- 6 haneli şifre hackerlar tarafından tahmin edilebilir mi?

    Hayır. Şifre 6 haneli olduğundan, oluşturulan şifrenin 1 milyon potansiyel kombinasyonu vardır. Ayrıca şifre her 30 saniyede bir değişir. Hackerların 30 saniyede şifreyi tahmin etmesi için saniyede 30.000 kombinasyon girmesi gerekir.


## Real World Case Studies

### Netflix'in Tech Stack'i

Bu yazı birçok Netflix mühendislik blogu ve open-source projelerinden yapılan araştırmaya dayanmaktadır. Herhangi bir yanlışlık görürseniz, lütfen bizi bilgilendirin.

<p>
  <img src="../images/netflix tech stack.png" style="width: 680px" />
</p>

**Mobile ve web**: Netflix native mobil uygulamalar geliştirmek için Swift ve Kotlin'i benimsedi. Web uygulaması için React kullanıyor.

**Frontend/server iletişimi**: Netflix GraphQL kullanıyor.

**Backend services**: Netflix ZUUL, Eureka, Spring Boot framework ve diğer teknolojilere güveniyor.

**Databases**: Netflix EV cache, Cassandra, CockroachDB ve diğer veritabanlarını kullanıyor.

**Messaging/streaming**: Netflix messaging ve streaming için Apache Kafka ve Fink kullanıyor.

**Video storage**: Netflix video depolama için S3 ve Open Connect kullanıyor.

**Data processing**: Netflix veri işleme için Flink ve Spark kullanıyor, bu da Tableau kullanılarak görselleştiriliyor. Yapılandırılmış veri ambarı bilgilerini işlemek için Redshift kullanılıyor.

**CI/CD**: Netflix CI/CD süreçleri için JIRA, Confluence, PagerDuty, Jenkins, Gradle, Chaos Monkey, Spinnaker, Atlas ve daha fazlası gibi çeşitli araçlar kullanıyor.

### Twitter Mimarisi 2022

Evet, bu gerçek Twitter mimarisidir. Elon Musk tarafından paylaşıldı ve daha iyi okunabilirlik için bizim tarafımızdan yeniden çizildi.

<p>
  <img src="../images/twitter-arch.jpeg" />
</p>


### Airbnb'nin microservice mimarisinin son 15 yıldaki evrimi

Airbnb'nin microservice mimarisi 3 ana aşamadan geçti.

<p>
  <img src="../images/airbnb_arch.jpeg" />
</p>


Monolith (2008 - 2017)

Airbnb ev sahipleri ve misafirler için basit bir marketplace olarak başladı. Bu bir Ruby on Rails uygulamasında - monolith'te inşa edildi.

Zorluk neydi?

- Karışık takım sahipliği + sahipsiz kod
- Yavaş deployment

Microservices (2017 - 2020)

Microservice bu zorlukları çözmeyi amaçlar. Microservice mimarisinde, temel servisler şunları içerir:

- Veri çekme servisi
- İş mantığı veri servisi
- Yazma iş akışı servisi
- UI aggregation servisi
- Her servisin bir sahip takımı vardı

Zorluk neydi?

Yüzlerce servis ve bağımlılığı insanların yönetmesi zordu.

Micro + macroservices (2020 - günümüz)

Bu Airbnb'nin şu anda üzerinde çalıştığı şey. Micro ve macroservice hibrit modeli API'ların birleştirilmesine odaklanıyor.

### Monorepo vs. Microrepo

Hangisi en iyisi? Neden farklı şirketler farklı seçenekleri seçiyor?

<p>
  <img src="../images/monorepo-microrepo.jpg" />
</p>


Monorepo yeni değil; Linux ve Windows ikisi de Monorepo kullanılarak oluşturuldu. Ölçeklenebilirliği ve build hızını iyileştirmek için, Google daha hızlı ölçeklendirmek için kendi dahili özel toolchain'ini ve tutarlı tutmak için katı kodlama kalite standartlarını geliştirdi.

Amazon ve Netflix Microservice felsefesinin büyük elçileridir. Bu yaklaşım doğal olarak servis kodunu ayrı repository'lere ayırır. Daha hızlı ölçeklenir ancak daha sonra yönetişim sorunlarına yol açabilir.

Monorepo'da, her servis bir klasördür ve her klasörün BUILD config'i ve OWNERS izin kontrolü vardır. Her servis üyesi kendi klasöründen sorumludur.

Öte yandan, Microrepo'da her servis kendi repository'sinden sorumludur, build config'i ve izinler genellikle tüm repository için ayarlanır.

Monorepo'da, bağımlılıklar işletmenizden bağımsız olarak tüm codebase'de paylaşılır, bu nedenle bir versiyon yükseltmesi olduğunda, her codebase versiyonlarını yükseltir.

Microrepo'da, bağımlılıklar her repository içinde kontrol edilir. İşletmeler kendi programlarına göre versiyonlarını ne zaman yükselteceklerini seçer.

Monorepo check-in'ler için bir standarda sahiptir. Google'ın kod inceleme süreci, işletmeden bağımsız olarak Monorepo için tutarlı bir kalite standardı sağlamakla ünlüdür.

Microrepo ya kendi standardını belirleyebilir ya da en iyi uygulamaları dahil ederek paylaşılan bir standardı benimseyebilir. İşletme için daha hızlı ölçeklenebilir, ancak kod kalitesi biraz farklı olabilir.
Google mühendisleri Bazel'i ve Meta Buck'ı inşa etti. Nx, Lerna ve diğerleri dahil olmak üzere başka open-source araçlar da mevcuttur.

Yıllar boyunca, Microrepo Java için Maven ve Gradle, NodeJS için NPM ve C/C++ için CMake dahil olmak üzere daha fazla desteklenen araca sahip oldu.

### Stack Overflow web sitesini nasıl tasarlarsınız?

Cevabınız on-premise sunucular ve monolith ise (aşağıdaki resmin altında), muhtemelen görüşmede başarısız olursunuz, ama gerçekte böyle inşa edilmiş!

<p>
  <img src="../images/stackoverflow.jpg" />
</p>


**İnsanların nasıl olması gerektiğini düşündüğü**

Görüşmeci muhtemelen resmin üst kısmındaki gibi bir şey bekliyor.

- Sistemi küçük bileşenlere ayırmak için microservice kullanılır.
- Her servisin kendi veritabanı vardır. Cache'i yoğun kullanır.
- Servis sharded'dır.
- Servisler birbirleriyle message queue'lar aracılığıyla asenkron olarak konuşur.
- Servis Event Sourcing ile CQRS kullanılarak uygulanır.
- Eventual consistency, CAP theorem gibi dağıtık sistemlerdeki bilgileri göstermek.

**Aslında nasıl**

Stack Overflow tüm trafiği sadece 9 on-premise web sunucusuyla karşılıyor ve monolith'te! Kendi sunucularına sahip ve cloud'da çalışmıyor.

Bu günlerde tüm popüler inançlarımızın aksine.

### Amazon Prime Video izleme neden serverless'tan monolithic'e geçti? %90 maliyeti nasıl düşürebilir?

Aşağıdaki diyagram migrasyon öncesi ve sonrası mimari karşılaştırmasını gösterir.

<p>
  <img src="../images/serverless-to-monolithic.jpeg" />
</p>


Amazon Prime Video İzleme Servisi nedir?

Prime Video servisi binlerce canlı yayının kalitesini izlemesi gerekiyor. İzleme aracı akışları gerçek zamanlı olarak otomatik analiz eder ve blok bozulması, video donması ve senkronizasyon sorunları gibi kalite sorunlarını belirler. Bu müşteri memnuniyeti için önemli bir süreçtir.

3 adım vardır: media converter, defect detector ve real-time notification.

- Eski mimarideki sorun neydi?

  Eski mimari servisleri hızlı bir şekilde oluşturmak için iyi olan Amazon Lambda'ya dayanıyordu. Ancak, mimarinin yüksek ölçekte çalıştırılması maliyet açısından verimli değildi. En pahalı iki işlem:

1. Orchestration workflow - AWS step functions kullanıcıları durum geçişleri başına ücretlendirir ve orchestration her saniye birden fazla durum geçişi gerçekleştirir.

2. Dağıtık bileşenler arasında veri aktarımı - ara veriler bir sonraki aşamanın indirebilmesi için Amazon S3'te saklanır. Hacim yüksek olduğunda indirme maliyetli olabilir.

- Monolithic mimari %90 maliyet tasarrufu sağlar

  Monolithic mimari maliyet sorunlarını çözmek için tasarlanmıştır. Hala 3 bileşen vardır, ancak media converter ve defect detector aynı süreçte deploy edilir, bu da network üzerinden veri aktarma maliyetinden tasarruf sağlar. Şaşırtıcı bir şekilde, bu deployment mimari değişikliği %90 maliyet tasarrufu sağladı!

Bu ilginç ve benzersiz bir vaka çalışmasıdır çünkü microservices teknoloji sektöründe tercih edilen ve moda bir seçenek haline gelmiştir. Mimarinin gelişimi ve artıları/eksileri hakkında daha dürüst tartışmalar yapmamız iyi. Bileşenleri dağıtık microservices'lara ayırmak bir maliyetle gelir.

- Amazon liderleri bu konuda ne dedi?

  Amazon CTO'su Werner Vogels: "**Evrimleşebilir yazılım sistemleri** geliştirmek bir stratejidir, din değil. Ve mimarinizi açık fikirle yeniden gözden geçirmek bir zorunluluktur."

Eski Amazon VP Sustainability Adrian Cockcroft: "Prime Video ekibi **Serverless First** dediğim bir yol izledi... Ben **Serverless Only** savunmuyorum".

### Disney Hotstar bir turnuva sırasında 5 Milyar Emoji'yi nasıl yakalıyor?

<p>
  <img src="../images/hotstar_emojis.jpeg" style="width: 720px" />
</p>

1. Client'lar emojileri standart HTTP istekleri üzerinden gönderir. Golang Service'i tipik bir Web Server olarak düşünebilirsiniz. Golang concurrent işlemleri iyi desteklediği için seçilmiştir. Golang'deki thread'ler hafiftir.

2. Write hacmi çok yüksek olduğundan, buffer olarak Kafka (message queue) kullanılır.

3. Emoji verileri Spark adlı bir streaming processing servisi tarafından toplanır. Her 2 saniyede bir veri toplar, bu süre ayarlanabilir. Aralığa göre bir trade-off yapılması gerekir. Daha kısa aralık, emojilerin diğer client'lara daha hızlı ulaştığı ancak daha fazla computing kaynağına ihtiyaç duyulduğu anlamına gelir.

4. Toplanan veriler başka bir Kafka'ya yazılır.

5. PubSub consumer'ları toplanan emoji verilerini Kafka'dan çeker.

6. Emojiler diğer client'lara PubSub altyapısı üzerinden real-time olarak iletilir. PubSub altyapısı ilginçtir. Hotstar şu protokolleri değerlendirdi: Socketio, NATS, MQTT ve gRPC, ve MQTT'de karar kıldı.

LinkedIn de saniyede bir milyon like'ı stream etmek için benzer bir tasarım kullanıyor.

### Discord Trilyonlarca Mesajı Nasıl Depoluyor

Aşağıdaki diyagram Discord'da mesaj depolamanın evrimini gösterir:

<p>
  <img src="../images/discord-store-messages.jpg" />
</p>

MongoDB ➡️ Cassandra ➡️ ScyllaDB

2015'te, Discord'un ilk versiyonu tek bir MongoDB replica üzerine kuruldu. 2015 Kasım civarında, MongoDB 100 milyon mesaj depoluyordu ve RAM artık veriyi ve index'i tutamıyordu. Latency öngörülemez hale geldi. Mesaj depolama başka bir veritabanına taşınmalıydı. Cassandra seçildi.

2017'de, Discord'un 12 Cassandra node'u vardı ve milyarlarca mesaj depoluyordu.

2022 başında, trilyonlarca mesajla 177 node'a sahipti. Bu noktada, latency öngörülemezdi ve maintenance operasyonları çalıştırmak çok maliyetli hale gelmişti.

Sorunun birkaç nedeni var:

- Cassandra internal data structure için LSM tree kullanır. Read'ler write'lardan daha maliyetlidir. Yüzlerce kullanıcılı bir sunucuda birçok eşzamanlı read olabilir, bu da hotspot'lara neden olur.
- SSTables'ı compact etmek gibi cluster maintenance işlemleri performansı etkiler.
- Garbage collection duraklamaları önemli latency spike'larına neden olurdu

ScyllaDB, C++'da yazılmış Cassandra uyumlu bir veritabanıdır. Discord mimarisini monolithic API, Rust'ta yazılmış bir data service ve ScyllaDB tabanlı storage olacak şekilde yeniden tasarladı.

ScyllaDB'de p99 read latency 15ms iken Cassandra'da 40-125ms'dir. p99 write latency ScyllaDB'de 5ms iken Cassandra'da 5-70ms'dir.

### YouTube, TikTok live veya Twitch'te video live streaming nasıl çalışır?

Live streaming, video içeriğinin internet üzerinden real-time olarak, genellikle sadece birkaç saniyelik latency ile gönderildiği için regular streaming'den farklıdır.

Aşağıdaki diyagram bunu mümkün kılan perde arkasındaki işlemleri açıklar.

<p>
  <img src="../images/live_streaming_updated.jpg" style="width: 640px" />
</p>

Adım 1: Raw video verisi mikrofon ve kamera tarafından yakalanır. Veri server tarafına gönderilir.

Adım 2: Video verisi sıkıştırılır ve encode edilir. Örneğin, sıkıştırma algoritması arka planı ve diğer video öğelerini ayırır. Sıkıştırmadan sonra, video H.264 gibi standartlara encode edilir. Video verisinin boyutu bu adımdan sonra çok daha küçüktür.

Adım 3: Encode edilmiş veri, indirmesi veya stream etmesi çok daha az zaman alacak şekilde, genellikle saniyeler uzunluğunda daha küçük segmentlere bölünür.

Adım 4: Segmentlere ayrılmış veri streaming server'a gönderilir. Streaming server farklı cihazları ve network koşullarını desteklemelidir. Buna 'Adaptive Bitrate Streaming' denir. Bu, adım 2 ve 3'te farklı bit hızlarında birden fazla dosya üretmemiz gerektiği anlamına gelir.

Adım 5: Live streaming verisi CDN (Content Delivery Network) tarafından desteklenen edge server'lara push edilir. Milyonlarca izleyici videoyu yakındaki bir edge server'dan izleyebilir. CDN veri iletim latency'sini önemli ölçüde düşürür.

Adım 6: İzleyicilerin cihazları video verisini decode eder, sıkıştırmayı açar ve videoyu bir video player'da oynatır.

Adım 7 ve 8: Eğer videonun tekrar izlenmek üzere saklanması gerekiyorsa, encode edilmiş veri bir storage server'a gönderilir ve izleyiciler daha sonra buradan tekrar izleme talebinde bulunabilir.

Live streaming için standart protokoller şunları içerir:

- RTMP (Real-Time Messaging Protocol): Başlangıçta Macromedia tarafından Flash player ve server arasında veri iletimi için geliştirildi. Şimdi internet üzerinden video verisi stream etmek için kullanılıyor. Skype gibi video konferans uygulamalarının daha düşük latency için RTC (Real-Time Communication) protokolü kullandığını unutmayın.
- HLS (HTTP Live Streaming): H.264 veya H.265 encoding gerektirir. Apple cihazları sadece HLS formatını kabul eder.
- DASH (Dynamic Adaptive Streaming over HTTP): DASH Apple cihazlarını desteklemez.
- Hem HLS hem de DASH adaptive bitrate streaming'i destekler.

## License

<p xmlns:cc="http://creativecommons.org/ns#" >This work is licensed under <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></a></p>
