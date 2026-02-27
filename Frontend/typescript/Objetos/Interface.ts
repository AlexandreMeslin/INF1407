interface Animal {
    readonly especie: string;
    anda(distancia: number): void;
    fala(qtd: number): string;
}

abstract class Mamifero implements Animal {
    peso: number; 
    
    constructor(public especie: string, peso: number) {
        this.peso = peso;
        console.log(`Criando ${this.especie} com ${this.peso} kg.`);
    }
    
    anda(distancia: number): void {
        console.log(`${this.especie} andando ${distancia} metros.`);
    }

    abstract fala(qtd: number): string;
}

class Cachorro extends Mamifero {
    fala(qtd: number): string {
        let voz = ''
        for(let i=0; i<qtd; i++) {
            voz += 'Au! ';
        }
        return voz;
    }
}

class Porco extends Mamifero {
    constructor(peso: number, especie?: string) {
        if(especie === undefined) super('Porco', peso);
        else super(especie, peso);
    }
    fala(qtd: number): string {
        let voz = ''
        for(let i=0; i<qtd; i++) {
            voz += 'Ronc! ';
        }
        return voz;
    }
} 

let porco = new Porco(52, "Porco");
let outroPorco = new Porco(87);
let cachorro = new Cachorro("Cachorro", 25);
console.log(porco.fala(5));
console.log(cachorro.fala(2)); 
porco.anda(3);
cachorro.anda(4);

let arcaDeNoe: Animal[] = []; 
arcaDeNoe.push(porco);
arcaDeNoe.push(cachorro);
console.log("Na Arca, temos", arcaDeNoe);
