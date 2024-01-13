import React from "react"
import ReactDOM from "react-dom/client"

/** Stylesheet */
import "./assets/css/index.css"

/** React Router DOM */
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

/** Components */
import Auth from "./pages/Auth"
import App from "./App"

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <div className="w-full h-screen p-4 bg-slate-950 antialiased font-dm-sans text-white tracking-tighter">
    <Router>
        <Routes>
          <Route path="/*" element={<App />} />
          <Route path="/" element={<Auth />} />
        </Routes>
      </Router>
    </div>
  </React.StrictMode>,
)
