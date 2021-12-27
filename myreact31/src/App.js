import { useState } from "react";
import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./pages/PageProfileCard";
import mem1 from "./img/member1.jpg";
import mem2 from "./img/member2.jpg";
import mem3 from "./img/member3.jpg";
import mem4 from "./img/member4.jpg";
import members from "./data/profiles.json";

function App() {
  // PageProfileCard 에서 인자로써 받아서 버튼으로...?
  const [pageName, setPageName] = useState("Julia");
  return (
    <>
      <h2>리액트 학습</h2>
      <PageLotto />
      {members.map((member) => {
        if (pageName === member.name) {
          return (
            <ProfileCard
              name={member.name}
              role={member.role}
              facebook_url={member.facebook_url}
              email={member.email}
              profileImage={mem1}
              changePage={setPageName}
            />
          );
        }
      })}
    </>
  );
}

export default App;
