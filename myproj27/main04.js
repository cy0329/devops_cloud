const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #4 좋아요수가 200,000 이상인 곡명만 출력하기
// Array의 filter 활용
// 출력포맷 : `[좋아요수] 곡명 가수명`

// 1.
// const gt200000_likes_song = song_array.filter(song => song.like >= 200000)

// for (const song of gt200000_likes_song) {
//     console.log(song.like, song.title, song.artist);
// }

// 2.
for (const song of gt200000_likes_song = song_array.filter(song => song.like >= 200000)) {
    console.log([song.like], song.title, song.artist);
}