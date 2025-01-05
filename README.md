# Teacher bot

<p align="center">
  <img src="https://github.com/j3rrryy/teacher_bot/actions/workflows/main.yml/badge.svg">
  <a href="https://www.python.org/downloads/release/python-3120/">
    <img src="https://img.shields.io/badge/Python-3.12-FFD64E.svg" alt="Python 3.12">
  </a>
  <a href="https://github.com/j3rrryy/teacher_bot/blob/main/LICENSE">
    <img src="https://img.shields.io/badge/License-MIT-blue.svg" alt="MIT License">
  </a>
  <a href="https://github.com/astral-sh/ruff">
    <img src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" alt="Ruff">
  </a>
</p>

## :book: Key features

- Uses PostgreSQL
- Uses Russian language to communicate
- Has a big collection of useful educational materials
- Has a few games with rating system

## :computer: Requirements

- Docker

## :hammer_and_wrench: Getting started

- Create `.env` file with variables as in the `examples/.env.example`

### :rocket: Start

```shell
docker compose up --build -d
```

### :x: Stop

```shell
docker compose stop
```
