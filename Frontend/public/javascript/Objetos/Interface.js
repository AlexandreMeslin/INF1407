"use strict";
class Mamifero {
    constructor(especie, peso) {
        this.especie = especie;
        this.peso = peso;
        console.log(`Criando ${this.especie} com ${this.peso} kg.`);
    }
    anda(distancia) {
        console.log(`${this.especie} andando ${distancia} metros.`);
    }
}
class Cachorro extends Mamifero {
    fala(qtd) {
        let voz = '';
        for (let i = 0; i < qtd; i++) {
            voz += 'Au! ';
        }
        return voz;
    }
}
class Porco extends Mamifero {
    constructor(peso, especie) {
        if (especie === undefined)
            super('Porco', peso);
        else
            super(especie, peso);
    }
    fala(qtd) {
        let voz = '';
        for (let i = 0; i < qtd; i++) {
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
let arcaDeNoe = [];
arcaDeNoe.push(porco);
arcaDeNoe.push(cachorro);
console.log("Na Arca, temos", arcaDeNoe);
