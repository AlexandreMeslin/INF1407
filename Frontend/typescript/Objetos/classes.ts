class Pessoa {
	constructor(
		private nome: string,
		readonly email: string,
		public idade: number,
	) { 
	}

	cumprimenta(): void {
		// this.email = "outroEmail@example.com"; <== errado (readonly)
		console.log(`Oi, eu sou ${this.nome}`);
	}
}

const pessoa = new Pessoa("Sandra", 'sandra@example.com', 15);
pessoa.cumprimenta(); 

let pessoas: Pessoa[] = [];
pessoas.push(pessoa);

// pessoa.nome = 'Paula'; <== errado (private)
// pessoa.email = "outroEmail@example.com"; <== errado (readonly)

pessoas.forEach(pessoa => {
	// console.log("Pessoa:", pessoa.nome); <== errado (private)
	console.log("Pessoa:", pessoa.email, pessoa.idade);
});
