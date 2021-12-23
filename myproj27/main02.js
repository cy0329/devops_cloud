const { melon_data: song_array, melon_data } = require("./melon_data");
// TOOD: #2 방탄소년단의 곡명만 출력
// 출력포맷 : `가수명 곡명 좋아요수`
// Array의 filter 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Array/filter

// 1.
// const filtered_song_array = song_array.filter(song => song.artist === '방탄소년단')
// for (const song of filtered_song_array) {
//     console.log(song.artist, song.title);
// }

// 2.
// for (const song of filtered_song_array = song_array.filter(song => song.artist === '방탄소년단')) {
//     console.log(song.artist, song.title, [song.like]);
// }


// -----solution-----
// 값 비교는 =를 3개 쓰는게 맞는 표현
const bts_song_array = song_array
    .filter(({ artist }) => artist === "방탄소년단")
// artist만 뽑아서 볼거라면 위 방식대로 {}로 묶어서 가능
// 이때는 song. 은 다 빼야함

for (const { artist, title, like } of bts_song_array) {
    console.log(artist, title, like)
}
// ---------------