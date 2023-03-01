import { Component } from "react";
import './splash.css'
import * as React from "react";
//import featuresWeb3 from "./assets/featuresWeb3.svg";
class Splash extends Component {
    constructor(props){
        super(props);
        this.state = {
            //insert here
        }
    }
    render() {
        return (
            <div className="splash-screen">
              <div className="cat-absolute-container">
                <span className="shelf-lyfe">SHELF LYFE</span>
                <span className="brief-project-descri">Brief project description</span>
                <div className="flex-container">
                  <button>Feature 1</button>
                  <button>Feature 2</button>
                </div>
                <div className="flex-container-1">
                  
                  <div className="cat-absolute-container-1">
                    <span className="get-started">Get Started</span>
                  </div>
                </div>
                <div className="flex-container-2">
                  <button>Feature 3</button>
                  <button>Feature 4</button>
                </div>
              </div>
              
            </div>
          );
    }
}
export default Splash