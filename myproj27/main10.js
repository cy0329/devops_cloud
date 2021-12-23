const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #10 방탄소년단의 좋아요의 총 합은?
// Array의 filter와 reduce를 활용해주세요.
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/Reduce

const BTS_song = song_array.filter(song => song.artist == '방탄소년단')
// const reducer = (prevValue, currValue) => prevValue + currValue;

// console.log(likes_BTS)
let BTSlikes = []
for (const obj of BTS_song) {
    BTSlikes.push(obj.like)
}
console.log(`BTS 좋아요 총합 : ${BTSlikes.reduce((a, b) => a + b)}`)


// -----solution-----

Array.prototype.sum = function () {
    return this.reduce((acc, element) => {
        return acc + element;
    }, 0);
}


const result = song_array
    .filter(
        ({ artist }) => artist === "방탄소년단"
    )
    // .reduce((acc, { like }) => acc + like, 0);
    // 줄인 것임, 원래 방식 생각해보고 줄이는 것 공부
    .map(({ like }) => like)
    .sum();

console.log(result)