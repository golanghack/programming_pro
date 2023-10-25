#! /usr/bin/env node 

const fs = require('fs');
const path = require('path');
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

async function listDirContents(filepath: string) {
    try {
    const files = await fs.promises.readdir(filepath);
    const detailFilesPromises = files.map(async (file: string) => {
        let fileDetails = await fs.promises.lstat(path.resolve(filepath, file));
        const { size, birthtime } = fileDetails;
        return { filename: file, 'size(kB)': size, created_at: birthtime};
    });
    const detailFiles = await Promise.all(detailFilesPromises);
    console.table(detailFiles);
    } catch (error) {
        console.error('Error -> ', error);
    }
}


function createDir(filepath: string) {
    if (!fs.existSync(filepath)) {
        fs.mkdirSync(filepath);
        console.log('Directory has been created!');
    }
}


function createFile(filepath: string) {
    fs.openSync(filepath, 'w');
    console.log('An e,pty file created');
}

if (options.ls) {
    const filepath = typeof options.ls === 'string' ? options.ls: __dirname;
    listDirContents(filepath);
}

if (options.mkdir) {
    createDir(path.resolve(__dirname, options.mkdir));
}

if (options.touch) {
    createFile(path.resolve(__dirname, options.touch));
}