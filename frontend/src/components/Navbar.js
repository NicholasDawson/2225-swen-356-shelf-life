import React, { Component } from "react";
import { Link } from "react-router-dom";

export default class Navbar extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //insert here
      user: {},
    };
  }

  componentWillMount() {
    this.props.sendRequest("protected").then((response) => {
      this.setState({ user: response.data.logged_in_as });
    });
  }

  render() {
    return (
      <div className="container">
        <header className="mb-3 border-bottom">
          <div className="container">
            <div className="d-flex flex-wrap align-items-center justify-content-center justify-content-lg-start">
              <Link
                to="/shelves"
                className="d-flex align-items-center mb-2 mb-lg-0 me-3 text-dark text-decoration-none"
              >
                <h1>SHELF LIFE</h1>
              </Link>

              <ul className="nav col-12 col-lg-auto me-lg-auto mb-2 justify-content-center mb-md-0">
                <li>
                  <a href="#" className="nav-link px-2 link-secondary">
                    Shelves
                  </a>
                </li>
              </ul>

              <div className="dropdown text-end">
                <a
                  href="#"
                  className="d-block link-dark text-decoration-none dropdown-toggle"
                  data-bs-toggle="dropdown"
                  aria-expanded="false"
                >
                  <img
                    src={this.state.user.picture}
                    alt="mdo"
                    width="32"
                    height="32"
                    className="rounded-circle"
                    referrerPolicy="no-referrer"
                  />
                </a>
                <ul className="dropdown-menu text-small">
                  <li>{this.state.user.name}</li>
                  <li>
                    <hr className="dropdown-divider" />
                  </li>
                  <li>
                    <button
                      className="dropdown-item"
                      onClick={this.props.logout}
                    >
                      Sign out
                    </button>
                  </li>
                </ul>
              </div>
            </div>
          </div>
        </header>
      </div>
    );
  }
}
