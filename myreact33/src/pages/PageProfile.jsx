import { useState } from 'react';

function PageProfile() {
  const [pageList, setPageList] = useState([]);

  return (
    <div>
      <h2>Page Profile</h2>
      {pageList.length === 0 ? <h4>등록된 프로필이 없습니다.</h4> : <h4></h4>}
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
