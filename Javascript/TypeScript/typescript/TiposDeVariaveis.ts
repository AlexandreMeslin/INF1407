{
	// Constantes
	const TEXTO: string = "Um texto";
	const OUTRO_TEXTO = "Um outro texto";
	//TEXTO = "Um novo texto"; <== ERRADO!
	//
	// Escalares 
	let nome: string;
	let idade: number;
	let matriculado: boolean;
	let uuid: string | number;
	let escreve: Function;
	uuid = "8752";
	uuid = 8752;
	//uuid = false; <== ERRADO!
}
{
	// Vetor de um tipo único
	let frutas = ['banana', 'laranja', 'abacaxi'];
	frutas.push('pera'); 
	frutas[2] = 'kiwi';
	//frutas.push(8752);  <== ERRADO!
	//frutas[1] = 8752;  <== ERRADO!

	// Vetor de vários Tipos
	let varios = ['banana', 8752]
	varios.push(2578)
	varios.push('laranja');
	//varios.push(true);  <== ERRADO!
	varios[1] = 'uva';
	varios[0] = 5;
	//varios[2] = false;  <== ERRADO!
	//
	let vetor = [];
	vetor.push(1);
	vetor.push("banana");
}
{
	// Vetores 
	let nomes: string[] = [];							// vetor de strings
	let mistura: (string|number|boolean)[] = [] 	// vetor de strings ou números ou booleanos
	let numeros: Array<number>; 						// vetor de números usando generics
}

{
	let aluno = { 
		nome: "Ana",
		idade: 20,
		matriculado: true,
	};

	aluno.nome = 'Katia';
	//aluno.nome = 30;  <== ERRADO!
	//aluno.disciplinas = [];  <== ERRADO!

	aluno = {
		nome: "Márcia",
		matriculado: false,
		idade: 40,
		//disciplinas = [],  <== ERRADO!
	};
}
{
	let visitante: object;	// visitante é um objeto qualquer
	visitante = { 				// logo, visitante pode ser uma estrutura
		nome: 'Renata',
		idade: 35, 
	};
	visitante = []; 				// ou um vetor
}
{
	let professor: {
		nome: string, 
		idade: number,
		ministrando: boolean,
	};

	professor = {
		nome: 'Carolina',
		idade: 50,
		ministrando: true,
		// disciplinas: [], <== ERRADO!
	};
}
{
	/*
	* Tupla 
	*/
	{
		let papel = [2, 'admim'];
		papel[1] = 1;
	}
	{
		let papel = [2, 'admin'] as [number, string];
		//papel[1] = 1; ==> ERRO!
	}
}
{
	// Tipo any (CUIDADO)
	let valor: any = 25; 
	valor = 'qualquer';
	valor = true;
	valor = { nome: "Regina", idade: 50, }
}
{
	/*
	* Enumeração 
	*/
	enum Papel {ADMIN, USER, ROOT, VISITOR, STUDENT};
	let estado: Papel;
	estado = Papel.USER;
	if(estado === Papel.USER) {
		console.log("Papel de usuário");
	}
}
{
	const circunferencia = (raio: number) => {
		return 2 * Math.PI * raio; 
	}

	console.log(circunferencia(5.7));
	//console.log(circunferencia(true)); <== ERRADO!
}
{
	const funcao = (a: number, b: number, 
					c?: number | string, 
					d: number = 32): void => {
		console.log(a+b+d);
		console.log(c) 
	}

	//funcao(1); <== ERRADO!
	funcao(1,2);
	funcao(1,2,4);
	funcao(1,2,'texto');
	funcao(1,2,4,16);
	//funcao(1,2,4,'texto'); <== ERRADO!
}
{
	// função do tipo void
	const funcao = (a: number, b: number, c?: number | string, d: number = 32): void => {
		console.log(a+b+d); 
		console.log(c)
	}

	// função do tipo numérico
	const soma = (a: number, b: number): number => {
		return a+b;
	}
}
{
	// Tipo never
	function falha(msg: string): never {
		throw new Error(msg);
	}
}
{
	const user = {
		name: "Daniel",
		age: 26,
	};
	//user.location; <== ERRADO!

	function flipCoin() {
		// Deveria ser Math.random()
		//return Math.random < 0.5; <== ERRADO!
		return Math.random() < 0.5;
	}

	const value = (Math.random() < 0.5 ? "a" : "b");
	if (value !== "a") {
		// ...
	//} else if (value === "b") {
		// Oops, unreachable
	}
}
{
	//function greet(person, date) { <== ERRADO!
	function greet(person: string, date: Date) {
		console.log(`Hello ${person}, today is ${date}!`);
	} 

	//greet("Brendan"); <== ERRADO!
	greet("Brendan", new Date());

	//greet("Brendan", "2024-01-01"); <== ERRADO!
	//greet("Brendan", Date()); <== ERRADO!
	greet("Brendan", new Date("2024-01-01"));
}