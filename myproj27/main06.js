const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #6 "곡명 / 단어수" 배열을 구성해주세요.
// Array의 map 활용
// 100줄에서 한 줄 출력의 예: `Dynamite / 1`

const song_dict = song_array.map(
    (song) => ({ title: song.title, words: song.title.split(' ') }),
);

// console.log(song_dict)

for (const obj of song_dict) {
    console.log(`${obj.title} / ${obj.words.length}`)
}

