const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set


let songA = new Set();

for (const song of song_array) {
    let song_count = 0;
    if (!songA.add(song.artist)) {
        song_count++
    }
    return songA, song_count
}
console.log(songA, song_count)
/*
TODO:
set 하면 중복된 값이 제거됨 -> 그때마다 카운트 시키면..
new Set으로 하나 만들고
for 문에서 if문으로 .add가 된다면 -> 카운트
카운트 값과 artist를 객체로 생성
카운트 값이 1이상인 객체들을 리스트화(array)
.size? .length
*/