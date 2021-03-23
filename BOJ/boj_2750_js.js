const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

rl.on('line', line => {
  input.push(line)
})
  .on('close', () => {
  let N = input.shift();
  N = parseInt(N);
  input.sort((a, b) => a-b)
  for (i=0; i<N; i++) {
    console.log(input[i])
  }
  process.exit();
});