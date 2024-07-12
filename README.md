# SISOR

[![Updated](https://github.com/splor-mg/loa-dados-2024/actions/workflows/all.yaml/badge.svg)](https://github.com/splor-mg/loa-dados-2024/actions/)

## Pré-requisitos

Esse projeto utiliza Docker para gerenciamento das dependências. Para fazer _build_  da imagem execute:

```bash
docker build --tag loa-elaboracao .
```

## Uso

Para executar o container

```bash
docker run -it --rm --mount type=bind,source=$(PWD),target=/project loa-elaboracao bash
```

Uma vez dentro do container execute os comandos do make

```bash
make all
```
