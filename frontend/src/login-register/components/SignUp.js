import React from "react";

const SignUp = () => {
  return (
    <div className="form-container sign-up-container">
      <form className="form" action="#">
        <h1 className="form-title">Sign Up</h1>

        <input type="text" placeholder="Your Name" />
        <input type="email" placeholder="Your Email" />
        <input type="password" placeholder="Enter Password" />
        <button className="form-button">sign up</button>
      </form>
    </div>
  );
};

export default SignUp;
