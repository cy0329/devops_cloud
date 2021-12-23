// 바뀌지 않는 데이터
// 전역 변수 : 바뀌지 않는 데이터

import { useState } from 'react';
import { Button as AntdButton } from 'react-bootstrap';
import { Button as BootstrapButton } from 'antd';
import initialSongList from './data/melon_data.json';
import './MelonTop100.css';
import 'bootstrap/dist/css/bootstrap.min.css';
import 'antd/dist/antd.css';

//    - 초기값을 정의

function MelonTop100() {
  const [songList, setSongList] = useState([]);

  const handleClick = () => {
    setSongList(initialSongList);
  };

  return (
    <div>
      <h2>멜론 top 100</h2>
      <AntdButton variant="success" onClick={handleClick}>
        로딩
      </AntdButton>
      <BootstrapButton type="primary" onClick={handleClick}>
        로딩
      </BootstrapButton>
      <ul className="songList">
        {songList.map((song) => {
          return (
            <li key={song.song_no}>
              {song.rank} {song.title} by {song.artist} {song.like} likes
            </li>
          );
        })}
      </ul>
    </div>
  );
}

export default MelonTop100;
