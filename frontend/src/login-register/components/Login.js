import React from "react";

const Login = () => {
  return (
    <div className="form-container sign-in-container">
      <form className="form" action="#">
        <h1 className="form-title">Sign In</h1>

        <input type="email" placeholder="Email" />
        <input type="password" placeholder="Password" />

        <button className="form-button">sign in</button>
        <a className="find-password" href="#">
          Forgot Password?
        </a>
      </form>
    </div>
  );
};

export default Login;
