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

Explicando sistemas complexos com visuais e termos simples.

Seja que você esteja se preparando para uma Entrevista de Design de Sistemas ou simplesmente deseja entender como sistemas funcionam por baixo do capô, esperamos que este repositório possa te ajudar.

# Tabela de Conteúdos

<!-- TOC toc.levels=2 -->

- [System Design 101](#system-design-101)
- [Tabela de Conteúdos](#tabela-de-conteúdos)
  - [Protocólos de Comunicação](#protocólos-de-comunicação)
    - [REST API vs. GraphQL](#rest-api-vs-graphql)
    - [Como o gRPC funciona?](#como-o-grpc-funciona)
    - [O que é um webhook?](#o-que-é-um-webhook)
    - [Como melhorar a performance de uma API?](#como-melhorar-a-performance-de-uma-api)
    - [HTTP 1.0 -\> HTTP 1.1 -\> HTTP 2.0 -\> HTTP 3.0 (QUIC)](#http-10---http-11---http-20---http-30-quic)
    - [SOAP vs REST vs GraphQL vs RPC](#soap-vs-rest-vs-graphql-vs-rpc)
    - [Code First vs. API First](#code-first-vs-api-first)
    - [Códigos de status HTTP](#códigos-de-status-http)
    - [O que faz um API gatway?](#o-que-faz-um-api-gatway)
    - [Como projetar APIs seguras e efetivas?](#como-projetar-apis-seguras-e-efetivas)
    - [Encapsulação TCP/IP](#encapsulação-tcpip)
    - [Por que o Nginx é chamado de uma proxy "reversa"?](#por-que-o-nginx-é-chamado-de-uma-proxy-reversa)
    - [Quais são os algoritmos de distribuição de carga comuns?](#quais-são-os-algoritmos-de-distribuição-de-carga-comuns)
    - [URL, URI, URN - Você sabe a diferênça?](#url-uri-urn---você-sabe-a-diferênça)
  - [CI/CD](#cicd)
    - [Pipeline CI/CD Explicado em Termos Simples](#pipeline-cicd-explicado-em-termos-simples)
    - [Netflix Stack Tecnológico (Pipeline de CI/CD)](#netflix-stack-tecnológico-pipeline-de-cicd)
  - [Padões de Arquitetura](#padões-de-arquitetura)
    - [MVC, MVP, MVVM, MVVM-C, e VIPER](#mvc-mvp-mvvm-mvvm-c-e-viper)
    - [18 Padrões de Design Essenciais Que Todo Desenvolvedor Deve Conhecer](#18-padrões-de-design-essenciais-que-todo-desenvolvedor-deve-conhecer)
  - [Bancos de Dados](#bancos-de-dados)
    - [Um guia prático de diferentes bancos de dados em serviços de nuvem](#um-guia-prático-de-diferentes-bancos-de-dados-em-serviços-de-nuvem)
    - [8 Estruturas de Dados que Impulsionam seus Bancos de Dados](#8-estruturas-de-dados-que-impulsionam-seus-bancos-de-dados)
    - [Como um comando SQL é executado no Banco de Dados?](#como-um-comando-sql-é-executado-no-banco-de-dados)
    - [Teorema CAP](#teorema-cap)
    - [Tipos de Memória e Armazenamento](#tipos-de-memória-e-armazenamento)
    - [Visualizando uma consulta SQL](#visualizando-uma-consulta-sql)
    - [Linguagem SQL](#linguagem-sql)
  - [Cache](#cache)
    - [Data is cached everywhere](#data-is-cached-everywhere)
    - [Why is Redis so fast?](#why-is-redis-so-fast)
    - [How can Redis be used?](#how-can-redis-be-used)
    - [Top caching strategies](#top-caching-strategies)
  - [Microservice architecture](#microservice-architecture)
    - [What does a typical microservice architecture look like?](#what-does-a-typical-microservice-architecture-look-like)
    - [Microservice Best Practices](#microservice-best-practices)
    - [What tech stack is commonly used for microservices?](#what-tech-stack-is-commonly-used-for-microservices)
    - [Why is Kafka fast](#why-is-kafka-fast)
  - [Payment systems](#payment-systems)
    - [How to learn payment systems?](#how-to-learn-payment-systems)
    - [Why is the credit card called “the most profitable product in banks”? How does VISA/Mastercard make money?](#why-is-the-credit-card-called-the-most-profitable-product-in-banks-how-does-visamastercard-make-money)
    - [How does VISA work when we swipe a credit card at a merchant’s shop?](#how-does-visa-work-when-we-swipe-a-credit-card-at-a-merchants-shop)
    - [Payment Systems Around The World Series (Part 1): Unified Payments Interface (UPI) in India](#payment-systems-around-the-world-series-part-1-unified-payments-interface-upi-in-india)
  - [DevOps](#devops)
    - [DevOps vs. SRE vs. Platform Engineering. What is the difference?](#devops-vs-sre-vs-platform-engineering-what-is-the-difference)
    - [What is k8s (Kubernetes)?](#what-is-k8s-kubernetes)
    - [Docker vs. Kubernetes. Which one should we use?](#docker-vs-kubernetes-which-one-should-we-use)
    - [How does Docker work?](#how-does-docker-work)
  - [GIT](#git)
    - [How Git Commands work](#how-git-commands-work)
    - [How does Git Work?](#how-does-git-work)
    - [Git merge vs. Git rebase](#git-merge-vs-git-rebase)
  - [Cloud Services](#cloud-services)
    - [A nice cheat sheet of different cloud services (2023 edition)](#a-nice-cheat-sheet-of-different-cloud-services-2023-edition)
    - [What is cloud native?](#what-is-cloud-native)
  - [Developer productivity tools](#developer-productivity-tools)
    - [Visualize JSON files](#visualize-json-files)
    - [Automatically turn code into architecture diagrams](#automatically-turn-code-into-architecture-diagrams)
  - [Linux](#linux)
    - [Linux file system explained](#linux-file-system-explained)
    - [18 Most-used Linux Commands You Should Know](#18-most-used-linux-commands-you-should-know)
  - [Security](#security)
    - [How does HTTPS work?](#how-does-https-work)
    - [Oauth 2.0 Explained With Simple Terms.](#oauth-20-explained-with-simple-terms)
    - [Top 4 Forms of Authentication Mechanisms](#top-4-forms-of-authentication-mechanisms)
    - [Session, cookie, JWT, token, SSO, and OAuth 2.0 - what are they?](#session-cookie-jwt-token-sso-and-oauth-20---what-are-they)
    - [How to store passwords safely in the database and how to validate a password?](#how-to-store-passwords-safely-in-the-database-and-how-to-validate-a-password)
    - [Explaining JSON Web Token (JWT) to a 10 year old Kid](#explaining-json-web-token-jwt-to-a-10-year-old-kid)
    - [How does Google Authenticator (or other types of 2-factor authenticators) work?](#how-does-google-authenticator-or-other-types-of-2-factor-authenticators-work)
  - [Real World Case Studies](#real-world-case-studies)
    - [Netflix's Tech Stack](#netflixs-tech-stack)
    - [Twitter Architecture 2022](#twitter-architecture-2022)
    - [Evolution of Airbnb’s microservice architecture over the past 15 years](#evolution-of-airbnbs-microservice-architecture-over-the-past-15-years)
    - [Monorepo vs. Microrepo.](#monorepo-vs-microrepo)
    - [How will you design the Stack Overflow website?](#how-will-you-design-the-stack-overflow-website)
    - [Why did Amazon Prime Video monitoring move from serverless to monolithic? How can it save 90% cost?](#why-did-amazon-prime-video-monitoring-move-from-serverless-to-monolithic-how-can-it-save-90-cost)
    - [How does Disney Hotstar capture 5 Billion Emojis during a tournament?](#how-does-disney-hotstar-capture-5-billion-emojis-during-a-tournament)
    - [How Discord Stores Trillions Of Messages](#how-discord-stores-trillions-of-messages)
    - [How do video live streamings work on YouTube, TikTok live, or Twitch?](#how-do-video-live-streamings-work-on-youtube-tiktok-live-or-twitch)
  - [License](#license)

<!-- /TOC -->

## Protocólos de Comunicação

Estilos de arquiteturas definem como os diferentes componentes de uma interface de programação de aplicações (API, _Application Programming Interface_) interagem entre si. Como resultado, eles garantem eficiência, confiabilidade e facilidade de integração com outros sistemas, proporcionando uma abordagem padrão para projetar e construir APIs. Aqui estão os estilos mais utilizados:

<p>
  <img src="../images/api-architecture-styles.png" style="width: 640px">
</p>

- SOAP:

  Amadurecido, abrangente, baseado em XML

  Ideal para aplicações empresariais

- RESTful:

  Popular, fácil implementação, métodos HTTP

  Ideal para serviços web

- GraphQL:

  Linguagem de Consulta, requisita dados específicos

  Reduz sobrecarga de rede, respostas mais rápidas

- gRPC:

  Moderno, alta performance, Protocol Buffers

  Adequado para arquiteturas de microsserviços

- WebSocket:

  Tempo-real, bidirecional, conexões persistentes

  Perfeito para troca de dados de baixa latência

- Webhook:

  Orientado a eventos, chamadas de retorno HTTP, assíncrono

  Notifica o sistema sobre a ocorrência de um evento

### REST API vs. GraphQL

Quando se trata de design de APIs, REST e GraphQL tem suas forças e fraquezas.

O diagrama abaixo mostra uma rápida comparação entre REST e GraphQL.

<p>
  <img src="../images/graphQL.jpg">
</p>

REST

- Utiliza métodos HTTP padrões como GET, POST, PUT, DELETE para operações CRUD.
- Funciona bem quando você precisa de uma interface simples e uniforme entre serviços/aplicações separadas.
- Estratégias de cache são de simples implementação.
- O lado negativo é que pode levar diversas viagens de ida-e-volta para montar os dados relacionados de endpoints separados.

GraphQL

- Fornece um único ponto para clientes realizarem consultas em qualquer dado que precisem.
- Os clientes especificam os campos exatos necessários em consultas aninhadas, e o servidor retorna cargas otimizadas contendo apenas esses campos.
- Suporta Mutations para modificar dados e Subscriptions para notificações em tempo real.
- Ótima para agregar dados de diversas fontes e se adapta bem com requeritos requisitos de frontend que evoluem rapidamente.
- No entanto, isso transfere a complexidade para o lado do cliente e pode permitir consultas abusivas se não forem devidamente protegidas.
- Estratégias de Caching podem ser mais complexas que REST.

A melhor escolha entre REST e GraphQL depende nos requisitos específicos da aplicação e time de desenvolvimento. GraphQL é uma boa opção para necessidades frontend complexas ou que mudam frequentemente, enquanto REST é adequado para aplicações onde contratos simples e consistentes são preferidos.

Nenhuma abordagem dessas APIs é uma solução milagrosa. Avaliar cuidadosamente os requisitos e as compensações é importante para escolher o estilo certo. Tanto REST quanto GraphQL são opções válidas para expor dados e impulsionar aplicações modernas.

### Como o gRPC funciona?

RCP (Chamada de Procedimento Remota, _Remote Procedure Call_) é chamada de "**remota**" pois habilita comunicação entre serviços quando estes são implantados em servidores sob a arquitetura de microsserviços. Do ponto de vista do usuário, ele age como uma chamada de função local.

O diagrama abaixo ilustra o fluxo geral de dados para o **gRPC**.

<p>
  <img src="../images/grpc.jpg">
</p>

Passo 1: Uma chamada REST parte do cliente. O corpo da requisição é geralmetne em formato JSON.

Passo 2 - 4: O Serviço de Pedidos (_Order Service_, que é o cliente gRPC) recebe a chamada REST, a transforma e realiza uma chamada RPC para o Serviço de Pagamentos (_Payment Service_). O gRPC codifica o stub do cliente em um formato binário e o envia para a camada de transporte de baixo nível.

Passp 5: O gRPC envia os pacotes pela rede via HTTP2. Por conta da codificação binária e otimizações de rede, o gRPC é dito ser 5x mais rápido que JSON.

Passo 6 - 8: O Serviço de Pagamentos (_Payment Service_, servidor gRPC) recebe os pacotes da rede, os decodifica e invoca a aplicação do servidor.

Passos 9 - 11: O resultado é retornado pela aplicação do servidor, codificado e enviado para a camada de transporte.

Passos 12 - 14: O Serviço de Pedidos (_Order Service_, cliente gRPC) recebe os pacotes, os decodifica e envia o resultado para a aplicação cliente.

### O que é um webhook?

O diagrama abaixo mostra uma comparação entre Polling e Webhook.

<p>
  <img src="../images/webhook.jpeg" style="width: 680px" />
</p>

Assuma que estamos rodando um website de eCommerce. Os clientes enviam ordens para o Serviço de Ordems pelo API gateway, que aciona o Serviço de Pagamento para transações de pagament. O Serviço de Pagamento fala com um provedor de serviços de pagamento (PSP) para completar as transações.

Há duas forms de lidar comcomunicações com um PSP.

**1. Polling Curto (Short Polling)**

Depois de enviar um pedido de pagamento para o PSP, o serviço de pagamento fica perguntando ao PSP sobre o status do pagamento. Depois de alguns rounds, o PSP finalmente retorna o status.

Polling curto possui duas desvantagens:

- Relizar polling constante a respeito do status consome recursos do Serviço de Pagamento.
- O Serviço Externo se comuica diretamente com o Serviço de Pagamento, criando vulnerabilidades.

**2. Webhook**

Nós podemos registrar um webhook com o Serviço Externo. Isso é: Me avise neste URL quando você tiver alguma atualização da requisição. Quando o PSP completaqr o processamento, ele irá invocar uma requisição HTTP para atualizar o status do pagamento.

Desta forma, o paradigma da programação mudou, quando o Serviço de Pagamento não precisa mais desperdiçar recursos fazendo polling no status de pagamento.

Mas e se o PSP não nos retorna? Podemos fazer uma tarefa/serviço de limpeza para checar o status de pagamento a cada hora.

Webhooks são geralmente referidos como APIs reversos ou push APIs, já que o servidor envia requisições HTTP para o cliente. Nós precisamos prestar atenção a 3 pontos quando utilizamos webhooks:

1. Precisamos projetar uma API adequada para ser chamada pelo serviço externo.
2. Precisamos configurar regras adequadas para o API gateway por razões de segurança.
3. Precisamos registrar a URL correta no Serviço Externo.

### Como melhorar a performance de uma API?

O diagrama abaixo mostra 5 truques comuns para melhorar a performance de uma API.

<p>
  <img src="../images/api-performance.jpg">
</p>

Paginação

Esta é uma otimização comun quando o tamanho do resultado é muito grande. Os resultados são transmitidos de volta para o cliete para melhorar a reponsividade do serviço.

Logging Assíncrono

O log síncrono lida com o disco a cada chamada e pode diminuir a velocidade do sistema. O log assíncrono envia os logs primeiro para um buffer sem bloqueio e retorna imediatamente. Os logs serão periodicamente gravados no disco. Isso reduz significativamente a sobrecarga de E/S (Entrada/Saída).

Caching

Nós podemos armazenar dados frequentemente acessados num cache. O cliente pode realizar uma consulta no cache primeiramente, ao invés de ir direto ao banco de dados. Se ocorrer um cache miss, o cliente deve realizar a consulta ao banco. Caches como Redis armazenam dados em memória, deixando o acesso aos dados muito mais rápido que em um banco de dados.

Compressão da Carga Útil

As slicitações e respostas podem ser comprimidas utilizando gzip etc para que os dados transmitidos tenham um tamanho menor. Isso acelera o upload e download.

Pool de Conexões

Ao acessar recursos, nós precisamos carregar dados do banco de dados. Abrir e fechar conexões com o baco adiciona uma sobrecarga significativa. Portanto podemos nos conectar por um pool de conexões abertas. O pool de conexões é responsável por gerenciar o ciclo de vida da conexão.

### HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)

Quais problemas são resolvidos por cada geração de HTTP?

O diagrama abaixo ilustra as principais características.

<p>
  <img src="../images/http3.jpg" />
</p>

- HTTP 1.0 foi finalizado e totalmente documentado em 1996. Cada solicitação ao mesmo servidor requer uma conexão TCP separada.

- HTTP 1.1 foi publicado em 1997. Uma conexão TCP pode ser deixada aberta para reutilização (conexão persistente), mas não resolve o problema do bloqueio HOL (head-of-line).

  Bloqueio HOL - quando o número de solicitações paralelas permitidas no navegador é esgotado, solicitações subsequentes precisam aguardar as anteriores serem concluídas.

- HTTP 2.0 foi publicado em 2015. Ele aborda o problema HOL por meio do multiplexamento de solicitações, o que elimina o bloqueio HOL na camada de aplicação, mas HOL ainda existe na camada de transporte (TCP).

  Como você pode ver no diagrama, o HTTP 2.0 introduziu o conceito de "streams" HTTP: uma abstração que permite multiplexar diferentes trocas de HTTP na mesma conexão TCP. Cada stream não precisa ser enviado em ordem.

- HTTP 3.0 teve seu rascunho publicado em 2020. Ele é o sucessor proposto do HTTP 2.0. Utiliza o QUIC em vez do TCP como protocolo de transporte subjacente, removendo assim o bloqueio HOL na camada de transporte.

  O QUIC é baseado no UDP. Ele introduz streams como cidadãos de primeira classe na camada de transporte. Os streams QUIC compartilham a mesma conexão QUIC, portanto, não são necessários handshake adicionais e inícios lentos para criar novas conexões, mas os streams QUIC são entregues independentemente, de modo que, na maioria dos casos, a perda de pacotes que afeta uma stream não afeta as outras.

### SOAP vs REST vs GraphQL vs RPC

O diagrama abaixo ilustra a linha do tempo da API e a comparação de estilos de API.

Ao longo do tempo, diferentes estilos arquiteturais de API são lançados. Cada um deles tem suas próprias técnicas para padronizar a troca de dados.

Você pode conferir os casos de uso de cada estilo no diagrama.

<p>
  <img src="../images/SOAP vs REST vs GraphQL vs RPC.jpeg" />
</p>

### Code First vs. API First

O diagrama abaixo mostra as diferenças entre o desenvolvimento Code First e o desenvolvimento API First. Por que queremos considerar o design API First?

<p>
  <img src="../images/api_first.jpg" style="width: 680px" />
</p>

- Microsserviços aumentar a complexidade do sistema e precisamos separar serviços para servir funções diferentes no sistema. Embora esse tipo de arquitetura facilite o desacoplamento e a segregação de responsabilidades, é necessário lidar com as diversas comunicações entre os serviços.

É melhor analisar a complexidade do sistema antes de escrever o código e definir cuidadosamente os limites dos serviços.

- Equipes funcionais separadas precisam falar a mesma linguagem, e as equipes funcionais dedicadas são responsáveis apenas por seus próprios componentes e serviços. Recomenda-se que a organização fale a mesma linguagem por meio do design de API.

Podemos simular solicitações e respostas para validar o design da API antes de escrever o código.

- Melhora a qualidade do software e a produtividade do desenvolvedor. Como resolvemos a maioria das incertezas no início do projeto, o processo de desenvolvimento é mais suave, e a qualidade do software é significativamente aprimorada.

Os desenvolvedores ficam satisfeitos com o processo, pois podem se concentrar no desenvolvimento funcional em vez de lidar com mudanças repentinas.

A possibilidade de surpresas no final do ciclo de vida do projeto é reduzida.

Como projetamos a API primeiro, os testes podem ser planejados enquanto o código está sendo desenvolvido. De certa forma, também temos o TDD (Design Orientado a Testes) ao usar o desenvolvimento API first.

### Códigos de status HTTP

<p>
  <img src="../images/http-status-code.jpg" style="width: 540px" />
</p>

Os códigos de resposta para o HTTP são divididos em cinco categorias:

Informativos (100-199)
Sucesso (200-299)
Redirecionamento (300-399)
Erro do Cliente (400-499)
Erro do Servidor (500-599)

### O que faz um API gatway?

O diagrama abaixo ilustra as principais características.

<p>
  <img src="../images/api_gateway.jpg" style="width: 520px" />
</p>

Passo 1 - O cliente enviar uma requisição HTTP para o API gateway.

Passo 2 - O API gateway analisa e valida os atributos na solicitação HTTP.

Passo 3 - O API gateway verifica a lista de permissões/negações.

Passo 4 - O API gateway se comunica com um provedor de identidade para autenticação e autorização.

Passo 5 - As regras de limitação de taxa são aplicadas à solicitação. Se estiver acima do limite, a solicitação é rejeitada.

Passos 6 e 7 - Agora que a solicitação passou pelas verificações básicas, o API gateway encontra o serviço relevante para rotear por meio de correspondência de caminho.

Passo 8 - O API gateway transforma a requisição no protocolo apropriado e o envia aos microsserviços do backend.

Passos 9-12: O API agteway pode lidar adequadamente com erros e tratar falhas se o erro levar mais tempo para se recuperar (circuit break). Também pode usar a pilha ELK (Elastic-Logstash-Kibana) para registro e monitoramento. Às vezes, são armazenados dados em cache no gateway de API.

### Como projetar APIs seguras e efetivas?

O diagrama abaixo ilustra os designs típicos de API com um exemplo de carrinho de compras.

<p>
  <img src="../images/safe-apis.jpg" />
</p>

Observe que o design da API não se resume apenas ao design do caminho do URL. Na maioria das vezes, precisamos escolher nomes apropriados para os recursos, identificadores e padrões de caminho. É igualmente importante projetar campos de cabeçalho HTTP adequados ou criar regras eficazes de limitação de taxa dentro do API gateway.

### Encapsulação TCP/IP

Como os dados são enviados pela rede? Por que nós precisamos de tantas camadas no modelo OSI?

O diagrama abaixo mostra como dados são encapsulados e desencapsulados ao trasmitidos pela rede.

<p>
  <img src="../images/osi model.jpeg" />
</p>

Passo 1: Quando o Dispositivo A envia dados para o Dispositivo B pela rede via protocolo HTTP, é primeiro adicionado um cabeçalho HTTP na camada de aplicação.

Passo 2: Em seguida, é adicionado um cabeçalho TCP ou UDP aos dados. Eles são encapsulados em segmentos TCP na camada de transporte. O cabeçalho contém a porta de origem, a porta de destino e o número de sequência.

Passo 3: Os segmentos são então encapsulados com um cabeçalho IP na camada de rede. O cabeçalho IP contém os endereços IP de origem/destino.

Passo 4: O datagrama IP é adicionado a um cabeçalho MAC na camada de enlace de dados, com endereços MAC de origem/destino.

Passo 5: Os quadros encapsulados são enviados para a camada física e transmitidos pela rede em bits binários.

Passos 6-10: Quando o Dispositivo B recebe os bits da rede, ele realiza o processo de desencapsulamento, que é um processo reverso do processo de encapsulamento. Os cabeçalhos são removidos camada por camada e, eventualmente, o Dispositivo B pode ler os dados.

Precisamos de camadas no modelo de rede porque cada camada se concentra em suas próprias responsabilidades. Cada camada pode depender dos cabeçalhos para obter instruções de processamento e não precisa conhecer o significado dos dados da camada anterior.

### Por que o Nginx é chamado de uma proxy "reversa"?

O diagrama abaixo mostra as diferenças entre um proxy de encaminhamento (𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐩𝐫𝐨𝐱𝐲) e um proxy de reverso (𝐫𝐞𝐯𝐞𝐫𝐬𝐞 𝐩𝐫𝐨𝐱𝐲).

<p>
  <img src="../images/Forward Proxy v.s. Reverse Proxy2x.jpg" style="width: 720px" />
</p>

Uma proxy de encaminhamento é um servidor que fica entre usuários e dispositivos na internet.

Uma proxy de encaminhamento é comumente utilizada para:

1. Proteger clientes
2. Burlar restrições de navegação
3. Bloquear acesso a conteúdos específicos

Uma proxy reversa é um servidor que aceita uma requisição de um cliente, direciona a requisição aos servidores web e retorna os resultados para o cliete como se o próprio servidor proxy tivesse processado a requisição.

Uma proxy reversa é boa para:

1. Proteger servidores
2. Distribuição de Carga
3. Cachear conteúdo estático
4. Encriptar e decriptar comunicações SSL

### Quais são os algoritmos de distribuição de carga comuns?

O diagrama abaixo mostra 6 algoritmos comuns.

<p>
  <img src="../images/lb-algorithms.jpg" />
</p>

- Algoritmos estáticos

1. Round robin

   As requisições dos clientes são enviadas para diferentes instancias de serviços em uma ordem sequencial. Os serviços são usualmente requeridos a serem stateless.

2. Round-robin pegajoso (_sticky_)

   Este é uma melhoria do algoritmo de orund-robin. De a primeira requisição de Alice vai para o serviço A, então as requisições seguintes também vão para o serviço A.

3. Round-robin ponderado (_weighted_)

   O administrador pode especificar um peso para cada serviço. Os que tiverem um peso maior, lidam com mais requisições que os outros.

4. Hash

   Este algoritmo aplica uma função hash (de disperção) nos IPs ou URLs das requisições. As requisições são roteadas para instâncias relvantes com base no resultado do resultado da função hash.

- Dynamic Algorithms

5. Least connections

   A new request is sent to the service instance with the least concurrent connections.

6. Least response time

   A new request is sent to the service instance with the fastest response time.

### URL, URI, URN - Você sabe a diferênça?

O diagrama abaixo mostra uma comparação de URL, URI e URN.

<p>
  <img src="../images/url-uri-urn.jpg" />
</p>

- URI

URI significa Idetificador Uniforme de Recursos (_Uniform Resource Identifier_). Ele identifica um recurso lógico ou físico na web. URL e URN são subtipos de URI. URL localiza um recurso, enquanto URN nomeia um recurso.

Um URI é composto das seguintes partes:
scheme:[//authority]path[?query][#fragment]

- URL

URL significa Localizador Uniforme de Recurso (_Uniform Resource Locator_), o conceito-chave do HTTP. É o endereço de um recurso único na web. Pode ser usado com outros protocolos, como FTP e JDBC.

- URN

URN significa Nome Uniforme de Recurso (_Uniform Resource Name_). Ele usa o esquema urn. URNs não podem ser usados para localizar um recurso. Um exemplo simples fornecido no diagrama é composto por um namespace e uma string específica do namespace.

Se você deseja obter mais detalhes sobre o assunto, eu recomendaria a [explicação do W3C](https://www.w3.org/TR/uri-clarification/).

## CI/CD

### Pipeline CI/CD Explicado em Termos Simples

<p>
  <img src="../images/ci-cd-pipeline.jpg" style="width: 680px" />
</p>

Seção 1 - SDLC com CI/CD

O ciclo de vida de desenvolvimento de software (SDLC, _Software Development Life Cycle_) consiste em várias etapas-chave: desenvolvimento, teste, implantação e manutenção. CI/CD automatiza e integra essas etapas para possibilitar lançamentos mais rápidos e confiáveis.

Quando o código é enviado para um repositório Git, isso aciona um processo automatizado de compilação e teste. Casos de teste de ponta a ponta (end-to-end ou e2e) são executados para validar o código. Se os testes são bem-sucedidos, o código pode ser implantado automaticamente no ambiente de preparo/produção. Se problemas são identificados, o código é enviado de volta para o desenvolvimento para correção de bugs. Essa automação proporciona um feedback rápido aos desenvolvedores e reduz o risco de erros em produção.

Seção 2 - Diferença entre CI e CD

Integração Continua (CI, Continous Integrations) automatiza o processo de compilação, teste e o processo de implantação. Roda testes quando código é comitado para detecção de problemas de integração precocemente. Isso encoraja commits frequentes e feedback rápido.

Entrega Contínua (CD, Continuous Delivery) automatiza processos de lançamento como mudanças de infraestrutura e implantação. Garante que o software possa ser lançado de maneira confiável a qualquer momento por meio de fluxos de trabalho automatizados. A CD também pode automatizar etapas de teste manual e aprovação necessárias antes da implantação em produção.

Seção 3 - Pipeline de CI/CD

Um pipeline típico de CI/CD tem alguns estágios conectados:

- O desenvolvedor comita mudanças de código para o controle de versão
- O servidor de CI detecta as mudanças e dá início à compilação
- Code é compilado e testado (unitário e de integração)
- Os resultados são reportados ao desenvolvedor
- No sucesso, artefatos são lançados para o ambiente de preparo (staging)
- Testes adicionais podem ser realizados no ambiente de preparo antes do lançamento
- O sistema de CD lança mudanças aprovadas para produção

### Netflix Stack Tecnológico (Pipeline de CI/CD)

<p>
  <img src="../images/netflix-ci-cd.jpg" style="width: 720px" />
</p>

Planejamento: A Engenharia da Netflix utiliza o JIRA para planejamento e o Confluence para documentação.

Codificação: Java é a linguagem de programação principal para o serviço backend, enquanto outras linguagens são utilizadas para diferentes casos de uso.

Compilação: Gradle é principalmente utilizado para compilação, e plugins do Gradle são construídos para suportar vários casos de uso.

Empacotamento: O pacote e suas dependências são empacotados em uma Imagem de Máquina Amazon (AMI, _Amazon Machine Image_) para lançamento.

Testes: Os testes enfatizam o foco da cultura de produção na construção de ferramentas de caos.

Implantação: A Netflix utiliza sua própria ferramenta Spinnaker para implantação de rollout de canário.

Monitoramento: As métricas de monitoramento são centralizadas no Atlas, e o Kayenta é utilizado para detectar anomalias.

Relatório de Incidentes: Incidentes são despachados de acordo com a prioridade, e o PagerDuty é utilizado para o tratamento de incidentes.

## Padões de Arquitetura

### MVC, MVP, MVVM, MVVM-C, e VIPER

Esses padrões de arquitetura estão entre os mais comumente utilizados no desenvolvimento de aplicativos, seja nas plataformas iOS ou Android. Os desenvolvedores os introduziram para superar as limitações de padrões anteriores. Então, como eles diferem?

<p>
  <img src="../images/client arch patterns.png" style="width: 720px" />
</p>

- MVC (Modelo-Visão-Controle, _Model View Controller_), o padrão mais antigo, de quase 50 anos
- Cada padrão possui uma "visão", _view_ (V) responsável por exibir conteúdo e receber entrada do usuário
- A maioria dos padrões incluem um "modelo", _model_ (M) para manusear dados de negócio
- "Controller", "presenter" e "view-model" são tradutores que atuam como mediadores entre a "view" e o "model" (ou "entity" no padrão VIPER).

### 18 Padrões de Design Essenciais Que Todo Desenvolvedor Deve Conhecer

Padrões são soluções reutilizáveis para problemas comuns de design, resultando em um processo de desenvolvimento mais linear e eficiente. Eles servem como modelos para construir estruturas de software mais sólidas. Aqui estão alguns dos padrões mais populares:

<p>
  <img src="../images/18-oo-patterns.png" />
</p>

- Fábrica Abstrata (_Abstract Factory_): Criador de Famílias - Cria grupos de itens relacionados.
- Construtor (_Builder_): Mestre Lego - Constrói objetos passo a passo, mantendo a criação e a aparência separadas.
- Protótipo (_Prototype_): Clone Maker - Cria cópias de exemplos totalmente preparados.
- Singleton: Único e Exclusivo - Uma classe especial com apenas uma instâcia.
- Adaptador(_Adapter_): Plugue Universal - Conecta coisas com interfaces diferentes.
- Ponte (_Bridge_): Connectador Funcional - Liga como um objeto funciona ao que ele faz.
- Composito (_Composite_): Constutor de Árvores - Forma uma estruturas semelhantes a árvore com partes simples e complexas.
- Decorador (_Decorator_): Customizador - Adiciona funcionalidade a objetos sem alterar seu núcleo.
- Façada (_Facade_): Tudo em Um - Representa um sistema inteiro com uma única interface simplificada.
- Peso Mosca (_Flyweight_): Economizador de Espaço - Compartilha itens pequenos e reutilizáveis de maneira eficiente.
- Proxy: Ator Substituto - Representa outro objeto, controlando acesso ou ações.
- Cadeia de Responsabilidades (_Chain of Responsibility_): Relé de Requisições - Passa uma requisição por uma cadeia de objetos até que seja tratada.
- Comando (_Command_): Envelopador de Tarefas - Transforma uma solicitação em um objeto, pronto para atuar.
- Iterador (_Iterator_): Exploração de Coleções - Acessa elementos em uma coleção, um a um.
- Mediador (_Mediator_): Central de Comunicações - Simplifica interações entre classes distintas.
- Lembrança (_Memento_): Cápsula do Tempo - Captura e restaura o estado de um objeto.
- Observador (_Observer_): Emissora de Notícias - Notifica classes sobre mudanças em outros objetos.
- Visitante (_Visitor_): Hóspede Habilidoso - Adiciona novas operações a uma classe sem alterá-la.

## Bancos de Dados

### Um guia prático de diferentes bancos de dados em serviços de nuvem

<p>
  <img src="../images/cloud-dbs2.png" />
</p>

Escolher o banco de dados correto para o seu projeto é uma tarefa complexa. Muitas opções de bancos de dados, cada uma adequada a casos de uso distintos, podem rapidamente levar à fadiga de decisões.

Esperamos que este guia prático forneça direcionamento de alto nível para identificar o serviço correto que esteja alinhado com as necessidades do seu projeto e evite possíveis ciladas.

Nota: O Google limitou a documentação para os casos de uso de seus banco de dados. Mesmo que tenhamos feito o nosso melhor para examinar o que estava disponível e chegar à melhor opção, algumas das entradas podem precisar de maior precisão.

### 8 Estruturas de Dados que Impulsionam seus Bancos de Dados

A resposta irá variar dependendo do seu caso de uso. Dados podem ser indexados em memória ou em disco. Similarmente, os formatos dos dados variam, como números, strings, coordenadas geográficas etc. O sistema pode ser intensivo em escrita (write-heavy) ou intensivo em leitura (read-heavy). Todos esses fatores afetam a escolha do formato de índice do banco de dados.

<p>
  <img src="../images/8-ds-db.jpg" />
</p>

A seguir estão algumas das estruturas de dados mais populares usadas para indexar dados:

- Skiplist: um tipo comum de índice em memória. Usado no Redis
- Índice de hash: uma implementação muito comum da estrutura de dados "Mapa" (ou "Coleção")
- SSTable: implementação em disco e imutável do "Mapa"
- Árvore LSM: Skiplist + SSTable. Alta taxa de gravação
- B-tree: solução baseada em disco. Desempenho de leitura/gravação consistente
- Índice invertido: usado para indexação de documentos. Usado no Lucene
- Árvore de sufixos: para pesquisa de padrões em strings
- R-tree: pesquisa multidimensional, como encontrar o vizinho mais próximo

### Como um comando SQL é executado no Banco de Dados?

O diagrama abaixo demonstra o processo. Note que a arquitetura de diferentes bancos são diferentes, o diagrama apresenta alguns designs comuns.

<p>
  <img src="../images/sql execution order in db.jpeg" style="width: 580px" />
</p>

Passo 1 - Uma instrução SQL é enviada para o banco de dados por meio de um protocolo de camada de transporte (por exemplo, TCP).

Passo 2 - A instrução SQL é enviada ao analisador (_parser_) de comandos, onde passa por análise sintática e semântica, e em seguida, uma árvore de consulta é gerada.

Passo 3 - A árvore de consulta é enviada ao otimizador. O otimizador cria um plano de execução.

Passo 4 - O plano de execução é enviado ao executor. O executor recupera os dados da execução.

Passo 5 - Métodos de acesso fornecem a lógica de recuperação de dados necessária para a execução, recuperando dados do mecanismo de armazenamento (_storage engine_).

Passo 6 - Os métodos de acesso decidem se a instrução SQL é somente leitura. Se a consulta for somente leitura (instrução SELECT), ela é enviada para o gerenciador de buffer para processamento adicional. O gerenciador de buffer procura os dados no cache ou nos arquivos de dados.

Passo 7 - Se a instrução for um UPDATE ou INSERT, ela é enviada para o gerenciador de transações para processamento adicional.

Passo 8 - Durante uma transação, os dados estão em modo de bloqueio. Isso é garantido pelo gerenciador de bloqueio. Ele também assegura as propriedades ACID da transação.

### Teorema CAP

O Teorema CAP é um dos termos mais famosos na ciência da computação, mas aposto que desenvolvedores diferentes tem interpretações diferentes. Vamos examinar o que é e por que pode ser confuso.

<p>
  <img src="../images/cap theorem.jpeg" />
</p>

O teorema CAP afirma que um sistema distribuído não pode fornecer mais do que duas destas três garantias simultaneamente.

**Consistência**: consistência significa que todos os clientes enxergam os mesmos dados ao mesmo tempo, não importando em qual nó eles se conectam.

**Disponibilidade**: disponibilidade significa que qualquer cliente que realizar uma requisição de dados terá uma resposta, mesmo que alguns nós não estejam de pé.

**Tolerância de Partição**: uma partição indica uma quebra na comunicação entre dois nós. Uma tolerância de partição significa que o sistema continua em operação apesar de partições de redes.

A formulação "2 de 3" pode ser útil, **mas essa simplificação pode ser enganosa**.

1. Escolher um banco de dados não é fácil. Justificar sua escolha puramente no teorema CAP não é o suficiente. Por exemplo, companhias não escolhem Cassandra para aplicativos de cat simplesmente por ser um sistema AP. Há uma lista de características que tornam uma opção boa para armazenamento de mensagens de chat. Precisamos cavar mais fundo.

2. "CAP proíbe apenas uma pequena parte do espaço de design: disponibilidade e consistência perfeitas na presença de partições, que são raras". Citado do artigo: CAP Twelve Years Later: How the "Rules" Have Changed.

3. O teorema trata de disponibilidade e consistência de 100%. Uma discussão mais realista envolveria as compensações entre latência e consistência quando não há partição de rede. Consulte o teorema PACELC para obter mais detalhes.

**O teorema CAP é de fato útil?**

Acredito que ainda é útil por abrir nossas mentes para um novo conjunto de discussões sobre compensações, mas é apenas uma parte da história. Precisamos nos aprofundar para esolcher o banco de dados correto.

### Tipos de Memória e Armazenamento

<p>
  <img src="../images/Types_of_Memory_and_Storage.jpeg" style="width: 420px" />
</p>

### Visualizando uma consulta SQL

<p>
  <img src="../images/sql-execution-order.jpg" style="width: 580px" />
</p>

As instruções SQL são executadas pelo sistema do banco de dados em várias etapas, incluindo:

- Analisando a instrução SQL e verificando sua validade
- Transformando o SQL em uma representação interna, como álgebra relacional
- Otimizando a representação interna e criando um plano de execução que utiliza informações de índices
- Executando o plano e retornando os resultados

A execução do SQL é altamente complexa e envolve muitas considerações, tais como:

- O uso de índices e caches
- A ordem de junções de tabelas
- Controle de concorrência
- Gerenciamento de transações

### Linguagem SQL

In 1986, SQL (Structured Query Language) became a standard. Over the next 40 years, it became the dominant language for relational database management systems. Reading the latest standard (ANSI SQL 2016) can be time-consuming. How can I learn it?

Em 1986, SQL (Linguagem de Busca Estruturada, _Structured Query Language_) se tornou um padrão. Ao longo os próximos 40 anos, ela se tornou a linguagem dominante para sistemas de manuseamento de bancos de dados relacionais. Ler o último padrão (ANSI SQL 2016) pode ser demorado. Como posso aprenê-lo?

<p>
  <img src="../images/how-to-learn-sql.jpg" />
</p>

Há 5 componentes da linguagem SQL:

- DDL: linguagem de definição de dados, como CREATE, ALTER, DROP
- DQL: linguagem de consulta de dados, como SELECT
- DML: linguagem de manipulação de dados, como INSERT, UPDATE, DELETE
- DCL: linguagem de controle de dados, como GRANT, REVOKE
- TCL: linguagem de controle de transações, como COMMIT, ROLLBACK

Para um engenheiro de backend, pode ser necessário saber a maior parte deles. Como um analista de dados, é importante ter uma boa noção do DQL. Selecione os tópicos que são mais relevantes para você.

## Cache

### Data is cached everywhere

This diagram illustrates where we cache data in a typical architecture.

<p>
  <img src="../images/where do we cache data.jpeg" style="width: 720px" />
</p>

There are **multiple layers** along the flow.

1. Client apps: HTTP responses can be cached by the browser. We request data over HTTP for the first time, and it is returned with an expiry policy in the HTTP header; we request data again, and the client app tries to retrieve the data from the browser cache first.
2. CDN: CDN caches static web resources. The clients can retrieve data from a CDN node nearby.
3. Load Balancer: The load Balancer can cache resources as well.
4. Messaging infra: Message brokers store messages on disk first, and then consumers retrieve them at their own pace. Depending on the retention policy, the data is cached in Kafka clusters for a period of time.
5. Services: There are multiple layers of cache in a service. If the data is not cached in the CPU cache, the service will try to retrieve the data from memory. Sometimes the service has a second-level cache to store data on disk.
6. Distributed Cache: Distributed cache like Redis holds key-value pairs for multiple services in memory. It provides much better read/write performance than the database.
7. Full-text Search: we sometimes need to use full-text searches like Elastic Search for document search or log search. A copy of data is indexed in the search engine as well.
8. Database: Even in the database, we have different levels of caches:

- WAL(Write-ahead Log): data is written to WAL first before building the B tree index
- Bufferpool: A memory area allocated to cache query results
- Materialized View: Pre-compute query results and store them in the database tables for better query performance
- Transaction log: record all the transactions and database updates
- Replication Log: used to record the replication state in a database cluster

### Why is Redis so fast?

There are 3 main reasons as shown in the diagram below.

<p>
  <img src="../images/why_redis_fast.jpeg" />
</p>

1. Redis is a RAM-based data store. RAM access is at least 1000 times faster than random disk access.
2. Redis leverages IO multiplexing and single-threaded execution loop for execution efficiency.
3. Redis leverages several efficient lower-level data structures.

Question: Another popular in-memory store is Memcached. Do you know the differences between Redis and Memcached?

You might have noticed the style of this diagram is different from my previous posts. Please let me know which one you prefer.

### How can Redis be used?

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

### Top caching strategies

Designing large-scale systems usually requires careful consideration of caching.
Below are five caching strategies that are frequently utilized.

<p>
  <img src="../images/top_caching_strategy.jpeg" style="width: 680px" />
</p>

## Microservice architecture

### What does a typical microservice architecture look like?

<p>
  <img src="../images/typical-microservice-arch.jpg" style="width: 520px" />
</p>

The diagram below shows a typical microservice architecture.

- Load Balancer: This distributes incoming traffic across multiple backend services.
- CDN (Content Delivery Network): CDN is a group of geographically distributed servers that hold static content for faster delivery. The clients look for content in CDN first, then progress to backend services.
- API Gateway: This handles incoming requests and routes them to the relevant services. It talks to the identity provider and service discovery.
- Identity Provider: This handles authentication and authorization for users.
- Service Registry & Discovery: Microservice registration and discovery happen in this component, and the API gateway looks for relevant services in this component to talk to.
- Management: This component is responsible for monitoring the services.
- Microservices: Microservices are designed and deployed in different domains. Each domain has its own database. The API gateway talks to the microservices via REST API or other protocols, and the microservices within the same domain talk to each other using RPC (Remote Procedure Call).

Benefits of microservices:

- They can be quickly designed, deployed, and horizontally scaled.
- Each domain can be independently maintained by a dedicated team.
- Business requirements can be customized in each domain and better supported, as a result.

### Microservice Best Practices

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

### What tech stack is commonly used for microservices?

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

### Why is Kafka fast

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

## Payment systems

### How to learn payment systems?

<p>
  <img src="../images/learn-payments.jpg" />
</p>

### Why is the credit card called “the most profitable product in banks”? How does VISA/Mastercard make money?

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

### DevOps vs. SRE vs. Platform Engineering. What is the difference?

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

## Real World Case Studies

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
