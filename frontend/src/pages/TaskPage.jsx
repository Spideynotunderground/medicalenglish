import { useState, useEffect, useRef } from 'react'
import { useParams, Link, useNavigate } from 'react-router-dom'
import { ArrowLeft, CheckCircle, XCircle, RefreshCw, ArrowRight, Sparkles, Mic, MicOff, Square } from 'lucide-react'
import api from '../services/api'
import toast from 'react-hot-toast'

export default function TaskPage() {
  const { id } = useParams()
  const navigate = useNavigate()
  const [task, setTask] = useState(null)
  const [loading, setLoading] = useState(true)
  const [answers, setAnswers] = useState({})
  const [submitting, setSubmitting] = useState(false)
  const [result, setResult] = useState(null)
  
  // Speech recognition states
  const [isRecording, setIsRecording] = useState(false)
  const [recordingTime, setRecordingTime] = useState(0)
  const recognitionRef = useRef(null)
  const timerRef = useRef(null)
  
  useEffect(() => {
    api.get(`/tasks/${id}/`).then(res => {
      setTask(res.data)
      setLoading(false)
    }).catch(() => {
      toast.error('Topshiriq topilmadi')
      navigate('/units')
    })
    
    return () => {
      // Cleanup on unmount
      if (recognitionRef.current) {
        recognitionRef.current.stop()
      }
      if (timerRef.current) {
        clearInterval(timerRef.current)
      }
    }
  }, [id])
  
  const handleAnswer = (key, value) => {
    setAnswers(prev => ({ ...prev, [key]: value }))
  }
  
  // Speech Recognition functions
  const startRecording = () => {
    if (!('webkitSpeechRecognition' in window) && !('SpeechRecognition' in window)) {
      toast.error('Brauzeringiz ovoz yozishni qo\'llab-quvvatlamaydi. Chrome yoki Edge ishlatib ko\'ring.')
      return
    }
    
    const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
    const recognition = new SpeechRecognition()
    
    recognition.continuous = true
    recognition.interimResults = true
    recognition.lang = 'en-US'
    
    let finalTranscript = answers.transcript || ''
    
    recognition.onstart = () => {
      setIsRecording(true)
      setRecordingTime(0)
      timerRef.current = setInterval(() => {
        setRecordingTime(prev => prev + 1)
      }, 1000)
      toast.success('Ovoz yozish boshlandi. Ingliz tilida gapiring!')
    }
    
    recognition.onresult = (event) => {
      let interimTranscript = ''
      
      for (let i = event.resultIndex; i < event.results.length; i++) {
        const transcript = event.results[i][0].transcript
        if (event.results[i].isFinal) {
          finalTranscript += transcript + ' '
        } else {
          interimTranscript += transcript
        }
      }
      
      handleAnswer('transcript', finalTranscript + interimTranscript)
    }
    
    recognition.onerror = (event) => {
      console.error('Speech recognition error:', event.error)
      if (event.error === 'no-speech') {
        toast.error('Ovoz eshitilmadi. Iltimos, gapiring.')
      } else if (event.error === 'not-allowed') {
        toast.error('Mikrofondan foydalanishga ruxsat berilmadi.')
      } else {
        toast.error('Ovoz yozishda xatolik: ' + event.error)
      }
      stopRecording()
    }
    
    recognition.onend = () => {
      if (isRecording) {
        // If still supposed to be recording, restart
        try {
          recognition.start()
        } catch (e) {
          stopRecording()
        }
      }
    }
    
    recognitionRef.current = recognition
    recognition.start()
  }
  
  const stopRecording = () => {
    setIsRecording(false)
    if (timerRef.current) {
      clearInterval(timerRef.current)
      timerRef.current = null
    }
    if (recognitionRef.current) {
      recognitionRef.current.stop()
      recognitionRef.current = null
    }
    toast.success('Ovoz yozish to\'xtatildi')
  }
  
  const formatTime = (seconds) => {
    const mins = Math.floor(seconds / 60)
    const secs = seconds % 60
    return `${mins}:${secs.toString().padStart(2, '0')}`
  }
  
  const handleSubmit = async () => {
    setSubmitting(true)
    try {
      const res = await api.post(`/tasks/${id}/submit/`, { answers })
      setResult(res.data)
      if (res.data.passed) {
        toast.success(`Tabriklaymiz! ${res.data.score}%`)
      }
    } catch (err) {
      toast.error('Xatolik yuz berdi')
    } finally {
      setSubmitting(false)
    }
  }
  
  const handleRetry = () => {
    setAnswers({})
    setResult(null)
  }
  
  if (loading) {
    return (
      <div className="flex items-center justify-center py-20">
        <div className="animate-spin w-8 h-8 border-4 border-blue-500 border-t-transparent rounded-full"></div>
      </div>
    )
  }
  
  return (
    <div className="max-w-3xl mx-auto animate-fade-in">
      {/* Header */}
      <div className="flex items-center justify-between mb-4">
        <Link to={`/units/${task.unit}`} className="inline-flex items-center gap-2 text-sm text-gray-600 hover:text-blue-600">
          <ArrowLeft className="w-4 h-4" />
          Orqaga
        </Link>
        <span className="badge badge-yellow">{task.points} ball</span>
      </div>
      
      {/* Task info */}
      <div className="card mb-6">
        <div className="flex items-center gap-2 mb-2">
          <span className="badge badge-blue">Task {task.number}</span>
          {task.is_ai_evaluated && (
            <span className="badge badge-purple"><Sparkles className="w-3 h-3 mr-1" /> AI Baholash</span>
          )}
        </div>
        <h1 className="text-xl font-bold mb-1">{task.title}</h1>
        <p className="text-gray-600 text-sm">{task.instruction}</p>
      </div>
      
      {/* Result */}
      {result && (
        <div className={`card mb-6 ${result.passed ? 'bg-green-50 border-green-200' : 'bg-red-50 border-red-200'}`}>
          <div className="flex items-center gap-4">
            {result.passed ? (
              <div className="w-16 h-16 rounded-full bg-green-100 flex items-center justify-center">
                <CheckCircle className="w-8 h-8 text-green-500" />
              </div>
            ) : (
              <div className="w-16 h-16 rounded-full bg-red-100 flex items-center justify-center">
                <XCircle className="w-8 h-8 text-red-500" />
              </div>
            )}
            <div className="flex-1">
              <div className="text-3xl font-bold">{result.score}%</div>
              <div className="text-sm text-gray-600">
                {result.passed ? 'Muvaffaqiyatli bajarildi!' : 'Qayta urinib ko\'ring'}
              </div>
            </div>
          </div>
          
          <p className="mt-4 p-3 bg-white/50 rounded-lg text-sm">{result.feedback}</p>
          
          <div className="flex gap-2 mt-4">
            <button onClick={handleRetry} className="btn btn-outline">
              <RefreshCw className="w-4 h-4" /> Qayta
            </button>
            <Link to={`/units/${task.unit}`} className="btn btn-primary">
              Keyingi <ArrowRight className="w-4 h-4" />
            </Link>
          </div>
        </div>
      )}
      
      {/* Questions */}
      {!result && (
        <>
          {/* For tasks with questions */}
          {task.questions?.length > 0 && (
            <div className="space-y-4 mb-6">
              {task.questions.map((q, i) => (
                <div key={q.id} className="card">
                  <p className="font-medium mb-3">{i + 1}. {q.question_text}</p>
                  
                  {q.options?.length > 0 ? (
                    <div className="grid grid-cols-1 sm:grid-cols-2 gap-2">
                      {q.options.map((opt, j) => (
                        <label key={j} className={`flex items-center gap-3 p-3 rounded-lg border-2 cursor-pointer transition-all ${
                          answers[q.id] === opt 
                            ? 'border-blue-500 bg-blue-50' 
                            : 'border-gray-200 hover:border-gray-300'
                        }`}>
                          <div className={`w-5 h-5 rounded-full border-2 flex items-center justify-center ${
                            answers[q.id] === opt ? 'border-blue-500' : 'border-gray-300'
                          }`}>
                            {answers[q.id] === opt && <div className="w-2.5 h-2.5 rounded-full bg-blue-500" />}
                          </div>
                          <span className="text-sm">{opt}</span>
                          <input
                            type="radio"
                            name={`q-${q.id}`}
                            checked={answers[q.id] === opt}
                            onChange={() => handleAnswer(q.id, opt)}
                            className="sr-only"
                          />
                        </label>
                      ))}
                    </div>
                  ) : (
                    <input
                      type="text"
                      value={answers[q.id] || ''}
                      onChange={(e) => handleAnswer(q.id, e.target.value)}
                      className="input"
                      placeholder="Javobingizni yozing..."
                    />
                  )}
                </div>
              ))}
            </div>
          )}
          
          {/* AI evaluated tasks */}
          {task.is_ai_evaluated && !task.questions?.length && (
            <div className="card mb-6">
              {task.task_type === 'translation' && (
                <>
                  <div className="bg-blue-50 border border-blue-200 p-4 rounded-lg mb-4">
                    <p className="text-xs text-blue-600 font-medium mb-1">Inglizcha matn:</p>
                    <p className="text-gray-800">{task.content?.text}</p>
                  </div>
                  <textarea
                    value={answers.translation || ''}
                    onChange={(e) => handleAnswer('translation', e.target.value)}
                    className="input min-h-[120px]"
                    placeholder="O'zbekcha tarjimani yozing..."
                  />
                </>
              )}
              
              {task.task_type === 'synonyms' && (
                <>
                  <div className="bg-purple-50 border border-purple-200 p-6 rounded-lg mb-4 text-center">
                    <p className="text-sm text-purple-600 mb-1">So'z:</p>
                    <p className="text-3xl font-bold text-purple-700">{task.content?.word}</p>
                  </div>
                  <textarea
                    value={answers.synonyms || ''}
                    onChange={(e) => handleAnswer('synonyms', e.target.value)}
                    className="input min-h-[100px]"
                    placeholder="Inglizcha sinonimlarni yozing (vergul bilan)..."
                  />
                </>
              )}
              
              {task.task_type === 'speaking' && (
                <>
                  <div className="bg-orange-50 border border-orange-200 p-4 rounded-lg mb-4">
                    <p className="text-sm text-orange-600 font-medium mb-1">Mavzu:</p>
                    <p className="text-gray-800 font-medium">{task.content?.topic}</p>
                    {task.content?.points && (
                      <p className="text-sm text-gray-500 mt-2">Gapiring: {task.content.points}</p>
                    )}
                  </div>
                  
                  {/* Recording controls */}
                  <div className="flex items-center justify-center gap-4 mb-4">
                    {!isRecording ? (
                      <button
                        onClick={startRecording}
                        className="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-red-500 to-pink-500 text-white rounded-2xl shadow-lg hover:shadow-xl hover:scale-105 transition-all"
                      >
                        <Mic className="w-6 h-6" />
                        <span className="font-semibold">Ovoz yozishni boshlash</span>
                      </button>
                    ) : (
                      <button
                        onClick={stopRecording}
                        className="flex items-center gap-3 px-6 py-4 bg-gradient-to-r from-gray-700 to-gray-900 text-white rounded-2xl shadow-lg hover:shadow-xl transition-all animate-pulse"
                      >
                        <Square className="w-6 h-6" />
                        <span className="font-semibold">To'xtatish</span>
                        <span className="bg-red-500 px-3 py-1 rounded-full text-sm font-mono">
                          {formatTime(recordingTime)}
                        </span>
                      </button>
                    )}
                  </div>
                  
                  {/* Recording indicator */}
                  {isRecording && (
                    <div className="flex items-center justify-center gap-2 mb-4 text-red-500">
                      <span className="relative flex h-3 w-3">
                        <span className="animate-ping absolute inline-flex h-full w-full rounded-full bg-red-400 opacity-75"></span>
                        <span className="relative inline-flex rounded-full h-3 w-3 bg-red-500"></span>
                      </span>
                      <span className="text-sm font-medium">Yozilmoqda... Ingliz tilida gapiring</span>
                    </div>
                  )}
                  
                  {/* Transcript display */}
                  <div className="relative">
                    <textarea
                      value={answers.transcript || ''}
                      onChange={(e) => handleAnswer('transcript', e.target.value)}
                      className="input min-h-[150px]"
                      placeholder={isRecording ? "Gapirayotganingiz shu yerda ko'rinadi..." : "Yoki matnni qo'lda yozing..."}
                    />
                    {answers.transcript && (
                      <div className="absolute bottom-3 right-3 text-xs text-gray-400">
                        {answers.transcript.split(/\s+/).filter(w => w).length} so'z
                      </div>
                    )}
                  </div>
                  
                  <p className="text-xs text-gray-500 mt-2 text-center">
                    💡 Mikrofon tugmasini bosing va ingliz tilida gapiring. Brauzer avtomatik matnga aylantiradi.
                  </p>
                </>
              )}
              
              {task.task_type === 'writing' && (
                <>
                  <div className="bg-green-50 border border-green-200 p-4 rounded-lg mb-4">
                    <p className="text-sm text-green-600 font-medium mb-1">Topshiriq:</p>
                    <p className="text-gray-800">{task.content?.prompt}</p>
                  </div>
                  <textarea
                    value={answers.essay || ''}
                    onChange={(e) => handleAnswer('essay', e.target.value)}
                    className="input min-h-[200px]"
                    placeholder="Ingliz tilida yozing..."
                  />
                </>
              )}
              
              {task.task_type === 'video' && (
                <>
                  <div className="bg-red-50 border border-red-200 p-4 rounded-lg mb-4">
                    <p className="text-sm text-red-600 font-medium mb-1">Video mavzusi:</p>
                    <p className="text-gray-800">{task.content?.topic}</p>
                  </div>
                  <textarea
                    value={answers.retelling || ''}
                    onChange={(e) => handleAnswer('retelling', e.target.value)}
                    className="input min-h-[150px]"
                    placeholder="Ingliz tilida qayta hikoya qiling..."
                  />
                </>
              )}
              
              {task.task_type === 'conversation' && (
                <div className="space-y-4">
                  {task.content?.questions?.map((q, i) => (
                    <div key={i}>
                      <p className="font-medium mb-2 text-sm">{i + 1}. {q}</p>
                      <textarea
                        value={answers[`q_${i}`] || ''}
                        onChange={(e) => handleAnswer(`q_${i}`, e.target.value)}
                        className="input min-h-[80px]"
                        placeholder="Ingliz tilida javob yozing..."
                      />
                    </div>
                  ))}
                </div>
              )}
            </div>
          )}
          
          <button
            onClick={handleSubmit}
            disabled={submitting}
            className="btn btn-primary w-full py-3"
          >
            {submitting ? (
              <>
                <div className="animate-spin w-4 h-4 border-2 border-white border-t-transparent rounded-full"></div>
                Tekshirilmoqda...
              </>
            ) : (
              'Yuborish'
            )}
          </button>
        </>
      )}
    </div>
  )
}
