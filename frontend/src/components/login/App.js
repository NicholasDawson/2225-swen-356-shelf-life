import { Component } from "react";
import "./login.css";
class Login extends Component {
    constructor(props){
        super(props);
        this.state = {
            //insert here
        }
    }

    render() {
        return (
            <div className="login">
                <div className="cat-absolute-container">
                    <button className="enter-username">Enter Username</button>
                    <button className="enter-password">Enter Password</button>
                    <button className="log-in">Log In</button>
                    <button className="dont-have-an-account">
                    Don’t have an account? Sign up instead.
                    </button>
                </div>
                
                </div>
        )
    }
}
export default Login