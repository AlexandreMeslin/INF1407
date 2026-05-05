# 🧪 Docker Multi-Architecture Lab (amd64 ↔ arm64)

Este laboratório demonstra como construir e executar imagens Docker para diferentes arquiteturas de CPU, como **amd64 (Intel/AMD)** e **arm64 (Apple Silicon, Raspberry Pi)**.

---

## 🎯 Objetivos

Ao final deste laboratório, você será capaz de:

* Entender o conceito de **multi-arquitetura em containers**
* Construir imagens Docker para arquiteturas diferentes da máquina host
* Utilizar o `docker buildx`
* Executar containers com emulação via QEMU
* Criar imagens **multi-arch (portáveis)**
* Comparar desempenho entre execução nativa e emulada

---

## 🧠 Conceito-chave

Containers **não são completamente portáveis por padrão** — a arquitetura da CPU importa.

| Arquitetura | Exemplos                      |
| ----------- | ----------------------------- |
| amd64       | PCs convencionais (Intel/AMD) |
| arm64       | Macs M1/M2/M3, Raspberry Pi   |

---

## 📁 Estrutura do projeto

```
multiarch-lab/
├── app/
│   ├── app.py
│   └── requirements.txt
├── Dockerfile
└── README.md
```

---

## 🐍 Aplicação de teste

A aplicação imprime:

* Arquitetura do sistema
* Tempo de execução de uma carga artificial

```python
import platform
import time

print("🚀 Aplicação iniciada")
print("Arquitetura:", platform.machine())

start = time.time()

for i in range(10_000_000):
    pass

end = time.time()

print("Tempo de execução:", end - start, "segundos")
```

---

## 🐳 Dockerfile

```Dockerfile
FROM python:3.11-slim

WORKDIR /app
COPY app/ .

CMD ["python", "app.py"]
```

---

## ⚙️ Preparação do ambiente

### 1. Instalar suporte a múltiplas arquiteturas

```bash
sudo docker run --privileged --rm tonistiigi/binfmt --install all
```

Resultado esperado:

```bash
$ sudo docker run --privileged --rm tonistiigi/binfmt --install all
Unable to find image 'tonistiigi/binfmt:latest' locally
latest: Pulling from tonistiigi/binfmt
4b3e935ac1b8: Pull complete 
cba9db6f3ddf: Pull complete 
Digest: sha256:d3b963f787999e6c0219a48dba02978769286ff61a5f4d26245cb6a6e5567ea3
Status: Downloaded newer image for tonistiigi/binfmt:latest
installing: arm64 OK
installing: arm OK
installing: mips64 OK
installing: loong64 OK
installing: s390x OK
installing: ppc64le OK
installing: riscv64 OK
installing: mips64le OK
{
  "supported": [
    "linux/amd64",
    "linux/amd64/v2",
    "linux/arm64",
    "linux/riscv64",
    "linux/ppc64le",
    "linux/s390x",
    "linux/386",
    "linux/mips64le",
    "linux/mips64",
    "linux/loong64",
    "linux/arm/v7",
    "linux/arm/v6"
  ],
  "emulators": [
    "python3.12",
    "qemu-aarch64",
    "qemu-arm",
    "qemu-loongarch64",
    "qemu-mips64",
    "qemu-mips64el",
    "qemu-ppc64le",
    "qemu-riscv64",
    "qemu-s390x"
  ]
}
```

---

### 2. Criar builder multi-arquitetura

Verifique se o plugin `buildx` está instalado:

```bash
$ docker buildx version
```

Resultado esperado se o plugin estiver instalado:

```bash
$ docker buildx version
github.com/docker/buildx 0.30.1 0.30.1-0ubuntu1~24.04.1
```

Resultado esperado se o plugin não estiver instalado:

```bash
$ docker buildx version
docker: 'buildx' is not a docker command.
See 'docker --help'
```

Instale o plugin se necessário:

```bash
$ sudo apt-get update
$ sudo apt-get install docker-buildx
```

```bash
docker buildx create --name multiarch --use
docker buildx inspect --bootstrap
```

---

## 🧪 Experimentos

---

### 🔹 Experimento 1 — Build nativo

```bash
docker build -t lab:local .
docker run lab:local
```

✔ Observe:

* Arquitetura (ex: x86_64)
* Tempo de execução

---

### 🔹 Experimento 2 — Build ARM64 em máquina x86

```bash
docker buildx build \
  --platform linux/arm64 \
  -t lab:arm64 \
  --load \
  .
```

Executar:

```bash
docker run --platform linux/arm64 lab:arm64
```

✔ Observe:

* Arquitetura: `aarch64`
* Execução mais lenta (emulação)

---

### 🔹 Experimento 3 — Build AMD64 em máquina ARM

(Para Macs M1/M2)

```bash
docker buildx build \
  --platform linux/amd64 \
  -t lab:amd64 \
  --load \
  .
```

---

### 🔹 Experimento 4 — Build multi-arquitetura

```bash
docker buildx build \
  --platform linux/amd64,linux/arm64 \
  -t seuusuario/lab:multi \
  --push .
```

---

### 🔹 Verificar manifest

```bash
docker buildx imagetools inspect seuusuario/lab:multi
```

✔ Deve mostrar:

```
Platforms:
  - linux/amd64
  - linux/arm64
```

---

### 🔹 Experimento 5 — Execução automática

```bash
docker run seuusuario/lab:multi
```

✔ O Docker escolhe automaticamente a arquitetura correta.

---

## 📊 Comparação de desempenho

Preencha a tabela:

| Execução   | Arquitetura | Tempo |
| ---------- | ----------- | ----- |
| Nativa     |             |       |
| Emulada    |             |       |
| Multi-arch |             |       |

---

## 💥 Experimento extra

Aumente a carga no código:

```python
for i in range(100_000_000):
    pass
```

✔ Observe o impacto da emulação no tempo.

---

## ⚠️ Problemas comuns

### ❌ Erro: no matching manifest

👉 A imagem não suporta a arquitetura da máquina.

---

### ❌ buildx não funciona

Execute novamente:

```bash
docker buildx create --use
```

---

## 🔍 Dicas úteis

Ver arquitetura da máquina:

```bash
uname -m
```

Forçar arquitetura ao rodar:

```bash
docker run --platform linux/arm64 imagem
```

---

## 🎓 Conclusão

Este laboratório demonstra que:

> Containers dependem da arquitetura da CPU, e a portabilidade total exige imagens multi-arquitetura.

---

## 🚀 Extensões possíveis

* Kubernetes com nós heterogêneos
* CI/CD com build multi-arch (GitHub Actions)
* Comparação com imagens `alpine` vs `slim`

---

## 📚 Referências

* Docker Buildx
* OCI Image Spec
* QEMU User Emulation

---

## 👨‍🏫 Uso em sala

Sugestão de dinâmica:

1. Execução individual dos experimentos
2. Coleta de tempos
3. Discussão sobre desempenho
4. Debate: "containers são realmente portáveis?"

---
