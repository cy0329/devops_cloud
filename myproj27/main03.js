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
// let ranking = 0;
// for (const song of (sorted_song_array = song_array.sort((song1, song2) => song2.like - song1.like)).slice(0, 10)) {
//     ranking++
//     console.log(`${ranking}위. [${song.like}] - ${song.title}`);
// }


// -----solution-----
// 좋아요 수에 대한 내림차순 정렬 -> 처음 10개
const like_top10 = song_array
    .sort(
        (song1, song2) => song2.like - song1.like,
    )
    .slice(0, 10)

// 좋아요 수에 대한 오름차순 정렬 -> 마지막 10개 -> 뒤집음 (이 방법도 있다.)

for (const { like, title, artist } of like_top10) {
    console.log(`[${like}] ${title} by ${artist}`)
}

// // index 붙이기, enumerate == entries
// for (const [index, { like, title, artist }] of like_top10.entries()) {
//     console.log(`${index + 1} [${like}] ${title} by${artist}`);
// }