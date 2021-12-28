import { useState } from "react";
import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./pages/PageProfileCard";
// import mem1 from "./img/member1.jpg";
// import mem2 from "./img/member2.jpg";
// import mem3 from "./img/member3.jpg";
// import mem4 from "./img/member4.jpg";
import members from "./data/profiles.json";

function App() {
  // PageProfileCard 에서 인자로써 받아서 버튼으로...?
  const [pageName, setPageName] = useState(members[0].name);
  return (
    <>
      <h2>리액트 학습</h2>
      <div className="lotto">
        <PageLotto />
      </div>
      {members.map((member, index) => {
        if (pageName === member.name) {
          return (
            <div className={`m${index % 4}`}>
              <ProfileCard
                {...member}
                profileImage={`/profile-image/member${index + 1}.jpg`}
              >
                <nav>
                  {members.map((member) => {
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
