const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #9 좋아요수가 200,000이상인 곡들의 곡명 리스트를 만들어보세요.
// Array의 filter와 map 활용

const over_200th_like = song_array.filter((song) => song.like >= 200000);
const song_titles = over_200th_like.map(
    (song) => ({ title: song.title })
)

let like200thSong = []
for (const obj of song_titles) {
    like200thSong.push(obj.title)
}

console.log(like200thSong)


// -----solution-----
// 체이닝을 써주는게 깔끔
const over_20th_like_songs = song_array
    .filter(({ like }) => like >= 200000)
    .map(({ title }) => title)

console.log(over_20th_like_songs)