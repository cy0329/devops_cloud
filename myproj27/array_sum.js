// prototype 정의시에 arrow function을 절대 쓰지 않는다.
// this 가 동작하려면 function을 써야함
Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
}


const result = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10].sum(); // 15
console.log(result);