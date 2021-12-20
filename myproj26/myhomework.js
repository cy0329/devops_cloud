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

// TODO: shuffle

// TODO: slicing

// TODO: input 받기
//   readline-sync 라이브러리를 설치
//   소스코드가 있는 폴더까지 이동해서 !!!
//   npm install readline-sync

const { question } = require("readline-sync");

// string
const number = question("Enter a number : ");
console.log(number);