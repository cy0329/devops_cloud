const { melon_data: song_array, melon_data } = require("./melon_data");
// // TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// // Array의 filter와 map 활용
// // 출력포맷 : [곡명1, 곡명2, 곡명3]

// const filtered_song_array = song_array.filter(song => song.artist === '방탄소년단')
// const mapped_fsa = filtered_song_array.map(
//     (song) => ({ title: song.title })
// )

// // console.log(mapped_fsa)
// let BTS_titles = []
// for (const obj of mapped_fsa) {
//     BTS_titles.push(obj.title)
// }

// console.log(BTS_titles)


// // -----solution-----

const bts_title_array = song_array
    .filter(({ artist }) => artist === '방탄소년단')
    .map(({ title }) => title);

for (const title of bts_title_array) {
    console.log(title);
}

// =======reduce 설명(가장 간단한 예)===========
// const numbers = [1, 2, 3, 4, 5];

// 1.
// const new_numbers = numbers.map(number => number * number)
// console.log(new_numbers);

// 2.
// const new_numbers = numbers.reduce((acc, number) => {
//     acc.push(number * number);
//     return acc;
// }, []);
// console.log(new_numbers);

// 3.
// const new_numbers_object = numbers.reduce((acc, number) => {
//     acc[number] = number * number;
//     return acc;
// }, {})
// console.log(new_numbers_object)


// const result_sum = numbers.reduce((acc, number) => {
//     acc += number;
//     return acc;
// })

// console.log(`합 : ${result_sum}`);