document.addEventListener("DOMContentLoaded", () => {
    // Para cada campo password, adiciona um ícone de olho para mostrar/ocultar a senha
    // cria um vetor de containers, cada um contendo um campo de senha e seu respectivo ícone de olho
    const containers = document.querySelectorAll<HTMLDivElement>(".password-container");
    // para cada container, adiciona um event listener ao ícone de olho para alternar entre mostrar e ocultar a senha
    containers.forEach(container => {
        const input = container.querySelector<HTMLInputElement>('input[type="password"]');
        const toggle = container.querySelector<HTMLImageElement>(".toggle-password");
        // verifica se o container está bem formado, ou seja, se contém um campo de senha e um ícone de olho
        if (!input || !toggle) return; // container mal formado
        // adiciona o event listener ao ícone de olho para alternar entre mostrar e ocultar a senha
        toggle.addEventListener("click", () => {
            if (input.type === "password") {
                input.type = "text";
                toggle.src = "img/eye.svg";
            } else {
                input.type = "password";
                toggle.src = "img/eye-off.svg";
            }
        });
    });
});

/**
 * Função para decodificar um token JWT e extrair seu payload.
 * 
 * @param token token a ser decodificado
 * @returns retorna o token decodificado
 */
const decodeJWT = (token: string): any => {
    const payload = token.split('.')[1];
    const decodedPayload = atob(payload);
    return JSON.parse(decodedPayload);
}

/**
 * 
 * @param token token cuja validade deve ser verificada
 * @returns verdadeiro se o token expirou, falso, caso contrário
 */
const isAccessTokenExpired = (token: string): boolean => {
    const decoded = decodeJWT(token);
    const now = Math.floor(Date.now() / 1000);

    // DEBUG
    console.log('Token expira em: ', decoded.exp, 'Tempo atual: ', now, 'faltam ', decoded.exp - now, 'segundos para expirar');
    return decoded.exp < now;
}

/**
 * Função para atualizar o token de acesso usando o token de refresh.
 * Se o token de refresh for inválido ou expirado, 
 * ambos os tokens são removidos do localStorage.
 * 
 * @returns nada
 */
const refreshAccessToken = async (): Promise<void> => {
    const refreshToken = localStorage.getItem('refresh_token');
    if (!refreshToken) {
        console.error('No refresh token available');
        return;
    }

    try {
        const response = await fetch(backendAddress + 'api/token/refresh/', {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ refresh: refreshToken })
        });

        if (response.ok) {
            const token = await response.json();
            localStorage.setItem('access_token', token.access);

            //DEBUG
            console.log('Access token refreshed successfully: ', localStorage.getItem('access_token'));
        } else {
            console.error('Failed to refresh access token');
            localStorage.removeItem('access_token');
            localStorage.removeItem('refresh_token');
        }
    } catch (error) {
        console.error('Error refreshing access token:', error);
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
    }
}

/**
 * Função para fazer requisições HTTP autenticadas usando o token de acesso.
 * Antes de fazer a requisição, verifica se o token de acesso expirou.
 * Se o token de acesso expirou, tenta atualizar o token usando o token de refresh.
 * Se a atualização do token for bem-sucedida, a requisição é feita com o novo token de acesso.
 * Se a atualização do token falhar, a requisição é feita sem o token de acesso.
 * 
 * @param url endereço do endpoint
 * @param options cabeçalhos da requisição http
 * @returns o resultado da requisição http feita usando fetch
 */
const authFetch = async (url: string, options: RequestInit = {}): Promise<Response> => {
    let accessToken = localStorage.getItem('access_token');

    if (accessToken && isAccessTokenExpired(accessToken)) {
        await refreshAccessToken();
        accessToken = localStorage.getItem('access_token');
    }

    if (accessToken) {
        options.headers = {
            ...(<any>options.headers || {}),
            'Authorization': 'Bearer ' + accessToken
        };
    }

    return fetch(url, options);
}
