import "./PageProfileCard.css";
// import mem1jpg from "./img/member1.jpg";
// import "../data/profiles.json";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faFacebook, faInstagram } from "@fortawesome/free-brands-svg-icons";
import {
  faBars,
  faStickyNote,
  faEnvelope,
} from "@fortawesome/free-solid-svg-icons";

function ProfileCard({
  name,
  role,
  mbti,
  instagram_url,
  profile_image_url,
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
        <img src={profile_image_url} alt="프로필 이미지" />

        <h1>{name}</h1>
        <h2>{role}</h2>

        <a href="#" className="btnView">
          VIEW MORE
        </a>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faInstagram} />
            <span>{instagram_url}</span>
          </li>
          <li>
            <span>MBTI : {mbti}</span>
          </li>
        </ul>
      </article>
      <nav className="others">{children}</nav>
    </section>
  );
}

export default ProfileCard;
