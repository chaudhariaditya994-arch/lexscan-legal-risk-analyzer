// in-memory simulation
let history = [];

const useMongoStore = () => {
  const saveAnalysis = (analysis) => {
    history.push(analysis);
  };

  const getHistory = () => {
    return history;
  };

  return { saveAnalysis, getHistory };
};

export default useMongoStore;