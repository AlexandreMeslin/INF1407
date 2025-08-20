# Exemplo de site com Docker e Apache

Execute o seguinte comando:

```bash
$ sudo docker-compose up --build
```

Use o endereço IP exibido no seu navegador.
No exemplo, o endereço é 172.23.0.2

Outros comandos interessantes:

```bash
$ sudo docker ps –a
$ sudo docker stop prog_web
$ sudo docker rm prog_web
$ sudo docker exec -it prog_web /usr/bin/bash
$ sudo docker rmi static-site_web
```

Veja o exemplo a seguir:

```bash
$ sudo docker-compose up --build
Building web
[+] Building 0.6s (7/7) FINISHED                                                                                                                 docker:default
 => [internal] load build definition from Dockerfile                                                                                                       0.0s
 => => transferring dockerfile: 256B                                                                                                                       0.0s
 => [internal] load metadata for docker.io/library/httpd:latest                                                                                            0.5s
 => [internal] load .dockerignore                                                                                                                          0.0s
 => => transferring context: 2B                                                                                                                            0.0s
 => [internal] load build context                                                                                                                          0.0s
 => => transferring context: 32B                                                                                                                           0.0s
 => [1/2] FROM docker.io/library/httpd:latest@sha256:932ac36fabe1d2103ed3edbe66224ed2afe0041b317bcdb6f5d9be63594f0030                                      0.0s
 => CACHED [2/2] COPY index.html /usr/local/apache2/htdocs/                                                                                                0.0s
 => exporting to image                                                                                                                                     0.0s
 => => exporting layers                                                                                                                                    0.0s
 => => writing image sha256:fc8b0292de23022236f679fdbd3602df64f1af6278744765f93dd6cf2fab8900                                                               0.0s
 => => naming to docker.io/library/static-site_web                                                                                                         0.0s
Creating prog_web ... done
Attaching to prog_web
prog_web | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.23.0.2. Set the 'ServerName' directive globally to suppress this message
prog_web | AH00558: httpd: Could not reliably determine the server's fully qualified domain name, using 172.23.0.2. Set the 'ServerName' directive globally to suppress this message
prog_web | [Wed Jul 31 22:13:38.334663 2024] [mpm_event:notice] [pid 1:tid 1] AH00489: Apache/2.4.62 (Unix) configured -- resuming normal operations
prog_web | [Wed Jul 31 22:13:38.334807 2024] [core:notice] [pid 1:tid 1] AH00094: Command line: 'httpd -D FOREGROUND'
```