const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #8 곡명에 "사랑"이 포함된 곡들의 곡명 배열을 구성해주세요.
// Array의 filter와 map 활용
// 출력포맷 : [곡명1, 곡명2, 곡명3]

const love_songs = song_array.filter(song => song.title.includes('사랑'))
const mapped_ls = love_songs.map(
    (song) => ({ title: song.title })
)

// console.log(mapped_ls)
let lovesong = []
for (const obj of mapped_ls) {
    lovesong.push(obj.title)
}

console.log(lovesong)