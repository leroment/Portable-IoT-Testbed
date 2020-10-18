import React, { useState } from "react";
import axios from "axios";

const SignUp = () => {
  const [username, setUserName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");

  const handleSubmit = (e) => {
    e.preventDefault();
    //registerInit(username, email, password);
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

// const registerInit = (username, email, password) => {
//   const base = "http://127.0.0.1:8000/api";

//   axios
//     .post(`${base}/register`, {
//       username: username,
//       email: email,
//       password: password,
//     })
//     .then((response) => {
//       console.log(response);
//     })
//     .catch((err) => {
//       console.log(err);
//     });

//     localStorage.setItem("token", )
//     axios.post(`${base}/login`,
//     {
//       email: email,
//       password: password,
//     }
//     )

//   const formData = new FormData();
//   formData.set("username", username);
//   formData.set("email", email);
//   formData.set("password", password);

//   const signup = await axios({
//     method: "POST",
//     url: `${base}/register`,
//     data: formData,
//     config: {},
//   });
// };

export default SignUp;
