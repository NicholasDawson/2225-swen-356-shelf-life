import "./App.css";
import Splash from "./components/splash/Splash.js";
import Signup from "./components/signup/SignUp";
import Login from "./components/login/Login";
import { HashRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <HashRouter>
      <Routes>
        <Route path="/" element={<Splash />} />
        <Route path="/splash" element={<Splash></Splash>} />
        <Route path="/login" element={<Login />} />
        <Route path="/signup" element={<Signup />} />
      </Routes>
    </HashRouter>
  );
}

export default App;
