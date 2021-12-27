import { useState } from "react";
import "./PageProfileCard.css";
// import mem1jpg from "./img/member1.jpg";

function ProfileCard({
  profileImage,
  name,
  role,
  facebook_url,
  email,
  changePage,
}) {
  return (
    <body>
      <section>
        <nav className="menu">
          <a href="#">
            <i className="fas fa-bars"></i>
          </a>
          <a href="#">
            <i className="far fa-sticky-note"></i>
          </a>
        </nav>
        <article className="profile">
          <img src={profileImage} alt="프로필 이미지" />

          <h1>{name}</h1>
          <h2>{role}</h2>

          <a href="#" className="btnView">
            VIEW MORE
          </a>
          <ul className="contact">
            <li>
              <i className="fab fa-facebook-f"></i>
              <span>{facebook_url}</span>
            </li>
            <li>
              <i className="fas fa-envelope"></i>
              <span>{email}</span>
            </li>
          </ul>
        </article>
        <nav className="others">
          <a onClick={() => changePage("mempf1")}></a>
          <a onClick={() => changePage("mempf2")}></a>
          <a onClick={() => changePage("mempf3")}></a>
          <a onClick={() => changePage("mempf4")}></a>
        </nav>
      </section>
    </body>
  );
}

export default ProfileCard;
