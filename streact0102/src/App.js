import './App.css';
import ProfileCard from './pages/ProfileCard';
import PageLotto from './pages/PageLotto';
import { useState, useEffect } from 'react';
// import profiles from './pages/data/profiles.json';
import Axios from 'axios';

function App() {
  const [pageName, setPageName] = useState('진');
  const [profiles, setProfiles] = useState([]);
  useEffect(() => {
    Axios.get(
      'https://classdevopscloud.blob.core.windows.net/data/profile-list.json',
    )
      .then((response) => setProfiles(response.data))
      .catch((error) => console.log(error));
  }, []);

  return (
    <>
      <PageLotto />
      {profiles.map((member, index) => {
        return (
          pageName === member.name && (
            <div className={`member${(index % 4) + 1}`} key={member.unique_id}>
              <ProfileCard {...member}>
                <nav>
                  {profiles.map((member) => {
                    return (
                      <a
                        className={pageName === member.name && 'on'}
                        onClick={() => setPageName(member.name)}
                      ></a>
                    );
                  })}
                </nav>
              </ProfileCard>
            </div>
          )
        );
      })}
    </>
  );
}

export default App;
