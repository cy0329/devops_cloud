// 바뀌지 않는 데이터
// 전역 변수 : 바뀌지 않는 데이터

import { useState } from 'react';
import initialSongList from './data/melon_data.json';
//    - 초기값을 정의

function MelonTop100() {
  const [songList, setSongList] = useState([]);

  const handleClick = () => {
    setSongList(initialSongList);
  };

  return (
    <div>
      <h2>멜론 top 100</h2>
      <button onClick={handleClick}>로딩</button>
      <ul>
        {songList.map((song) => {
          return <li>{song.title}</li>;
        })}
        <li>제목1</li>
        <li>제목2</li>
        <li>제목3</li>
      </ul>
    </div>
  );
}

export default MelonTop100;
