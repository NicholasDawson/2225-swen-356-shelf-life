import { Component } from "react";
import "./splash.css";
import * as React from "react";
import food from "./food.svg";
import receipt from "./receipt.svg";
import empty from "./shelf_empty.svg";
import pantryImg from "./food-pantry-shelves.jpg";
import axios from "axios";

class Splash extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //insert here
      accessToken: null,
    };
  }

  componentDidMount() {
    const searchParams = new URLSearchParams(window.location.search);
    const accessToken = searchParams.get('access_token');

    if (accessToken) {
      // Store the access token in local storage
      localStorage.setItem('access_token', accessToken);
      // Remove the access token from the URL
      window.history.replaceState({}, document.title, window.location.pathname);
      // Update the component state
      this.setState({ accessToken });
    } else {
      // Check if the access token is already stored in local storage
      const storedAccessToken = localStorage.getItem('access_token');

      if (storedAccessToken) {
        this.setState({ accessToken: storedAccessToken });
      }
    }
  }

  login() {
    // redirect to authorize endpoint
    window.location.href = 'http://localhost:5000/login';
  }

  sendRequest() {
    axios.get('http://localhost:5000/protected', {
      headers: {
        'Authorization': `Bearer ${this.state.accessToken}`
      }
    })
    .then(response => {
      console.log(response.data);
      // do something with the response
    })
    .catch(error => {
      console.error(error);
      // handle the error
    });
  }

  logout() {
    axios.get('http://localhost:5000/logout', {
      headers: {
        'Authorization': `Bearer ${this.state.accessToken}`
      }
    })
    .then(response => {
      console.log(response.data);
      // do something with the response
      // delete the token
    this.setState({accessToken: null});
    localStorage.removeItem('accessToken'); // remove token from local storage

    })
    .catch(error => {
      console.error(error);
      // handle the error
    });
  }

  render() {
    const { accessToken } = this.state;
    return (
      <main>
      {accessToken && (
          <div>
            <h1>{accessToken}</h1>
            <button onClick={() => this.sendRequest()}>Send Request</button>
            <button onClick={() => this.logout()}>Logout</button>
          </div>
        )}
        <div className="container w-100">
          <div className="row vh-100">
            <div className="col-4 bg-blue d-flex flex-column justify-content-center text-center px-5">
              <h1>
                <b>SHELF LIFE</b>
              </h1>
              <img
                src={pantryImg}
                alt="pantry photograph"
                className="img-fluid rounded my-5"
              ></img>
              <button
                type="button"
                className="btn btn-light btn-lg"
                onClick={this.login}
              >
                <b>Get Started</b>
              </button>
            </div>
            <div className="col-8">
              <div className="container px-4 py-5">
                <h2 className="pb-2">
                  <i>Track the shelf life of grocery items in your pantry</i>
                </h2>
                <div className="row g-4 py-5 row-cols-1 row-cols-lg-2">
                  <div className="col d-flex align-items-start">
                    <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
                      <img src={food} alt="" height="36em" width="36em"></img>
                    </div>
                    <div>
                      <h3 className="fs-2">Shelf Life Tracking</h3>
                      <p>
                        Guarentee that all ingredients in your pantry are safe and edible
                      </p>
                    </div>
                  </div>
                  <div className="col d-flex align-items-start">
                    <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
                      <img
                        src={receipt}
                        alt=""
                        height="36em"
                        width="36em"
                      ></img>
                    </div>
                    <div>
                      <h3 className="fs-2">Recipe Tracking</h3>
                      <p>
                        See what ingredients you have in stock for any recipe book
                      </p>
                    </div>
                  </div>
                  <div className="col d-flex align-items-start">
                    <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
                      <img src={empty} alt="" height="36em" width="36em"></img>
                    </div>
                    <div>
                      <h3 className="fs-2">Inventory Mangement</h3>
                      <p>
                        Get insights on your food Inventory without having to rummage through your pantry 
                      </p>
                    </div>
                  </div>
                  <div className="col d-flex align-items-start">
                    <div className="icon-square text-bg-light d-inline-flex align-items-center justify-content-center fs-4 flex-shrink-0 me-3">
                      <img src={empty} alt="" height="36em" width="36em"></img>
                    </div>
                    <div>
                      <h3 className="fs-2">Restocking</h3>
                      <p>
                        Easily create lists and order ingredients that you're running low on
                      </p>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </main>
    );
  }
}
export default Splash;
