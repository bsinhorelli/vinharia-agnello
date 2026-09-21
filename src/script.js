alert("Vamos cadastrar um novo vinho! Responda às perguntas a seguir.");

// coleta de dados do vinho para cadastro.
var nomeVinho = prompt("Nome do Vinho: ");
var tipoVinho = prompt("Tipo (Branco, Tinto, Rosé): ");
var safraVinho = prompt("Safra (ano): ");
var quantEstoque = prompt("Quantidade em estoque: ");

alert("Cadastro realizado! Veja os detalhes no console.");

alert("abrindo console");

console.log(`
Vinho: ${nomeVinho} 
Tipo de vinho:${tipoVinho} 
Safra: ${safraVinho} 
Quantidade em estoque: ${quantEstoque}
`);
