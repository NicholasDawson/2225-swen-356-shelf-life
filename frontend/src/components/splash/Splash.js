import { Component } from "react";
import './splash.css'
import * as React from "react";
import food from './food.svg';
import receipt from './receipt.svg'
import empty from './shelf_empty.svg'
//import featuresWeb3 from "./assets/featuresWeb3.svg";
class Splash extends Component {
    constructor(props){
        super(props);
        this.state = {
            //insert here
        }
    }
    render() {
      //<svg class="bi" width="1em" height="1em"><use xlink:href="#collection"/></svg>
        return (
            <main>
            <h1 class="visually-hidden">Features examples</h1>
          
            <div class="container px-4 py-5" id="featured-3">
              <h2 class="pb-2 border-bottom">Columns with icons 
                <button class="btn btn-primary">Get Started</button>
                <button class="btn btn-secondary">Login</button></h2>
              <div class="row g-4 py-5 row-cols-1 row-cols-lg-3">
                <div class="feature col">
                  <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
                    <img src={food} alt="" height="36em" width="36em"></img>
                  </div>
                  <h3 class="fs-2">Featured title</h3>
                  <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
                  <a href="#" class="icon-link d-inline-flex align-items-center">
                    Learn More
                  </a>
                </div>
                <div class="feature col">
                  <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
                    <img src={receipt} alt="" height="36em" width="36em"></img>
                  </div>
                  <h3 class="fs-2">Featured title</h3>
                  <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
                  <a href="#" class="icon-link d-inline-flex align-items-center">
                    Learn More
                  </a>
                </div>
                <div class="feature col">
                  <div class="feature-icon d-inline-flex align-items-center justify-content-center text-bg-primary bg-gradient fs-2 mb-3">
                    <img src={empty} alt="" height="36em" width="36em"></img>
                  </div>
                  <h3 class="fs-2">Featured title</h3>
                  <p>Paragraph of text beneath the heading to explain the heading. We'll add onto it with another sentence and probably just keep going until we run out of words.</p>
                  <a href="#" class="icon-link d-inline-flex align-items-center">
                    Learn More
                  </a>
                </div>
              </div>
            </div>
          
          
          
          </main>
          );
    }
}
export default Splash