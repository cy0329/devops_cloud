import { useState } from "react";
import "./PageProfileCard.css";
// import mem1jpg from "./img/member1.jpg";
// import "../data/profiles.json";

function ProfileCard({
  name,
  role,
  facebook_url,
  email,
  profileImage,
  changePage,
}) {
  return (
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
        <a onClick={() => changePage("Julia")}></a>
        <a onClick={() => changePage("Romanov")}></a>
        <a onClick={() => changePage("Tom")}></a>
        <a onClick={() => changePage("Jackson")}></a>
      </nav>
    </section>
  );
}

export default ProfileCard;
