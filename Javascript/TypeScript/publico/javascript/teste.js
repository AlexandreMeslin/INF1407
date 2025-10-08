"use strict";
onload = function () {
    var realizaSoma = document.getElementById("realizaSoma");
    var numero1 = document.getElementById("numero1");
    var numero2 = document.getElementById("numero2");
    realizaSoma === null || realizaSoma === void 0 ? void 0 : realizaSoma.addEventListener("click", function () {
        console.log(soma(parseFloat(numero1.value), parseFloat(numero2.value)));
    });
};
function soma(numero1, numero2) {
    return numero1 + numero2;
}
