const  { Command } = require("commander");
const figlet = require( "figlet" );

const program = new Command();

console.log(figlet.textSync("Simple File Manager"));

program
    .version("1.0.0")
    .description("Simple file manager")
    .option("-l, --ls, [value]", "List directory and containts")
    .option("-m, --mkdir <value>", "Create a dir")
    .option("-t, --touch <value>", "Create a file")
    .parse(process.argv);

const options = program.opts();
