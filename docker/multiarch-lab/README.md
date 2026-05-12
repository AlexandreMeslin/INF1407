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

- Criar um container dedicado a realizar builds

```bash
$ sudo docker buildx inspect --bootstrap
Name:          default
Driver:        docker
Last Activity: 2024-09-29 15:26:54 +0000 UTC

Nodes:
Name:             default
Endpoint:         default
Status:           running
BuildKit version: v0.18.2
Platforms:        linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/386, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/mips64le, linux/mips64, linux/loong64, linux/arm/v7, linux/arm/v6
Labels:
 org.mobyproject.buildkit.worker.moby.host-gateway-ip: 172.17.0.1
```
Verificar se o drive está correto.

```bash
$ docker buildx inspect --bootstrap
Name:          multiarch
Driver:        docker-container
Last Activity: 2026-05-06 01:02:06 +0000 UTC

Nodes:
Name:                  multiarch0
Endpoint:              unix:///var/run/docker.sock
Status:                running
BuildKit daemon flags: --allow-insecure-entitlement=network.host
BuildKit version:      v0.29.0
Platforms:             linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/mips64le, linux/mips64, linux/loong64, linux/arm/v7, linux/arm/v6
Labels:
 org.mobyproject.buildkit.worker.executor:         oci
 org.mobyproject.buildkit.worker.hostname:         98f438139229
 org.mobyproject.buildkit.worker.network:          host
 org.mobyproject.buildkit.worker.oci.process-mode: sandbox
 org.mobyproject.buildkit.worker.selinux.enabled:  false
 org.mobyproject.buildkit.worker.snapshotter:      overlayfs
GC Policy rule#0:
 All:            false
 Filters:        type==source.local,type==exec.cachemount,type==source.git.checkout
 Keep Duration:  48h0m0s
 Max Used Space: 488.3MiB
GC Policy rule#1:
 All:            false
 Keep Duration:  1440h0m0s
 Reserved Space: 9.313GiB
 Max Used Space: 93.13GiB
 Min Free Space: 43.77GiB
GC Policy rule#2:
 All:            false
 Reserved Space: 9.313GiB
 Max Used Space: 93.13GiB
 Min Free Space: 43.77GiB
GC Policy rule#3:
 All:            true
 Reserved Space: 9.313GiB
 Max Used Space: 93.13GiB
 Min Free Space: 43.77GiB
```

Verifique se o resultado contém as seguintes linhas:

```
Driver:        docker-container

Platforms:             linux/amd64, linux/amd64/v2, linux/amd64/v3, linux/arm64, linux/riscv64, linux/ppc64le, linux/s390x, linux/386, linux/mips64le, linux/mips64, linux/loong64, linux/arm/v7, linux/arm/v6
```

Faça login no Docker Hub:

```bash
 docker login

USING WEB-BASED LOGIN
To sign in with credentials on the command line, use 'docker login -u <username>'

Your one-time device confirmation code is: BWKZ-SKKS
Press ENTER to open your browser or submit your device code here: https://login.docker.com/activate

Waiting for authentication in the browser…

WARNING! Your password will be stored unencrypted in /home/meslin/.docker/config.json.
Configure a credential helper to remove this warning. See
https://docs.docker.com/engine/reference/commandline/login/#credential-stores

Login Succeeded
```

Execute o build:

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

```bash
$ docker run --platform linux/arm64 lab:arm64
🚀 Aplicação iniciada
Arquitetura: aarch64
Tempo de execução: 9.685957670211792 segundos

$ docker run meslin/lab:multi
🚀 Aplicação iniciada
Arquitetura: x86_64
Tempo de execução: 0.28368544578552246 segundos
```

Preencha a tabela:

- Execução nativa:

  ```bash
  $ docker run --rm --platform linux/amd64 meslin/lab:multi
  🚀 Aplicação iniciada
  Arquitetura: x86_64
  Tempo de execução: 0.2773442268371582 segundos
  ```

- Execução emulada:

  ```bash
  $ docker run --rm --platform linux/arm64 meslin/lab:multi
  🚀 Aplicação iniciada
  Arquitetura: aarch64
  Tempo de execução: 9.679927825927734 segundos
  ```

| Execução   | Arquitetura | Tempo |
| ---------- | ----------- | ----- |
| Nativa     |             |       |
| Emulada    |             |       |

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
