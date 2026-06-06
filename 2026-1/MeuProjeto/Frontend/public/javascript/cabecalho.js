"use strict";
var __awaiter = (this && this.__awaiter) || function (thisArg, _arguments, P, generator) {
    function adopt(value) { return value instanceof P ? value : new P(function (resolve) { resolve(value); }); }
    return new (P || (P = Promise))(function (resolve, reject) {
        function fulfilled(value) { try { step(generator.next(value)); } catch (e) { reject(e); } }
        function rejected(value) { try { step(generator["throw"](value)); } catch (e) { reject(e); } }
        function step(result) { result.done ? resolve(result.value) : adopt(result.value).then(fulfilled, rejected); }
        step((generator = generator.apply(thisArg, _arguments || [])).next());
    });
};
addEventListener('load', () => __awaiter(void 0, void 0, void 0, function* () {
    var _a;
    (_a = document.getElementById('logout')) === null || _a === void 0 ? void 0 : _a.addEventListener('click', logout);
    identifica();
}));
/**
 * Função para realizar o logout do usuário.
 * Removendo os tokens do armazenamento local
 * e redireciona para a home page.
 * @param evento click de mouse
 */
const logout = (evento) => {
    evento.preventDefault();
    localStorage.removeItem('access_token');
    localStorage.removeItem('refresh_token');
    window.location.href = '/';
};
/**
 * Função para identificar o usuário autenticado.
 * Exibe o nome do usuário autenticado
 * ou "visitante" se não houver um usuário autenticado.
 */
const identifica = () => __awaiter(void 0, void 0, void 0, function* () {
    var _b;
    const spanElement = document.getElementById('identificacao');
    const headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + localStorage.getItem('access_token')
    };
    const response = yield authFetch(backendAddress + 'accounts/whoami/', {
        method: 'GET',
        headers: headers
    });
    let objDivlogged = document.getElementById('logged');
    let objDivunlogged = document.getElementById('unlogged');
    if (response.ok) {
        // token enviado no cabeçalho foi aceito pelo servidor
        const data = yield response.json();
        objDivlogged.classList.remove('invisivel');
        objDivlogged.classList.add('visivel');
        objDivunlogged.classList.remove('visivel');
        objDivunlogged.classList.add('invisivel');
        spanElement.textContent = (_b = data.username) !== null && _b !== void 0 ? _b : 'visitante';
    }
    else {
        // token enviado no cabeçalho foi rejeitado pelo servidor
        objDivlogged.classList.remove('visivel');
        objDivlogged.classList.add('invisivel');
        objDivunlogged.classList.remove('invisivel');
        objDivunlogged.classList.add('visivel');
        spanElement.textContent = 'visitante';
    }
});
