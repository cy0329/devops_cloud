
// 객체
// const age = "나이";

// const tom = {
//     "name": "Tom",
//     // "age": 10,
//     // age: 10,
//     // ["ag" + "e"]: 10,
//     [age]: 10,
// }
// js에서는 key를 문자열로 쓰지 않아도 똑같음
// 대괄호로 묶어주는 것은 계산해주라는 뜻
// console.log(tom);

// const name = "Tom";
// const age = 10;
// const tom1 = {
//     "name": name,
//     "age": age,
// }
// 좀 더 줄이는 문법이 있다.
// key에서 문자열 아니어도 됨
// key와 value가 같으면 value 생략 가능
const name = "Tom";
const age = 10;
const tom1 = {
    name,
    age: age,
    print() {
        // console.log(this.name, this.age);

        // Template Literals
        console.log(`안녕, 나는 ${this.name}이야. 
        ${this.age}살이지`);
    }
}

tom1.print();