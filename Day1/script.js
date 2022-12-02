const fs = require('fs');

const findTop = (elves) => {
  const sums = [];

  for (let i = 0; i < elves.length; i++) {
    let totalCalories = 0;
    for (let j = 0; j < elves[i].length; j++) {
      totalCalories += elves[i][j];
    }

    sums.push(totalCalories);
  }

  sums.sort((a, b) => b - a);

  return [sums[0], sums[1], sums[2]];
};

fs.readFile('./input.txt', 'utf-8', (err, data) => {
  if (err) {
    console.error(err);
    return;
  }

  const split = data.split('\n');
  const parsedData = [];
  let elf = [];
  for (let i = 0; i < split.length; i++) {
    if (split[i] === '') {
      parsedData.push(elf);
      elf = [];
    } else {
      elf.push(parseInt(split[i], 10));
    }
  }
  const top = findTop(parsedData);
  const totalTopCalories = top.reduce((a, v) => a + v);

  console.log(`The elf carrying most calories is carrying ${top[0]}`);
  console.log(`The top three elves are carrying in total ${totalTopCalories}`);
});
