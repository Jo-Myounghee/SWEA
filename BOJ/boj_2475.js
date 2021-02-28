const readline = require('readline');

const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout
});

rl.on('line', line => {
  const nums = line.split(" ")
  let doubles = 0

  nums.forEach(num => {
    doubles += (num * num)
  })

  console.log(doubles % 10)

  rl.close();
}).on("close", () => {
  process.exit();
});