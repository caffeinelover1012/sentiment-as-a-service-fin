import { render } from "react-dom";
import React, { Component, useState, useEffect } from 'react';

export default function App() {
  const [usrname, setUsrname] = useState("");

  useEffect(() => {
      const url = "/api/getuser/";

      const fetchData = async () => {
          try {
              const response = await fetch(url);
              const json = await response.json();
              console.log(json);
              setUsrname(json.n);
          } catch (error) {
              console.log("error", error);
          }
      };

      fetchData();
  }, []);

  return (
    <>
    <ul>
    <li><a href="/">Home</a></li>
    <li><a href="/web">Web</a></li>
    <li><a href="/manapi">API</a></li>
    <li><a href="/login/auth0">Login</a></li>
    <li><a href="/logout">Logout</a></li>
  </ul>
    <br />
  <div className="content">
    <p>Hello, {usrname} </p>
    <p>Welcome to Sentiment Analysis as a Service!</p>
    <p>You can use the web/api version to get the sentiment of a text input using various models.</p>
    <p>Log in to enjoy unlimited API access!</p>
  </div>
  </>
  );
}

const appDiv = document.getElementById('app');
render(<App/>,appDiv);
