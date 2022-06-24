import logo from './logo.svg';
import './App.css';
import React, { useState, useEffect } from 'react';
import axios from "axios";

function App() {
  const [data, setData] = useState([{}])
  const [data2, setData2] = useState([{}])

  useEffect(() => {
    fetch("/members").then(
      res => res.json()
    ).then(
      data => {
        setData(data)
        console.log(data)
      }
    )
  }, [])

  // useEffect(() => {
  //   axios
  //     .get("http://127.0.0.1:5000/members")
  //     .then(response => setData2(response.members)); a
  // }, []);

  

  return (
    <div className="App">
      {(typeof data.members === 'undefined') ? (
        <p>Loading ...</p>
      ): (
        data.members.map((member, i) => (
          <p key={i}>{member}</p>
        ))
      )}
    </div>
  );
}

export default App;
