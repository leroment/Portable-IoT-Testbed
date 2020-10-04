import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route } from "react-router-dom";

import Login from "./login-register/components/Login";
import LoginRegister from "./login-register/pages/LoginRegister";

function App() {
  return (
    <div className="App">
      <Router>
        <Route path="/">
          <LoginRegister />
        </Route>
      </Router>
      {/* <h1> Grafana in React App</h1>
      <iframe
        src="http://localhost:3000/d-solo/c8J-K7dMz/andrews-ecg-readings?orgId=1&from=1599960944380&to=1599960992217&panelId=2"
        width="100%"
        height="800"
        frameborder="0"
        title="ecg readings"
      ></iframe> */}
    </div>
  );
}

export default App;
