var data = new Date();
var semana = data.getDay();

switch(semana) {
    case 0:
    case 6:
        console.log('Fim de semana')
        break;
    case 1:
    case 2:
        console.log("início da semana");
        break
    case 3:
        console.log("meio da semana")
        break;
    case 4:
    case 5:
        console.log("SEXTOU!!!");
}

var seletor = 'banana'
switch(seletor) {
    case 'a':
        console.log("A");
        break;
    case 'b':
        console.log("B");
        break;
    case 'banana':
        console.log('Banana');
        break;
    case 3:
        console.log(3)
        break;
}
