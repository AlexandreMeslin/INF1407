"use strict";
function funcao1(numero) {
    console.log("O valor é " + numero);
    return; // opcional 
}
function funcao2(numero) {
    console.log("O valor é " + numero);
    return; // obrigatório 
}
{
    // Assinatura da função calculadora
    let calculadora;
    calculadora = (num1, num2, operacao) => {
        switch (operacao) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            case '*':
                return num1 * num2;
            case '/':
                return num1 / num2;
            default:
                return NaN;
        }
    };
}
{
    let matriculaAluno;
    matriculaAluno = (aluno) => {
        return true;
    };
    //matriculaAluno = (aluno: {nome:string, idade: number}): boolean => {
    // return true;
    //}	==> Correto!
    // O tipo Aluno é do mesmo tipo do parâmetro da função e é aceito em TypeScript
    let aluno;
    aluno = { nome: 'Sandra', idade: 10 };
    matriculaAluno(aluno);
}
{
    function funcao1(numero) {
        console.log("O valor é " + numero);
        return; // opcional 
    }
}
{
    function funcao2(numero) {
        console.log("O valor é " + numero);
        return; // obrigatório 
    }
}
{
    // Assinatura da função calculadora
    let calculadora;
    calculadora = (num1, num2, operacao) => {
        switch (operacao) {
            case '+':
                return num1 + num2;
            case '-':
                return num1 - num2;
            case '*':
                return num1 * num2;
            case '/':
                return num1 / num2;
            default:
                return NaN;
        }
    };
}
{
    let matriculaAluno;
    matriculaAluno = (aluno) => {
        return true;
    };
    //matriculaAluno = (aluno: {nome:string, idade: number}): boolean => {
    // return true;
    //}	==> Correto!
    // O tipo Aluno é do mesmo tipo do parâmetro da função e é aceito em TypeScript
    let aluno;
    aluno = { nome: 'Sandra', idade: 10 };
    matriculaAluno(aluno);
}
