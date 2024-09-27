# Microsserviço Backend API Externa
=====================================

## Introdução
---------------

Este é um microsserviço backend que fornece informações sobre CEPs. Este README.md irá guiar você passo a passo para executar a aplicação.

## Requisitos
--------------

* Docker instalado na máquina local

## Passos para Executar a Aplicação
-----------------------------------

### 1. Construir a Imagem

Execute o comando `docker build -t minha-api .` para construir a imagem da aplicação.

### 2. Verificar Vulnerabilidades de Segurança

Execute o comando `docker scout quickview` para verificar vulnerabilidades de segurança na imagem.

### 3. Executar o Container

Execute o comando `docker run -d -p 5001:5001 -v ${PWD}:/app --name api-container minha-api` rodar o container com volume, para permitir que alterações no código reflitam no container.

### 4. Acessar a API

Acesse a API através da porta 8080 do seu host, por exemplo, `http://127.0.0.1:5001`.

## Parar ou Remover o Container
--------------------------------

Para parar o container, execute o comando `docker stop meu-container`. Para remover o container, execute o comando `docker rm meu-container`.

## Observações
--------------

* Lembre-se de substituir `minha-api` pelo nome real da sua imagem.
* Lembre-se de substituir `meu-container` pelo nome real do seu container.