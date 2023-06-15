import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap/dist/js/bootstrap";
import React  from "react";
import Navbar from "./components/Navbar";
import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import Pelis from "./pages/Pelis";




function App() {
  return (
    <Router>
      <div className="App">
        <Navbar />
      </div>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/pelis" element={<Pelis />} />     
      </Routes>
    </Router>
  );
}

const Home = () => {
  return (
    <div className="App">
        HOME PAGE
    </div>
  );
};

export default App;