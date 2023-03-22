import React, { Component } from "react";
import Navbar from "./Navbar";
import axios from "axios";

export default class Shelves extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //insert here
      shelves: [],
      shelfName: "",
      shelfIdAdding: "",
      foodName: "",
      expirationDate: "",
      quantity: 1,
    };
  }

  updateInputValue(evt) {
    const val = evt.target.value;
    // ...
    this.setState({
      shelfName: val,
    });
  }

  updateFoodName(evt) {
    const val = evt.target.value;
    // ...
    this.setState({
      foodName: val,
    });
  }

  updateExpirationDate(evt) {
    const val = evt.target.value;
    // ...
    this.setState({
      expirationDate: val,
    });
  }

  updateQuantity(evt) {
    const val = evt.target.value;
    // ...
    this.setState({
      quantity: val,
    });
  }

  sendPostRequest(path, data) {
    return axios.post(process.env.REACT_APP_BACKEND_URL + path, data, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      },
    });
  }

  sendRequest(path) {
    return axios.get(process.env.REACT_APP_BACKEND_URL + path, {
      headers: {
        Authorization: `Bearer ${localStorage.getItem("access_token")}`,
      },
    });
  }

  createShelf() {
    this.sendPostRequest("shelf", { shelfName: this.state.shelfName }).then(
      () => {
        this.updateShelves();
      }
    );
  }

  deleteShelf(shelfId) {
    this.sendPostRequest("deleteshelf", { shelfId: shelfId }).then(() => {
      this.updateShelves();
    });
  }

  deleteFood(foodId) {
    this.sendPostRequest("deletefood", { foodId: foodId }).then(() => {
      this.updateShelves();
    });
  }

  addFood(shelfId) {
    this.setState({ shelfIdAdding: shelfId });
  }

  closeFoodMenu() {
    this.setState({
      foodName: "",
      expirationDate: "",
      quantity: 1,
    });
  }

  addFoodMenu() {
    this.sendPostRequest("/food", {
      shelfId: this.state.shelfIdAdding,
      name: this.state.foodName,
      expiration_date: this.state.expirationDate,
      quantity: this.state.quantity,
    }).then(() => {
      this.closeFoodMenu();
      this.updateShelves();
    });
  }

  updateShelves() {
    this.sendRequest("shelf").then((response) => {
      this.setState({ shelves: response.data });
    });
  }

  componentDidMount() {
    this.updateShelves();
  }

  render() {
    return (
      <>
        <div
          className="modal fade"
          id="addFoodModal"
          tabIndex="-1"
          aria-labelledby="exampleModalLabel"
          aria-hidden="true"
        >
          <div className="modal-dialog">
            <div className="modal-content">
              <div className="modal-header">
                <h1 className="modal-title fs-5" id="exampleModalLabel">
                  Add Food
                </h1>
                <button
                  type="button"
                  className="btn-close"
                  data-bs-dismiss="modal"
                  aria-label="Close"
                ></button>
              </div>
              <div className="modal-body">
                <label class="form-label">Food Name</label>
                <input
                  value={this.state.foodName}
                  onChange={(evt) => this.updateFoodName(evt)}
                  type="text"
                  class="form-control mb-3"
                  placeholder="Food Name"
                />

                <label class="form-label">Expiration Date</label>
                <input
                  value={this.state.expirationDate}
                  onChange={(evt) => this.updateExpirationDate(evt)}
                  type="date"
                  class="form-control mb-3"
                  placeholder="Expiration Date"
                />

                <label class="form-label">Quantity</label>
                <input
                  value={this.state.quantity}
                  onChange={(evt) => this.updateQuantity(evt)}
                  type="number"
                  class="form-control mb-3"
                  placeholder="Quantity"
                />
              </div>
              <div className="modal-footer">
                <button
                  type="button"
                  className="btn btn-secondary"
                  data-bs-dismiss="modal"
                  onClick={() => this.closeFoodMenu()}
                >
                  Close
                </button>
                <button
                  type="button"
                  className="btn btn-primary"
                  data-bs-dismiss="modal"
                  onClick={() => this.addFoodMenu()}
                >
                  Add
                </button>
              </div>
            </div>
          </div>
        </div>

        <Navbar
          sendRequest={this.props.sendRequest}
          logout={this.props.logout}
        />
        <div className="container">
          <div className="input-group mb-3">
            <input
              type="text"
              className="form-control"
              value={this.state.shelfName}
              onChange={(evt) => this.updateInputValue(evt)}
              placeholder="Shelf name"
              aria-label="Shelf name"
              aria-describedby="button-addon2"
            />
            <button
              className="btn btn-outline-secondary"
              type="button"
              id="button-addon2"
              onClick={() => this.createShelf()}
            >
              Create Shelf
            </button>
          </div>
          <div>
            <h1>Your Shelves</h1>
            {this.state.shelves.map((shelf) => (
              <div className="card mb-3" key={shelf[0][0]}>
                <div className="card-body">
                  {shelf[0][1]}
                  <button
                    type="button"
                    className="btn btn-danger ms-3"
                    onClick={() => this.deleteShelf(shelf[0][0])}
                  >
                    Delete
                  </button>
                  <button
                    type="button"
                    className="btn btn-success ms-3"
                    onClick={() => this.addFood(shelf[0][0])}
                    data-bs-toggle="modal"
                    data-bs-target="#addFoodModal"
                  >
                    Add Food
                  </button>
                </div>
                <div>
                  <ul>
                    {shelf[1].map((food) => (
                      <li className="pb-3">
                        {food[2]}{" "}
                        <span className="badge text-bg-info mx-1">
                          Date Added:{" "}
                          {new Date(food[3]).toLocaleDateString("en-US")}
                        </span>
                        <span className="badge text-bg-warning mx-1">
                          Expiration Date:{" "}
                          {new Date(food[4]).toLocaleDateString("en-US")}
                        </span>
                        <span className="badge text-bg-success mx-1">
                          Quantity: {food[5]}
                        </span>{" "}
                        <button
                          type="button"
                          className="btn btn-danger ms-3"
                          onClick={() => this.deleteFood(food[0])}
                        >
                          Delete Food
                        </button>
                      </li>
                    ))}
                  </ul>
                </div>
              </div>
            ))}
          </div>
        </div>
      </>
    );
  }
}
