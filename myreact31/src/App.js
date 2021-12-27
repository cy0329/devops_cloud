import { useState } from "react";
import "./App.css";
import PageLotto from "./pages/PageLotto";
import ProfileCard from "./pages/PageProfileCard";
import mem1 from "./img/member1.jpg";
import mem2 from "./img/member2.jpg";
import mem3 from "./img/member3.jpg";
import mem4 from "./img/member4.jpg";

function App() {
  // PageProfileCard 에서 인자로써 받아서 버튼으로...?
  const [pageName, setPageName] = useState("mempf1");
  return (
    <>
      <h2>리액트 학습</h2>
      <PageLotto />
      {pageName === "mempf1" && (
        <ProfileCard
          profileImage={mem1}
          name="Julia"
          role="UI/UX Developer"
          facebook_url="facebook.com/juliafb1"
          email="juuulia@naver.com"
          changePage={setPageName}
        />
      )}
      {pageName === "mempf2" && (
        <ProfileCard
          profileImage={mem2}
          name="Romanov"
          role="GUI Designer"
          facebook_url="facebook.com/romav"
          email="rooomanv@naver.com"
          changePage={setPageName}
        />
      )}
      {pageName === "mempf3" && (
        <ProfileCard
          profileImage={mem3}
          name="Tom"
          role="3D Graphic Designer"
          facebook_url="facebook.com/tommy_79"
          email="ttoommy@naver.com"
          changePage={setPageName}
        />
      )}
      {pageName === "mempf4" && (
        <ProfileCard
          profileImage={mem4}
          name="Jackson"
          role="CPU Builder"
          facebook_url="facebook.com/jackson"
          email="jksn123@naver.com"
          changePage={setPageName}
        />
      )}
    </>
  );
}

export default App;
