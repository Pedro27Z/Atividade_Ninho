--
-- PostgreSQL database dump
--

-- Dumped from database version 15.2
-- Dumped by pg_dump version 15.2

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
-- Name: Assinatura; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Assinatura" (
    "ID" integer NOT NULL,
    "Cliente" integer,
    "Plano" integer
);


ALTER TABLE public."Assinatura" OWNER TO postgres;

--
-- Name: Assinatura_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Assinatura" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Assinatura_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Cliente; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Cliente" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "CPF" character(11) NOT NULL
);


ALTER TABLE public."Cliente" OWNER TO postgres;

--
-- Name: Cliente_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Cliente" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Cliente_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Name: Plano; Type: TABLE; Schema: public; Owner: postgres
--

CREATE TABLE public."Plano" (
    "ID" integer NOT NULL,
    "Nome" character varying(255) NOT NULL,
    "Tipo" character varying(255) NOT NULL,
    "Valor" numeric
);


ALTER TABLE public."Plano" OWNER TO postgres;

--
-- Name: Plano_ID_seq; Type: SEQUENCE; Schema: public; Owner: postgres
--

ALTER TABLE public."Plano" ALTER COLUMN "ID" ADD GENERATED ALWAYS AS IDENTITY (
    SEQUENCE NAME public."Plano_ID_seq"
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1
);


--
-- Data for Name: Assinatura; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Assinatura" ("ID", "Cliente", "Plano") FROM stdin;
1	1	2
2	2	1
\.


--
-- Data for Name: Cliente; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Cliente" ("ID", "Nome", "CPF") FROM stdin;
2	Matheus	123456789-2
1	José	123456789-1
\.


--
-- Data for Name: Plano; Type: TABLE DATA; Schema: public; Owner: postgres
--

COPY public."Plano" ("ID", "Nome", "Tipo", "Valor") FROM stdin;
1	Solteiro	Basico	18.90
2	Casal	Padrão	39.90
3	Familia	Premium	55.90
\.


--
-- Name: Assinatura_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Assinatura_ID_seq"', 2, true);


--
-- Name: Cliente_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Cliente_ID_seq"', 2, true);


--
-- Name: Plano_ID_seq; Type: SEQUENCE SET; Schema: public; Owner: postgres
--

SELECT pg_catalog.setval('public."Plano_ID_seq"', 3, true);


--
-- Name: Assinatura Assinatura_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Assinatura"
    ADD CONSTRAINT "Assinatura_pkey" PRIMARY KEY ("ID");


--
-- Name: Cliente Cliente_CPF_key; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_CPF_key" UNIQUE ("CPF");


--
-- Name: Cliente Cliente_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Cliente"
    ADD CONSTRAINT "Cliente_pkey" PRIMARY KEY ("ID");


--
-- Name: Plano Plano_pkey; Type: CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Plano"
    ADD CONSTRAINT "Plano_pkey" PRIMARY KEY ("ID");


--
-- Name: Assinatura fk_cliente; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Assinatura"
    ADD CONSTRAINT fk_cliente FOREIGN KEY ("Cliente") REFERENCES public."Cliente"("ID");


--
-- Name: Assinatura fk_plano; Type: FK CONSTRAINT; Schema: public; Owner: postgres
--

ALTER TABLE ONLY public."Assinatura"
    ADD CONSTRAINT fk_plano FOREIGN KEY ("Plano") REFERENCES public."Plano"("ID");


--
-- PostgreSQL database dump complete
--

