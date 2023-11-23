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

Vizual va oddiy atamalar yordamida murakkab tizimlarni tushuning.

Tizim dizayni bo'yicha intervyuga tayyorlanyapsizmi yoki tizimlar qanday ishlashini tushunishni xohlaysizmi, umid qilamizki, ushbu repository sizga bunga erishishda yordam beradi.

# Mundarija

<!-- TOC toc.levels=2 -->

- [Aloqa protokollari](#aloqa-protokollari)
  - [REST API va GraphQL](#rest-api-va-graphql)
  - [gRPC qanday ishlaydi?](#grpc-qanday-ishlaydi)
  - [Webhook nima?](#webhook-nima)
  - [API ish faoliyatini qanday yaxshilash mumkin?](#api-ish-faoliyatini-qanday-yaxshilash-mumkin)
  - [HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)](#http-10---http-11---http-20---http-30-quic)
  - [SOAP va REST va GraphQL va RPC](#soap-va-rest-va-graphql-va-rpc)
  - [Code First va API First](#code-first-va-api-first)
  - [HTTP holat kodlari](#http-holat-kodlari)
  - [API shlyuzi nima qiladi?](#api-shlyuzi-nima-qiladi)
  - [Qanday qilib samarali va xavfsiz API-larni loyihalashtiramiz?](#qanday-qilib-samarali-va-xavfsiz-api-larni-loyihalashtiramiz)
  - [TCP/IP inkapsulyatsiyasi](#tcpip-inkapsulyatsiyasi)
  - [Nima uchun Nginx "teskari" proksi-server deb ataladi?](#nima-uchun-nginx-teskari-proksi-server-deb-ataladi)
  - [Umumiy yuklarni muvozanatlash algoritmlari qanday?](#umumiy-yuklarni-muvozanatlash-algoritmlari-qanday)
  - [URL, URI, URN - Farqlarni bilasizmi?](#url-uri-urn---farqlarni-bilasizmi)
- [CI/CD](#cicd)
  - [CI/CD quvur liniyasi oddiy so'zlar bilan tushuntirilgan](#cicd-quvur-liniyasi-oddiy-sozlar-bilan-tushuntirilgan)
  - [Netflix Tech Stack (CI/CD Pipeline)](#netflix-tech-stack-cicd-pipeline)
- [Arxitektura naqshlari](#arxitektura-naqshlari)
  - [MVC, MVP, MVVM, MVVM-C va VIPER](#mvc-mvp-mvvm-mvvm-c-va-viper)
  - [Har bir dasturchi bilishi kerak bo'lgan 18 ta asosiy dizayn naqshlari](#har-bir-dasturchi-bilishi-kerak-bolgan-18-ta-asosiy-dizayn-naqshlari)
- [Ma'lumotlar bazasi](#malumotlar-bazasi)
  - [Bulutli xizmatlardagi turli xil ma'lumotlar bazalarining chiroyli cheat varag'i](#bulutli-xizmatlardagi-turli-xil-malumotlar-bazalarining-chiroyli-cheat-varagi)
  - [Ma'lumotlar bazalaringizni quvvatlantiradigan 8 ta ma'lumotlar tuzilmasi](#malumotlar-bazalaringizni-quvvatlantiradigan-8-ta-malumotlar-tuzilmasi)
  - [Ma'lumotlar bazasida SQL operatori qanday bajariladi?](#malumotlar-bazasida-sql-operatori-qanday-bajariladi)
  - [CAP teoremasi](#cap-teoremasi)
  - [Xotira va saqlash turlari](#xotira-va-saqlash-turlari)
  - [SQL so'rovini vizualizatsiya qilish](#sql-sorovini-vizualizatsiya-qilish)
  - [SQL tili](#sql-tili)
- [Kesh](#kesh)
  - [Ma'lumotlar hamma joyda keshlangan](#malumotlar-hamma-joyda-keshlangan)
  - [Nima uchun Redis juda tez?](#nima-uchun-redis-juda-tez)
  - [Redisdan qanday foydalanish mumkin?](#redisdan-qanday-foydalanish-mumkin)
  - [Eng yaxshi keshlash strategiyalari](#eng-yaxshi-keshlash-strategiyalari )
- [Mikroservis arxitekturasi](#mikroservis-arxitekturasi)
  - [Oddiy mikroservis arxitekturasi nimaga o'xshaydi?](#oddiy-mikroservis-arxitekturasi-nimaga-oxshaydi)
  - [Mikroservisning eng yaxshi amaliyotlari](#mikroservisning-eng-yaxshi-amaliyotlari)
  - [Mikroservislar uchun qanday texnologik stek ishlatiladi?](#mikroservislar-uchun-qanday-texnologik-stek-ishlatiladi)
  - [Nega Kafka tez](#nega-kafka-tez)
- [To'lov tizimlari](#tolov-tizimlari)
  - [To'lov tizimini qanday o'rganish mumkin?](#tolov-tizimini-qanday-organish-mumkin)
  - [Nima uchun kredit karta "banklardagi eng daromadli mahsulot" deb ataladi? VISA/Mastercard qanday qilib pul ishlaydi?](#nima-uchun-kredit-karta-banklardagi-eng-daromadli-mahsulot-deb-ataladi-visamastercard-qanday-qilib-pul-ishlaydi)
  - [Savdogarlar do'konida kredit kartani o'tkazganimizda VISA qanday ishlaydi?](#savdogarlar-dokonida-kredit-kartani-otkazganimizda-visa-qanday-ishlaydi)
  - [Dunyo bo'ylab to'lov tizimlari seriyasi (1-qism): Hindistonda yagona to'lov interfeysi (UPI)](#dunyo-boylab-tolov-tizimlari-seriyasi-1-qism-hindistonda-yagona-tolov-interfeysi-upi)
- [DevOps](#devops)
  - [DevOps va SRE va platforma muhandisligi. Farqi nimada?](#devops-va-sre-va-platforma-muhandisligi-farqi-nimada)
  - [K8s (Kubernetes) nima?](#k8s-kubernetes-nima)
  - [Docker va Kubernetes. Qaysi birini ishlatishimiz kerak?](#docker-va-kubernetes-qaysi-birini-ishlatishimiz-kerak)
  - [Docker qanday ishlaydi?](#docker-qanday-ishlaydi)
- [GIT](#git)
  - [Git buyruqlari qanday ishlaydi](#git-buyruqlari-qanday-ishlaydi)
  - [Git qanday ishlaydi?](#git-qanday-ishlaydi)
  - [Git merge va Git rebase](#git-merge-va-git-rebase)
- [Bulutli xizmatlar](#bulutli-xizmatlar)
  - [Turli xil bulut xizmatlarining chiroyli cheat varag'i (2023 yil nashri)](#turli-xil-bulut-xizmatlarining-chiroyli-cheat-varagi-2023-yil-nashri)
  - [Mahalliy bulut nima?](#mahalliy-bulut-nima)
- [Ishlab chiquvchi mahsuldorlik vositalari](#ishlab-chiquvchi-mahsuldorlik-vositalari)
  - [JSON fayllarini vizualizatsiya qilish](#json-fayllarini-vizualizatsiya-qilish)
  - [Kodni avtomatik ravishda arxitektura diagrammalariga aylantiring](#kodni-avtomatik-ravishda-arxitektura-diagrammalariga-aylantiring)
- [Linux](#linux)
  - [Linux fayl tizimi tushuntirildi](#linux-fayl-tizimi-tushuntirildi)
  - [Siz bilishingiz kerak bo'lgan 18 ta eng ko'p ishlatiladigan Linux buyruqlari](#siz-bilishingiz-kerak-bolgan-18-ta-eng-kop-ishlatiladigan-linux-buyruqlari)
- [Xavfsizlik](#xavfsizlik)
  - [HTTPS qanday ishlaydi?](#https-qanday-ishlaydi)
  - [Oauth 2.0 oddiy shartlar bilan tushuntirilgan.](#oauth-20-oddiy-shartlar-bilan-tushuntirilgan)
  - [Autentifikatsiya mexanizmlarining 4 ta eng yaxshi shakllari](#autentifikatsiya-mexanizmlarining-4-ta-eng-yaxshi-shakllari)
  - [Sessiya, cookie, JWT, token, SSO va OAuth 2.0 - ular nima?](#sessiya-cookie-jwt-token-sso-va-oauth-20---ular-nima)
  - [Ma'lumotlar bazasida parollarni qanday xavfsiz saqlash va parolni qanday tekshirish mumkin?](#malumotlar-bazasida-parollarni-qanday-xavfsiz-saqlash-va-parolni-qanday-tekshirish-mumkin)
  - [10 yoshli bolaga JSON Web Token (JWT) haqida tushuntirish](#10-yoshli-bolaga-json-web-token-jwt-haqida-tushuntirish)
  - [Google Authenticator (yoki 2 faktorli autentifikatsiyaning boshqa turlari) qanday ishlaydi?](#google-authenticator-yoki-2-faktorli-autentifikatsiyaning-boshqa-turlari-qanday-ishlaydi)
- [Haqiqiy dunyo misollari](#haqiqiy-dunyo-misollari)
  - [Netflixning Tech Stacki](#netflixning-tech-stacki)
  - [Twitter arxitekturasi 2022](#twitter-arxitekturasi-2022)
  - [Oxirgi 15 yil ichida Airbnb mikroservis arxitekturasining evolyutsiyasi](#oxirgi-15-yil-ichida-airbnb-mikroservis-arxitekturasining-evolyutsiyasi)
  - [Monorepo va mikrorepo.](#monorepo-va-mikrorepo)
  - [Stack Overflow veb-saytini qanday loyihalashtirasiz?](#stack-overflow-veb-saytini-qanday-loyihalashtirasiz)
  - [Nima uchun Amazon Prime Video monitoringi serversizdan monolitga o'tdi? Qanday qilib 90% xarajatlarni tejash mumkin?](#nima-uchun-amazon-prime-video-monitoringi-serversizdan-monolitga-otdi-qanday-qilib-90-xarajatlarni-tejash-mumkin)
  - [Disney Hotstar turnir davomida 5 milliard kulgichni qanday suratga oladi?](#disney-hotstar-turnir-davomida-5-milliard-kulgichni-qanday-suratga-oladi)
  - [Discord qanday qilib trillionlab xabarlarni saqlaydi?](#discord-qanday-qilib-trillionlab-xabarlarni-saqlaydi)
  - [YouTube, TikTok live yoki Twitch-da jonli video oqimlari qanday ishlaydi?](#youtube-tiktok-live-yoki-twitch-da-jonli-video-oqimlari-qanday-ishlaydi)

<!-- /TOC -->

## Aloqa protokollari

Arxitektura uslublari amaliy dasturlash interfeysining (API) turli komponentlari bir-biri bilan qanday o'zaro ta'sir qilishini belgilaydi.Natijada, ular API-larni loyihalash va qurishda standart yondashuvni ta'minlash orqali samaradorlik, ishonchlilik va boshqa tizimlar bilan integratsiya qulayligini ta'minlaydi. Bu erda eng ko'p ishlatiladigan uslublar:

<p>
  <img src="../images/api-architecture-styles.png" style="width: 640px">
</p>

- SOAP:
  
  Yetuk, keng qamrovli, XML-ga asoslangan 
  
  Korporativ ilovalar uchun eng yaxshi

- RESTful:

  Ommabop, amalga oshirish oson, HTTP usullari

  Veb-xizmatlar uchun ideal

- GraphQL:

  So'rov tili, maxsus ma'lumotlarni so'rash

  Tarmoq yukini kamaytiradi, tezroq javob beradi

- gRPC:

  Zamonaviy, yuqori samarali, protokol buferlari

  Mikroservislar arxitekturasi uchun javob beradi

- WebSocket:

  Real-time, bidirectional, persistent connections

  Kam kechikishli ma'lumotlar almashinuvi uchun juda mos keladi

- Webhook:

  Voqealarga asoslangan, HTTP qo'ng'iroqlari, asinxron

  Voqea sodir bo'lganda tizimlarni xabardor qiladi


### REST API va GraphQL

API dizayni haqida gap ketganda, REST va GraphQL har birining kuchli va zaif tomonlari bor.

Quyidagi diagrammada REST va GraphQL o'rtasidagi tezkor taqqoslash ko'rsatilgan.

<p>
  <img src="../images/graphQL.jpg">
</p>

REST

- CRUD operatsiyalari uchun GET, POST, PUT, DELETE kabi standart HTTP usullaridan foydalanadi.
- Alohida xizmatlar/ilovalar o'rtasida oddiy, bir xil interfeyslar kerak bo'lganda yaxshi ishlaydi.
- Keshlash strategiyalarini amalga oshirish oson.
- Salbiy tomoni shundaki, u alohida so'nggi nuqtalardan tegishli ma'lumotlarni yig'ish uchun bir nechta aylanishlarni talab qilishi mumkin.

GraphQL

- Mijozlarga kerakli ma'lumotlarni aniq so'rashlari uchun yagona so'nggi nuqtani taqdim etadi.
- Mijozlar ichki so'rovlarda talab qilinadigan aniq maydonlarni belgilaydi va server faqat shu maydonlarni o'z ichiga olgan optimallashtirilgan foydali yuklarni qaytaradi.
- Ma'lumotlarni o'zgartirish uchun mutatsiyalarni va real vaqtda bildirishnomalar uchun obunalarni qo'llab-quvvatlaydi.
- Bir nechta manbalardan ma'lumotlarni jamlash uchun ajoyib va tez rivojlanayotgan frontend talablari bilan yaxshi ishlaydi.
- Biroq, u murakkablikni mijoz tomoniga o'tkazadi va agar to'g'ri himoyalanmagan bo'lsa, haqoratli so'rovlarga ruxsat berishi mumkin.
- Keshlash strategiyalari RESTga qaraganda murakkabroq bo'lishi mumkin.

REST va GraphQL o'rtasidagi eng yaxshi tanlov dastur va ishlab chiqish guruhining o'ziga xos talablariga bog'liq. GraphQL murakkab yoki tez-tez o'zgaruvchan frontend ehtiyojlari uchun juda mos keladi, REST esa oddiy va izchil shartnomalar afzal ko'rilgan ilovalarga mos keladi.

Hech bir API yondashuvi kumush o'q emas. To'g'ri uslubni tanlash uchun talablar va kelishuvlarni diqqat bilan baholash muhimdir. REST va GraphQL ikkalasi ham ma'lumotlarni oshkor qilish va zamonaviy ilovalarni quvvatlantirish uchun to'g'ri tanlovdir.


### gRPC qanday ishlaydi?

RPC (Remote Procedure Call) "**remote(masofaviy)**" deb nomlanadi, chunki u xizmatlar mikroservis arxitekturasi ostida turli serverlarga o'rnatilganda masofaviy xizmatlar o'rtasida aloqa o'rnatish imkonini beradi. Foydalanuvchi nuqtai nazaridan, u mahalliy funktsiya chaqiruvi kabi ishlaydi.

Quyidagi diagramma **gRPC** uchun umumiy ma'lumotlar oqimini ko'rsatadi.

<p>
  <img src="../images/grpc.jpg">
</p>

1-qadam: REST qo'ng'irog'i mijozdan amalga oshiriladi. So'rovning asosiy qismi odatda JSON formatida bo'ladi.

2-4-qadamlar: Buyurtma xizmati (gRPC mijozi) REST qo'ng'irog'ini qabul qiladi, uni o'zgartiradi va to'lov xizmatiga RPC qo'ng'irog'ini qiladi. gRPC **client stub(mijoz stubi)** ni ikkilik formatga kodlaydi va uni past darajadagi transport qatlamiga yuboradi.

5-qadam: gRPC paketlarni HTTP2 orqali tarmoq orqali yuboradi. Ikkilik kodlash va tarmoqni optimallashtirish tufayli gRPC JSONga qaraganda 5X tezroq deb aytiladi.

6-8-qadamlar: Toʻlov xizmati (gRPC serveri) tarmoqdan paketlarni qabul qiladi, ularni dekodlaydi va server ilovasini ishga tushiradi.

9-11-qadamlar: Natija server ilovasidan qaytariladi va kodlanadi va transport qatlamiga yuboriladi.

12-14-qadamlar: Buyurtma xizmati paketlarni qabul qiladi, ularni dekodlaydi va natijani mijoz ilovasiga yuboradi.

### Webhook nima?

Quyidagi diagrammada so'rov va Webhook o'rtasidagi taqqoslash ko'rsatilgan.

<p>
  <img src="../images/webhook.jpeg" style="width: 680px" />
</p>

Faraz qilaylik, biz elektron tijorat veb-saytini ishga tushiramiz. Mijozlar to'lov operatsiyalari uchun to'lov xizmatiga o'tadigan API shlyuzi orqali buyurtma xizmatiga buyurtma yuboradilar. Keyin to'lov xizmati tranzaktsiyalarni bajarish uchun tashqi to'lov xizmati provayderi (PSP) bilan gaplashadi.

Tashqi PSP bilan aloqa qilishning ikki yo'li mavjud.

**1. Short polling(Qisqa ovoz berish)**

To'lov so'rovi PSP ga yuborilgandan so'ng, to'lov xizmati PSP dan to'lov holati haqida so'rashda davom etadi. Bir necha turdan so'ng, PSP nihoyat holatga qaytadi.

Qisqa so'rovning ikkita kamchiligi bor:
* Doimiy ravishda vaziyatni so'rash to'lov xizmatidan resurslarni talab qiladi.
* Tashqi xizmat to'lov xizmati bilan to'g'ridan-to'g'ri bog'lanib, xavfsizlik zaifliklarini yaratadi.

**2. Webhook**

Biz webhukni tashqi xizmatda ro'yxatdan o'tkazishimiz mumkin. Buning ma'nosi: so'rov bo'yicha yangilanishlar mavjud bo'lganda, menga ma'lum bir URL orqali qo'ng'iroq qiling. PSP qayta ishlashni tugatgandan so'ng, to'lov holatini yangilash uchun HTTP so'rovini chaqiradi.

Shu tarzda, dasturlash paradigmasi o'zgartiriladi va to'lov xizmati endi to'lov holatini so'rash uchun resurslarni isrof qilishiga hojat yo'q.

Agar PSP hech qachon qo'ng'iroq qilmasa nima bo'ladi? Biz har soatda to'lov holatini tekshirish uchun uy ishlarini o'rnatishimiz mumkin.

WebhooksWebhuklar ko'pincha teskari API yoki push API deb ataladi, chunki server mijozga HTTP so'rovlarini yuboradi. Webhukdan foydalanishda 3 narsaga e'tibor qaratishimiz kerak:

1. Biz tashqi xizmat qo'ng'iroq qilish uchun tegishli APIni loyihalashimiz kerak.
2. Xavfsizlik nuqtai nazaridan API shlyuzida tegishli qoidalarni o'rnatishimiz kerak.
3. Biz tashqi xizmatda to'g'ri URL manzilini ro'yxatdan o'tkazishimiz kerak.

### API ish faoliyatini qanday yaxshilash mumkin?

Quyidagi diagrammada API ish faoliyatini yaxshilash uchun 5 ta umumiy hiyla ko'rsatilgan.

<p>
  <img src="../images/api-performance.jpg">
</p>

Pagination(Sahifalar)

Natijaning o'lchami katta bo'lsa, bu keng tarqalgan optimallashtirishdir. Natijalar xizmatning javob berish qobiliyatini yaxshilash uchun mijozga qaytariladi.

Asynchronous Logging(Asinxron ro'yxatga olish)

Sinxron ro'yxatga olish har bir qo'ng'iroq uchun disk bilan ishlaydi va tizimni sekinlashtirishi mumkin. Asinxron ro'yxatga olish jurnallarni avval qulflanmagan buferga yuboradi va darhol qaytadi. Jurnallar diskka vaqti-vaqti bilan tozalanadi. Bu kiritish-chiqarish xarajatlarini sezilarli darajada kamaytiradi.

Caching(Keshlash)

Biz tez-tez foydalaniladigan ma'lumotlarni keshga saqlashimiz mumkin. Mijoz to'g'ridan-to'g'ri ma'lumotlar bazasiga tashrif buyurish o'rniga, avval keshni so'rashi mumkin. Agar kesh o'tkazib yuborilgan bo'lsa, mijoz ma'lumotlar bazasidan so'rashi mumkin. Redis kabi keshlar ma'lumotlarni xotirada saqlaydi, shuning uchun ma'lumotlarga kirish ma'lumotlar bazasiga qaraganda ancha tezroq.

Payload Compression(Yuk yukini siqish)

So'rovlar va javoblar uzatiladigan ma'lumotlar hajmi ancha kichik bo'lishi uchun gzip va boshqalar yordamida siqilishi mumkin. Bu yuklash va yuklab olishni tezlashtiradi.

Connection Pool(Aloqa hovuzi)

Resurslarga kirishda biz ko'pincha ma'lumotlar bazasidan ma'lumotlarni yuklashimiz kerak. Yopuvchi db ulanishlarini ochish sezilarli yukni oshiradi. Shunday qilib, biz DB ga ochiq ulanishlar hovuzi orqali ulanishimiz kerak. Ulanish havzasi ulanishning hayot aylanishini boshqarish uchun javobgardir.

### HTTP 1.0 -> HTTP 1.1 -> HTTP 2.0 -> HTTP 3.0 (QUIC)

HTTP ning har bir avlodi qanday muammoni hal qiladi?

Quyidagi diagrammada asosiy xususiyatlar ko'rsatilgan.

<p>
  <img src="../images/http3.jpg" />
</p>

- HTTP 1.0 1996 yilda yakunlangan va to'liq hujjatlashtirilgan. Bitta serverga har bir so'rov alohida TCP ulanishini talab qiladi.

- HTTP 1.1 1997 yilda nashr etilgan. TCP ulanishi qayta foydalanish uchun ochiq qoldirilishi mumkin (doimiy ulanish), lekin bu HOL (yo'nalish boshi(head-of-line)) blokirovkasi muammosini hal qilmaydi. 

  HOL blokirovkasi - brauzerda ruxsat etilgan parallel so'rovlar soni tugaganda, keyingi so'rovlar avvalgilarining bajarilishini kutishlari kerak.

- HTTP 2.0 2015-yilda nashr etilgan. U HOL muammosini soʻrovni multiplekslash orqali hal qiladi, bu esa dastur qatlamida HOL bloklanishini bartaraf qiladi, biroq HOL transport (TCP) qatlamida hali ham mavjud.

  Diagrammada ko'rib turganingizdek, HTTP 2.0 HTTP "oqimlari" tushunchasini taqdim etdi: bir xil TCP ulanishiga turli xil HTTP almashinuvlarini multiplekslash imkonini beruvchi abstraksiya. Har bir oqimni tartibda yuborish shart emas.

- HTTP 3.0 ning birinchi loyihasi 2020-yilda chop etilgan. U HTTP 2.0 ning tavsiya etilgan vorisi hisoblanadi. U asosiy transport protokoli uchun TCP o'rniga QUIC dan foydalanadi, shuning uchun transport qatlamidagi HOL blokirovkasini olib tashlaydi. 

QUIC UDP ga asoslangan. U oqimlarni transport qatlamida birinchi darajali fuqarolar sifatida tanishtiradi. QUIC oqimlari bir xil QUIC ulanishiga ega, shuning uchun yangilarini yaratish uchun qo'shimcha qo'l siqish(handshake) va sekin boshlash(slow start) talab qilinmaydi, lekin QUIC oqimlari mustaqil ravishda yetkazib beriladi, ko'p hollarda bitta oqimga ta'sir qiladigan paket yo'qotilishi boshqalarga ta'sir qilmaydi.

### SOAP va REST va GraphQL va RPC

Quyidagi diagrammada API vaqt jadvali va API uslublarini taqqoslash tasvirlangan.

Vaqt o'tishi bilan turli xil API arxitektura uslublari chiqariladi. Ularning har biri ma'lumotlar almashinuvini standartlashtirishning o'ziga xos naqshlariga ega. 

Diagrammada har bir uslubning foydalanish holatlarini tekshirishingiz mumkin.

<p>
  <img src="../images/SOAP vs REST vs GraphQL vs RPC.jpeg" />
</p>


### Code First va API First 

Quyidagi diagrammada birinchi kodni ishlab chiqish va API-birinchi ishlanma o'rtasidagi farqlar ko'rsatilgan. Nima uchun biz API birinchi dizaynini ko'rib chiqmoqchimiz?

<p>
  <img src="../images/api_first.jpg" style="width: 680px" />
</p>


- Mikroservislar tizimning murakkabligini oshiradi va bizda tizimning turli funktsiyalarini bajarish uchun alohida xizmatlar mavjud. Ushbu turdagi arxitektura vazifalarni ajratish va ajratishni osonlashtirsa-da, biz xizmatlar o'rtasidagi turli xil aloqalarni boshqarishimiz kerak. 

Kodni yozishdan va xizmatlar chegaralarini sinchkovlik bilan belgilashdan oldin tizimning murakkabligini o'ylab ko'rgan ma'qul.

- Alohida funktsional guruhlar bir xil tilda gapirishlari kerak va maxsus funktsional guruhlar faqat o'zlarining tarkibiy qismlari va xizmatlari uchun javobgardir. Tashkilotga API dizayni orqali bir xil tilda gapirish tavsiya etiladi. 

Kod yozishdan oldin API dizaynini tasdiqlash uchun so'rovlar va javoblarni masxara qilishimiz mumkin.

- Dasturiy ta'minot sifati va ishlab chiquvchining mahsuldorligini oshirish Loyiha boshlanganda noaniqliklarning ko'pini bartaraf etganimiz sababli, umumiy ishlab chiqish jarayoni yanada silliqlashadi va dasturiy ta'minot sifati sezilarli darajada yaxshilanadi.

Ishlab chiquvchilar ham jarayondan xursandlar, chunki ular to'satdan o'zgarishlarni muhokama qilish o'rniga funktsional rivojlanishga e'tibor berishlari mumkin.

Loyihaning hayotiy tsiklining oxiriga kelib kutilmagan hodisalar bo'lish ehtimoli kamayadi.

Biz APIni birinchi bo'lib ishlab chiqqanimiz sababli, testlar kod ishlab chiqilayotganda ishlab chiqilishi mumkin. Qaysidir ma'noda, API birinchi ishlanmasidan foydalanganda bizda TDD (Test Driven Design) mavjud.

### HTTP holat kodlari

<p>
  <img src="../images/http-status-code.jpg" style="width: 540px" />
</p>


HTTP uchun javob kodlari besh toifaga bo'lingan:

Informational (100-199) \
Success (200-299) \
Redirection (300-399) \
Client Error (400-499) \
Server Error (500-599) 

### API shlyuzi nima qiladi?

Quyidagi diagrammada tafsilotlar ko'rsatilgan. 

<p>
  <img src="../images/api_gateway.jpg" style="width: 520px" />
</p>

1-qadam - mijoz API shlyuziga HTTP so'rovini yuboradi.

2-qadam - API shlyuzi HTTP so'rovidagi atributlarni tahlil qiladi va tasdiqlaydi.

3-qadam - API shlyuzi ruxsat-roʻyxat/rad etish roʻyxatini tekshirishni amalga oshiradi.

4-qadam - API shlyuzi autentifikatsiya va avtorizatsiya uchun identifikatsiya provayderi bilan gaplashadi.

5-qadam - so'rovga tarifni cheklash qoidalari qo'llaniladi. Agar limitdan oshib ketgan bo'lsa, so'rov rad etiladi.

6 va 7-qadamlar - Endi so'rov asosiy tekshiruvlardan o'tgan bo'lsa, API shlyuzi mos keladigan yo'nalish bo'yicha yo'nalish uchun tegishli xizmatni topadi.

8-qadam - API shlyuzi so'rovni tegishli protokolga o'zgartiradi va uni backend mikroservislariga yuboradi. 

9-12-qadamlar: API shlyuzi xatolarni to'g'ri boshqarishi mumkin va agar xatoni tiklash uchun ko'proq vaqt kerak bo'lsa, xatolar bilan shug'ullanadi (elektron uzilish). Shuningdek, u ro'yxatga olish va monitoring qilish uchun ELK (Elastic-Logstash-Kibana) stekidan foydalanishi mumkin. Biz ba'zan ma'lumotlarni API shlyuzida keshlaymiz. 

### Qanday qilib samarali va xavfsiz API-larni loyihalashtiramiz?

Quyidagi diagrammada xarid savatchasi misoli bilan odatiy API dizaynlari ko'rsatilgan.

<p>
  <img src="../images/safe-apis.jpg" />
</p>


E'tibor bering, API dizayni shunchaki URL yo'l dizayni emas. Ko'pincha biz to'g'ri manba nomlarini, identifikatorlarni va yo'l naqshlarini tanlashimiz kerak. Tegishli HTTP sarlavhalari maydonlarini loyihalash yoki API shlyuzida samarali tezlikni cheklovchi qoidalarni ishlab chiqish bir xil darajada muhimdir. 

### TCP/IP inkapsulyatsiyasi

Ma'lumotlar tarmoq orqali qanday uzatiladi? Nima uchun bizga OSI modelida juda ko'p qatlamlar kerak?

<p>
  <img src="../images/osi model.jpeg" />
</p>

Quyidagi diagrammada tarmoq orqali uzatishda ma'lumotlarning qanday inkapsullanganligi va inkapsulatsiyasi ko'rsatilgan.

1-qadam: A qurilmasi HTTP protokoli orqali tarmoq orqali B qurilmaga ma'lumotlarni yuborganda, u birinchi navbatda dastur sathida HTTP sarlavhasi qo'shiladi.

2-qadam: Keyin ma'lumotlarga TCP yoki UDP sarlavhasi qo'shiladi. U transport qatlamida TCP segmentlariga inkapsullangan. Sarlavhada manba porti, maqsad porti va tartib raqami mavjud.

3-qadam: Keyin segmentlar tarmoq sathida IP sarlavhasi bilan qoplangan. IP sarlavhasi manba/maqsad IP manzillarini o'z ichiga oladi.

4-qadam: IP-datagramma manba/maqsad MAC manzillari bilan ma'lumotlar havolasi qatlamiga MAC sarlavhasi qo'shiladi.

5-qadam: Inkapsullangan ramkalar jismoniy qatlamga yuboriladi va tarmoq orqali ikkilik bitlarda yuboriladi.

6-10-qadamlar: B qurilmasi tarmoqdan bitlarni qabul qilganda, u inkapsulyatsiya jarayonining teskari ishlovi bo'lgan de-kapsulyatsiya jarayonini amalga oshiradi. Sarlavhalar qavatma-qavat o'chiriladi va oxir-oqibat B qurilmasi ma'lumotlarni o'qiy oladi.

Tarmoq modelida qatlamlar kerak, chunki har bir qatlam o'z mas'uliyatiga e'tibor qaratadi. Har bir qatlam ko'rsatmalarni qayta ishlash uchun sarlavhalarga tayanishi mumkin va oxirgi qatlamdagi ma'lumotlarning ma'nosini bilish shart emas.

### Nima uchun Nginx "teskari" proksi-server deb ataladi?

Quyidagi diagrammada 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐩𝐫𝐨𝐱𝐲 va 𝐫𝐞𝐯𝐞𝐫𝐬𝐞 𝐩𝐱𝐨 oʻrtasidagi farqlar koʻrsatilgan.

<p>
  <img src="../images/Forward Proxy v.s. Reverse Proxy2x.jpg" style="width: 720px" />
</p>

Oldinga proksi-server foydalanuvchi qurilmalari va internet o'rtasida joylashgan serverdir.

Proksi-server odatda quyidagilar uchun ishlatiladi:

1. Mijozlarni himoya qilish
2. Ko'rib chiqish cheklovlarini chetlab o'tish
3. Muayyan tarkibga kirishni bloklash

Teskari proksi-server mijozning so'rovini qabul qiladigan, so'rovni veb-serverlarga yo'naltiradigan va proksi-server so'rovni qayta ishlagandek natijalarni mijozga qaytaradigan serverdir.

Teskari proksi-server quyidagilar uchun mos keladi:

1. Serverlarni himoya qilish
2. Yukni muvozanatlash
3. Statik tarkibni keshlash
4. SSL aloqalarini shifrlash va shifrini ochish

### Umumiy yuklarni muvozanatlash algoritmlari qanday?

Quyidagi diagrammada 6 ta umumiy algoritm ko'rsatilgan.

<p>
  <img src="../images/lb-algorithms.jpg" />
</p>

- Statik Algoritmlar 

1. Aylanma o'yin(Round robin)

    Mijoz so'rovlari turli xil xizmat ko'rsatish instantsiyalariga ketma-ket tartibda yuboriladi. Xizmatlar odatda fuqaroligi bo'lmagan bo'lishi kerak.

2. Yopishqoq aylanma-robin (Sticky round-robin)

    Bu round-robin algoritmini takomillashtirishdir. Agar Elisning birinchi so'rovi A xizmatiga kirsa, keyingi so'rovlar ham A xizmatiga o'tadi. 

3. Og'irlangan aylanma-robin (Weighted round-robin)

    Administrator har bir xizmat uchun vaznni belgilashi mumkin. Og'irligi yuqori bo'lganlar boshqalarga qaraganda ko'proq so'rovlarni qabul qilishadi. 

4. Hesh

    Ushbu algoritm kiruvchi so'rovlarning IP yoki URL manzilida xesh funktsiyasini qo'llaydi. So'rovlar xesh funksiyasi natijasi asosida tegishli instansiyalarga yo'naltiriladi. 

- Dinamik Algoritmlar

5. Eng kam ulanishlar

    Eng kam parallel ulanishlar bilan xizmat ko'rsatish instantsiyasiga yangi so'rov yuboriladi. 

6. Eng kam javob vaqti

    Yangi so'rov eng tez javob vaqti bilan xizmat instantsiyasiga yuboriladi.

### URL, URI, URN - Farqlarni bilasizmi?

Quyidagi diagrammada URL, URI va URN solishtirish ko'rsatilgan. 

<p>
  <img src="../images/url-uri-urn.jpg" />
</p>

- URI 

URI yagona resurs identifikatorini (Uniform Resource Identifier) anglatadi. U internetdagi mantiqiy yoki jismoniy manbani aniqlaydi. URL va URN URI ning pastki turlaridir. URL manbani aniqlaydi, URN esa resurs nomini beradi.

URI quyidagi qismlardan iborat: 
scheme:[//authority]path[?query][#fragment] 

- URL 

URL HTTP ning asosiy tushunchasi bo'lgan Yagona Resurs Locator (Uniform Resource Locator) degan ma'noni anglatadi. Bu internetdagi noyob manbaning manzili. U FTP va JDBC kabi boshqa protokollar bilan ishlatilishi mumkin. 

- URN 

URN yagona manba nomini (Uniform Resource Name) anglatadi. U urn sxemasidan foydalanadi. Resursni topish uchun URN-lardan foydalanib bo'lmaydi. Diagrammada keltirilgan oddiy misol nomlar maydoni va nomlar maydoniga xos qatordan iborat.

Agar siz ushbu mavzu bo'yicha batafsil ma'lumot olishni istasangiz, men [W3C'ning tushuntirishini](https://www.w3.org/TR/uri-clarification/) tavsiya qilaman. 

## CI/CD

### CI/CD quvur liniyasi oddiy so'zlar bilan tushuntirilgan

<p>
  <img src="../images/ci-cd-pipeline.jpg" style="width: 680px" />
</p>

1-bo'lim - CI/CD bilan SDLC

Dasturiy ta'minotni ishlab chiqish hayotiy tsikli (SDLC) bir necha asosiy bosqichlardan iborat: ishlab chiqish, sinovdan o'tkazish, joylashtirish va texnik xizmat ko'rsatish. CI/CD tezroq va ishonchli relizlarni yoqish uchun ushbu bosqichlarni avtomatlashtiradi va birlashtiradi.

Kod git omboriga yuborilsa, u avtomatlashtirilgan qurish va sinov jarayonini ishga tushiradi. Kodni tekshirish uchun end-to-end (e2e) test holatlari ishga tushiriladi. Agar testlar muvaffaqiyatli o'tsa, kod avtomatik ravishda sahnalashtirish/ishlab chiqarishga o'rnatilishi mumkin. Muammolar aniqlansa, kod xatolarni tuzatish uchun ishlab chiqishga qaytariladi. Ushbu avtomatlashtirish ishlab chiquvchilarga tezkor javob beradi va ishlab chiqarishdagi xatolar xavfini kamaytiradi.

2-bo'lim - CI va CD o'rtasidagi farq

Uzluksiz integratsiya (CI) qurish, sinovdan o'tkazish va birlashtirish jarayonini avtomatlashtiradi. U integratsiya muammolarini erta aniqlash uchun kod so'ralganda testlarni o'tkazadi. Bu tez-tez kod topshirishni va tezkor fikr-mulohazalarni rag'batlantiradi.

Uzluksiz yetkazib berish (CD) infratuzilmani o'zgartirish va joylashtirish kabi reliz jarayonlarini avtomatlashtiradi. Bu dasturiy ta'minotni avtomatlashtirilgan ish oqimlari orqali istalgan vaqtda ishonchli tarzda chiqarishni ta'minlaydi. CD, shuningdek, ishlab chiqarishni joylashtirishdan oldin talab qilinadigan qo'lda sinov va tasdiqlash bosqichlarini avtomatlashtirishi mumkin.

3-bo'lim - CI/CD quvur liniyasi

Oddiy CI/CD quvur liniyasi bir nechta bog'langan bosqichlarga ega:
- Ishlab chiquvchi manba boshqaruviga kod o'zgarishlarini kiritadi
- CI server o'zgarishlarni aniqlaydi va qurilishni ishga tushiradi
- Kod tuzilgan va sinovdan o'tgan (birlik, integratsiya testlari)
- Sinov natijalari ishlab chiquvchiga xabar qilinadi
- Muvaffaqiyatga erishgandan so'ng, artefaktlar sahnalashtirish muhitiga joylashtiriladi
- Chiqarishdan oldin sahnalashtirishda qo'shimcha sinovlar o'tkazilishi mumkin
- CD tizimi ishlab chiqarishga tasdiqlangan o'zgarishlarni kiritadi

### Netflix Tech Stack (CI/CD Pipeline)

<p>
  <img src="../images/netflix-ci-cd.jpg" style="width: 720px" />
</p>

Rejalashtirish: Netflix Engineering rejalashtirish uchun JIRA va hujjatlar uchun Confluence-dan foydalanadi. 

Kodlash: Java backend xizmati uchun asosiy dasturlash tilidir, boshqa tillar esa turli xil foydalanish holatlari uchun ishlatiladi.

Build: Gradle asosan qurilish uchun ishlatiladi va Gradle plaginlari turli xil foydalanish holatlarini qo'llab-quvvatlash uchun qurilgan.

Qadoqlash: Paket va bog'liqliklar chiqarish uchun Amazon Machine Image (AMI) ichiga qadoqlangan. 

Sinov: Sinov ishlab chiqarish madaniyatining betartiblik vositalarini yaratishga qaratilganligini ta'kidlaydi.

Joylashtirish: Netflix kanareykalarni tarqatish uchun o'z-o'zidan ishlab chiqarilgan Spinnaker-dan foydalanadi.

Monitoring: Monitoring ko'rsatkichlari Atlasda markazlashtirilgan va Kayenta anomaliyalarni aniqlash uchun ishlatiladi.  

Voqea haqida hisobot: Hodisalar ustuvorlikka ko'ra jo'natiladi va PagerDuty hodisani hal qilish uchun ishlatiladi.

## Arxitektura naqshlari

### MVC, MVP, MVVM, MVVM-C va VIPER
Ushbu arxitektura naqshlari iOS yoki Android platformalarida ilovalarni ishlab chiqishda eng ko'p qo'llaniladi. Ishlab chiquvchilar ularni oldingi naqshlarning cheklovlarini yengish uchun taqdim etdilar. Xo'sh, ular qanday farq qiladi?

<p>
  <img src="../images/client arch patterns.png" style="width: 720px" />
</p>

- MVC, eng qadimgi naqsh deyarli 50 yil oldin paydo bo'lgan
- Har bir naqsh kontentni ko'rsatish va foydalanuvchi ma'lumotlarini qabul qilish uchun javobgar bo'lgan "ko'rinish" (V) ga ega
- Aksariyat naqshlar biznes ma'lumotlarini boshqarish uchun "model" (M) ni o'z ichiga oladi
- "Controller", "presenter" va "view-model" ko'rinish va model o'rtasida vositachilik qiluvchi tarjimonlardir (VIPER naqshidagi "obyekt")

### Har bir dasturchi bilishi kerak bo'lgan 18 ta asosiy dizayn naqshlari

Naqshlar umumiy dizayn muammolariga qayta foydalanish mumkin bo'lgan echimlar bo'lib, natijada yanada silliq va samaraliroq ishlab chiqish jarayoniga olib keladi. Ular yaxshi dasturiy tuzilmalarni yaratish uchun rejalar bo'lib xizmat qiladi. Bu eng mashhur naqshlardan ba'zilari: 

<p>
  <img src="../images/18-oo-patterns.png" />
</p>

- Abstract Factory: Family Creator - tegishli elementlar guruhlarini yaratadi. 
- Quruvchi: Lego Master - yaratilish va tashqi ko'rinishini alohida saqlagan holda ob'ektlarni bosqichma-bosqich quradi. 
- Prototip: Clone Maker - to'liq tayyorlangan misollarning nusxalarini yaratadi. 
- Singleton: One and Only - Faqat bitta misolga ega maxsus sinf. 
- Adapter: Universal Plug - turli interfeyslarga ega narsalarni ulaydi. 
- Ko'prik: Funktsiya ulagichi - ob'ekt qanday ishlashini u nima bilan bog'laydi. 
- Kompozit: Tree Builder - oddiy va murakkab qismlarning daraxtga o'xshash tuzilmalarini hosil qiladi. 
- Dekorator: moslashtiruvchi - ob'ektlarning asosiy qismini o'zgartirmasdan ularga xususiyatlar qo'shadi. 
- Fasad: Yagona oyna - yagona, soddalashtirilgan interfeysga ega butun tizimni ifodalaydi. 
- Flyweight: Space Saver - kichik, qayta foydalanish mumkin bo'lgan narsalarni samarali taqsimlaydi. 
- Proksi: Stand-In Actor - kirish yoki harakatlarni boshqaradigan boshqa ob'ektni ifodalaydi. 
- Mas'uliyat zanjiri: so'rov o'tkazmasi - so'rovni ko'rib chiqilgunga qadar ob'ektlar zanjiri orqali o'tkazadi. 
- Buyruq: Task Wrapper - so'rovni harakatga tayyor ob'ektga aylantiradi. 
- Iterator: Collection Explorer - To'plamdagi elementlarga birma-bir murojaat qiladi. 
- Mediator: Communication Hub - turli sinflar o'rtasidagi o'zaro aloqalarni soddalashtiradi. 
- Yodgorlik: Vaqt kapsulasi - ob'ekt holatini suratga oladi va tiklaydi. 
- Observer: News Broadcaster - boshqa ob'ektlardagi o'zgarishlar haqida sinflarni xabardor qiladi. 
- Mehmon: Mohir mehmon - sinfni o'zgartirmasdan unga yangi operatsiyalar qo'shadi.

## Ma'lumotlar bazasi

### Bulutli xizmatlardagi turli xil ma'lumotlar bazalarining chiroyli cheat varag'i

<p>
  <img src="../images/cloud-dbs2.png" />
</p>

Loyihangiz uchun to'g'ri ma'lumotlar bazasini tanlash murakkab vazifadir. Har biri alohida foydalanish holatlariga mos keladigan ko'plab ma'lumotlar bazasi variantlari tezda qaror qabul qilishning charchashiga olib kelishi mumkin. 

Umid qilamizki, ushbu hiyla varaqasi loyihangiz ehtiyojlariga mos keladigan to'g'ri xizmatni aniqlash va yuzaga kelishi mumkin bo'lgan tuzoqlardan qochish uchun yuqori darajadagi yo'nalish beradi.

Eslatma: Google maʼlumotlar bazasidan foydalanish holatlari uchun cheklangan hujjatlarga ega. Garchi biz mavjud bo'lgan narsalarni ko'rib chiqish va eng yaxshi variantni topish uchun qo'limizdan kelganini qilgan bo'lsak ham, ba'zi yozuvlar aniqroq bo'lishi kerak bo'lishi mumkin. 

### Ma'lumotlar bazalaringizni quvvatlantiradigan 8 ta ma'lumotlar tuzilmasi

Javob sizning foydalanish holatingizga qarab farq qiladi. Ma'lumotlar xotirada yoki diskda indekslanishi mumkin. Xuddi shunday, ma'lumotlar formatlari ham farqlanadi, masalan, raqamlar, satrlar, geografik koordinatalar va boshqalar. Tizim og'ir yozish yoki o'qish uchun og'ir bo'lishi mumkin. Bu omillarning barchasi ma'lumotlar bazasi indeksi formatini tanlashga ta'sir qiladi.

<p>
  <img src="../images/8-ds-db.jpg" />
</p>

Quyida ma'lumotlarni indekslash uchun ishlatiladigan eng mashhur ma'lumotlar tuzilmalari keltirilgan:

- Skiplist: umumiy xotiradagi indeks turi. Redisda ishlatiladi
- Xesh indeksi: "Xarita" ma'lumotlar strukturasining (yoki "To'plam") juda keng tarqalgan qo'llanilishi.
- SSTable: o'zgarmas diskda "Xarita" ni amalga oshirish
- LSM daraxti: Skiplist + SSTable. Yuqori yozish qobiliyati
- B-daraxt: diskga asoslangan yechim. Doimiy o'qish/yozish samaradorligi 
- Inverted indeks: hujjatlarni indekslash uchun ishlatiladi. Lucenda ishlatiladi
- Suffiks daraxti: qator namunalarini qidirish uchun
- R-daraxt: ko'p o'lchovli qidiruv, masalan, eng yaqin qo'shnini topish 

### Ma'lumotlar bazasida SQL operatori qanday bajariladi?

Quyidagi diagrammada jarayon ko'rsatilgan. E'tibor bering, turli xil ma'lumotlar bazalari uchun arxitekturalar har xil, diagrammada ba'zi umumiy dizaynlar ko'rsatilgan.

<p>
  <img src="../images/sql execution order in db.jpeg" style="width: 580px" />
</p>


1-qadam - SQL bayonoti ma'lumotlar bazasiga transport qatlami protokoli (masalan, TCP) orqali yuboriladi.

2-qadam - SQL bayonoti buyruq tahlilchisiga yuboriladi, u erda sintaktik va semantik tahlildan o'tadi va keyin so'rovlar daraxti hosil bo'ladi.

3-qadam - so'rovlar daraxti optimallashtiruvchiga yuboriladi. Optimallashtiruvchi ijro rejasini yaratadi.

4-bosqich - ijro rejasi ijrochiga yuboriladi. Ijrochi ijrodan ma'lumotlarni oladi.

5-qadam - Kirish usullari bajarish uchun zarur bo'lgan ma'lumotlarni olish mantiqini ta'minlaydi, ma'lumotlarni saqlash mexanizmidan oladi.

6-qadam - Kirish usullari SQL bayonotining faqat o'qish uchun ekanligini hal qiladi. Agar so'rov faqat o'qish uchun bo'lsa (SELECT iborasi), u keyingi ishlov berish uchun bufer menejeriga uzatiladi. Bufer menejeri kesh yoki ma'lumotlar fayllaridagi ma'lumotlarni qidiradi.

7-qadam - Agar bayonot UPDATE yoki INSERT bo'lsa, u keyingi qayta ishlash uchun tranzaksiya menejeriga uzatiladi.

8-qadam - Tranzaksiya paytida ma'lumotlar blokirovka rejimida. Bu qulflash menejeri tomonidan kafolatlanadi. Shuningdek, u tranzaksiyaning ACID xususiyatlarini ta'minlaydi. 

###  CAP teoremasi

CAP teoremasi kompyuter fanidagi eng mashhur atamalardan biridir, ammo men turli ishlab chiquvchilar turli xil tushunchalarga ega ekanligiga aminman. Keling, bu nima ekanligini va nima uchun bu chalkash bo'lishi mumkinligini ko'rib chiqaylik.

<p>
  <img src="../images/cap theorem.jpeg" />
</p>

CAP teoremasi taqsimlangan tizim bir vaqtning o'zida ushbu uchta kafolatdan ikkitadan ko'pini ta'minlay olmasligini bildiradi.

**Muvofiqlik**: izchillik barcha mijozlar qaysi tugunga ulanishidan qat'i nazar, bir vaqtning o'zida bir xil ma'lumotlarni ko'rishini anglatadi.

**Mavjudlik**: mavjudlik degani, ma'lumotlarni so'ragan har qanday mijoz, hatto ba'zi tugunlar ishlamay qolgan bo'lsa ham, javob oladi.

**Bo'limga tolerantlik**: bo'lim ikki tugun o'rtasidagi aloqa uzilishini bildiradi. Bo'limga tolerantlik tizim tarmoq bo'limlariga qaramay ishlashda davom etishini anglatadi.

"2 dan 3" formulasi foydali bo'lishi mumkin, **ammo bu soddalashtirish noto'g'ri bo'lishi mumkin**.

1. Ma'lumotlar bazasini tanlash oson emas. Bizning tanlovimizni faqat CAP teoremasi asosida asoslash etarli emas. Masalan, kompaniyalar AP tizimi bo'lgani uchun chat ilovalari uchun Cassandrani tanlamaydi.Cassandrani chat xabarlarini saqlash uchun kerakli variantga aylantiradigan yaxshi xususiyatlar ro'yxati mavjud. Biz chuqurroq qazishimiz kerak.

2. "CAP dizayn maydonining faqat kichik bir qismini taqiqlaydi: kamdan-kam uchraydigan qismlar mavjud bo'lganda mukammal mavjudlik va mustahkamlik". Maqoladan iqtibos: O'n ikki yil o'tib CAP: "Qoidalar" qanday o'zgargan.

3. Teorema taxminan 100% mavjudlik va izchillikdir. Tarmoq bo'limi bo'lmaganda kechikish va izchillik o'rtasidagi kelishuv yanada realroq muhokama bo'ladi. Batafsil ma'lumot uchun PACELC teoremasiga qarang.

**CAP teoremasi haqiqatan ham foydalimi?**

O'ylaymanki, bu hali ham foydali, chunki u bizning fikrimizni bir qator munozaralar uchun ochadi, ammo bu hikoyaning faqat bir qismi. To'g'ri ma'lumotlar bazasini tanlashda biz chuqurroq qazishimiz kerak.

### Xotira va saqlash turlari

<p>
  <img src="../images/Types_of_Memory_and_Storage.jpeg" style="width: 420px" />
</p>


### SQL so'rovini vizualizatsiya qilish

<p>
  <img src="../images/sql-execution-order.jpg" style="width: 580px" />
</p>

SQL bayonotlari ma'lumotlar bazasi tizimi tomonidan bir necha bosqichda amalga oshiriladi, jumladan: 

- SQL bayonotini tahlil qilish va uning haqiqiyligini tekshirish 
- SQLni relyatsion algebra kabi ichki tasvirga aylantirish
- Ichki vakillikni optimallashtirish va indeks ma'lumotlaridan foydalanadigan ijro rejasini yaratish
- Rejani bajarish va natijalarni qaytarish

SQL-ni bajarish juda murakkab va ko'plab fikrlarni o'z ichiga oladi, masalan:

- Indekslar va keshlardan foydalanish 
- Jadvalni birlashtirish tartibi 
- Parametrlarni nazorat qilish 
- Tranzaksiyalarni boshqarish

### SQL tili

1986 yilda SQL (Structured Query Language) standartga aylandi. Keyingi 40 yil ichida u relyatsion ma'lumotlar bazasini boshqarish tizimlari uchun dominant tilga aylandi. Eng so'nggi standartni (ANSI SQL 2016) o'qish ko'p vaqt talab qilishi mumkin. Uni qanday o'rganishim mumkin?

<p>
  <img src="../images/how-to-learn-sql.jpg" />
</p>

SQL tilining 5 ta komponenti mavjud:

- DDL: CREATE, ALTER, DROP kabi ma'lumotlarni aniqlash tili
- DQL: ma'lumotlar so'rovi tili, masalan, SELECT
- DML: INSERT, UPDATE, DELETE kabi ma'lumotlarni manipulyatsiya qilish tili 
- DCL: ma'lumotlarni boshqarish tili, masalan, GRANT, REVOKE
- TCL: COMMIT, ROLLBACK kabi tranzaktsiyalarni boshqarish tili

Backend muhandisi uchun siz uning ko'p qismini bilishingiz kerak bo'lishi mumkin. Ma'lumotlar tahlilchisi sifatida siz DQL haqida yaxshi tushunchaga ega bo'lishingiz kerak bo'lishi mumkin. Sizga eng mos keladigan mavzularni tanlang.

## Kesh

### Ma'lumotlar hamma joyda keshlangan

Ushbu diagramma odatiy arxitekturada ma'lumotlarni keshlash joyini ko'rsatadi.

<p>
  <img src="../images/where do we cache data.jpeg" style="width: 720px" />
</p>


Oqim bo'ylab **bir nechta qatlamlar** mavjud.

1. Mijoz ilovalari: HTTP javoblari brauzer tomonidan keshlanishi mumkin. Biz HTTP orqali birinchi marta maʼlumot soʻrayapmiz va ular HTTP sarlavhasida amal qilish muddati siyosati bilan qaytariladi; biz yana ma'lumotlarni so'raymiz va mijoz ilovasi avval brauzer keshidan ma'lumotlarni olishga harakat qiladi.
2. CDN: CDN statik veb-resurslarni keshlaydi. Mijozlar yaqin atrofdagi CDN tugunidan ma'lumotlarni olishlari mumkin.
3. Load Balancer: Load Balancer resurslarni ham keshlashi mumkin.
4. Xabarlar infratuzilmasi: Xabar brokerlari xabarlarni avval diskda saqlaydi va keyin iste'molchilar ularni o'z tezligida oladilar. Saqlash siyosatiga qarab, ma'lumotlar ma'lum vaqt davomida Kafka klasterlarida keshlanadi.
5. Xizmatlar: Xizmatda keshning bir nechta qatlamlari mavjud. Agar ma'lumotlar CPU keshida keshlanmagan bo'lsa, xizmat ma'lumotlarni xotiradan olishga harakat qiladi. Ba'zan xizmatda ma'lumotlarni diskda saqlash uchun ikkinchi darajali kesh mavjud.
6. Taqsimlangan kesh: Redis kabi taqsimlangan kesh xotirada bir nechta xizmatlar uchun kalit-qiymat juftlarini saqlaydi. Bu ma'lumotlar bazasiga qaraganda ancha yaxshi o'qish/yozish unumdorligini ta'minlaydi.
7. To'liq matnli qidiruv: biz ba'zan hujjat qidirish yoki jurnaldan qidirish uchun Elastik qidiruv kabi to'liq matnli qidiruvlardan foydalanishimiz kerak. Ma'lumotlarning nusxasi qidiruv tizimida ham indekslanadi.
8. Ma'lumotlar bazasi: Hatto ma'lumotlar bazasida ham bizda turli darajadagi keshlar mavjud:
- WAL (Oldindan yozish jurnali): ma'lumotlar B daraxti indeksini yaratishdan oldin WAL-ga yoziladi
- Bufferpool: Kesh so'rovi natijalari uchun ajratilgan xotira maydoni
- Materiallashtirilgan ko'rinish: so'rov natijalarini oldindan hisoblab chiqing va so'rovlar yaxshi ishlashi uchun ularni ma'lumotlar bazasi jadvallarida saqlang
- Tranzaksiya jurnali: barcha tranzaktsiyalar va ma'lumotlar bazasi yangilanishlarini yozib oling
- Replikatsiya jurnali: ma'lumotlar bazasi klasterida replikatsiya holatini yozish uchun ishlatiladi

### Nima uchun Redis juda tez?

Quyidagi diagrammada ko'rsatilgandek 3 ta asosiy sabab bor.

<p>
  <img src="../images/why_redis_fast.jpeg" />
</p>


1. Redis - bu RAMga asoslangan ma'lumotlar do'koni. RAMga kirish tasodifiy diskdan foydalanishdan kamida 1000 marta tezroq.
2. Redis ijro samaradorligi uchun IO multiplekslash va bitta torli bajarish siklidan foydalanadi.
3. Redis bir nechta samarali quyi darajadagi ma'lumotlar tuzilmalaridan foydalanadi.

Savol: Yana bir mashhur xotira do'koni - Memcached. Redis va Memcached o'rtasidagi farqni bilasizmi?

Siz ushbu diagrammaning uslubi oldingi postlarimdan farq qilganini payqagan bo'lishingiz mumkin. Iltimos, qaysi birini afzal ko'rishingizni menga xabar bering.

### Redisdan qanday foydalanish mumkin?

<p>
  <img src="../images/top-redis-use-cases.jpg" style="width: 520px" />
</p>


Redisda keshlashdan ko'ra ko'proq narsa bor.

Diagrammada ko'rsatilganidek, Redis turli stsenariylarda ishlatilishi mumkin.

- Sessiya 

  Biz Redisdan foydalanuvchi sessiyasi ma'lumotlarini turli xizmatlar o'rtasida almashish uchun foydalanishimiz mumkin. 

- Kesh  

  Ob'ektlar yoki sahifalarni keshlash uchun Redis-dan foydalanishimiz mumkin, ayniqsa hotspot ma'lumotlari uchun. 

- Tarqalgan qulf  

  Tarqatilgan xizmatlar orasida qulflarni olish uchun Redis qatoridan foydalanishimiz mumkin. 

- Hisoblagich  

  Biz maqolalar uchun qancha yoqtirish yoki qancha o'qishni hisoblashimiz mumkin. 

- Tarif cheklovchisi  

  Biz ma'lum foydalanuvchi IP-lari uchun tarif cheklovchisini qo'llashimiz mumkin. 

- Global ID generator 

  Global ID uchun Redis Int dan foydalanishimiz mumkin. 

- Xarid savati  

  Xarid qilish savatidagi kalit-qiymat juftligini ko'rsatish uchun Redis Hash-dan foydalanishimiz mumkin. 

- Foydalanuvchini ushlab turishni hisoblash 

  Bitmap-dan foydalanuvchi loginini har kuni ko'rsatish va foydalanuvchini ushlab turishini hisoblash uchun foydalanishimiz mumkin. 

- Xabar navbati 

  Biz xabarlar navbati uchun List-dan foydalanishimiz mumkin 

- Reyting 

  Maqolalarni saralash uchun ZSet dan foydalanishimiz mumkin.

### Eng yaxshi keshlash strategiyalari

Katta miqyosli tizimlarni loyihalash odatda keshlashni diqqat bilan ko'rib chiqishni talab qiladi. Quyida tez-tez ishlatiladigan beshta keshlash strategiyasi keltirilgan. 

<p>
  <img src="../images/top_caching_strategy.jpeg" style="width: 680px" />
</p>



## Mikroservis arxitekturasi

### Oddiy mikroservis arxitekturasi nimaga o'xshaydi? 

<p>
  <img src="../images/typical-microservice-arch.jpg" style="width: 520px" />
</p>


Quyidagi diagrammada mikroservisning odatiy arxitekturasi ko'rsatilgan.

- Load Balancer: Bu kiruvchi trafikni bir nechta backend xizmatlariga taqsimlaydi.
- CDN (Content Delivery Network): CDN bu tezroq yetkazib berish uchun statik tarkibga ega bo'lgan geografik taqsimlangan serverlar guruhidir. Mijozlar avval CDN-da tarkibni qidiradi, keyin esa backend xizmatlariga o'tadi.
- API Gateway: Bu kiruvchi so'rovlarni ko'rib chiqadi va ularni tegishli xizmatlarga yo'naltiradi. U identifikatsiya provayderi va xizmat kashfiyoti bilan gaplashadi.
- Identifikatsiya provayderi: Bu foydalanuvchilar uchun autentifikatsiya va avtorizatsiya bilan shug'ullanadi. 
- Xizmat reestri va kashfiyot: Mikroservisni ro'yxatdan o'tkazish va ochish ushbu komponentda sodir bo'ladi va API shlyuzi suhbatlashish uchun ushbu komponentda tegishli xizmatlarni qidiradi. 
- Boshqaruv: Ushbu komponent xizmatlarni kuzatish uchun javobgardir.
- Mikroservislar: Mikroservislar turli sohalarda ishlab chiqilgan va joylashtirilgan. Har bir domen o'z ma'lumotlar bazasiga ega. API shlyuzi REST API yoki boshqa protokollar orqali mikroservislar bilan gaplashadi va bir domendagi mikroservislar RPC (Remote Procedure Call) yordamida bir-biri bilan gaplashadi.

Mikroservislarning afzalliklari:

- Ular tezda ishlab chiqilishi, joylashtirilishi va gorizontal ravishda o'lchanishi mumkin.
- Har bir domen maxsus guruh tomonidan mustaqil ravishda saqlanishi mumkin.
- Biznes talablari har bir domenda moslashtirilishi va natijada yaxshiroq qo'llab-quvvatlanishi mumkin.

### Mikroservisning eng yaxshi amaliyotlari

Rasm ming so'zga arziydi: mikroservislarni ishlab chiqish bo'yicha 9 ta eng yaxshi amaliyot.

<p>
  <img src="../images/microservice-best-practices.jpeg" />
</p>

 
Mikroservislarni ishlab chiqishda biz quyidagi eng yaxshi amaliyotlarga amal qilishimiz kerak: 

1. Har bir mikroxizmat uchun alohida maʼlumotlarni saqlashdan foydalaning  
2. Kodni xuddi shunday etuklik darajasida saqlang 
3. Har bir mikroservis uchun alohida tuzilma  
4. Har bir mikroxizmatni bitta mas'uliyat bilan tayinlang responsibility 
5. Konteynerlarga joylashtiring 
6. Fuqaroligi bo'lmagan xizmatlarni loyihalash 
7. Domenga asoslangan dizaynni qabul qiling
8. Mikro frontendni loyihalash
9. Mikroservislarni tashkil qilish

### Mikroservislar uchun qanday texnologik stek ishlatiladi?

Quyida siz mikroservis texnologiyalari stekini ishlab chiqish bosqichida ham, ishlab chiqarishda ham ko'rsatadigan diagrammani topasiz.

<p>
  <img src="../images/microservice-tech.jpeg" />
</p>


▶️ 𝐏𝐫𝐞-𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧

- Define API - Bu frontend va backend o'rtasida shartnoma o'rnatadi. Buning uchun Postman yoki OpenAPI dan foydalanishimiz mumkin.
- Ishlab chiqish - Node.js yoki react frontend ishlab chiqish uchun, java/python/go esa backend ishlab chiqish uchun mashhur. Bundan tashqari, API ta'riflariga muvofiq API shlyuzidagi konfiguratsiyalarni o'zgartirishimiz kerak.
- Uzluksiz integratsiya - avtomatlashtirilgan sinov uchun JUnit va Jenkins. Kod Docker tasviriga qadoqlangan va mikroservislar sifatida joylashtirilgan.

▶️ 𝐏𝐫𝐨𝐝𝐮𝐜𝐭𝐢𝐨𝐧

- NGinx yuk balanslagichlari uchun keng tarqalgan tanlovdir. Cloudflare CDN (Content Delivery Network) bilan ta'minlaydi. 
- API Gateway - Biz shlyuz uchun bahor yuklashdan foydalanishimiz mumkin va xizmatni aniqlash uchun Eureka/Zookeeper dan foydalanishimiz mumkin.
- Mikroservislar bulutlarda joylashtirilgan. Bizda AWS, Microsoft Azure yoki Google GCP orasida variantlar mavjud. Kesh va to'liq matnli qidiruv - Redis kalit-qiymat juftlarini keshlash uchun keng tarqalgan tanlovdir. Elasticsearch to'liq matnli qidiruv uchun ishlatiladi.
- Aloqa - xizmatlar bir-biri bilan gaplashishi uchun biz xabar almashish infra Kafka yoki RPC dan foydalanishimiz mumkin.
- Qat'iylik - Biz aloqador ma'lumotlar bazasi uchun MySQL yoki PostgreSQL va ob'ektlarni saqlash uchun Amazon S3 dan foydalanishimiz mumkin. Agar kerak bo'lsa, biz Cassandra-dan keng ustunli do'kon uchun ham foydalanishimiz mumkin.
- Boshqaruv va monitoring - Ko'plab mikroservislarni boshqarish uchun umumiy Ops vositalariga Prometey, Elastic Stack va Kubernetes kiradi.

### Nega Kafka tez

Kafkaning ishlashiga hissa qo'shgan ko'plab dizayn qarorlari mavjud. Ushbu postda biz ikkitasiga e'tibor qaratamiz. Bizning fikrimizcha, bu ikkisi eng ko'p og'irlikni ko'targan.

<p>
  <img src="../images/why_is_kafka_fast.jpeg" />
</p>

1. Birinchisi, Kafkaning Sequential I/U-ga tayanishi.
2. Kafkaning ishlash ustunligini ta'minlaydigan ikkinchi dizayn tanlovi - bu samaradorlikka e'tibor: nol nusxa ko'chirish printsipi.
 
Diagrammada ma'lumotlar ishlab chiqaruvchi va iste'molchi o'rtasida qanday uzatilishi va nol nusxasi nimani anglatishini ko'rsatadi.
 
- 1.1 - 1.3-qadam: Ishlab chiqaruvchi diskka ma'lumotlarni yozadi
- 2-qadam: Iste'molchi ma'lumotlarni nol nusxasiz o'qiydi

2.1 Ma'lumotlar diskdan OS keshiga yuklanadi

2.2 Ma'lumotlar OT keshidan Kafka ilovasiga ko'chiriladi

2.3 Kafka ilovasi ma'lumotlarni rozetka buferiga ko'chiradi

2.4 Ma'lumotlar soket buferidan tarmoq kartasiga ko'chiriladi

2.5 Tarmoq kartasi ma'lumotlarni iste'molchiga yuboradi

- 3-qadam: Iste'molchi ma'lumotlarni nol nusxada o'qiydi

3.1: Ma'lumotlar diskdan OS keshiga yuklanadi

3.2 OT keshi ma'lumotlarni sendfile() buyrug'i orqali to'g'ridan-to'g'ri tarmoq kartasiga ko'chiradi 

3.3 Tarmoq kartasi ma'lumotlarni iste'molchiga yuboradi
 
Nolinchi nusxa - dastur konteksti va yadro konteksti o'rtasida bir nechta ma'lumotlar nusxalarini saqlash uchun yorliq.

## To'lov tizimlari

### To'lov tizimini qanday o'rganish mumkin?

<p>
  <img src="../images/learn-payments.jpg" />
</p>

###  Nima uchun kredit karta "banklardagi eng daromadli mahsulot" deb ataladi? VISA/Mastercard qanday qilib pul ishlaydi? 

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

### Savdogarlar do'konida kredit kartani o'tkazganimizda VISA qanday ishlaydi?

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

### Dunyo bo'ylab to'lov tizimlari seriyasi (1-qism): Hindistonda yagona to'lov interfeysi (UPI)


What’s UPI? UPI is an instant real-time payment system developed by the National Payments Corporation of India.

It accounts for 60% of digital retail transactions in India today.

UPI = payment markup language + standard for interoperable payments


<p>
  <img src="../images/how-does-upi-work.png"  style="width: 600px" />
</p>


## DevOps

###  DevOps va SRE va platforma muhandisligi. Farqi nimada?

The concepts of DevOps, SRE, and Platform Engineering have emerged at different times and have been developed by various individuals and organizations. 

<p>
  <img src="../images/devops-sre-platform.jpg" />
</p>

DevOps as a concept was introduced in 2009 by Patrick Debois and Andrew Shafer at the Agile conference. They sought to bridge the gap between software development and operations by promoting a collaborative culture and shared responsibility for the entire software development lifecycle. 

SRE, or Site Reliability Engineering, was pioneered by Google in the early 2000s to address operational challenges in managing large-scale, complex systems. Google developed SRE practices and tools, such as the Borg cluster management system and the Monarch monitoring system, to improve the reliability and efficiency of their services. 

Platform Engineering is a more recent concept, building on the foundation of SRE engineering. The precise origins of Platform Engineering are less clear, but it is generally understood to be an extension of the DevOps and SRE practices, with a focus on delivering a comprehensive platform for product development that supports the entire business perspective. 

It's worth noting that while these concepts emerged at different times. They are all related to the broader trend of improving collaboration, automation, and efficiency in software development and operations. 

### K8s (Kubernetes) nima?

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

### Docker va Kubernetes. Qaysi birini ishlatishimiz kerak?

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

### Docker qanday ishlaydi?

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

### Git buyruqlari qanday ishlaydi

To begin with, it's essential to identify where our code is stored. The common assumption is that there are only two locations - one on a remote server like Github and the other on our local machine. However, this isn't entirely accurate. Git maintains three local storages on our machine, which means that our code can be found in four places: 

<p>
  <img src="../images/git-commands.png" style="width: 600px" />
</p>


- Working directory: where we edit files 
- Staging area: a temporary location where files are kept for the next commit 
- Local repository: contains the code that has been committed 
- Remote repository: the remote server that stores the code 

Most Git commands primarily move files between these four locations. 

### Git qanday ishlaydi?

The diagram below shows the Git workflow. 

<p>
  <img src="../images/git-workflow.jpeg" style="width: 520px" />
</p>


Git is a distributed version control system. 

Every developer maintains a local copy of the main repository and edits and commits to the local copy. 

The commit is very fast because the operation doesn’t interact with the remote repository. 

If the remote repository crashes, the files can be recovered from the local repositories. 

### Git merge va Git rebase]

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

## Bulutli xizmatlar

### Turli xil bulut xizmatlarining chiroyli cheat varag'i (2023 yil nashri)

<p>
  <img src="../images/cloud-compare.jpg" />
</p>


### Mahalliy bulut nima?

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

## Ishlab chiquvchi mahsuldorlik vositalari

### JSON fayllarini vizualizatsiya qilish

Nested JSON files are hard to read.

**JsonCrack** generates graph diagrams from JSON files and makes them easy to read.

Additionally, the generated diagrams can be downloaded as images.

<p>
  <img src="../images/json-cracker.jpeg" />
</p>


### Kodni avtomatik ravishda arxitektura diagrammalariga aylantiring

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

### Linux fayl tizimi tushuntirildi

<p>
  <img src="../images/linux-file-systems.jpg" style="width: 680px" />
</p>

The Linux file system used to resemble an unorganized town where individuals constructed their houses wherever they pleased. However, in 1994, the Filesystem Hierarchy Standard (FHS) was introduced to bring order to the Linux file system.

By implementing a standard like the FHS, software can ensure a consistent layout across various Linux distributions. Nonetheless, not all Linux distributions strictly adhere to this standard. They often incorporate their own unique elements or cater to specific requirements.
To become proficient in this standard, you can begin by exploring. Utilize commands such as "cd" for navigation and "ls" for listing directory contents. Imagine the file system as a tree, starting from the root (/). With time, it will become second nature to you, transforming you into a skilled Linux administrator.

### Siz bilishingiz kerak bo'lgan 18 ta eng ko'p ishlatiladigan Linux buyruqlari

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

## Xavfsizlik

### HTTPS qanday ishlaydi?

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

### Oauth 2.0 oddiy shartlar bilan tushuntirilgan.

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

### Autentifikatsiya mexanizmlarining 4 ta eng yaxshi shakllari

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

### Sessiya, cookie, JWT, token, SSO va OAuth 2.0 - ular nima?

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

### Ma'lumotlar bazasida parollarni qanday xavfsiz saqlash va parolni qanday tekshirish mumkin?

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

### 10 yoshli bolaga JSON Web Token (JWT) haqida tushuntirish

<p>
  <img src="../images/jwt.jpg" />
</p>

Imagine you have a special box called a JWT. Inside this box, there are three parts: a header, a payload, and a signature.

The header is like the label on the outside of the box. It tells us what type of box it is and how it's secured. It's usually written in a format called JSON, which is just a way to organize information using curly braces { } and colons : .

The payload is like the actual message or information you want to send. It could be your name, age, or any other data you want to share. It's also written in JSON format, so it's easy to understand and work with.
Now, the signature is what makes the JWT secure. It's like a special seal that only the sender knows how to create. The signature is created using a secret code, kind of like a password. This signature ensures that nobody can tamper with the contents of the JWT without the sender knowing about it.

When you want to send the JWT to a server, you put the header, payload, and signature inside the box. Then you send it over to the server. The server can easily read the header and payload to understand who you are and what you want to do.

### Google Authenticator (yoki 2 faktorli autentifikatsiyaning boshqa turlari) qanday ishlaydi?

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


##  Haqiqiy dunyo misollari

### Netflixning Tech Stacki

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

### Twitter arxitekturasi 2022

Yes, this is the real Twitter architecture. It is posted by Elon Musk and redrawn by us for better readability. 

<p>
  <img src="../images/twitter-arch.jpeg" />
</p>


### Oxirgi 15 yil ichida Airbnb mikroservis arxitekturasining evolyutsiyasi

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

### Monorepo va mikrorepo.

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
Google engineers built Bazel, and Meta built Buck. There are other open-source tools available, including Nix, Lerna, and others. 

Over the years, Microrepo has had more supported tools, including Maven and Gradle for Java, NPM for NodeJS, and CMake for C/C++, among others. 

### Stack Overflow veb-saytini qanday loyihalashtirasiz?

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

### Nima uchun Amazon Prime Video monitoringi serversizdan monolitga o'tdi? Qanday qilib 90% xarajatlarni tejash mumkin?

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

### Disney Hotstar turnir davomida 5 milliard kulgichni qanday suratga oladi?

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

### Discord qanday qilib trillionlab xabarlarni saqlaydi?

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

### YouTube, TikTok live yoki Twitch-da jonli video oqimlari qanday ishlaydi?
 
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
