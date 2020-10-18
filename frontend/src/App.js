import React from "react";
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


//private route
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
        <MainNavigation />
        <main>
          <Switch>
            {/* <PrivateRoute
          path="/dashboard"
          exact
          authenticated-={() => {}}
          component={Dashboard}
        /> */}
            <Route path="/dashboard" exact>
              <Dashboard />
            </Route>
            <Route path="/patientslist" exact>
              <Patientslist />
            </Route>
            <Route path="/" exact>
              <LoginRegister />
            </Route>
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
