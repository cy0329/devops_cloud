import "./PageProfileCard.css";
// import mem1jpg from "./img/member1.jpg";
// import "../data/profiles.json";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook } from "@fortawesome/free-brands-svg-icons";
import {
  faBars,
  faStickyNote,
  faEnvelope,
} from "@fortawesome/free-solid-svg-icons";
import { Children } from "react/cjs/react.production.min";

function ProfileCard({
  name,
  role,
  facebook_url,
  email,
  profileImage,
  children,
}) {
  return (
    <section>
      <nav className="menu">
        <a href="#">
          <FontAwesomeIcon icon={faBars} />
        </a>
        <a href="#">
          <FontAwesomeIcon icon={faStickyNote} />
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
            <FontAwesomeIcon icon={faFacebook} />
            <span>{facebook_url}</span>
          </li>
          <li>
            <FontAwesomeIcon icon={faEnvelope} />
            <span>{email}</span>
          </li>
        </ul>
      </article>
      <nav className="others">{children}</nav>
    </section>
  );
}

export default ProfileCard;
