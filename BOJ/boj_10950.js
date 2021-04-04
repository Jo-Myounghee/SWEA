const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];

const printAnswer = input => {
  const A = parseInt(input[0])
  const ans = parseInt(input[0]) + parseInt(input[1])
  console.log(ans)
  // for (let i=0; i<N; i++) {
  //   const value = parseInt(input[1][i])
  //   minValue = minValue > value ? value : minValue;
  //   maxValue = maxValue < value ? value : maxValue;
  // }
  // console.log(minValue, maxValue);
}

rl.on('line', line => {
  input.push(line.split(' '))
})
  .on('close', () => {
    printAnswer(input)
    process.exit();
});