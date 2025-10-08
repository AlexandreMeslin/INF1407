onload = function() {
	var realizaSoma = 
		document.getElementById("realizaSoma") as 
		HTMLButtonElement; 
	var numero1 = document.getElementById("numero1")! as 
		HTMLInputElement
	var numero2 = document.getElementById("numero2")! as 
		HTMLInputElement;
	realizaSoma?.addEventListener("click", function(){
		console.log(soma(parseFloat(numero1.value), 		parseFloat(numero2.value)));
	});
}

function soma(numero1: number, numero2: number) {
	return numero1 + numero2;
}
