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

  Real vaqtda, ikki tomonlama, doimiy ulanishlar

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

Webhuklar ko'pincha teskari API yoki push API deb ataladi, chunki server mijozga HTTP so'rovlarini yuboradi. Webhukdan foydalanishda 3 narsaga e'tibor qaratishimiz kerak:

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

Kod yozishdan oldin API dizaynini tasdiqlash uchun so'rovlar va javoblarni haqiqiy bo'lmagan xomaki qilishimiz mumkin.

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

Quyidagi diagrammada 𝐟𝐨𝐫𝐰𝐚𝐫𝐝 𝐩𝐫𝐨𝐱𝐲 va 𝐫𝐞𝐯𝐞𝐫𝐬𝐞 𝐩𝐫𝐨𝐱𝐲 oʻrtasidagi farqlar koʻrsatilgan.

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

Quyidagi diagrammada kredit karta to'lovlari oqimining iqtisodiyoti ko'rsatilgan.

<p>
  <img src="../images/how does visa makes money.jpg" style="width: 640px" />
</p>

1.&nbsp;&nbsp;Karta egasi mahsulot sotib olish uchun savdogarga 100 dollar to'laydi.

2.&nbsp;Savdogar yuqori savdo hajmiga ega kredit kartasidan foydalanishdan foyda oladi va to'lov xizmatini taqdim etganlik uchun emitent va karta tarmog'iga kompensatsiya to'lashi kerak. Qabul qiluvchi bank savdogardan "savdogar chegirma to'lovi" deb nomlangan to'lovni belgilaydi.

3 - 4.  Ekvaying bank ekvayring ustamasi sifatida 0,25 AQSh dollarini ushlab turadi va 1,75 AQSh dollari almashuv komissiyasi sifatida emitent bankka to'lanadi. Savdogar chegirma to'lovi almashinuv to'lovini qoplashi kerak.

O'zaro almashish to'lovi karta tarmog'i tomonidan belgilanadi, chunki har bir emitent bank uchun har bir savdogar bilan to'lovlarni kelishib olish unchalik samarali emas.

5.&nbsp;&nbsp;Karta tarmogʻi har bir bank bilan tarmoqni baholash va toʻlovlarni oʻrnatadi, u har oy karta tarmogʻiga oʻz xizmatlari uchun toʻlaydi. Masalan, VISA har bir surish uchun 0,11% baho va 0,0195 AQSh dollari miqdorida foydalanish to'lovini oladi.

6.&nbsp;&nbsp;Karta egasi emitent bankka xizmatlari uchun to'laydi.

Nima uchun emitent bank kompensatsiya to'lashi kerak?

- Emitent karta egasi emitentga to'lamagan taqdirda ham savdogarga to'laydi. 
- Emitent karta egasi emitentga to'lashdan oldin savdogarga to'laydi.
- Emitent boshqa operatsion xarajatlarga ega, jumladan, mijozlar hisoblarini boshqarish, hisobotlarni taqdim etish, firibgarlikni aniqlash, risklarni boshqarish, kliring va hisob-kitoblar va boshqalar.

### Savdogarlar do'konida kredit kartani o'tkazganimizda VISA qanday ishlaydi?

<p>
  <img src="../images/visa_payment.jpeg" />
</p>


VISA, Mastercard va American Express pul mablag'larini kliring va hisob-kitob qilish uchun karta tarmoqlari sifatida ishlaydi. Kartani qabul qiluvchi bank va kartani emitent banki har xil bo'lishi mumkin va ko'pincha bir-biridan farq qiladi. Agar banklar birin-ketin hisob-kitoblarni vositachisiz amalga oshirsalar, har bir bank boshqa barcha banklar bilan hisob-kitob qilishlari kerak edi. Bu juda samarasiz. 
 
Quyidagi diagrammada VISA ning kredit karta bilan to'lov jarayonidagi roli ko'rsatilgan. Ikkita oqim ishtirok etadi. Avtorizatsiya oqimi mijoz kredit kartasini surish paytida sodir bo'ladi. Qo'lga olish va hisob-kitoblar oqimi savdogar kunning oxirida pul olishni xohlasa sodir bo'ladi.
 
- Avtorizatsiya oqimi

0-qadam: Kartani chiqaruvchi bank o'z mijozlariga kredit kartalarini chiqaradi.
 
1-qadam: Karta egasi mahsulot sotib olmoqchi va kredit kartani sotuvchining do'konidagi Savdo nuqtasi (POS) terminalida suradi.
 
2-qadam: POS-terminal tranzaktsiyani POS-terminalni taqdim etgan ekvaying bankka yuboradi.
 
3 va 4-qadamlar: Ekvaying bank tranzaktsiyani kartalar tarmog'iga yuboradi, shuningdek, karta sxemasi deb ataladi. Karta tarmog'i tranzaksiyani tasdiqlash uchun emitent bankka yuboradi.
 
4.1, 4.2 va 4.3-qadamlar: Agar tranzaktsiya tasdiqlangan bo'lsa, emitent bank pulni muzlatib qo'yadi. Tasdiqlash yoki rad etish ekvayerga, shuningdek POS terminalga qaytariladi.
 
- Qo'lga olish va joylashtirish oqimi

1 va 2-qadamlar: Savdogar kun oxirida pul yig'ishni xohlaydi, shuning uchun ular POS terminalida "qo'lga olish" tugmasini bosadilar. Tranzaktsiyalar to'plamda ekvayerga yuboriladi. Ekvayer paketli faylni tranzaktsiyalar bilan karta tarmog'iga yuboradi.
 
3-qadam: Karta tarmog'i turli ekvayerlardan yig'ilgan tranzaktsiyalar uchun kliringni amalga oshiradi va kliring fayllarini turli emitent banklarga yuboradi.
 
4-qadam: Emitent banklar kliring fayllari to'g'riligini tasdiqlaydi va tegishli ekvayring banklarga pul o'tkazadi.
 
5-qadam: Ekvayer bank so'ng savdogarning bankiga pul o'tkazadi. 
 
6-qadam: Karta tarmog'i turli ekvayring banklardan tranzaktsiyalarni tozalaydi. Kliring - bu o'zaro kompensatsiya operatsiyalari hisoblangan jarayondir, shuning uchun umumiy operatsiyalar soni kamayadi.
 
Bu jarayonda karta tarmog'i har bir bank bilan gaplashish yukini o'z zimmasiga oladi va buning evaziga xizmat haqi oladi.

### Dunyo bo'ylab to'lov tizimlari seriyasi (1-qism): Hindistonda yagona to'lov interfeysi (UPI)


UPI nima? UPI - bu Hindiston Milliy To'lovlar Korporatsiyasi tomonidan ishlab chiqilgan tezkor real vaqtda to'lov tizimi.

Bugungi kunda Hindistondagi raqamli chakana savdo operatsiyalarining 60% ni tashkil qiladi.

UPI = to'lovni belgilash tili + o'zaro to'lovlar uchun standart


<p>
  <img src="../images/how-does-upi-work.png"  style="width: 600px" />
</p>


## DevOps

###  DevOps va SRE va platforma muhandisligi. Farqi nimada?

DevOps, SRE va Platform Engineering kontseptsiyalari turli vaqtlarda paydo bo'lgan va turli shaxslar va tashkilotlar tomonidan ishlab chiqilgan.

<p>
  <img src="../images/devops-sre-platform.jpg" />
</p>

DevOps kontseptsiya sifatida 2009 yilda Agile konferentsiyasida Patrik Debois va Endryu Shafer tomonidan taqdim etilgan. Ular hamkorlik madaniyatini va dasturiy ta'minotni ishlab chiqishning butun hayotiy tsikli uchun umumiy mas'uliyatni rag'batlantirish orqali dasturiy ta'minotni ishlab chiqish va operatsiyalar o'rtasidagi tafovutni bartaraf etishga intildi.

SRE yoki Site Reliability Engineering 2000-yillarning boshida Google tomonidan keng koʻlamli, murakkab tizimlarni boshqarishdagi operatsion muammolarni hal qilish uchun kashshof boʻlgan. Google xizmatlarining ishonchliligi va samaradorligini oshirish uchun Borg klasterini boshqarish tizimi va Monarch monitoring tizimi kabi SRE amaliyotlari va vositalarini ishlab chiqdi.

Platforma muhandisligi - bu SRE muhandisligi asosiga qurilgan eng yangi kontseptsiya. Platforma muhandisligining aniq kelib chiqishi unchalik aniq emas, lekin bu odatda DevOps va SRE amaliyotlarining kengaytmasi sifatida tushuniladi, asosiy e'tibor butun biznes istiqbolini qo'llab-quvvatlaydigan mahsulotni ishlab chiqish uchun keng qamrovli platformani taqdim etishga qaratilgan.

Ta'kidlash joizki, bu tushunchalar turli davrlarda paydo bo'lgan. Ularning barchasi dasturiy ta'minotni ishlab chiqish va ishlashda hamkorlik, avtomatlashtirish va samaradorlikni oshirishning kengroq tendentsiyasi bilan bog'liq.

### K8s (Kubernetes) nima?

K8s konteyner orkestrlash tizimidir. U konteynerni joylashtirish va boshqarish uchun ishlatiladi. Uning dizayniga Google ichki tizimi Borg katta ta'sir ko'rsatadi.

<p>
  <img src="../images/k8s.jpeg" style="width: 680px" />
</p>

K8s klasteri konteynerlashtirilgan ilovalarni ishga tushiradigan tugunlar deb ataladigan ishchi mashinalar to'plamidan iborat. Har bir klasterda kamida bitta ishchi tugun mavjud.

Ishchi tugun(lar) dastur ish yukining komponentlari bo'lgan podlarni joylashtiradi. Boshqaruv tekisligi ishchi tugunlarni va klasterdagi podlarni boshqaradi. Ishlab chiqarish muhitida boshqaruv tekisligi odatda bir nechta kompyuterlar bo'ylab ishlaydi va klaster odatda xatolarga chidamlilik va yuqori mavjudlikni ta'minlaydigan bir nechta tugunlarni boshqaradi.

- Tekshirish tekisligi komponentlari

1. API serveri

    API serveri k8s klasteridagi barcha komponentlar bilan gaplashadi. Podkalardagi barcha operatsiyalar API serveri bilan gaplashish orqali amalga oshiriladi.

2. Rejalashtiruvchi

    Rejalashtiruvchi pod ish yuklarini kuzatadi va yangi yaratilgan podkalarga yuklarni tayinlaydi.

3. Nazoratchi menejeri

    Nazoratchi menejeri kontrollerlarni, jumladan Node Controller, Job Controller, EndpointSlice Controller va ServiceAccount Controllerni boshqaradi.

4. Etcd
    
    etcd - barcha klaster ma'lumotlari uchun Kubernetesning qo'llab-quvvatlovchi do'koni sifatida foydalaniladigan kalit-qiymat do'koni.

- Tugunlar

1. Podlar

    Pod - bu konteynerlar guruhi va k8s boshqaradigan eng kichik birlikdir. Podlar pod ichidagi har bir konteynerga qo'llaniladigan yagona IP-manzilga ega.

2. Kubelet

    Klasterdagi har bir tugunda ishlaydigan agent. Bu konteynerlarning Podda ishlashini ta'minlaydi.

3. Kube proksi

    Kube-proksi - bu klasteringizdagi har bir tugunda ishlaydigan tarmoq proksi-serveri. U xizmatdan tugunga keladigan trafikni yo'naltiradi. U ish uchun so'rovlarni to'g'ri konteynerlarga yuboradi.

### Docker va Kubernetes. Qaysi birini ishlatishimiz kerak?

<p>
  <img src="../images/docker-vs-k8s.jpg" style="width: 680px" />
</p>


Docker nima?

Docker ochiq kodli platforma bo'lib, u alohida konteynerlarda ilovalarni paketlash, tarqatish va ishga tushirish imkonini beradi. U konteynerlashtirishga qaratilgan bo'lib, ilovalar va ularning bog'liqliklarini qamrab oladigan engil muhitlarni ta'minlaydi. 

Kubernetes nima?

Ko'pincha K8s deb ataladigan Kubernetes ochiq manbali konteyner orkestr platformasidir. U tugunlar klasterida konteynerlashtirilgan ilovalarni joylashtirish, masshtablash va boshqarishni avtomatlashtirish uchun asos yaratadi. 

Ikkalasi bir-biridan qanday farq qiladi?

Docker: Docker bitta operatsion tizim xostida individual konteyner darajasida ishlaydi.

Har bir xostni qo'lda boshqarishingiz kerak va tarmoqlarni sozlash, xavfsizlik siyosati va bir nechta tegishli konteynerlar uchun saqlash murakkab bo'lishi mumkin.

Kubernetes: Kubernetes klaster darajasida ishlaydi. U bir nechta hostlarda bir nechta konteynerli ilovalarni boshqaradi, yuklarni muvozanatlash, masshtablash va ilovalarning kerakli holatini ta'minlash kabi vazifalarni avtomatlashtirishni ta'minlaydi.

Muxtasar qilib aytganda, Docker alohida xostlarda konteynerlashtirish va konteynerlarni ishga tushirishga e'tibor qaratadi, Kubernetes esa xostlar klasteri bo'ylab konteynerlarni boshqarish va tartibga solishga ixtisoslashgan.

### Docker qanday ishlaydi?

Quyidagi diagrammada Docker arxitekturasi va biz "docker build", "docker pull" va "docker run" ni ishga tushirganimizda qanday ishlashi ko'rsatilgan.

<p>
  <img src="../images/docker.jpg" style="width: 680px" />
</p>

Docker arxitekturasida 3 ta komponent mavjud:

- Docker mijozi
    
    Docker mijozi Docker demoni bilan gaplashadi.

- Docker host 

    Docker demoni Docker API so‘rovlarini tinglaydi va tasvirlar, konteynerlar, tarmoqlar va hajmlar kabi Docker obyektlarini boshqaradi.

- Docker registrlari 

    Docker registrida Docker tasvirlari saqlanadi. Docker Hub - bu hamma foydalanishi mumkin bo'lgan ommaviy reestr.

Misol sifatida "docker run" buyrug'ini olaylik.

  1. Docker tasvirni registrdan oladi.
  2. Docker yangi konteyner yaratadi.
  3. Docker konteynerga o'qish va yozish fayl tizimini ajratadi.
  4. Docker konteynerni standart tarmoqqa ulash uchun tarmoq interfeysini yaratadi.
  5. Docker konteynerni ishga tushiradi.

## GIT

### Git buyruqlari qanday ishlaydi

Boshlash uchun kodimiz qayerda saqlanishini aniqlash kerak. Umumiy taxmin shundan iboratki, faqat ikkita joy bor - biri Github kabi uzoq serverda, ikkinchisi bizning mahalliy mashinamizda. Biroq, bu to'liq aniq emas. Git bizning mashinamizda uchta mahalliy xotirani saqlaydi, ya'ni bizning kodimizni to'rtta joyda topish mumkin:

<p>
  <img src="../images/git-commands.png" style="width: 600px" />
</p>


- Ishchi katalog: biz fayllarni tahrir qiladigan joy
- Sahna maydoni: fayllar keyingi topshiriq uchun saqlanadigan vaqtinchalik joy
- Mahalliy ombor: o'rnatilgan kodni o'z ichiga oladi
- Masofaviy ombor: kodni saqlaydigan masofaviy server

Ko'pgina Git buyruqlari asosan fayllarni ushbu to'rtta joy o'rtasida ko'chiradi.

### Git qanday ishlaydi?

Quyidagi diagrammada Git ish jarayoni ko'rsatilgan.

<p>
  <img src="../images/git-workflow.jpeg" style="width: 520px" />
</p>


Git - bu taqsimlangan versiyani boshqarish tizimi.

Har bir ishlab chiquvchi asosiy omborning mahalliy nusxasini saqlaydi va mahalliy nusxani tahrirlaydi va majburiyatini oladi.

Amal qilish juda tez, chunki operatsiya masofaviy ombor bilan o'zaro ta'sir qilmaydi.

Agar masofaviy ombor ishlamay qolsa, fayllar mahalliy omborlardan tiklanishi mumkin. 

### Git merge va Git rebase

Qanday farqlar bor?

<p>
  <img src="../images/git-merge-git-rebase.jpeg" style="width: 680px" />
</p>


**O'zgarishlar**ni bir Git filialidan boshqasiga **birlashtirgan**da, biz "git merge" yoki "git rebase" dan foydalanishimiz mumkin. Quyidagi diagrammada ikkita buyruq qanday ishlashi ko'rsatilgan.

**Git merge**

Bu asosiy filialda yangi G' majburiyatini yaratadi. G' asosiy va xususiyatli tarmoqlarning tarixini bog'laydi.

Git birlashmasi **buzilmaydi**. Na asosiy, na xususiyat filiali o'zgartirilmaydi.

**Git birlashmasi (Git rebase)**

Git rebase xususiyat filiallari tarixini asosiy filialning boshiga o'tkazadi. U xususiyat bo'limidagi har bir topshiriq uchun yangi E', F' va G' majburiyatlarini yaratadi.

Qayta tiklashning afzalligi shundaki, u chiziqli **majburiyat tarixiga (commit history)** ega.

Agar "git rebase ning oltin qoidasiga" rioya qilinmasa, rebase xavfli bo'lishi mumkin.

**Git Rebase ning oltin qoidasi (The Golden Rule of Git Rebase)**

Uni hech qachon ommaviy filiallarida ishlatmang!

## Bulutli xizmatlar

### Turli xil bulut xizmatlarining chiroyli cheat varag'i (2023 yil nashri)

<p>
  <img src="../images/cloud-compare.jpg" />
</p>


### Mahalliy bulut nima?

Quyida 1980-yillardan beri arxitektura va jarayonlarning evolyutsiyasini ko'rsatadigan diagramma keltirilgan.

<p>
  <img src="../images/cloud-native.jpeg" style="width: 640px" />
</p>

Tashkilotlar bulutli mahalliy texnologiyalardan foydalangan holda ommaviy, xususiy va gibrid bulutlarda kengaytiriladigan ilovalarni yaratishi va ishga tushirishi mumkin.

Bu shuni anglatadiki, ilovalar bulut xususiyatlaridan foydalanish uchun mo'ljallangan, shuning uchun ular yuklanishga chidamli va masshtablash oson.

Cloud native 4 jihatni o'z ichiga oladi:

1. Rivojlanish jarayoni 

    Bu sharsharadan agilegacha, DevOpsga o'tdi.

2. Ilova arxitekturasi

    Arxitektura monolitlikdan mikroservislarga o'tdi. Har bir xizmat kichik, bulutli konteynerlardagi cheklangan resurslarga moslashish uchun mo'ljallangan.

3. Joylashtirish va qadoqlash

    Ilovalar jismoniy serverlarda o'rnatilar edi. Keyin 2000-yillarda kechikishga sezgir bo'lmagan ilovalar odatda virtual serverlarda o'rnatildi. Bulutli mahalliy ilovalar bilan ular docker tasvirlariga o'raladi va konteynerlarga joylashtiriladi.

4. Ilova infratuzilmasi

    Ilovalar o'z-o'zidan joylashtirilgan serverlar o'rniga bulutli infratuzilmada ommaviy ravishda joylashtirilgan.

## Ishlab chiquvchi mahsuldorlik vositalari

### JSON fayllarini vizualizatsiya qilish

Ichki JSON fayllarini o'qish qiyin.

**JsonCrack** JSON fayllaridan grafik diagrammalarni yaratadi va ularni o'qishni osonlashtiradi.

Bundan tashqari, yaratilgan diagrammalarni tasvir sifatida yuklab olish mumkin.

<p>
  <img src="../images/json-cracker.jpeg" />
</p>


### Kodni avtomatik ravishda arxitektura diagrammalariga aylantiring

<p>
  <img src="../images/diagrams_as_code.jpeg" style="width: 640px" />
</p>


Bu nima qiladi?

- Python kodida bulut tizimi arxitekturasini chizing.
- Diagrammalar to'g'ridan-to'g'ri Jupyter noutbuklarida ham ko'rsatilishi mumkin.
- Dizayn vositalari kerak emas.
- Quyidagi provayderlarni qo'llab-quvvatlaydi: AWS, Azure, GCP, Kubernetes, Alibaba Cloud, Oracle Cloud va boshqalar.
 
[Github repo](https://github.com/mingrammer/diagrams)

## Linux

### Linux fayl tizimi tushuntirildi

<p>
  <img src="../images/linux-file-systems.jpg" style="width: 680px" />
</p>

Linux fayl tizimi uyushmagan shaharchaga o'xshar edi, u erda odamlar o'z uylarini xohlagan joyda quradilar. Biroq, 1994 yilda Linux fayl tizimini tartibga solish uchun Fayl tizimi ierarxiyasi standarti (FHS) joriy etildi.

FHS kabi standartni amalga oshirish orqali dasturiy ta'minot turli xil Linux distributivlarida izchil tartibni ta'minlashi mumkin. Shunga qaramay, barcha Linux distributivlari ushbu standartga qat'iy rioya qilmaydi. Ular ko'pincha o'zlarining noyob elementlarini o'z ichiga oladi yoki muayyan talablarga javob beradi. Ushbu standartda malakali bo'lish uchun siz kashf qilishdan boshlashingiz mumkin. Navigatsiya uchun "cd" va katalog tarkibini ro'yxatga olish uchun "ls" kabi buyruqlardan foydalaning. Fayl tizimini ildiz (/) dan boshlab daraxt sifatida tasavvur qiling. Vaqt o'tishi bilan u siz uchun ikkinchi tabiatga aylanadi va sizni malakali Linux ma'muriga aylantiradi.

### Siz bilishingiz kerak bo'lgan 18 ta eng ko'p ishlatiladigan Linux buyruqlari

Linux buyruqlari operatsion tizim bilan o'zaro ishlash uchun ko'rsatmalardir. Ular fayllarni, kataloglarni, tizim jarayonlarini va tizimning boshqa ko'plab jihatlarini boshqarishga yordam beradi. Linux-ga asoslangan tizimlarni samarali va samarali boshqarish uchun siz ushbu buyruqlar bilan tanishishingiz kerak.

Quyidagi diagrammada mashhur Linux buyruqlari ko'rsatilgan:

<p>
  <img src="../images/18 Most-Used Linux Commands You Should Know-01.jpeg" style="width: 680px" />
</p>


- ls - Fayllar va kataloglarni ro'yxatlash
- cd - Joriy katalogni o'zgartirish
- mkdir - Yangi katalog yarating
- rm - Fayllar yoki kataloglarni olib tashlang
- cp - fayllar yoki kataloglarni nusxalash
- mv - fayllar yoki kataloglarni ko'chirish yoki nomini o'zgartirish
- chmod - fayl yoki katalog ruxsatlarini o'zgartirish
- grep - fayllardan naqsh izlash 
- find - fayllar va kataloglarni qidirish
- tar - tarball arxiv fayllarini boshqarish
- vi - matn muharrirlari yordamida fayllarni tahrirlash 
- cat - fayllar tarkibini ko'rsatish 
- top - jarayonlar va resurslardan foydalanishni ko'rsatish
- ps - displey ma'lumotlarni qayta ishlaydi 
- kill - signal yuborish orqali jarayonni tugatish 
- du - fayl maydonidan foydalanishni taxmin qilish 
- ifconfig - Tarmoq interfeyslarini sozlang  
- ping - Xostlar o'rtasida tarmoq ulanishini sinab ko'ring

## Xavfsizlik

### HTTPS qanday ishlaydi?

Xavfsiz gipermatn uzatish protokoli (HTTPS) gipermatnni uzatish protokolining (HTTP) kengaytmasi bo'lib, HTTPS shifrlangan ma'lumotlarni Transport Layer Security (TLS) yordamida uzatadi. 

<p>
  <img src="../images/https.jpg" />
</p>


Ma'lumotlar qanday shifrlangan va shifrlangan?

1-qadam - mijoz (brauzer) va server TCP ulanishini o'rnatadi.

2-qadam - Mijoz serverga "mijozga salom" yuboradi. Xabarda zarur shifrlash algoritmlari toʻplami (shifr toʻplami) va u qoʻllab-quvvatlaydigan soʻnggi TLS versiyasi mavjud. Server "serverga salom" bilan javob beradi, shuning uchun brauzer algoritmlar va TLS versiyasini qo'llab-quvvatlashi mumkinligini biladi.

Keyin server mijozga SSL sertifikatini yuboradi. Sertifikatda ochiq kalit, xost nomi, amal qilish muddati va boshqalar mavjud. Mijoz sertifikatni tasdiqlaydi.

3-qadam - SSL sertifikatini tekshirgandan so'ng, mijoz sessiya kalitini yaratadi va uni ochiq kalit yordamida shifrlaydi. Server shifrlangan seans kalitini oladi va uni shaxsiy kalit bilan hal qiladi.

4-qadam -- Endi mijoz ham, server ham bir xil seans kalitiga ega (simmetrik shifrlash), shifrlangan maʼlumotlar xavfsiz ikki yoʻnalishli kanalda uzatiladi.

Nima uchun HTTPS ma'lumotlarni uzatishda nosimmetrik shifrlashga o'tadi? Ikkita asosiy sabab bor:

1. Xavfsizlik: assimetrik shifrlash faqat bitta yo'l bilan amalga oshiriladi. Bu shuni anglatadiki, agar server shifrlangan ma'lumotlarni mijozga qaytarib yuborishga harakat qilsa, har kim ochiq kalit yordamida ma'lumotlarning shifrini ochishi mumkin.

2. Server resurslari: assimetrik shifrlash juda ko'p matematik yuklarni qo'shadi. Uzoq seanslarda ma'lumotlarni uzatish uchun mos emas.

### Oauth 2.0 oddiy shartlar bilan tushuntirilgan.

OAuth 2.0 kuchli va xavfsiz tizim boʻlib, u turli ilovalarga maxfiy hisob maʼlumotlarini baham koʻrmasdan foydalanuvchilar nomidan bir-biri bilan xavfsiz oʻzaro aloqada boʻlish imkonini beradi.

<p>
  <img src="../images/oAuth2.jpg" />
</p>

OAuth bilan bog'liq bo'lgan ob'ektlar - bu foydalanuvchi, server va identifikatsiya provayderi (IDP).

OAuth tokeni nima qila oladi?

OAuth-dan foydalanganda siz shaxsingiz va ruxsatlaringizni ifodalovchi OAuth tokenini olasiz. Ushbu token bir nechta muhim ishlarni bajarishi mumkin:

Yagona tizimga kirish (SSO): OAuth tokeni yordamida siz faqat bitta login yordamida bir nechta xizmatlar yoki ilovalarga kirishingiz mumkin, bu esa hayotni oson va xavfsizroq qiladi.

Tizimlar bo'ylab avtorizatsiya: OAuth tokeni avtorizatsiya yoki kirish huquqlarini turli tizimlar bo'ylab almashish imkonini beradi, shuning uchun hamma joyda alohida tizimga kirishingiz shart emas.

Foydalanuvchi profiliga kirish: OAuth tokeni boʻlgan ilovalar siz ruxsat bergan foydalanuvchi profilingizning ayrim qismlariga kirishi mumkin, lekin ular hammasini koʻra olmaydi.

Esingizda bo'lsin, OAuth 2.0 barcha ilovalar va xizmatlarda onlayn tajribangizni muammosiz va muammosiz qilish bilan birga sizni va ma'lumotlaringizni xavfsiz saqlashga qaratilgan.

### Autentifikatsiya mexanizmlarining 4 ta eng yaxshi shakllari

<p>
  <img src="../images/top4-most-used-auth.jpg" />
</p>

1. SSH kalitlari:
   
    Kriptografik kalitlar masofaviy tizimlar va serverlarga xavfsiz kirish uchun ishlatiladi 

1. OAuth tokenlari:

    Uchinchi tomon ilovalarida foydalanuvchi ma'lumotlariga cheklangan kirishni ta'minlaydigan tokenlar

1. SSL sertifikatlari:
  
    Raqamli sertifikatlar serverlar va mijozlar o'rtasida xavfsiz va shifrlangan aloqani ta'minlaydi 

1. Hisob maʼlumotlari:: 

    Foydalanuvchi autentifikatsiya ma'lumotlari turli tizimlar va xizmatlarga kirishni tekshirish va ruxsat berish uchun ishlatiladi

### Sessiya, cookie, JWT, token, SSO va OAuth 2.0 - ular nima?

Ushbu shartlarning barchasi foydalanuvchi identifikatorini boshqarish bilan bog'liq. Veb-saytga kirganingizda, siz kimligingizni e'lon qilasiz (identifikatsiya). Shaxsingiz tasdiqlandi (autentifikatsiya) va sizga kerakli ruxsatnomalar (avtorizatsiya) beriladi. O'tmishda ko'plab echimlar taklif qilingan va ro'yxat o'sib bormoqda.

<p>
  <img src="../images/session.jpeg" />
</p>

Oddiydan murakkabgacha, men foydalanuvchi identifikatorini boshqarish haqidagi tushuncham:

- WWW-Authenticate - eng asosiy usul. Brauzer sizdan foydalanuvchi nomi va parolni so'raydi. Loginning hayot aylanishini nazorat qila olmaslik natijasida bugungi kunda u kamdan-kam qo'llaniladi.

- Kirishning hayotiy siklini yanada nozik nazorat qilish - bu seans-cookie. Server seans xotirasini saqlaydi, brauzer esa sessiya identifikatorini saqlaydi. Cookie odatda faqat brauzerlar bilan ishlaydi va mobil ilovaga mos kelmaydi.

- Moslik muammosini hal qilish uchun tokendan foydalanish mumkin. Mijoz tokenni serverga yuboradi va server tokenni tasdiqlaydi. Salbiy tomoni shundaki, token shifrlanishi va shifrlanishi kerak, bu ko'p vaqt talab qilishi mumkin.

- JWT tokenlarni ifodalashning standart usulidir. Ushbu ma'lumot raqamli imzolanganligi sababli tekshirilishi va ishonchli bo'lishi mumkin. JWT imzoni o'z ichiga olganligi sababli, sessiya ma'lumotlarini server tomonida saqlashga hojat yo'q.

- SSO (bitta tizimga kirish) yordamida siz faqat bir marta tizimga kirishingiz va bir nechta veb-saytlarga kirishingiz mumkin. U saytlararo ma'lumotlarni saqlash uchun CAS (markaziy autentifikatsiya xizmati) dan foydalanadi.

- OAuth 2.0 dan foydalanib, siz bitta veb-saytga boshqa veb-saytdagi ma'lumotlaringizga kirishga ruxsat berishingiz mumkin.

### Ma'lumotlar bazasida parollarni qanday xavfsiz saqlash va parolni qanday tekshirish mumkin?

<p>
  <img src="../images/salt.jpg" style="width: 720px" />
</p>

 
**Qilinmaydigan narsalar**

- Parollarni oddiy matnda saqlash yaxshi fikr emas, chunki ichki kirish huquqiga ega bo'lgan har bir kishi ularni ko'rishi mumkin.

- Parol xeshlarini to'g'ridan-to'g'ri saqlash etarli emas, chunki u kamalak jadvallari kabi oldindan hisoblash hujumlari uchun kesilgan.

- Oldindan hisoblash hujumlarini yumshatish uchun biz parollarni tuzlaymiz.

**Tuz (salt) nima??**

OWASP ko'rsatmalariga ko'ra, "tuz - bu xeshlash jarayonining bir qismi sifatida har bir parolga qo'shiladigan noyob, tasodifiy yaratilgan satr".
 
**Parol va tuzni qanday saqlash kerak?**

1. xesh natijasi har bir parol uchun noyobdir.
1. Parol ma'lumotlar bazasida quyidagi formatda saqlanishi mumkin: hash(parol + tuz).

**Parolni qanday tekshirish mumkin?**

Parolni tasdiqlash uchun u quyidagi jarayondan o'tishi mumkin:

1. Mijoz parolni kiritadi.
2. Tizim ma'lumotlar bazasidan mos keladigan tuzni oladi.
3. Tizim tuzni parolga qo'shib, uni xeshlaydi. Xeshlangan qiymatni H1 deb ataymiz.
4. Tizim H1 va H2 ni taqqoslaydi, bu erda H2 ma'lumotlar bazasida saqlangan xeshdir. Agar ular bir xil bo'lsa, parol haqiqiy hisoblanadi.

### 10 yoshli bolaga JSON Web Token (JWT) haqida tushuntirish

<p>
  <img src="../images/jwt.jpg" />
</p>

Tasavvur qiling-a, sizda JWT deb nomlangan maxsus quti bor. Ushbu qutining ichida uchta qism mavjud: sarlavha, foydali yuk va imzo.

Sarlavha qutining tashqi tomonidagi yorliq kabi. U qanday turdagi quti ekanligini va qanday himoyalanganligini aytadi. U odatda JSON deb nomlangan formatda yoziladi, bu shunchaki jingalak qavslar { } va ikki nuqta : yordamida ma'lumotni tartibga solish usulidir.

Foydali yuk siz yubormoqchi bo'lgan haqiqiy xabar yoki ma'lumotga o'xshaydi. Bu sizning ismingiz, yoshingiz yoki siz baham ko'rmoqchi bo'lgan boshqa ma'lumotlar bo'lishi mumkin. U JSON formatida ham yozilgan, shuning uchun uni tushunish va ishlash oson.
Endi imzo JWTni xavfsiz qiladi. Bu maxsus muhrga o'xshaydi, uni qanday yaratishni faqat jo'natuvchi biladi. Imzo parol kabi maxfiy kod yordamida yaratiladi. Ushbu imzo jo'natuvchi bu haqda bilmasdan JWT mazmunini hech kim o'zgartira olmasligini ta'minlaydi.

JWT-ni serverga yubormoqchi bo'lganingizda, siz sarlavhani, foydali yukni va imzoni qutiga qo'yasiz. Keyin uni serverga yuborasiz. Server sizning kimligingizni va nima qilishni xohlayotganingizni tushunish uchun sarlavha va foydali yukni osongina o'qiy oladi.

### Google Authenticator (yoki 2 faktorli autentifikatsiyaning boshqa turlari) qanday ishlaydi?
Ikki bosqich mavjud: 1-bosqich - foydalanuvchi Google ikki bosqichli tekshiruvini yoqadi. 2-bosqich - foydalanuvchi tizimga kirish uchun autentifikatordan foydalanadi va hokazo.

Google Authenticator odatda 2 faktorli autentifikatsiya yoqilganda hisobimizga kirish uchun ishlatiladi. Qanday qilib u xavfsizlikni kafolatlaydi?
 
Google Authenticator - bu ikki bosqichli tekshirish xizmatini amalga oshiradigan dasturiy ta'minotga asoslangan autentifikatsiya. Quyidagi diagrammada batafsil ma'lumot berilgan.

<p>
  <img src="../images/google_authenticate.jpeg" />
</p>


Ikki bosqich mavjud

- 1-bosqich - foydalanuvchi Google ikki bosqichli tekshiruvini yoqadi.
- 2-bosqich - foydalanuvchi tizimga kirish uchun autentifikatordan foydalanadi va hokazo.

Keling, ushbu bosqichlarni ko'rib chiqaylik.
 
**1-bosqich**

1 va 2-qadamlar: Bob ikki bosqichli tekshiruvni yoqish uchun veb-sahifani ochadi. Old tomon maxfiy kalitni so'raydi. Autentifikatsiya xizmati Bob uchun maxfiy kalitni yaratadi va uni ma'lumotlar bazasida saqlaydi.

3-qadam: Autentifikatsiya xizmati URI-ni old tomonga qaytaradi. URI kalit emitent, foydalanuvchi nomi va maxfiy kalitdan iborat. URI veb-sahifada QR kod ko'rinishida ko'rsatiladi.
 
3-qadam: Autentifikatsiya xizmati URI-ni old tomonga qaytaradi. URI kalit emitent, foydalanuvchi nomi va maxfiy kalitdan iborat. URI veb-sahifada QR kod ko'rinishida ko'rsatiladi. 
 
4-qadam: Keyin Bob yaratilgan QR kodni skanerlash uchun Google Authenticator-dan foydalanadi. Maxfiy kalit autentifikatorda saqlanadi.

**2-bosqich**
1 va 2-qadamlar: Bob Google ikki bosqichli tekshiruvi bilan veb-saytga kirmoqchi. Buning uchun unga parol kerak. Har 30 soniyada Google Authenticator TOTP (Vaqtga asoslangan bir martalik parol) algoritmi yordamida 6 xonali parolni yaratadi. Bob veb-saytga kirish uchun paroldan foydalanadi.
 
3 va 4-qadamlar: Frontend autentifikatsiya qilish uchun Bob kiritgan parolni backendga yuboradi. Autentifikatsiya xizmati ma'lumotlar bazasidan maxfiy kalitni o'qiydi va mijoz bilan bir xil TOTP algoritmidan foydalangan holda 6 xonali parolni yaratadi.
 
5-qadam: Autentifikatsiya xizmati mijoz va server tomonidan yaratilgan ikkita parolni solishtiradi va taqqoslash natijasini frontendga qaytaradi. Bob kirish jarayonini faqat ikkita parol mos kelgan taqdirdagina davom ettirishi mumkin.
 
Ushbu autentifikatsiya mexanizmi xavfsizmi?

- Yashirin kalitni boshqalar olishi mumkinmi?

    Yashirin kalit HTTPS orqali uzatilishiga ishonch hosil qilishimiz kerak. Autentifikatsiya mijozi va ma'lumotlar bazasi maxfiy kalitni saqlaydi va biz maxfiy kalitlar shifrlanganligiga ishonch hosil qilishimiz kerak.

- 6 xonali parolni xakerlar taxmin qilishlari mumkinmi?
    
    Yo'q. Parol 6 ta raqamga ega, shuning uchun yaratilgan parol 1 million potentsial kombinatsiyaga ega. Bundan tashqari, parol har 30 soniyada o'zgaradi. Agar xakerlar parolni 30 soniya ichida taxmin qilmoqchi bo'lsa, ular soniyasiga 30 000 ta kombinatsiyani kiritishlari kerak.


##  Haqiqiy dunyo misollari

### Netflixning Tech Stacki

Ushbu post ko'plab Netflix muhandislik bloglari va ochiq manba loyihalari tadqiqotlariga asoslangan. Agar biron bir noaniqliklarga duch kelsangiz, iltimos, bizga xabar bering.

<p>
  <img src="../images/netflix tech stack.png" style="width: 680px" />
</p>

**Mobil va veb**: Netflix mahalliy mobil ilovalarni yaratish uchun Swift va Kotlinni qabul qildi. O'zining veb-ilovasi uchun u React-dan foydalanadi.

**Frontend/server aloqasi**: Netflix GraphQL-dan foydalanadi.

**Backend xizmatlari**: Netflix ZUUL, Eureka, Spring Boot ramkasi va boshqa texnologiyalarga tayanadi.

**Ma'lumotlar bazalari**: Netflix EV keshi, Cassandra, CockroachDB va boshqa ma'lumotlar bazalaridan foydalanadi.

**Xabar almashish/striming**: Netflix xabar almashish va oqimlash uchun Apache Kafka va Fink-dan foydalanadi.

**Video saqlash**: Netflix video saqlash uchun S3 va Open Connect-dan foydalanadi.

**Ma'lumotlarni qayta ishlash**: Netflix ma'lumotlarni qayta ishlash uchun Flink va Spark-dan foydalanadi, keyin esa Tableau yordamida vizualizatsiya qilinadi. Redshift tuzilgan ma'lumotlar ombori ma'lumotlarini qayta ishlash uchun ishlatiladi.

**CI/CD**: Netflix CI/CD jarayonlari uchun JIRA, Confluence, PagerDuty, Jenkins, Gradle, Chaos Monkey, Spinnaker, Atlas va boshqalar kabi turli xil vositalardan foydalanadi.

### Twitter arxitekturasi 2022

Ha, bu haqiqiy Twitter arxitekturasi. U Elon Mask tomonidan joylashtirilgan va biz uni yaxshiroq o'qish uchun qayta chizganmiz.

<p>
  <img src="../images/twitter-arch.jpeg" />
</p>


### Oxirgi 15 yil ichida Airbnb mikroservis arxitekturasining evolyutsiyasi

Airbnb mikroservis arxitekturasi 3 asosiy bosqichdan o'tdi.

<p>
  <img src="../images/airbnb_arch.jpeg" />
</p>


Monolit (2008 - 2017)

Airbnb mezbonlar va mehmonlar uchun oddiy bozor sifatida boshlangan. Bu Ruby on Rails ilovasida - monolitda qurilgan. 

Qiyinchilik nima?

- Chalkash jamoa egaligi + egaliksiz kod
- Sekin joylashtirish

Mikroservislar (2017 - 2020)

Microservice ushbu muammolarni hal qilishga qaratilgan. Mikroservis arxitekturasida asosiy xizmatlarga quyidagilar kiradi:

- Ma'lumot olish xizmati
- Biznes mantiqiy ma'lumotlar xizmati
- Ish jarayonini yozish xizmati
- UI yig'ish xizmati
- Har bir xizmatning bitta egasi bor edi

Qiyinchilik nima?

Yuzlab xizmatlar va qaramliklarni boshqarish odamlar uchun qiyin edi.

Micro + makroservislar (2020 yildan hozirgi kungacha)

Hozirda Airbnb shu narsa ustida ishlamoqda. Mikro va makroservis gibrid modeli asosiy e'tibor API larni birlashtirishga qaratilgan.

### Monorepo va mikrorepo.

Qaysi biri eng yaxshisi? Nima uchun turli kompaniyalar turli xil variantlarni tanlaydilar?

<p>
  <img src="../images/monorepo-microrepo.jpg" />
</p>


Monorepo yangi emas; Linux va Windows ikkalasi ham Monorepo yordamida yaratilgan. Kengaytirish va qurish tezligini yaxshilash uchun Google uni tezroq kengaytirish uchun ichki maxsus asboblar zanjirini va uni izchil saqlash uchun qattiq kodlash sifat standartlarini ishlab chiqdi. 

Amazon va Netflix Microservice falsafasining asosiy elchilaridir. Ushbu yondashuv tabiiy ravishda xizmat kodini alohida omborlarga ajratadi. U tezroq tarqaladi, lekin keyinchalik boshqaruvning og'riqli nuqtalariga olib kelishi mumkin. 

Monorepo ichida har bir xizmat papka bo'lib, har bir jildda BUILD konfiguratsiyasi va HONERS ruxsati boshqaruvi mavjud. Har bir xizmatchi o'z papkasi uchun javobgardir.

Boshqa tomondan, Microrepo-da har bir xizmat o'z ombori uchun javobgar bo'lib, qurish konfiguratsiyasi va ruxsatlar odatda butun ombor uchun o'rnatiladi.

Monorepo-da bog'liqliklar biznesingizdan qat'i nazar, butun kod bazasi bo'ylab taqsimlanadi, shuning uchun versiyani yangilash mavjud bo'lganda, har bir kod bazasi o'z versiyasini yangilaydi.

Microrepo-da bog'liqliklar har bir ombor ichida nazorat qilinadi. Korxonalar o'z jadvallari asosida o'z versiyalarini qachon yangilashni tanlashadi.

Monorepoda ro'yxatdan o'tish uchun standart mavjud. Google-ning kodni ko'rib chiqish jarayoni biznesdan qat'i nazar, Monorepo uchun izchil sifat standartini ta'minlaydigan yuqori barni o'rnatishi bilan mashhur.

Microrepo o'z standartini o'rnatishi yoki eng yaxshi tajribalarni o'z ichiga olgan umumiy standartni qabul qilishi mumkin. U biznes uchun tezroq kengayishi mumkin, ammo kod sifati biroz boshqacha bo'lishi mumkin.
Google muhandislari Bazelni, Meta esa Bakni yaratdi. Boshqa ochiq manbali vositalar mavjud, jumladan Nix, Lerna va boshqalar.

Yillar davomida Microrepo ko'proq qo'llab-quvvatlanadigan vositalarga ega bo'ldi, jumladan Java uchun Maven va Gradle, NodeJS uchun NPM va C/C++ uchun CMake va boshqalar.

### Stack Overflow veb-saytini qanday loyihalashtirasiz?

Agar sizning javobingiz mahalliy serverlar va monolit (quyidagi rasmning pastki qismida) bo'lsa, siz intervyuda muvaffaqiyatsiz bo'lishingiz mumkin, ammo u haqiqatda shunday qurilgan!

<p>
  <img src="../images/stackoverflow.jpg" />
</p>


**Odamlar qanday ko'rinishi kerak deb o'ylashadi**

Suhbatdosh, ehtimol, rasmning yuqori qismiga o'xshash narsani kutmoqda.

- Mikroservis tizimni kichik qismlarga ajratish uchun ishlatiladi.
- Har bir xizmat o'z ma'lumotlar bazasiga ega. Keshni qattiq ishlating.
- Xizmat ajratilgan.
- Xizmatlar bir-biri bilan asinxron tarzda xabarlar navbatlari orqali gaplashadi.
- Xizmat CQRS bilan Event Sourcing yordamida amalga oshiriladi.
- Taqsimlangan tizimlarda bilimlarni namoyish qilish, masalan, yakuniy izchillik, CAP teoremasi va boshqalar.

**Bu aslida nima**

Stack Overflow barcha trafikni faqat 9 ta mahalliy veb-serverlar bilan ta'minlaydi va u monolitda! Uning o'z serverlari bor va bulutda ishlamaydi.

Bu bizning barcha mashhur e'tiqodlarimizga ziddir.

### Nima uchun Amazon Prime Video monitoringi serversizdan monolitga o'tdi? Qanday qilib 90% xarajatlarni tejash mumkin?

Quyidagi diagrammada migratsiyadan oldin va keyin arxitektura taqqoslash ko'rsatilgan.

<p>
  <img src="../images/serverless-to-monolithic.jpeg" />
</p>


Amazon Prime Video Monitoring xizmati nima?

Prime Video xizmati minglab jonli translatsiyalar sifatini kuzatishi kerak. Monitoring vositasi real vaqtda oqimlarni avtomatik ravishda tahlil qiladi va blokirovka buzilishi, videoni muzlatish va sinxronlash muammolari kabi sifat muammolarini aniqlaydi. Bu mijozlar ehtiyojini qondirish uchun muhim jarayon.

3 bosqich mavjud: media konvertori, nuqsonlarni aniqlovchi va real vaqtda bildirishnoma. 

- Eski arxitekturada qanday muammo bor?

  Qadimgi arxitektura Amazon Lambda-ga asoslangan bo'lib, u tezda xizmatlarni qurish uchun yaxshi edi. Biroq, arxitekturani yuqori miqyosda ishga tushirishda bu iqtisodiy jihatdan samarali emas edi. Ikkita eng qimmat operatsiya:

1. Orkestratsiya ish oqimi - AWS qadam funktsiyalari foydalanuvchilarni holat o'tishlari bo'yicha to'laydi va orkestr har soniyada bir nechta holat o'tishlarini amalga oshiradi.

2. Taqsimlangan komponentlar o'rtasida ma'lumotlar uzatish - oraliq ma'lumotlar Amazon S3 da saqlanadi, shunda keyingi bosqich yuklab olinadi. Ovoz balandligi baland bo'lsa, yuklab olish qimmatga tushishi mumkin.

- Monolitik arxitektura 90% xarajatlarni tejaydi

  Monolitik arxitektura xarajatlar bilan bog'liq muammolarni hal qilish uchun mo'ljallangan. Hali ham 3 ta komponent mavjud, biroq media konvertor va nuqson detektori bir xil jarayonda joylashtiriladi, bu esa tarmoq orqali ma'lumotlarni uzatish xarajatlarini tejaydi. Ajablanarlisi shundaki, joylashtirish arxitekturasini o'zgartirishga bunday yondashuv xarajatlarni 90% tejashga olib keldi! 

Bu qiziqarli va noyob misoldir, chunki mikroservislar texnologiya sanoatida mashhur va moda tanloviga aylandi. Biz arxitekturani rivojlantirish va uning ijobiy va salbiy tomonlari haqida ko'proq halol muhokamalar olib borayotganimizni ko'rish juda yaxshi. Komponentlarni taqsimlangan mikroservislarga ajratish qimmatga tushadi.

- Amazon rahbarlari bu haqda nima dedilar?
  
  Amazon CTO Verner Vogels: "**Rivojlanuvchan dasturiy ta'minot tizimlarini** yaratish din emas, balki strategiyadir. Va arxitekturangizni ochiq fikr bilan qayta ko'rib chiqish shart.".

Amazonning Barqarorlik bo'yicha sobiq vitse-prezidenti Adrian Kokkroft: "Prime Video jamoasi men **birinchi bo'lib Serversiz** deb ataydigan yo'ldan bordi... Men Faqat **Serversizni** yoqlamayman".

### Disney Hotstar turnir davomida 5 milliard kulgichni qanday suratga oladi?

<p>
  <img src="../images/hotstar_emojis.jpeg" style="width: 720px" />
</p>


1. Mijozlar emojilarni standart HTTP so'rovlari orqali yuboradilar. Golang xizmatini odatiy veb-server sifatida tasavvur qilishingiz mumkin. Golang tanlangan, chunki u parallellikni yaxshi qo'llab-quvvatlaydi. Golangdagi iplar engildir.

2. Yozish hajmi juda yuqori bo'lgani uchun bufer sifatida Kafka (xabar navbati) ishlatiladi.

3. Emoji ma'lumotlari Spark deb nomlangan oqimni qayta ishlash xizmati tomonidan jamlanadi. U sozlanishi mumkin bo'lgan har 2 soniyada ma'lumotlarni jamlaydi. Interval asosida amalga oshiriladigan savdo-sotiq mavjud. Qisqaroq intervalli emojilar boshqa mijozlarga tezroq yetkazilishini anglatadi, lekin bu ko'proq hisoblash resurslari kerakligini anglatadi.

4. Yig'ilgan ma'lumotlar boshqa Kafkaga yoziladi.

5. PubSub iste'molchilari Kafkadan jamlangan emoji ma'lumotlarini olishadi.

6. Emojilar boshqa mijozlarga real vaqt rejimida PubSub infratuzilmasi orqali yetkaziladi. PubSub infratuzilmasi qiziqarli. Hotstar quyidagi protokollarni ko'rib chiqdi: Socketio, NATS, MQTT va gRPC va MQTT bilan hisob-kitob qildi.
 
Shunga o'xshash dizayn LinkedIn tomonidan qabul qilingan bo'lib, u sekundiga millionlab yoqtirishlarni oladi.

### Discord qanday qilib trillionlab xabarlarni saqlaydi?

Quyidagi diagrammada Discord-da xabarlarni saqlash evolyutsiyasi ko'rsatilgan:

<p>
  <img src="../images/discord-store-messages.jpg" />
</p>


MongoDB ➡️ Cassandra ➡️ ScyllaDB 

2015 yilda Discord-ning birinchi versiyasi bitta MongoDB nusxasi ustiga qurilgan. Taxminan 2015 yil noyabr oyida MongoDB 100 million xabarni saqladi va operativ xotira ma'lumotlarni va indeksni boshqa saqlay olmadi. Kechikish oldindan aytib bo'lmaydigan bo'lib qoldi. Xabarni saqlash boshqa ma'lumotlar bazasiga ko'chirilishi kerak. Kassandra tanlandi.

2017 yilda Discord 12 ta Cassandra tuguniga ega bo'lib, milliardlab xabarlarni saqlagan.

2022 yil boshida u trillionlab xabarlarga ega 177 tugunga ega edi. Bu vaqtda kechikishni oldindan aytib bo'lmaydi va texnik xizmat ko'rsatish operatsiyalari bajarish uchun juda qimmatga tushdi.

Muammoning bir nechta sabablari bor:

- Kassandra ichki ma'lumotlar tuzilishi uchun LSM daraxtidan foydalanadi. O'qishlar yozishdan qimmatroq. Yuzlab foydalanuvchilari bo'lgan serverda bir vaqtning o'zida ko'plab o'qishlar bo'lishi mumkin, natijada ulanish nuqtalari paydo bo'ladi. 
- Klasterlarni saqlash, masalan, SSTablelarni ixchamlashtirish, ishlashga ta'sir qiladi.
- Axlat yig'ish to'xtatilishi sezilarli kechikishlarga olib keladi

ScyllaDB - bu C++ da yozilgan Cassandra mos ma'lumotlar bazasi. Discord o'z arxitekturasini monolit API, Rust-da yozilgan ma'lumotlar xizmati va ScyllaDB-ga asoslangan saqlash uchun qayta ishlab chiqdi.

ScyllaDB-da p99 o'qish kechikishi Cassandra-da 40-125ms bilan solishtirganda 15ms ni tashkil qiladi. p99 yozish kechikishi Kassandrada 5-70 ms ga nisbatan 5 ms ni tashkil qiladi. 

### YouTube, TikTok live yoki Twitch-da jonli video oqimlari qanday ishlaydi?
 
Jonli translatsiya oddiy oqimdan farq qiladi, chunki video kontent real vaqtda internet orqali yuboriladi, odatda bir necha soniya kechikish bilan.
 
Quyidagi diagramma buni amalga oshirish uchun sahna ortida nima sodir bo'lishini tushuntiradi.

<p>
  <img src="../images/live_streaming_updated.jpg" style="width: 640px" />
</p>

 
1-qadam: Xom video ma'lumotlari mikrofon va kamera tomonidan olinadi. Ma'lumotlar server tomoniga yuboriladi.
 
2-qadam: Video ma'lumotlar siqiladi va kodlanadi. Masalan, siqish algoritmi fon va boshqa video elementlarini ajratib turadi. Siqilgandan so'ng, video H.264 kabi standartlarga kodlangan. Ushbu bosqichdan so'ng video ma'lumotlarining hajmi ancha kichik bo'ladi.
 
3-qadam: Kodlangan ma'lumotlar kichikroq segmentlarga bo'linadi, odatda uzunligi soniyalar, shuning uchun yuklab olish yoki oqimlash uchun juda kam vaqt talab etiladi.
 
4-qadam: Segmentlangan ma'lumotlar oqim serveriga yuboriladi. Oqim serveri turli qurilmalar va tarmoq sharoitlarini qo'llab-quvvatlashi kerak. Bu "Adaptive Bitrate Streaming" deb ataladi. Bu 2 va 3-bosqichlarda turli bit tezligida bir nechta fayllarni ishlab chiqarishimiz kerakligini anglatadi.
 
5-qadam: Jonli oqim ma'lumotlari CDN (Content Delivery Network.) tomonidan qo'llab-quvvatlanadigan chekka serverlarga uzatiladi. Millionlab tomoshabinlar videoni yaqin atrofdagi chekka serverdan ko'rishlari mumkin. CDN ma'lumotlar uzatish kechikishini sezilarli darajada kamaytiradi.
 
6-qadam: Tomoshabinlar qurilmalari video ma'lumotlarini dekodlaydi va ochadi va videoni video pleerda o'ynaydi.
 
7 va 8-qadamlar: Agar videoni takrorlash uchun saqlash kerak bo'lsa, kodlangan ma'lumotlar saqlash serveriga yuboriladi va tomoshabinlar keyinchalik undan takrorlashni talab qilishlari mumkin.
 
Jonli efir uchun standart protokollarga quyidagilar kiradi:

- RTMP (Real-Time Messaging Protocol): Bu dastlab Macromedia tomonidan Flash pleer va server o'rtasida ma'lumotlarni uzatish uchun ishlab chiqilgan. Endi u internet orqali video ma'lumotlarni uzatish uchun ishlatiladi. E'tibor bering, Skype kabi video konferentsiya ilovalari kamroq kechikish uchun RTC (Real-Time Communication) protokolidan foydalanadi.
- HLS (HTTP Live Streaming): U H.264 yoki H.265 kodlashni talab qiladi. Apple qurilmalari faqat HLS formatini qabul qiladi.
- DASH (HTTP orqali dinamik adaptiv oqim): DASH Apple qurilmalarini qo'llab-quvvatlamaydi.
- HLS ham, DASH ham adaptiv bit tezligini qo'llab-quvvatlaydi.

## License

<p xmlns:cc="http://creativecommons.org/ns#" >Ushbu ish <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">CC BY-NC-ND 4.0</a> bo'yicha litsenziyalangan <img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/nd.svg?ref=chooser-v1"></p>
