const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.

const BTS_songs = song_array.filter(song => song.artist === '방탄소년단')

const reducer = (pv, cv) => pv.like > cv.like ? pv : cv;
// console.log(like_of_BTS_song)


console.log(`좋아요수가 최고인 BTS 노래 :${BTS_songs.reduce(reducer).title}`)