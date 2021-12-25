import React from 'react';
import ReactPlayer from 'react-player';
import { Layout, List, Avatar } from 'antd';
import { useState } from 'react';

function Player2() {
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
    {
      title: '삼겹살에 치즈김치볶음밥 처음 먹어본 영국 고등학생들의 반응!?',
      youtube_id: 'https://www.youtube.com/watch?v=xnI1QBVKJEI',
      thumbnail_url:
        'https://i.ytimg.com/vi/xnI1QBVKJEI/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCGW0Jt2EFzDq2J3GEeMQHWfE7umQ',
    },
    {
      title: '김밥천국을 먹어본 영국 고등학생들의 반응?!',
      youtube_id: 'https://www.youtube.com/watch?v=VgFA7K-4kn4',
      thumbnail_url:
        'https://i.ytimg.com/vi/VgFA7K-4kn4/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLCKzbLPx8kDPtM235EEonHqToGYYw',
    },
    {
      title: '수능 영어를 풀어본 영국 고등학생들…!!?',
      youtube_id: 'https://www.youtube.com/watch?v=M_uGV2L5q3s',
      thumbnail_url:
        'https://i.ytimg.com/vi/M_uGV2L5q3s/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLB6ycxTTihFQhijvUi7xYbDd1MC3Q',
    },
    {
      title: '길거리토스트 처음 먹어본 영국 고등학생들의 반응!?',
      youtube_id: 'https://www.youtube.com/watch?v=P5zouxkguEM&t=4s',
      thumbnail_url:
        'https://i.ytimg.com/vi/P5zouxkguEM/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLD7VlsTCObaPOowi66fqljhZAcxIA',
    },
    {
      title: '한국 길거리 토스트 먹어 본 특별게스트들 반응은!? 🤭',
      youtube_id: 'https://www.youtube.com/watch?v=uf2yiQDTuUE',
      thumbnail_url:
        'https://i.ytimg.com/vi/uf2yiQDTuUE/hqdefault.jpg?sqp=-oaymwEcCPYBEIoBSFXyq4qpAw4IARUAAIhCGAFwAcABBg==&rs=AOn4CLBI9ltSymZazZE4hkUvTuuZN9FFJQ',
    },
  ];
  // TODO: 리스트 형식으로 만들고 클릭 시 그 영상이 보여지도록

  const [youtubeUrl, setYoutubeUrl] = useState('');

  return (
    <>
      <table>
        {video_list.map((video) => (
          <tr>
            <td>
              <div
                onClick={() => {
                  setYoutubeUrl(video.youtube_id);
                }}
                onMouseOver="this.style.cursor='hand'"
              >
                <img src={video.thumbnail_url} />
                <h3>{video.title}</h3>
              </div>
            </td>
          </tr>
        ))}
        <td>
          <ReactPlayer url={youtubeUrl} />
        </td>
      </table>
    </>
  );
}
export default Player2;
