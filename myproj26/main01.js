
//
// 변수/상수 선언
//

// var name = "김최열";  // 선언
// name = "스티브";  // 변경

// 변수
let name = "김최열"  // 선언
name = "스티브";  // 변경

// 상수(Constant) - 처음 만들때 지정할 수 있고 바꾸는건 불가
const age = 10;
// age = 12;  // 상수는 값을 변경할 수 없다.

// console.log(name, age);

//
// 제어구조
//

const number = 10;
if (number % 2 === 0) {
    console.log("짝수"); // 들여쓰기 없어도 에러는 안남(읽기 어려울 뿐)
}
else {
    console.log("홀수");
}

for (let i = 1; i < 11; i++) {
    console.log(i);
}

for (let i = 1; i < 11; i += 2) {
    console.log(i);
}

//
// 함수
//

function mysum(x, y) {
    return x + y
}

// 호출 (똑같음)
console.log(mysum(1, 2))

// 익명함수
const mysum2 = function (x, y) {
    return x + y;
};

// arrow function
const mysum3 = (x, y) => {
    return x + y
};

const mysum4 = (x, y) => x + y;

// 2,4 방식을 가장 많이 씀


function mysum5(x, y, ...args) {
    console.log(x, y, args);
}

mysum5(1, 2, 3, 4, 5);
// js에는 기본적으로 sum이라는 내장함수가 없음 => 직접 만들어줘야함



function reducer(prevValue, currentValue) {
    return prevValue + currentValue;
}

// array (계열) [1,2,3,4,5]
const result = [1, 2, 3, 4, 5].reduce(reducer, 0);
console.log(result);


const result2 = [1, 2, 3, 4, 5].reduce((prevValue, currentValue) => {
    return prevValue + currentValue;
}, 0);

console.log(result2)


const result3 = [1, 2, 3, 4, 5].reduce((prevValue, currentValue) => prevValue + currentValue, 0);

console.log(result3)

const result4 = [1, 2, 3, 4, 5].reduce((x, y) => x + y, 0);

console.log(result3)