import React from 'react';
import ReactPlayer from 'react-player';
import { List, Avatar } from 'antd';
import { useState } from 'react';

function Player() {
  const video_list = [
    {
      title: '한국 급식을 처음 먹어본 영국 중학생들의 반응!?',
      youtube_id: 'https://www.youtube.com/watch?v=nxrgOqNzBcg',
      thumbnail_url:
        'https://i.ytimg.com/vi/nxrgOqNzBcg/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD5ZvUJGBb5ZCobrPA6O-umfxSV5A',
    },
    {
      title: '한국 분식을 처음 먹어본 영국 고등학생들의 반응?!',
      youtube_id: 'https://www.youtube.com/watch?v=AZxZIUQHx5Q',
      thumbnail_url:
        'https://i.ytimg.com/vi/AZxZIUQHx5Q/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDL5NlM_5uaARuJ0_ASfeb_syeRHQ',
    },
    {
      title: '흔한 한국 과자를 먹어보고 깜짝 놀란 영국 중학생들의 반응?!',
      youtube_id: 'https://www.youtube.com/watch?v=oaeEIzS1Gms',
      thumbnail_url:
        'https://i.ytimg.com/vi/oaeEIzS1Gms/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDEchvGsYT5-BgHjNKx7A-T10vjdg',
    },
    {
      title:
        '편의점 꿀조합을 처음 먹어본 영국 고등학생들의 반응!? (ft.짜파구리 마크정식)',
      youtube_id: 'https://www.youtube.com/watch?v=HICNKK-nEKc',
      thumbnail_url:
        'https://i.ytimg.com/vi/HICNKK-nEKc/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBdu7K8q9XIUWOOXpcDo_IyV4ksBA',
    },
    {
      title:
        '영국 고등학생들에게 불닭볶음면을 줘봤더니…?ㅎ🔥🥵 얘들아 미안…;;🚽',
      youtube_id: 'https://www.youtube.com/watch?v=0Pu--Gf98xY',
      thumbnail_url:
        'https://i.ytimg.com/vi/0Pu--Gf98xY/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLDK0FhChfj7jAejB-d8JUixxKciow',
    },
  ];
  // TODO: 리스트 형식으로 만들고 클릭 시 그 영상이 보여지도록

  const [youtubeUrl, setYoutubeUrl] = useState('');

  return (
    <div>
      <table>
        <tr>
          <td colspan={10}>
            {video_list.map((video) => (
              <div
                onClick={() => {
                  setYoutubeUrl(video.youtube_id);
                }}
                onMouseOver="this.style.cursor='hand'"
              >
                <h3>{video.title}</h3>
                <img src={video.thumbnail_url} />
              </div>
            ))}
          </td>
          <td colSpan={20}>
            <ReactPlayer url={youtubeUrl} />
          </td>
        </tr>
      </table>
    </div>
  );
}
export default Player;
