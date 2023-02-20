import logo from './logo.svg';
import './App.css';
import Splash from "./components/splash/Splash";
import Signup from "./components/signup/SignUp";
import Login from "./components/login/App";
import { BrowserRouter, Routes, Route } from "react-router-dom";
function App() {
  return (
    <BrowserRouter>
      <Routes>
          <Route path="/splash" element={<Splash />} />
          <Route path="/login" element={<Login />} />
          <Route path="/signup" element={<Signup />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
