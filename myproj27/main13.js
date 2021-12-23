const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #13 방탄소년단의 곡 중에 좋아요 수가 가장 큰 곡명은?
// Array의 filter와 reduce를 활용해주세요.

// const BTS_songs = song_array.filter(song => song.artist === '방탄소년단')

// const reducer = (pv, cv) => pv.like > cv.like ? pv : cv;
// // console.log(like_of_BTS_song)


// console.log(`좋아요수가 최고인 BTS 노래 :${BTS_songs.reduce(reducer).title}`)


// -----solution-----
// 1. 
// song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .reduce((acc, song) => {
//         if (!acc || acc.like < song.like)
//             return song;
//         else
//             return acc;
//     }, null);

// // if 문 안쪽 내용 이해 = main12 주석 참조
// // acc : null  곡1.like=100    =>  곡1 이라는 객체를 남기고
// // acc : 곡1(100)  곡2(200)    =>  곡2 라는 객체를 남긴다

// // ***위에서 초기 값(null)을 지정해주지 않으면 "!acc ||" 이 부분은 빼도 됨***
// song_array
//     .filter(({ artist }) => artist === "방탄소년단")
//     .reduce((acc, song) => {
//         if (acc.like < song.like)
//             return acc.like < song.like ? song : acc;
//     });

// 2.
Array.prototype.max = function (key_fn) {
    return this.reduce((acc, song) => {
        // key_fn(acc);  // 정렬 기준값을 뽑아줌
        // key_fn(song);
        return key_fn(acc) < key_fn(song) ? song : acc;
    });
};

const top_song = song_array
    .filter(({ artist }) => artist === "방탄소년단")
    .max(song => song.like);  // max(key_fn) 형식

console.log(top_song)