import React, {useState} from "react";
import axios from "axios";
import { Redirect} from "react-router-dom";

const Login = () => {

  const [username, setUserName] = useState("");
  const [password, setPassword] = useState("");
  const [redirectToDashboard, setRedirectToDashboard] = useState(false);


  if (redirectToDashboard) {
    return <Redirect to="/dashboard" />;
  }

  const handleSubmit = (e) => {
    e.preventDefault();

    axios.post(`/api/login`, {
      "username": username,
      "password": password
    }).then((response) => {
      console.log(response);
      if (response.status === 200 && response.data.token) {
        localStorage.setItem("token", response.data.token);
        setRedirectToDashboard(true);
      }
    }
    ).catch((err) => {
      console.log(err);
    })
  };
  
  return (
    <div className="form-container sign-in-container">
      <form className="form" onSubmit={handleSubmit}>
        <h1 className="form-title">Sign In</h1>

        <input type="text" placeholder="Username" onChange={(e) => setUserName(e.target.value) } />
        <input type="password" placeholder="Password" onChange={(e) => setPassword(e.target.value)} />

        <button className="form-button">sign in</button>
        <a className="find-password" href="#">
          Forgot Password?
        </a>
      </form>
    </div>
  );
};

export default Login;
