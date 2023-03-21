import React, { Component } from "react";
import Navbar from "./Navbar";

export default class Shelves extends Component {
  constructor(props) {
    super(props);
    this.state = {
      //insert here
      shelves: [],
    };
  }

  componentWillMount() {}

  render() {
    return (
      <>
        <Navbar sendRequest={this.props.sendRequest} logout={this.props.logout} />
        <div className="container">{this.shelves}</div>
      </>
    );
  }
}
