function soma(a, b) {
    var resultado;
    resultado = a + b;
    return resultado;
}

function concatena(str1, str2) {
    return str1 + " " + str2;
}

var result = soma(5,3);
console.log("A soma de", 5, "com", 3, "é", result);
console.log("Nome:", concatena("Alexandre", "Meslin"))