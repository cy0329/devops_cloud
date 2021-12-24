import Counter from 'components/Counter';

function PageCounter() {
  return (
    <>
      <Counter initial={10} color={'blue'} />
      <Counter initial={10} color={'red'} />
      <Counter initial={10} color={'green'} />
    </>
  );
}

export default PageCounter;
