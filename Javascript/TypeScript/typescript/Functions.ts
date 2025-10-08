function funcao1(numero: number) : void {
	console.log("O valor é " + numero);
	return; // opcional 
}

function funcao2(numero: number) : undefined {
	console.log("O valor é " + numero);
	return; // obrigatório 
}

{
	// Assinatura da função calculadora
	let calculadora: (n1: number, n2: number, op: string) => number;
	calculadora = (num1: number, num2: number, operacao: string): number => {
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
	}
}

{
	let matriculaAluno: (aluno: {nome: string, idade: number}) => boolean;
	type Aluno = {nome:string, idade: number};

	matriculaAluno = (aluno: Aluno): boolean => { 
		return true;
	}
	//matriculaAluno = (aluno: {nome:string, idade: number}): boolean => {
	// return true;
	//}	==> Correto!

	// O tipo Aluno é do mesmo tipo do parâmetro da função e é aceito em TypeScript
	let aluno: Aluno;
	aluno = {nome: 'Sandra', idade: 10};
	matriculaAluno(aluno);
}
{
	function funcao1(numero: number) : void {
		console.log("O valor é " + numero);
		return; // opcional 
	}
}
{
	function funcao2(numero: number) : undefined {
		console.log("O valor é " + numero);
		return; // obrigatório 
	}
}
{
	// Assinatura da função calculadora
	let calculadora: (n1: number, n2: number, op: string) => number;
	calculadora = (num1: number, num2: number, operacao: string): number => {
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
	}
}
{
	let matriculaAluno: (aluno: {nome: string, idade: number}) => boolean;
	type Aluno = {nome:string, idade: number};

	matriculaAluno = (aluno: Aluno): boolean => { 
		return true;
	}
	//matriculaAluno = (aluno: {nome:string, idade: number}): boolean => {
	// return true;
	//}	==> Correto!

	// O tipo Aluno é do mesmo tipo do parâmetro da função e é aceito em TypeScript
	let aluno: Aluno;
	aluno = {nome: 'Sandra', idade: 10};
	matriculaAluno(aluno);
}