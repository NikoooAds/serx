--
-- PostgreSQL database dump
--

-- Dumped from database version 16.1 (Debian 16.1-1.pgdg120+1)
-- Dumped by pg_dump version 16.1 (Debian 16.1-1.pgdg120+1)

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- Name: marketplace; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.marketplace (
    code_shop bigint NOT NULL,
    shop_name character varying(15),
    address character varying(100),
    region character varying(25),
    area character varying(20),
    geolocation point
);


ALTER TABLE public.marketplace OWNER TO postgres;

--
-- Name: nomenclature; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.nomenclature (
    code bigint NOT NULL,
    description character varying(120) NOT NULL
);


ALTER TABLE public.nomenclature OWNER TO postgres;

--
-- Name: users; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public.users (
    user_id bigint NOT NULL,
    username text,
    "isActive" boolean DEFAULT true NOT NULL,
    "isAdmin" boolean DEFAULT false NOT NULL,
    "isBlocked" boolean DEFAULT false NOT NULL,
    entry_date timestamp with time zone DEFAULT CURRENT_TIMESTAMP NOT NULL,
    full_name character varying(128)
);


ALTER TABLE public.users OWNER TO postgres;

--
-- Data for Name: marketplace; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.marketplace (code_shop, shop_name, address, region, area, geolocation) FROM stdin;
1	Евроопт	Минская обл, Воложинский р-н, Воложин г., Советская ул., д. 95	Воложин г.	Минская обл	(26.52094,54.09234)
2	Евроопт	Минск г., Пушкина пр., д. 3А	Минск г.	Минская обл	(27.49594,53.89668)
3	Хит! Экспресс	Минск г., Ольшевского ул., дом № 20 пом.2	Минск г.	Минская обл	(27.50212,53.91738)
4		Витебская обл, Орша г., Ленина ул., дом № 230Ю	Орша г.	Витебская обл	(30.4464,54.53907)
5		Минская обл, Борисовский р-н, Борисов г., Гагарина ул., д. 107	Борисов г.	Минская обл	(28.48617,54.20665)
6	Грошык	Минская обл, Борисов г., Труда ул., дом № 2	Борисов г	Минская обл	(28.52969,54.2239)
7	Евроопт	Минская обл, Червенский р-н, Турец аг., Юбилейная ул., д. 16	Червенский р-н	Минская обл	(28.08086,53.66634)
8		Минская обл, Смолевичский р-н, Смолевичи г., Первомайская ул., д. 1	Смолевичский р-н	Минская обл	(28.09104,54.02913)
9	Евроопт	Минская обл, Березино г., Купалы Я. ул., д. 1/2	Березино г.	Минская обл	(28.99065,53.83005)
10	Хит! Экспресс	Минская обл, Логойск г., Народная ул., дом № 2Б	Логойск г.	Минская обл	(27.84719,54.18906)
\.


--
-- Data for Name: nomenclature; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.nomenclature (code, description) FROM stdin;
313273	Мороженое пломбир с ароматом ванили м.д.ж. 15% 0,07кг г/я 3,36кг (МФМ) Зам
57	Тушка ЦБ 1 сорта пакет г/я
257245	Микс ЦБ (Плечевая часть крыла, локтевая часть крыла) вес лоток г/я 12кг Зам
269705	Микс ЦБ: (Бедро, голень) вес лоток г/я 6кг Охл
236411	Микс ЦБ: (Бедро, голень) лоток 1,5 кг г/я 12 кг Зам
1168	Бедро ЦБ вес лоток г/я 6 кг Зам
1170	Большое филе ЦБ вес лоток г/я 6,8 кг Зам
335615	Сосиски Нежные Свиные в/с вес т/ф газ г/я Охл
286763	Колбаски Кабаносы в/к в/с т/ф 0,55кг г/я 3,3кг (РФ) Охл
296732	Колбаса Сервелат с сыром в/к в/с т/ф вак 0,36кг г/я 2,88кг (РФ) Охл
\.


--
-- Data for Name: users; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public.users (user_id, username, "isActive", "isAdmin", "isBlocked", entry_date, full_name) FROM stdin;
6438298557	nkadamov	t	f	f	2023-12-09 15:41:08.725495+00	Nikooo
1091426476	None	t	f	f	2023-12-10 08:35:01.426907+00	Лена Адамова
940910978	Lyubbles	t	f	f	2023-12-10 08:36:41.421389+00	Адамова Любовь
\.


--
-- Name: marketplace marketplace_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.marketplace
    ADD CONSTRAINT marketplace_pkey PRIMARY KEY (code_shop);


--
-- Name: nomenclature nomenclature_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.nomenclature
    ADD CONSTRAINT nomenclature_pkey PRIMARY KEY (code);


--
-- Name: users users_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public.users
    ADD CONSTRAINT users_pkey PRIMARY KEY (user_id);


--
-- PostgreSQL database dump complete
--

