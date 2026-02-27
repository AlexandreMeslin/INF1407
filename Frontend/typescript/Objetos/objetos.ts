{
	let pessoa1: { 			// variável com campos mas sem valores
		nome: string; 		// note o uso de ; ao especificar tipo
		idade: number; 
	}

	let estudante1 = {		// variável com campos com valores
		nome: 'Sandra',		// note o uso de , ao especificar valor
		idade: 15,
	}

	const estudante2 = {	// constante com campos e valores
		nome: 'Paula',
		idade: 18
	}
}
{
	let estudante3: { // não precisa ser tão detalhista
		nome: string;
		idade: number; 
	} = {
		nome: 'Fernanda',
		idade: 12,
	}

	const pessoa2: { // não precisa ser tão detalhista
		nome: string;
		idade: number;
	} = {
		nome: 'Fernanda',
		idade: 12,
	}
}
