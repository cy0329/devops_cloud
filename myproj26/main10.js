const mysum2 = (x, y) => { x, y };  // 코드 블럭을 쓰겠다는 의미, 중괄호는 코드의 시작을 의미
console.log(mysum2(1, 2));  // return 이 없으므로 undefined


const mysum3 = (x, y) => {
    return { x, y };
};
console.log(mysum3(1, 2));

const mysum4 = (x, y) => ({ x, y });  // 객체를 바로 리턴할 목적이라면 소괄호로 묶어주어야...
console.log(mysum4(1, 2));