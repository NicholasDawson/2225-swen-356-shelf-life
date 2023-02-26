import { Component } from "react";
import './signup.css'
class SignUp extends Component {
    constructor(props){
        super(props);
        this.state = {
            //insert here
        }
    }

    render() {
        return (
            <div className="signup">
            <div className="cat-absolute-container">
                <button className="enter-username">Enter Username</button>
                <button className="enter-password">Enter Password</button>
                <button className="confirm-password">Confirm Password</button>
                <button className="sign-up">Sign Up</button>
            </div>
            </div>
        )
    }
}
export default SignUp