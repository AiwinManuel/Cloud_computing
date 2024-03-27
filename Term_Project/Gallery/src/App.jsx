import React from 'react';
import { BrowserRouter, Routes, Route } from 'react-router-dom';
import { Gallery } from './Gallery';
import Login from './Login'; 
import './styles.css';

function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Login />} />
        <Route path="/gallery" element={<Gallery />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
