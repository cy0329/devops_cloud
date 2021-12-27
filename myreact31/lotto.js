const range = (size) => [...Array(size).keys()];

const makeLottoNumbers = () => {
  range(45)
    .map((number) => number + 1)
    .sort(() => Math.random - Math.random);
};

console.log(predict());
