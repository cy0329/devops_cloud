const animal_names = [
    "cat",
    "dog",
    "fox",
    "monkey",
    "mouse",
    "panda",
    "frog",
    "snake",
    "wolf",
];

// TODO: 현재 timestamp
const { question } = require("readline-sync");
const number = question("Press Anything+Enter : ");
// const { timeStamp } = require("console"); ???
const begin_time = new Date().getTime() / 1000;

// TODO: shuffle
function shuffle(array) { array.sort(() => Math.random() - 0.5); }

const animals_not_sliced = animal_names;
shuffle(animal_names);

const animals = animals_not_sliced.slice(0, 5);

let ok_counter = 0

for (animal of animals) {
    console.log(animal)
    const input = question(">>> ");
    if (input == animal) {
        ok_counter += 1
        console.log("정확합니다!")
    }
    else {
        console.log("오타가 있습니다.")
    }
}

const end_time = new Date().getTime() / 1000;

const time = end_time - begin_time

console.log(`${ok_counter}번 맞추셨습니다. ${time.toFixed(3)}초 걸렸습니다.`)


// TODO: slicing

// TODO: input 받기
//   readline-sync 라이브러리를 설치
//   소스코드가 있는 폴더까지 이동해서 !!!
//   npm install readline-sync

// string
