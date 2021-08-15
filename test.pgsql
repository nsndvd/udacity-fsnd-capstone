--
-- PostgreSQL database dump
--

-- Dumped from database version 13.4
-- Dumped by pg_dump version 13.4

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
-- Name: Booking; Type: TABLE; Schema: public; Owner: grandprix
--

CREATE TABLE public."Booking" (
    id integer NOT NULL,
    developer_id integer NOT NULL,
    resource_id integer NOT NULL,
    start_time timestamp without time zone,
    expected_duration_hours integer
);


ALTER TABLE public."Booking" OWNER TO grandprix;

--
-- Name: Booking_id_seq; Type: SEQUENCE; Schema: public; Owner: grandprix
--

CREATE SEQUENCE public."Booking_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Booking_id_seq" OWNER TO grandprix;

--
-- Name: Booking_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: grandprix
--

ALTER SEQUENCE public."Booking_id_seq" OWNED BY public."Booking".id;


--
-- Name: Developer; Type: TABLE; Schema: public; Owner: grandprix
--

CREATE TABLE public."Developer" (
    id integer NOT NULL,
    username character varying NOT NULL,
    full_name character varying NOT NULL
);


ALTER TABLE public."Developer" OWNER TO grandprix;

--
-- Name: Developer_id_seq; Type: SEQUENCE; Schema: public; Owner: grandprix
--

CREATE SEQUENCE public."Developer_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Developer_id_seq" OWNER TO grandprix;

--
-- Name: Developer_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: grandprix
--

ALTER SEQUENCE public."Developer_id_seq" OWNED BY public."Developer".id;


--
-- Name: Resource; Type: TABLE; Schema: public; Owner: grandprix
--

CREATE TABLE public."Resource" (
    id integer NOT NULL,
    name character varying NOT NULL,
    note character varying,
    img_url character varying
);


ALTER TABLE public."Resource" OWNER TO grandprix;

--
-- Name: Resource_id_seq; Type: SEQUENCE; Schema: public; Owner: grandprix
--

CREATE SEQUENCE public."Resource_id_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public."Resource_id_seq" OWNER TO grandprix;

--
-- Name: Resource_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: grandprix
--

ALTER SEQUENCE public."Resource_id_seq" OWNED BY public."Resource".id;


--
-- Name: alembic_version; Type: TABLE; Schema: public; Owner: grandprix
--

CREATE TABLE public.alembic_version (
    version_num character varying(32) NOT NULL
);


ALTER TABLE public.alembic_version OWNER TO grandprix;

--
-- Name: Booking id; Type: DEFAULT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Booking" ALTER COLUMN id SET DEFAULT nextval('public."Booking_id_seq"'::regclass);


--
-- Name: Developer id; Type: DEFAULT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Developer" ALTER COLUMN id SET DEFAULT nextval('public."Developer_id_seq"'::regclass);


--
-- Name: Resource id; Type: DEFAULT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Resource" ALTER COLUMN id SET DEFAULT nextval('public."Resource_id_seq"'::regclass);

--
-- Data for Name: Developer; Type: TABLE DATA; Schema: public; Owner: grandprix
--

COPY public."Developer" (id, username, full_name) FROM stdin;
2	auth0|610329ab1a16cb00688d4fb9	Manager
3	auth0|6103297e9e8634006a748d1d	DeveloperAlice
4	auth0|611934817c71c400694669ce	DeveloperBob
5	notarealidentifier	DeveloperDeletable
\.


--
-- Data for Name: Resource; Type: TABLE DATA; Schema: public; Owner: grandprix
--

COPY public."Resource" (id, name, note, img_url) FROM stdin;
1	Pirelli Testrack	\N	data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHcAAABCCAMAAABaULmmAAAAdVBMVEX/////3gDiGRf/4kbfABjgABj/4AD0rwz/5AD7ywf1qgz/5wDtcRH/6oH/643hCRfsexHpXxP80QX/7AD3tgvwlA/jKRfmShTugRDjMRb5xQjmUBXzoA3/7ZX/4T7/7p7rahL91wPoVxTwhw/kPxb4vAr/9QDWj1hkAAACD0lEQVRYhe2YAXfaIBDHC4OThGyocbVF15oY+/0/4o6DJOTNLGubuPcqf316dxB+Asclz4eHpKSkpKSke9avl2+31ssrcr+z2+tH4t4RF5bVGBfsakFdQI1wVSHkguJWjXDXhreaidUPyLkxFUxwTb3NZlEdg+VRTXE3pZpDOpcx92mSu1/ls6jh75ovNzPtb4w1z2xqf7kR82vfp9XieRWp0lHhGM0rDaC0k4LWaqWo+AxCfUCF2tTHOy8qG3/hYvU6FUVxwlyAlbNarS9uAIhDJ3AXk5XRpIB5z68sbKnzebReDbk7YYxxua9+SuNMVwfwS6w19qVQSD+BI+pHarSeVHHnia33Mhqp0f/IleHMIZfO1mazoQ5ihzGfqvuDU+Pm+0xHJXDZI3Vsuf76j3FlXurS/4KTDlxpSxJerBflnodccz6SYEEub+p6Tx1k3q1ztL+LcQ2mCo1dU15FlWhZbnOgZlO468P+XlT7KNFyfaDleu+T+/tW+Em6WQRunlknPLWBm5Nfea7ckcc+xz2qyq/3oezWORzggw5cv+HCem7wsu0Et+hqOA4EKyHxtXZcjEhxVOoJv/CNlUcNSz5yeedJcWHGG/SRZWSN1g2IbgaANcc6Axc1xCvcNt+IyQN2UPQxEHmWsWve2H0hfo7tvdj6s/V64LrHxri3U+J+fe7/+p8hKSkpKSnpfvUbF7VS5A0oQhgAAAAASUVORK5CYII=
2	Yokohama Testrack	\N	data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHcAAAA8CAMAAABreNUXAAAAmVBMVEX///8AAADl5eXvnJ38/Py8vLyZmZn39/fu7u7MzMy5ubnS0tL09PTgAAD0urqysrLExMTwoqPqbG+oqKhWVVWgoKDf398rKSr98vL519jmS07qc3X3zs/pZ2rtiInwp6dqaWnnVlgYEhOHh4d3d3dAPz83NTVLSkv1xcbukpPoX2H54eHsgILlQEPjIifjFhzkLzMiICAMAAWcbxSgAAACiUlEQVRYhe2VbXOiMBCAdwERgUKQAL4bEwRBbQ/+/4+7TWinnbmZ6nTu7lOeUQgb5MluEgSwWCwWi8VisVgsP6Vzk9tlue6vmxVcT9fNtV9vL4fjvxf3bnc79sl997p+2/3abZJ9dtgGjkddgTOHMgwd0wTwHAdilkZ0GVMPzJ1Y9wSgm455mPMZesg+I/GexC/03SRL0kKKPvXgGAskBEArPRAYFvqyKql/ATDDUN+EdFggMq1FLOhUofdUxll3yPbJhsSnSQtwxjnkmHIUs5AjB15BiCrHJmUKMXj3zgAYavsCZU2/KsaxMINInyr1KTsY8frluMy6pQ4xSng456j0RY1MNA6e6eOZPjHTXqa9Yqi4Vg00UGik9grZtE95KePDLVvqjDuTLdFWBTKOpj1HIRqOcW6KCcCHAgvGfPLGqAp0yKsox5KOOd1d51g+Jz4dD527TE67l3etrlwDH+OWZyGpAAqnBeOjknqiyVtgGVPPAtOWg5Iz8uYYxVOdHrJ63d0vNLfuVOQpKUqukVMbuWgaDPz3NOqRzGmqyNtIzmWlvTkGQx2R90yhQT6zslZvRrt1u/1nUJFETYVNsRBNhG2EevFQbdtwml8WYUXggnwBCnMucdCh8Mls++O2c79ojdfBkVZmjuOc1nOOvkAVQ9QgC6f1zGp0PI+MOs92lDpvZUKSQ/RgF5ts++Otc/uvYe2FyEwjtTgVjmPYmsviY//mtMMIgamJKfL60qyJGqMif5TtJvlTC8zX4w18zgvaIWnuQezTw0Wr9Hh8ej+Vfujrlxc1ZtSIKeb46UcoKr9d06u3yz3Zu7dbdvq+LH+ZZL3eXZNVsvoPfwUWi8VisVgsFstP+Q2TyTQNF/o0FgAAAABJRU5ErkJggg==
3	Michelin Testrack	\N	data:image/jpeg;base64,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
4	Deleteable	\N	\N
5	Bookable	\N	\N
6	Goodyear Testrack	\N	data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAHcAAAAcCAMAAABs1NAhAAAAqFBMVEUATJj////p6vEAN5D/3wD/4wAAO5//4QD/5QAASpn/5wAcT5k8ZKMASpcAPZ4AR5oARZsAQpwAP50AOaAAN6H/7ADy1yDYxT733BcAMKIANKEAPJIlVpwVUJeMknLt1SeUl26rpmKyrFzOvkgAJ6XjzjPBt1EvWZOgnmh3hHuAiXgANJEpVJVQbIpEZI29tFVtfYA8X5JjdYXJuk0AFqpYcYgAIqcALKRORzL6AAAD6klEQVRIicVWiXLbRgxlW+7pknvwWqkWD9GUSFY8JNXN//9ZAUqZxMc4GqUTYzzWErvAAx4XAL3fPke8T8T9/VfLFfevP/4n+fu2Y49X3AfvfhGhOBw2ylIa6s0gbjL58ytucDesGjPpGGcuTVOXTObX4CqzIW6eG5amnPOitTdZ/QA3EN+pxTsMCjoXnSxSSYg7UmGpvi3a17iBtjSm5oKgqToqqi4HLd3vI4OndLRICBBizBJyymrCzud1TDFXS42iFwnRYQgLtUR4VZp3cJXNMybd7gjAAc2LJEmKHs3NsZZJwidPeLokvs8IK3LrmTopTgdXMPkPvtyz9eIzqQaGD841BvIoYNErT+wJLJhzRWXf4KrRcdK0UwJPgc0kS7uUydZ4ppOEVxOQqYMwI4xkFWEy18FjeXTPjvsDBS0jilZJtqo4LJum2BrPbmHNW+3pHBYsB2YkRPcSV+w58+XeGAXphjvu8/KpAc2jGqXP0tUJNJXRDFTP/zKfudDT3fb45OpBg1/fl6c+SU0ENiz7EgKjYMh8n2AAZ+Kz5ksPp5LXuJAJuA+FUPA3SPAzBvj/hJ7ILt4Sn9T0GVScQiQ+ARrLuazKwXjiAAqWcXJQD+CblCt8j2HjF2gKuA5+qzWg+5K+xBXHBAwmux+HYbQAwtiqwyzGA2zwfr2gRy1sZOuSwzbQt3ecj3WnPIzNZ/JZqxkjcAySNGXS7/C4FZgGP60AnUMUL3AVksC7uElkMq0Q5Bwv6OGCfsA8eL7OYKONa+QyVKcePEnSbwJTEdyGu7bFe1eknRIb3jyhh4bqFnfbCRhrVPASV5fofhOg+zkGXF6ukKUthYBYES/oSiNTz2vkv1NhlvZc1t20h+sG+XKo9whtzl+geGgt5yPipnbZZRzWRSRe3WfVwe1pLtRqC6HJowANe1BjAuhr8CBLe0IWV/CSSRaKo+SdK7d5GHgh6ht6edG8j60BwnmSLKRrhe+8rRE8el2/gYaqbMYaiQnhbhO+bzkhg/LsTpLtwRE5RQaLpCgbIhuN3LLU1HCtPHWSl4JRvcQqyrJt5Pw+z/G8FDMo5VDienydL9RRRogEKFlBCRwz6BRk2mCzoS2DFtLM1LONv9R/UdKFUnnKDnhCtzAWGAwjM+F8gLZRtqyz2gzw6A4VKunoisLl6k3fEDaKYhRz7YyP0bVlmmizNyFahNd2B10Suomcz97XpgqCS3NtiNos/XFpmsIsbVPQMLx08I/nwvdTIXgzFaDEyXx+b1r8WH5iDgYeXOSdvgv2p+Zv0G9ze+fY/oZ7h+3o3ThtP8C957vuxk+4D7/rPus79jPks3D/A4kFZuv7EQhIAAAAAElFTkSuQmCC
7	Continental Testrack	\N	https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRSheTLLwvJheisiZ_8F6oUTG3E5TeS0mGYVRcsIBk&usqp=CAE&s
\.

--
-- Data for Name: Booking; Type: TABLE DATA; Schema: public; Owner: grandprix
--

COPY public."Booking" (id, developer_id, resource_id, start_time, expected_duration_hours) FROM stdin;
2	2	1	2021-08-14 21:23:16.702877	1
3	3	3	2021-08-14 21:23:22.510458	1
4	4	6	2021-08-16 20:57:25.342090	2
5	3	7	2021-08-18 13:45:12.932030	2
\.

--
-- Data for Name: alembic_version; Type: TABLE DATA; Schema: public; Owner: grandprix
--

COPY public.alembic_version (version_num) FROM stdin;
2af635d2d9e4
\.


--
-- Name: Booking_id_seq; Type: SEQUENCE SET; Schema: public; Owner: grandprix
--

SELECT pg_catalog.setval('public."Booking_id_seq"', 5, true);


--
-- Name: Developer_id_seq; Type: SEQUENCE SET; Schema: public; Owner: grandprix
--

SELECT pg_catalog.setval('public."Developer_id_seq"', 5, true);


--
-- Name: Resource_id_seq; Type: SEQUENCE SET; Schema: public; Owner: grandprix
--

SELECT pg_catalog.setval('public."Resource_id_seq"', 7, true);


--
-- Name: Booking Booking_pkey; Type: CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Booking"
    ADD CONSTRAINT "Booking_pkey" PRIMARY KEY (id);


--
-- Name: Developer Developer_pkey; Type: CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Developer"
    ADD CONSTRAINT "Developer_pkey" PRIMARY KEY (id);


--
-- Name: Developer Developer_username_key; Type: CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Developer"
    ADD CONSTRAINT "Developer_username_key" UNIQUE (username);


--
-- Name: Resource Resource_pkey; Type: CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Resource"
    ADD CONSTRAINT "Resource_pkey" PRIMARY KEY (id);


--
-- Name: alembic_version alembic_version_pkc; Type: CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public.alembic_version
    ADD CONSTRAINT alembic_version_pkc PRIMARY KEY (version_num);


--
-- Name: Booking Booking_developer_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Booking"
    ADD CONSTRAINT "Booking_developer_id_fkey" FOREIGN KEY (developer_id) REFERENCES public."Developer"(id);


--
-- Name: Booking Booking_resource_id_fkey; Type: FK CONSTRAINT; Schema: public; Owner: grandprix
--

ALTER TABLE ONLY public."Booking"
    ADD CONSTRAINT "Booking_resource_id_fkey" FOREIGN KEY (resource_id) REFERENCES public."Resource"(id);


--
-- PostgreSQL database dump complete
--

