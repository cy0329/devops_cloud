const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #3 좋아요수 top10을 출력
// Array의 sort 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

// 1.
// const sorted_song_array = song_array.sort((song1, song2) => song2.like - song1.like)

// let ranking = 0;
// for (const song of sorted_song_array.slice(0, 10)) {
//     ranking++
//     console.log(`${ranking}위. ${song.like} - ${song.title}`);
// }

// 2.
let ranking = 0;
for (const song of (sorted_song_array = song_array.sort((song1, song2) => song2.like - song1.like)).slice(0, 10)) {
    ranking++
    console.log(`${ranking}위. [${song.like}] - ${song.title}`);
}