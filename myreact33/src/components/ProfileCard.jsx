import './ProfileCard.css';
// import mem1jpg from "./img/member1.jpg";
// import "../data/profiles.json";
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faInstagram } from '@fortawesome/free-brands-svg-icons';
import { faBars, faStickyNote } from '@fortawesome/free-solid-svg-icons';

function ProfileCard({ name, role, mbti, instagramUrl, profileImageUrl }) {
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
        <img src={profileImageUrl} alt="프로필 이미지" />

        <h1>{name}</h1>
        <h2>{role}</h2>

        <a href="#" className="btnView">
          VIEW MORE
        </a>
        <ul className="contact">
          <li>
            <FontAwesomeIcon icon={faInstagram} />
            <span>{instagramUrl}</span>
          </li>
          <li>
            <span>MBTI : {mbti}</span>
          </li>
        </ul>
      </article>
    </section>
  );
}

export default ProfileCard;
