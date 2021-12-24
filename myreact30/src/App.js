import TopNav from 'components/TopNav';
import PageAbout from 'pages/PageAbout';
import PageCounter from 'pages/PageCounter';
import PageLotto from 'pages/PageLotto';
import PagePlaylist from 'pages/PagePlaylist';
import { useState } from 'react';

function App() {
  const [pageName, setPageName] = useState('about');
  // const changePageName = (pageName) => {
  //   setPageName(pageName);
  // };
  return (
    <div>
      <h1>여리의 리액트</h1>
      <TopNav changePageName={setPageName} />
      {pageName === 'about' && <PageAbout />}
      {pageName === 'counter' && <PageCounter />}
      {pageName === 'lotto' && <PageLotto />}
      {pageName === 'playlist' && <PagePlaylist />}
    </div>
  );
}

export default App;
