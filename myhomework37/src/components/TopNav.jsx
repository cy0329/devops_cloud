import { Link } from 'react-router-dom';
// a 태그를 쓰면 페이지를 넘어갈때마다 페이지를 새로 구현
// Link 를 쓰면 SPA => single page application
function TopNav() {
  return (
    <div className="my-3">
      <ul className="flex gap-4">
        <li>
          <NavLink to="/">Home</NavLink>
        </li>
        <li>
          <NavLink to="/todos">Todos</NavLink>
        </li>
        <li>
          <NavLink to="/reviews">Reviews</NavLink>
        </li>
        <li>
          <NavLink to="/counter">Counter</NavLink>
        </li>
      </ul>
    </div>
  );
}
// 통일 시켜서 스타일링 하기 위해 이런 방법...
function NavLink({ to, children }) {
  return (
    <Link
      to={to}
      className="pb-1 border-red-400 hover:border-b-4 hover:text-red-400 duration-75 text-sm"
    >
      {children}
    </Link>
  );
}

export default TopNav;
