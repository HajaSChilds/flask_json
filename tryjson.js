
var person = {"name": "Andrew", "loves" : "Open Source"};
var asJSON = JSON.stringify(person);

console.log(`person is of type ${typeof person}`);
console.log(`asJSON is of type ${typeof asJSON}`);

var asObject = JSON.parse(asJSON);
console.log(`asObject is of type ${typeof asObject}`);

console.log(asJSON);
console.log(asObject);