import { useEffect, useState } from 'react';
import Axios from 'axios';

function PageProfile() {
  const [pageList, setPageList] = useState([]);
  const handleRefresh = () =>
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => {
        const profileList = response.data.map((profile) => ({
          ...profile,
          profileImageUrl: profile.profile_image_url,
          instagramUrl: profile.instagram_url,
        }));
        setPageList(profileList);
      })
      .catch((error) => console.error(error));

  useEffect(() => handleRefresh(), []);

  return (
    <div>
      <h2>Page Profile</h2>
      <button onClick={() => setPageList([])}>clear</button>
      <button onClick={handleRefresh}>refresh</button>
      {pageList.length === 0 && <h4>등록된 프로필이 없습니다.</h4>}
      {pageList.map((member) => (
        <>
          <h3>{member.name}</h3>
          <ul>
            <li>{member.role}</li>
            <li>{member.mbti}</li>
            <li>{member.instagramUrl}</li>
            <img src={member.profileImageUrl} alt="" />
          </ul>
        </>
      ))}
    </div>
  );
}

export default PageProfile;
