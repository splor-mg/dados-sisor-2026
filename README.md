# SISOR

[![Updated](https://github.com/splor-mg/dados-sisor-2026/actions/workflows/all.yaml/badge.svg)](https://github.com/splor-mg/dados-sisor-2026/actions/)

## Pré-requisitos

Esse projeto utiliza Docker para gerenciamento das dependências. Para fazer _build_  da imagem execute:

```bash
docker build --tag dados-sisor-2026 .
```

## Uso

Para executar o container:

```bash
make docker
```

Uma vez dentro do container execute os comandos:

```bash
make all
make publish # faz o push das modificações para o GitHub
```
