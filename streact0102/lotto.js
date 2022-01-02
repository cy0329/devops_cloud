const makeLottoNumbers = () => {
  const lottoSet = new Set();
  while (lottoSet.size < 7) {
    lottoSet.add(Math.floor(Math.random() * 45) + 1);
  }
  const lottoList = Array.from(lottoSet);
  lottoList.sort((a, b) => a - b);
  return lottoList;
};

console.log(makeLottoNumbers());
