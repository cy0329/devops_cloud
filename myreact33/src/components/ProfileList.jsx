import ProfileCard from './ProfileCard';

function ProfileList({ orgProfile }) {
  return (
    <div>
      {orgProfile.length === 0 && <h4>등록된 프로필이 없습니다.</h4>}
      {orgProfile.map((member) => {
        return <ProfileCard {...member} />;
      })}
    </div>
  );
}
export default ProfileList;
