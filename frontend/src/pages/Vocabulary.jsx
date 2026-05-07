import { useState, useEffect } from "react";
import { Search, Volume2, BookMarked } from "lucide-react";
import api from "../services/api";

export default function Vocabulary() {
  const [words, setWords] = useState([]);
  const [search, setSearch] = useState("");
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    api.get("/vocabulary/").then((res) => {
      setWords(res.data);
      setLoading(false);
    });
  }, []);

  const filtered = words.filter(
    (w) =>
      w.word.toLowerCase().includes(search.toLowerCase()) ||
      w.translation.toLowerCase().includes(search.toLowerCase())
  );

  if (loading) {
    return (
      <div className="flex items-center justify-center py-20">
        <div className="animate-spin w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full"></div>
      </div>
    );
  }

  return (
    <div className="animate-fade-in">
      <div className="flex items-center gap-3 mb-6">
        <div className="w-10 h-10 rounded-xl bg-green-100 flex items-center justify-center">
          <BookMarked className="w-5 h-5 text-green-600" />
        </div>
        <div>
          <h1 className="text-xl font-bold">Glossariy</h1>
          <p className="text-sm text-gray-500">Tibbiy ingliz tili lug'ati</p>
        </div>
      </div>

      <div className="relative mb-6">
        <Search className="absolute left-3 top-1/2 -translate-y-1/2 w-5 h-5 text-gray-400" />
        <input
          type="text"
          value={search}
          onChange={(e) => setSearch(e.target.value)}
          className="input"
          style={{ paddingLeft: "2.5rem" }}
          placeholder="Qidirish..."
        />
      </div>

      <div className="grid gap-3">
        {filtered.map((word) => (
          <div key={word.id} className="card">
            <div className="flex items-start justify-between">
              <div>
                <div className="flex items-center gap-2 mb-1">
                  <span className="text-lg font-semibold text-blue-600">
                    {word.word}
                  </span>
                  <button className="p-1 text-gray-400 hover:text-blue-500 rounded">
                    <Volume2 className="w-4 h-4" />
                  </button>
                </div>
                <p className="text-green-600 font-medium">{word.translation}</p>
              </div>
            </div>
            {word.definition && (
              <p className="text-sm text-gray-600 mt-2">{word.definition}</p>
            )}
            {word.example && (
              <p className="text-sm text-gray-500 mt-2 italic border-l-2 border-gray-200 pl-3">
                "{word.example}"
              </p>
            )}
          </div>
        ))}
      </div>

      {filtered.length === 0 && (
        <div className="text-center py-12 text-gray-500">
          Hech narsa topilmadi
        </div>
      )}
    </div>
  );
}
