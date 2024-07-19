import React from 'react';
import 'bootstrap/dist/css/bootstrap.min.css';
import Login from './components/Login';
import Register from './components/Register';

function App() {
  return (
    <div>
      <Login />
      <hr />
      <Register />
    </div>
  );
}

export default App;
