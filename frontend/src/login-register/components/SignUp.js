import React, { useState } from "react";
import axios from "axios";
import { Redirect } from "react-router-dom";
import { Alert } from "@material-ui/lab";

const SignUp = () => {
  const [username, setUserName] = useState("");
  const [firstName, setFirstName] = useState("");
  const [lastName, setLastName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [redirectToDashboard, setRedirectToDashboard] = useState(false);
  const [error, setError] = useState({ message: "" });

  if (redirectToDashboard) {
    return <Redirect to="/dashboard" exact/>;
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    axios
      .post(`/api/register`, {
        username: username,
        email: email,
        first_name: firstName,
        last_name: lastName,
        password: password,
      })
      .then((response) => {
        console.log(response);
        if (response.status === 200 && response.data.token) {
          localStorage.setItem("token", response.data.token);
          localStorage.setItem("id", response.data.user.id);
          localStorage.setItem("username", response.data.user.username);
          setRedirectToDashboard(true);
        }
      })
      .catch((err) => {
        console.log(err.response);
        setError((error) => ({
          ...error,
          message: err.response.data.username || err.response.data.detail,
        }));
      });
  };

  return (
    <div className="form-container sign-up-container">
      <form className="form" onSubmit={handleSubmit}>
        <h1 className="form-title">Sign Up</h1>
        {error.message && (
          <Alert variant="filled" severity="warning">
            {error.message}
          </Alert>
        )}
        <input
          type="text"
          placeholder="Your Username"
          onChange={(e) => setUserName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Your Email"
          onChange={(e) => setEmail(e.target.value)}
        />
        <input
          type="text"
          placeholder="Your First Name"
          onChange={(e) => setFirstName(e.target.value)}
        />
        <input
          type="text"
          placeholder="Your Last Name"
          onChange={(e) => setLastName(e.target.value)}
        />
        <input
          type="password"
          placeholder="Enter Password"
          onChange={(e) => setPassword(e.target.value)}
        />
        <button className="form-button">sign up</button>
      </form>
    </div>
  );
};

export default SignUp;
