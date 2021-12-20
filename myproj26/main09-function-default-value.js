// 아래 3개는 같은 것
const get_default_value = () => {
    console.log("get_default_value() 함수 호출")
    return 10;
};
// const get_default_value = () => {
//     return 10;
// };

// function get_default_value() {
//     return 10;
// }

function hello(name, age = get_default_value()) {
    console.log(`안녕. 나는 ${name}이야. ${age}살이지.`);
}

hello("Tom", 10);
hello("Steve", 14);
hello("John", 18);