const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

// 1.
// const filtered_songs = song_array.filter(song => song.like >= 200000);
// const filter_sorted_songs = filtered_songs.sort((song1, song2) => {
//     if (song1.title < song2.title) {
//         return -1
//     }
//     else if (song1.title > song2.title) {
//         return 1
//     }
//     else {
//         return 0
//     }
// }
// );

// for (const song of filter_sorted_songs) {
//     console.log([song.like], song.title, song.artist);
// }


// -----solution-----
function compare_string_for_sort(string1, string2, is_ascending = true) {
    if (string1 < string2) {
        // 3항 연산자 (c, c++, java 등)
        return is_ascending ? -1 : 1;
    }
    else if (string1 > string2) {
        return is_ascending ? 1 : -1;
    }
    else {
        return 0
    }
}

const new_song_array = song_array
    .filter(({ like }) => like >= 200_000)
    .sort(
        (song1, song2) => {
            return compare_string_for_sort(song1.title, song2.title, true)
        }
    );

for (const { like, title, artist } of new_song_array) {
    console.log(`[${like}] ${title} ${artist}`)
}

        // 오름차순
        // song1이 song2보다 크다면, 음수를 반환
        // song1이 song2보다 작다면, 양수를 반환
        // 내림차순
        // song1이 song2보다 크다면, 양수를 반환
        // song1이 song2보다 작다면, 음수를 반환