const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #11 멜론 top100 리스트에 랭크된 가수는 총 몇 팀인가요?
// Set와 속성 .size를 활용
// ref: https://developer.mozilla.org/ko/docs/Web/JavaScript/Reference/Global_Objects/Set

// 1.
// const mapped_songs = song_array.map((song) => ({ artist: song.artist }))

// let artist_set = new Set();
// for (const obj of mapped_songs) {
//     artist_set.add(obj.artist)
// }

// console.log(`TOP100 랭크된 가수 팀 수 :${artist_set.size}`)

// 2. (.add 안쓰고)
const mapped_songs = song_array.map((song) => (song.artist))
let artist_set = new Set(mapped_songs);


console.log(`TOP100 랭크된 가수 팀 수 :${artist_set.size}`)