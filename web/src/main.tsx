import React, { lazy } from "react"
import ReactDOM from "react-dom/client"

/** Stylesheet */
import "./assets/css/index.css"

/** React Router DOM */
import { BrowserRouter as Router, Routes, Route } from "react-router-dom"

/** Routes configuration */
import routesConfiguration from "./routes/routes.json"

/** Components */
const components: { [key: string]: React.LazyExoticComponent<() => JSX.Element> } = {
  Auth: lazy(() => import("./pages/Auth")),
  App: lazy(() => import("./App"))
};

ReactDOM.createRoot(document.getElementById("root")!).render(
  <React.StrictMode>
    <div className="w-full h-screen p-4 bg-slate-950 antialiased font-dm-sans text-white tracking-tighter">
      <Router>
        <Routes>
          { routesConfiguration.routes.map((route, index) => {
            const Component = components[route.component];
            return <Route key={index} path={route.path} element={<Component />} />;
          })}
        </Routes>
      </Router>
    </div>
  </React.StrictMode>,
)
