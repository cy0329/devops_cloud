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
// for (const song of sorted_song_array = song_array.sort((song1, song2) => song1.like - song2.like)) {
//     console.log(song.like, song.title);
// }

// -----solution-----

// JS에서 Array의 sort는 자신(array)의 순서도 변경하고, 자신을 반환
// Python에서 List의 sort는 자신(List)의 순서만 변경하고, 리턴값이 없음.(None)
song_array
    .sort(
        (song1, song2) => {
            return song1.like - song2.like;
            //song2가 크면, 음수를 반환
            //song1이 크면, 양수를 반환
            //같으면 0을 반환
        }
    )

// 에로우 펑션에서는 {}를 사용하면 안됨
// ==> "{" = 함수의 시작, "}" = 함수의 끝

for (const { like, title } of song_array) {
    console.log(like, title);
}
// --------------