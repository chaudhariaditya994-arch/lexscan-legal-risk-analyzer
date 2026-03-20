import { useMemo, useState } from "react";

const STORAGE_KEY = "lexscan-history";
const memoryStore = [];

function readHistory() {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? JSON.parse(raw) : memoryStore;
  } catch {
    return memoryStore;
  }
}

function writeHistory(items) {
  memoryStore.splice(0, memoryStore.length, ...items);
  localStorage.setItem(STORAGE_KEY, JSON.stringify(items));
}

export function useMongoStore() {
  const [history, setHistory] = useState(() => readHistory());

  const api = useMemo(
    () => ({
      history,
      add(item) {
        const next = [item, ...history].slice(0, 20);
        writeHistory(next);
        setHistory(next);
      },
      removeById(id) {
        const next = history.filter((entry) => entry.id !== id);
        writeHistory(next);
        setHistory(next);
      },
      clear() {
        writeHistory([]);
        setHistory([]);
      },
    }),
    [history],
  );

  return api;
}
