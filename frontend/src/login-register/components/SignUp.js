import React, { useState } from "react";
import axios from "axios";
import { Redirect, Link as RouterLink } from "react-router-dom";

const SignUp = () => {
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [redirectToDashboard, setRedirectToDashboard] = useState(false);

  if (redirectToDashboard) {
    return <Redirect to="/dashboard" />;
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post(`/api/register`, {
      "username": username,
      "email": email,
      "password": password
    }).then((response) => {
      console.log(response);
      if (response.status == 200 && response.data.token) {
        localStorage.setItem("token", response.data.token);
        setRedirectToDashboard(true);
      }
    }
    ).catch((err) => {
      console.log(err);
    })
  };

  return (
    <div className="form-container sign-up-container">
      <form className="form" onSubmit={handleSubmit}>
        <h1 className="form-title">Sign Up</h1>

        <input
          type="text"
          placeholder="Your Name"
          onChange={(e) => setUserName(e.target.value)}
        />
        <input
          type="email"
          placeholder="Your Email"
          onChange={(e) => setEmail(e.target.value)}
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
