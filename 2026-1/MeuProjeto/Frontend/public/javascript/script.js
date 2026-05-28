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
    var objBtnRemover = document.getElementById('remove');
    objBtnRemover.addEventListener('click', apagaCarros);
};
function apagaCarros(evento) {
    return __awaiter(this, void 0, void 0, function* () {
        evento.preventDefault();
        const checkboxes = document.querySelectorAll('input[name="id"]:checked');
        const checkedValues = [];
        checkboxes.forEach((checkbox) => {
            checkedValues.push(checkbox.value);
        });
        try {
            console.log('IDs dos carros a serem removidos:', checkedValues);
            const response = yield fetch(backendAddress + 'carros/varioscarros/', {
                method: 'DELETE',
                headers: {
                    'Content-Type': 'application/json'
                },
                // NÃO enviar o nome do campo, apenas a lista dos IDs
                body: JSON.stringify(checkedValues)
            });
            if (!response.ok) {
                throw new Error('Erro ao remover carros');
            }
            alert('Carros removidos com sucesso!');
        }
        catch (error) {
            console.error('Erro ao remover carros:', error);
            alert('Erro ao remover carros. Por favor, tente novamente.');
        }
        finally {
            // com ou sem erro, a lista de carros tem que ser atualizadas
            exibeListaDeCarros();
        }
    });
}
function exibeListaDeCarros() {
    return __awaiter(this, void 0, void 0, function* () {
        try {
            const response = yield fetch(backendAddress + 'carros/varioscarros/');
            if (!response.ok) {
                throw new Error('Erro ao buscar lista de carros');
            }
            const carros = yield response.json();
            let campos = ['name', 'mpg', 'cyl', 'disp', 'hp', 'wt', 'qsec', 'vs', 'am', 'gear'];
            let objTBody = document.getElementById('tbody');
            objTBody.innerHTML = '';
            carros.forEach((carro) => {
                let objTr = document.createElement('tr');
                campos.forEach(campo => {
                    let objTd = document.createElement('td');
                    //objTd.textContent = carro[campo];
                    let objHref = document.createElement('a');
                    objHref.setAttribute('href', `update.html?id=${carro.id}`);
                    objHref.textContent = carro[campo];
                    objTd.appendChild(objHref);
                    objTr.appendChild(objTd);
                });
                var objCheckbox = document.createElement('input');
                objCheckbox.setAttribute('type', 'checkbox');
                objCheckbox.setAttribute('value', carro.id);
                objCheckbox.setAttribute('id', 'id');
                objCheckbox.setAttribute('name', 'id');
                var objTd = document.createElement('td');
                objTd.appendChild(objCheckbox);
                objTr.appendChild(objTd);
                objTBody.appendChild(objTr);
            });
        }
        catch (error) {
            console.error('Erro ao buscar lista de carros:', error);
        }
    });
}
