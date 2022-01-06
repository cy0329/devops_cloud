import PageReviewList from 'page/PageReviewList';
import PageCounter from 'page/PageCounter';
import PageTodoList from 'page/PageTodoList';
import { Route, Routes } from 'react-router-dom';
import './App.css';
import TopNav from 'components/TopNav';
import PageNotFound from 'page/PageNotFound';

function App() {
  return (
    <div className="app-center">
      <TopNav />
      <Routes>
        <Route path="/" element={<div>대문</div>} />
        <Route path="/reviews" element={<PageReviewList />} />
        <Route path="/counter" element={<PageCounter />} />
        <Route path="/todos" element={<PageTodoList />} />
        <Route path="*" element={<PageNotFound />} />
      </Routes>
    </div>
  );
}

export default App;
