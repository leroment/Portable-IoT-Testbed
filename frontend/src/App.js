import React from "react";
import "./App.css";
import { BrowserRouter as Router, Route, Redirect } from "react-router-dom";

import LoginRegister from "./login-register/Pages/LoginRegister";
import Dashboard from "./dashboard/Dashboard";

const PrivateRoute = ({ component: Component, authenticated, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) =>
        authenticated === true ? (
          <Component {...props} />
        ) : (
          <Redirect to={{ pathname: "/", state: { from: props.location } }} />
        )
      }
    />
  );
};

function App() {
  return (
    <div className="App">
      <Router>
        <PrivateRoute
          path="/dashboard"
          exact
          authenticated-={() => {}}
          component={Dashboard}
        />
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
