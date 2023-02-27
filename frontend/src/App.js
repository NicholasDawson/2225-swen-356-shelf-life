import './App.css';
import Splash from "./components/splash/Splash.js";
import Signup from "./components/signup/SignUp";
import Login from "./components/login/Login";
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <BrowserRouter>
      <Routes>
          <Route path="/splash" element={<Splash></Splash>} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
