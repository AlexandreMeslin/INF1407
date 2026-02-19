/*
Apenas remove os tokens do localStorage para garantir que o usuário seja deslogado após a alteração da senha.
*/
localStorage.removeItem('access_token');
localStorage.removeItem('refresh_token');

setTimeout(() => {
    location.href = "login.html";
}, 3000);
