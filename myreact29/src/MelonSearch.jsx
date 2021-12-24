import { Input, Typography } from 'antd';
import { useState } from 'react';

import { List, Avatar, Tooltip, Button, notification } from 'antd';
import { SearchOutlined } from '@ant-design/icons';
import Axios from 'axios';
import jsonpAdapter from 'axios-jsonp';

function MelonSearch() {
  const [query, setQuery] = useState('');
  const [songList, setSongList] = useState([]);

  const handleChange = (e) => {
    const {
      target: { value },
    } = e;
    console.group('handleChange');
    console.log(value);
    console.groupEnd();
    setQuery(value);
  };
  const handlePressEnter = () => {
    console.group('handlePressEnter');
    console.log(`검색어 ${query}(으)로 검색합니다.`);
    console.groupEnd();

    const url = 'https://www.melon.com/search/keyword/index.json';

    Axios({
      url: url,
      adapter: jsonpAdapter,
      callbackParamName: 'jscallback',
      params: {
        query: query,
      },
    })
      .then((response) => {
        // ALBUMCONTENTS, ARTISTCONTENTS
        const {
          data: { SONGCONTENTS: searchedSongList = [] },
        } = response;
        console.group('멜론 검색결과');
        console.log(response);
        console.log(searchedSongList);
        console.groupEnd();
        setSongList(searchedSongList);
        notification.info({
          message: '멜론 검색',
          description: `${searchedSongList.length}개의 노래 검색결과가 있습니다.`,
        });
      })
      .catch((error) => {
        console.group('멜론 검색 에러');
        console.log(error);
        console.groupEnd();

        notification.error({
          message: '멜론 검색 에러',
          // 유저 친화적인 코드는 아님!!!
          description: JSON.stringify(error),
        });
      });
  };

  const data = [{ title: '' }];
  return (
    <div style={{ width: 300, margin: '0 auto' }}>
      <h2>멜론 검색</h2>
      검색어 : {query}
      <Input
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onPressEnter={handlePressEnter}
      />
      <Tooltip title="search">
        <Button
          type="primary"
          shape="circle"
          icon={<SearchOutlined />}
          onClick={handlePressEnter}
        />
      </Tooltip>
      {songList.map((song) => (
        <List
          bordered={true}
          itemLayout="horizontal"
          dataSource={data}
          renderItem={() => (
            <List.Item>
              <List.Item.Meta avatar={<Avatar src={song.ALBUMIMG} />} />
              <Typography.Text
                onClick={() => {
                  console.log('clicked');
                }}
              >
                <a
                  href={`https://www.melon.com/song/detail.htm?songId=${song.SONGID}`}
                  target={'_blank'}
                >
                  {song.SONGNAME}
                </a>
              </Typography.Text>
            </List.Item>
          )}
        />
      ))}
    </div>
  );
}

export default MelonSearch;
