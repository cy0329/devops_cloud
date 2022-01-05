import './Review.css';
import Stars from './ScoreStars';

function Review({ review }) {
  return (
    <div className="m-1 p-1 rounded text-lg border-4">
      <Stars score={review.score} />
      {review.content.split('\n').map((letter) => (
        <p>{letter}</p>
      ))}
    </div>
  );
}

export default Review;
