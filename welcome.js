const readline = require("readline");
const rl = readline.createInterface({
  input: process.stdin,
  output: process.stdout,
});

const getName = () => {
  return new Promise((resolve) => {
    rl.question("Enter your name", (name) => {
      console.log(`Your name is ${name}`);
      rl.close();
      resolve(name);
    });
  });
};

function welcome(name) {
  console.log(`Welcome ${name}`);
}

welcome("ABED");
