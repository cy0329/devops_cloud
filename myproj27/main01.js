const { melon_data: song_array, melon_data } = require("./melon_data");


// TODO: like 오름차순으로 정렬
// for (const song of song_array) {
//     console.log(song.like, song.title);
// }


// // 1.
// const sorted_song_array = song_array.sort(
//     (song1, song2) => {
//         return song1.like - song2.like;
//     }
// )

// for (const sorted_song of sorted_song_array) {
//     console.log(sorted_song.like, sorted_song.title);
// }

// // 2.
// sorted_song_array = song_array.sort((song1, song2) => song1.like - song2.like)
// for (const song of sorted_song_array) {console.log(song.like, song.title);}

// 3.
for (const song of sorted_song_array = song_array.sort((song1, song2) => song1.like - song2.like)) {
    console.log(song.like, song.title);
}