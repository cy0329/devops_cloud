const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #14 방탄소년단의 곡 중에 좋아요 수가 가장 작은 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const BTS_songs = song_array.filter(song => song.artist === '방탄소년단')

const reducer = (pv, cv) => pv.like > cv.like ? cv : pv;
// console.log(like_of_BTS_song)

let likes_list = []
console.log(`좋아요수가 최저인 BTS 노래: ${BTS_songs.reduce(reducer).title}`)