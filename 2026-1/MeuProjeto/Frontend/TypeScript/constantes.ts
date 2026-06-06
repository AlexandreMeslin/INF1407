const backendAddress = 'https://supreme-space-guacamole-5vpvp7vw5q627p6-8000.app.github.dev/';

interface JwtResposta {
    access: string;     // token JWT de acesso
    refresh: string;    // token JWT para obter um novo token de acesso quando o atual expirar
}
