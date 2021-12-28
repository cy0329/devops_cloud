import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./pages/PageProfileCard";
// import members from "./data/profiles.json"; // 이건 local 파일 사용
import Axios from "axios";

const { useState, useEffect } = require("react");

function App() {
  const [profileList, setProfileList] = useState([]);

  useEffect(() => {
    Axios.get(
      "https://classdevopscloud.blob.core.windows.net/data/profile-list.json"
    )
      .then((response) => {
        // reponse는 axios 객체
        // response.data => 응답 내용
        setProfileList(response.data);
      })
      .catch((error) => {
        console.error(error);
      });
  }, []);

  const [pageName, setPageName] = useState(profileList[0].name);

  return (
    <>
      <h2>리액트 학습</h2>
      <div className="lotto">
        <PageLotto />
      </div>
      {profileList.map((member, index) => {
        if (pageName === member.name) {
          return (
            <div className={`m${index % 4}`}>
              <ProfileCard
                {...member}
                // name={member.name}
                // role={member.role}
                // mbti={member.mbti}
                // instagram_url={member.instagram_url}
                // profile_image_url={member.profile_image_url}
              >
                <nav>
                  {profileList.map((member) => {
                    return (
                      <a
                        className={pageName == member.name ? "on" : ""}
                        onClick={() => setPageName(member.name)}
                      ></a>
                    );
                  })}
                </nav>
              </ProfileCard>
            </div>
          );
        }
      })}
    </>
  );
}

export default App;
