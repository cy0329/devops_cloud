const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #7 방탄소년단의 곡명 문자열로 구성된 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const filtered_song_array = song_array.filter(song => song.artist == '방탄소년단')
const mapped_fsa = filtered_song_array.map(
    (song) => ({ title: song.title })
)

// console.log(mapped_fsa)
let BTS_titles = []
for (const obj of mapped_fsa) {
    BTS_titles.push(obj.title)
}

console.log(BTS_titles)