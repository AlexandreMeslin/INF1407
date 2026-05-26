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
onload = function () {
    exibeListaDeCarros();
};
function exibeListaDeCarros() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield fetch(backendAddress + 'carros/varioscarros/', {
                method: 'GET',
                headers: {
                    'Content-Type': 'application/json',
                    'Access-Control-Allow-Origin': '*'
                }
            });
            if (!response.ok) {
                throw new Error('Erro ao buscar lista de carros');
            }
            const carros = yield response.json();
            let campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
            let objTBody = document.getElementById('idtbody');
            objTBody.innerHTML = '';
            carros.forEach((carro) => {
                let objTr = document.createElement('tr');
                campos.forEach(campo => {
                    let objTd = document.createElement('td');
                    objTd.textContent = carro[campo];
                    objTr.appendChild(objTd);
                });
                objTBody.appendChild(objTr);
            });
        }
        catch (error) {
            console.error('Erro ao buscar lista de carros:', error);
        }
    });
}
