const { melon_data: song_array, melon_data } = require("./melon_data");
// TODO: #5 좋아요수가 200,000이상인 곡명에 대해서, 곡명 오름차순 정렬
// Array의 filter와 sort를 연계
// 출력포맷 : `[좋아요수] 곡명 가수명`

// 1.
const filtered_songs = song_array.filter(song => song.like >= 200000);
const filter_sorted_songs = filtered_songs.sort((song1, song2) => {
    if (song1.title < song2.title) {
        return -1
    }
    else if (song1.title > song2.title) {
        return 1
    }
    else {
        return 0
    }
}
);

for (const song of filter_sorted_songs) {
    console.log([song.like], song.title, song.artist);
}