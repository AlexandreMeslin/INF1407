"use strict";
{
    var estado;
    estado = ["Rio de Janeiro", "Minas Gerais", "Paraná", "Bahia", "São Paulo"];
    document.write(estado + "<br />");
    document.write(estado.sort() + "<br/>");
    document.write(estado.reverse() + "<br />");
}
{
    var estado;
    estado = ["Rio de Janeiro", "Minas Gerais", "Paraná", "Bahia", "São Paulo"];
    console.log(estado + "<br />");
    console.log(estado.sort() + "<br/>");
    console.log(estado.reverse() + "<br />");
}
{
    var vetor = new Array();
    vetor[0] = "indice 0";
    vetor[1] = 8752;
    //vetor.campo2 = "Campo 2";     ==> não funciona em TypeScript
    //vetor["campo3"] ="Campo 3";   ==> não funciona em TypeScript
    console.log(vetor[0] + "<br/>");
    console.log(vetor[1] + "<br/>");
    //console.log(vetor.campo2 + "<br/>");      ==> não funciona em TypeScript
    //console.log(vetor.campo3 + "<br/>");      ==> não funciona em TypeScript
    //console.log(vetor["campo2"] + "<br/>");   ==> não funciona em TypeScript
    //console.log(vetor["campo3"] + "<br/>");   ==> não funciona em TypeScript
}
{
    var data, diaSemana;
    data = new Date();
    diaSemana = new Array(7);
    diaSemana[0] = "domingo";
    diaSemana[1] = "segunda-feira";
    diaSemana[2] = "terça-feira";
    diaSemana[3] = "quarta-feira";
    diaSemana[4] = "quinta-feira";
    diaSemana[5] = "sexta-feira";
    diaSemana[6] = "sábado";
    console.log("Hoje é " + diaSemana[data.getDay()]);
}
{
    var data;
    data = new Date();
    // 27 de agosto de 1970
    data.setFullYear(1970, 7, 27);
    console.log("Data: " + data);
}
{
    var minhaData = new Date();
    minhaData.setFullYear(1970, 6, 27);
    var hoje = new Date();
    if (hoje > minhaData)
        alert("Hoje é depois de 27/07/1970");
    else
        alert("Hoje é antes de 27/07/1970");
}
