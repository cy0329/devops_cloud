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
// -----과제 by 열-----
// const number = question("Press Anything+Enter : ");
// // const { timeStamp } = require("console"); ???
// const begin_time = new Date().getTime() / 1000;

// // TODO: shuffle
// function shuffle(array) { array.sort(() => Math.random() - 0.5); }

// const animals_not_sliced = animal_names;
// shuffle(animal_names);

// const animals = animals_not_sliced.slice(0, 5);

// let ok_counter = 0

// for (animal of animals) {
//     console.log(animal)
//     const input = question(">>> ");
//     if (input == animal) {
//         ok_counter += 1
//         console.log("정확합니다!")
//     }
//     else {
//         console.log("오타가 있습니다.")
//     }
// }

// const end_time = new Date().getTime() / 1000;

// const time = end_time - begin_time

// console.log(`${ok_counter}번 맞추셨습니다. ${time.toFixed(3)}초 걸렸습니다.`)


// TODO: slicing

// TODO: input 받기
//   readline-sync 라이브러리를 설치
//   소스코드가 있는 폴더까지 이동해서 !!!
//   npm install readline-sync

// string

// ==========================

// -----과제 풀이 by 찬들+@-----
// const random_animal_names = animal_names
//     .map((name) => ({
//             name,
//             value: Math.random(),
//     }))
//     .sort((obj_a, obj_b) => {
//         return obj_a.value - obj_b.value;
//     })
//     .map(obj => {
//         return obj.value;
//     })

// 줄여본다면
const shuffled_animal_names = animal_names
    .map((name) => ({
        name,
        value: Math.random(),
    }))
    .sort((obj_a, obj_b) => {
        return obj_a.value - obj_b.value;
    })
    .map(({ name }) => name);

const begin_time = new Date().getTime(); // float
let ok_counter = 0;

for (const animal_name of shuffled_animal_names.slice(0, 5)) {
    const line = question(`${animal_name} >>> `);
    if (line === animal_name) {
        ok_counter++;
    }
}

const end_time = new Date().getTime();  // float

const time = end_time - begin_time;

console.log(`총 ${time / 1000}초가 걸렸습니다.`)  // 정수가 필요하면 parseint
console.log(`총 ${ok_counter}회 맞추셨습니다.`)