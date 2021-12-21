const numbers = [1, 3, 5, 4, 2];

// Array의 sort
function make_random_value(number1, number2) {
    return Math.random();
}

// -- 체이닝 --
const new_numbers = numbers.map(
    (number) => ({ number, 기준값: Math.random() }),
)
// .sort(
//     (value1, value2) => {
//         return value1.기준값 - value2.기준값;
//     }
// ).map(
//     (value) => value.number
// );

console.log(new_numbers);

// js 에서 sort는 비교함수 --> 값을 두 개 받아야 함



// 새로운 Array(배열), 제곱수로 구성된 숫자 배열
// function mapper(number) {
//     return number ** 2;
// }

// const mapper = (number) => {
//     return number ** 2;
// }

// const mapper = (number) => number ** 2;

// const mapper = number => number ** 2;

// const new_numbers = numbers.map(mapper);
// console.log(new_numbers);

// const new_numbers = numbers.map(
//     number => number ** 2
// );
// console.log(new_numbers);