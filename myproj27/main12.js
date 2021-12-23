const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #12 2곡 이상 랭크된 가수는 총 몇 팀인가요?
// reduce, Set

// const Artistcount = song_array.reduce((allArtist, song) => {
//     if (song.artist in allArtist) {
//         allArtist[song.artist]++
//     }
//     else {
//         allArtist[song.artist] = 1
//     }
//     return allArtist
// }, {});

// console.log(allArtist)

// const filtered_artist = Object.values(Artistcount).filter(
//     (value) => (value > 1)
// );

// console.log(filtered_artist.length)

/*
TODO:
set 하면 중복된 값이 제거됨 -> 그때마다 카운트 시키면..
new Set으로 하나 만들고
for 문에서 if문으로 .add가 된다면 -> 카운트
카운트 값과 artist를 객체로 생성
카운트 값이 1이상인 객체들을 리스트화(array)
.size? .length
*/

// -----solution-----
// 1. 처음엔 이 형태로 만들 것임
// {
//     "가수1": 2,
//     "가수2": 10,
//     "가수3": 3,
// }


// artist 값이 없을 때 접근하면 undefined 뜸
const artist_count_object = song_array
    .reduce((acc, { artist }) => {
        // if (!acc[artist]) acc[artist] = 0;
        // python version
        // if artist not in acc:
        //     acc[artist] = 0
        acc[artist] ||= 0;   // js 14 버전에는 없는 문법
        acc[artist] += 1;
        return acc;
    }, {});
// 위의 ||=(or) 의 의미 = 참이면(존재하면) 그 키의 값을 그대로 활용, 거짓이면 그 키의 값을 0으로 대입하겠다.
// 원래 acc[artist] = acc[artist] || 0; 
// python 에서 사전의 경우 d.key[0] , d.value[0], d.items[0] 이런것을 Object.key value 등으로 씀
console.log(Object.values(artist_count_object)
    .filter(number => number >= 2)
    .length
);

// console.log(artist_count_object)