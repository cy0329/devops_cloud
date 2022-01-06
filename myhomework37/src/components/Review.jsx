import { useState } from 'react';
import './Review.css';
// import Stars from './ScoreStars';
import Stars2 from './ScoreStars2';

function Review({ review }) {
  const [showMenu, setShowMenu] = useState(true);

  return (
    <div
      className="m-1 p-1 pt-2 rounded text-lg border-4 relative"
      onMouseEnter={() => setShowMenu(true)}
      onMouseLeave={() => setShowMenu(false)}
    >
      <Stars2 score={review.score} />
      {review.content.split('\n').map((letter) => (
        <>
          {letter}
          <br />
        </>
      ))}
      {showMenu && (
        <div className="text-xs absolute top-0 right-0">
          <span className="cursor-pointer mr-1 text-green-700 hover:text-green-500 hover:bg-gray-100 rounded">
            수정
          </span>
          <span className="cursor-pointer text-red-700 hover:text-red-300 hover:bg-gray-100 rounded">
            삭제
          </span>
        </div>
      )}
    </div>
  );
}

export default Review;
