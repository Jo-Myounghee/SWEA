const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

let input = [];
let max_val = 0;
let min_val = 1000000;

rl.on('line', line => {
  const nums = line.split(' ')
  for (i=0; i<nums.length; i++) {
    let num = parseInt(nums[i])
    input.push(num)
  }
})
  .on('close', () => {
    let N = input.shift()
    for (i=0; i<N; i++) {
      if (input[i] < min_val) {
        min_val = input[i]
      } else {
        if (input[i] > max_val) {
          max_val = input[i]
        }
      }
    }
    console.log(min_val, max_val)
  process.exit();
});