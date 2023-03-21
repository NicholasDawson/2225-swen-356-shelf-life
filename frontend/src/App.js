import "./App.css";
import Splash from "./components/splash/Splash";
import Shelves from "./components/Shelves";

import { HashRouter, Routes, Route } from "react-router-dom";
import { Component } from "react";
import axios from "axios";

class App extends Component {
  sendRequest(path) {
    return axios.get("http://localhost:5000/" + path, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      },
    });
  }

  logout() {
    console.log("logout");
    axios
      .get("http://localhost:5000/logout", {
        headers: {
          Authorization: `Bearer ${localStorage.getItem("access_token")}`,
        },
      })
      .then((response) => {
        console.log(response.data);
        // do something with the response
        // delete the token
        localStorage.removeItem("accessToken"); // remove token from local storage
      })
      .catch((error) => {
        localStorage.removeItem("accessToken"); // remove token from local storage
        // handle the error
      });

    window.location.href = "/";
  }

  componentDidMount() {
    const searchParams = new URLSearchParams(window.location.search);
    const accessToken = searchParams.get("access_token");

    if (accessToken) {
      // Store the access token in local storage
      localStorage.setItem("access_token", accessToken);
      // Remove the access token from the URL
      window.history.replaceState({}, document.title, window.location.pathname);
    }
  }

  login() {
    // redirect to authorize endpoint
    window.location.href = "http://localhost:5000/login";
  }

  isAuthenticated() {
    const storedAccessToken = localStorage.getItem("access_token");
    return storedAccessToken !== null;
  }

  render() {
    return (
      <HashRouter>
        <Routes>
          <Route
            path="/"
            element={
              <Splash
                login={this.login}
                isAuthenticated={this.isAuthenticated}
              />
            }
          />
          <Route
            path="shelves"
            element={
              <Shelves logout={this.logout} sendRequest={this.sendRequest} />
            }
          />
        </Routes>
      </HashRouter>
    );
  }
}

export default App;
