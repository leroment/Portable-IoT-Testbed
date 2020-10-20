import React, { useState, useEffect } from "react";
import "./App.css";
import {
  BrowserRouter as Router,
  Route,
  Redirect,
  Switch,
} from "react-router-dom";

import LoginRegister from "./login-register/pages/LoginRegister";
import Dashboard from "./dashboard/pages/Dashboard";
import MainNavigation from "./shared/components/Navigation/MainNavigation";
import Patientslist from "./patientslist/pages/Patientslist";
import Alerts from "./alerts/Alerts";

const isAuthenticated = () => {
  console.log("from app js" + localStorage.getItem("token"));
  return !!localStorage.getItem("token");
};
//private route
const PrivateRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) =>
        isAuthenticated() ? (
          <div>
            <MainNavigation authenticated={isAuthenticated()} />
            <Component {...props} />
          </div>
        ) : (
          <Redirect to={{ pathname: "/" }} />
        )
      }
    />
  );
};

const PublicRoute = ({ component: Component, ...rest }) => {
  return (
    <Route
      {...rest}
      render={(props) =>
        isAuthenticated() ? (
          <div>
            <Redirect to={{ pathname: "/dashboard" }} />
          </div>
        ) : (
          <div>
            <MainNavigation authenticated={isAuthenticated()} />
            <Component {...props} />
          </div>
        )
      }
    />
  );
};

function App() {
  // const [authenticated, setAuthenticated] = useState(isAuthenticated);

  // const updateAuthenticated = (value) => {
  //   setAuthenticated(value)
  // }

  return (
    <div className="App">
      <Router>
        <main>
          <Switch>
            <PrivateRoute path="/dashboard" exact component={Dashboard} />
            {/* <Route path="/dashboard" exact>
              <Dashboard />
            </Route> */}
            <PrivateRoute path="/patientslist" exact component={Patientslist} />
            <PrivateRoute path="/alerts" exact component={Alerts} />
            <PublicRoute path="/" exact component={LoginRegister} />
            {/* <LoginRegister /> */}
            {/* </PublicRoute> */}
          </Switch>
        </main>
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
