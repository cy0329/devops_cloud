import { useEffect, useState } from 'react';
import Axios from 'axios';
import ProfileList from 'components/ProfileList';

function PageProfile() {
  const [pageList, setPageList] = useState([]);
  const [errorObject, setErrorObject] = useState(null);
  const [query, setQuery] = useState('');

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
  const orgProfile = pageList.filter((member) => {
    if (query.length === 0) {
      return true;
    }
    const pattern = new RegExp(query, 'i');
    const queryTarget = [member.name, member.role, member.mbti];
    return pattern.test(queryTarget);
  });

  return (
    <>
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

      <ProfileList
        orgProfile={orgProfile}
        handleChange={handleChange}
        handleKeyPress={handleKeyPress}
        handleRefresh={handleRefresh}
        query={query}
        pageList={pageList}
      />
    </>
  );
}

export default PageProfile;
