import { useEffect, useState } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [pageList, setPageList] = useState([]);
  const [errorObject, setErrorObject] = useState(null);
  const handleRefresh = () => {
    setErrorObject(null);
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const profileList = response.data.map((profile) => ({
          ...profile,
          uniqueID: profile.unique_id,
          profileImageUrl: profile.profile_image_url,
          instagramUrl: profile.instagram_url,
        }));
        setPageList(profileList);
      })
      .catch((error) => setErrorObject(error));
  };

  useEffect(() => handleRefresh(), []);

  const [query, setQuery] = useState('');

  const handleChange = (e) => {
    const value = e.target.value;
    console.log(value);
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      console.log('ENTER');
      const value = e.target.value;
      setQuery(value);
    }
  };

  return (
    <div>
      <h2>Page Profile</h2>
      <input
        type="text"
        placeholder="검색어를 입력해주세요."
        onChange={handleChange}
        onKeyPress={handleKeyPress}
      />

      <br />
      <button onClick={() => setPageList([])}>clear</button>
      <button onClick={handleRefresh}>refresh</button>
      {errorObject && (
        <h3>조회시에 오류가 발생하였습니다. 잠시 후 다시 시도해주세요.</h3>
      )}
      {pageList.length === 0 && <h4>등록된 프로필이 없습니다.</h4>}
      {pageList
        .filter(
          (member) =>
            member.name.includes(query) ||
            member.role.includes(query) ||
            member.mbti.includes(query) ||
            query == '',
        )
        .map((member) => (
          <div key={member.uniqueID}>
            <h3>{member.name}</h3>
            <ul>
              <li>{member.role}</li>
              <li>{member.mbti}</li>
              <li>{member.instagramUrl}</li>
              <img src={member.profileImageUrl} alt="" />
            </ul>
          </div>
        ))}
    </div>
  );
}

export default PageProfile;
