var a;
var b;
var c;

a = 5;
b = 7.1;
c = 5;

var d = '5';

console.log("a == b?", a == b);
console.log("a == c?", a == c);
console.log("a == d?", a == d);
console.log("a === d?", a === d);

console.log("typeof a", typeof a);
console.log("typeof b", typeof b);
console.log("typeof d", typeof d);

var pi = '3.14'
a = parseFloat(pi);
console.log("typeof a", typeof a, "a =", a);
b = parseInt(pi);
console.log("typeof b", typeof b, "b =", b);
