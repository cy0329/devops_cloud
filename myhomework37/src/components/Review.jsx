import { useState } from 'react';
import './Review.css';
// import Stars from './ScoreStars';
import Stars2 from './ScoreStars2';

// review : 보여줄 review 객체
// handleEdit : 인자 없는 함수, 수정 버튼 클릭 시에 호출
// handleDelete : 인자 없는 함수, 삭제 버튼 클릭 시에 호출

function Review({ review, handleDelete, handleEdit }) {
  const [showMenu, setShowMenu] = useState(false);

  const handleClickedDeleteButton = () => {
    if (handleDelete) {
      handleDelete();
    } else {
      console.warn('[Review] handleDelete 속성값이 지정되지 않았습니다.');
    }
  };

  const handleClickedEditButton = () => {
    if (handleEdit) {
      handleEdit();
    } else {
      console.warn('[Review] handleEdit 속성값이 지정되지 않았습니다.');
    }
  };

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
          <span
            onClick={handleClickedEditButton}
            className="cursor-pointer mr-1 text-green-700 hover:text-green-500 hover:bg-gray-100 rounded"
          >
            수정
          </span>
          <span
            onClick={handleClickedDeleteButton}
            className="cursor-pointer text-red-700 hover:text-red-300 hover:bg-gray-100 rounded"
          >
            삭제
          </span>
        </div>
      )}
    </div>
  );
}

export default Review;
