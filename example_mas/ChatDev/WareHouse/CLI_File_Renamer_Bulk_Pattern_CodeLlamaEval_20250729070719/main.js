const { renameFiles } = require('./renamer');
const pattern = process.argv[2];
const directory = process.argv[3];
renameFiles(pattern, directory);